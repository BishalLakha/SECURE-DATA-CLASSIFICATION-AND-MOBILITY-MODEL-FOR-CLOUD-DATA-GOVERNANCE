from .add_rule import system
from typing import List
from fastapi import APIRouter
from .schema import FeatureIn,FeatureOut,UserDataOut,UserDataIn
from .db_manager import *
import pandas as pd
from fastapi import File, UploadFile
from io import StringIO
from fastapi import BackgroundTasks
from .worker import celery
import json


fuzzy = APIRouter()


@fuzzy.post('/save-feature/', status_code=201)
async def predict_single(features: FeatureIn):
    try:
        features = features.dict()
        name = features["Name"]
        features.pop("Name")
        output = system.evaluate_output(features)

        features.update({"Sensitivity":output["Sensitivity"],"Name":name})

        await add_feature(features)

        return {"prediction":output,
                "message": "Successfully predicted",
                "success": True}
    except Exception as E:
        return {"prediction": None, "message": str(E),
                "success": False}


@fuzzy.post('/save-user-data/', status_code=201)
async def save_data(data: UserDataIn):
    try:
        await add_user_data(data)
        return {"message": "Successfully saved",
                "success": True}
    except Exception as E:
        return {"prediction": None, "message": str(E),
                "success": False}


@fuzzy.post("/save-data")
async def upload_csv(background_tasks: BackgroundTasks, csv_file: UploadFile = File(...)):
    task_name = "save_in_db.task"

    if csv_file.filename.split(".")[-1] != "csv":
        return {"message":"Please use csv file","success":False, "status":400}

    dataframe = pd.read_csv(StringIO(str(csv_file.file.read(), 'utf-8')), encoding='utf-8',index_col=["SN"])
    dataframe = dataframe.astype(str)
    features = await get_all_features()

    feat_sens = {}

    for feat in features:
        feat_sens.update({feat["Name"]: feat["Sensitivity"]})

    task = celery.send_task(task_name, args=[dataframe.to_dict(), feat_sens, csv_file.filename])
    return dict(id=task.id,message="Started encryption and saving data")


@fuzzy.get('/all-features', response_model=List[FeatureOut])
async def get_all_results():
    return await get_all_features()


@fuzzy.get('/all-user-data', response_model=List[UserDataOut])
async def get_all_data():
    return await get_all_user_data()


@fuzzy.get('/delete-all-data')
async def delete_all_users_data():
    await delete_all_user_data()
    return {"message": "All user data deleted"}



# @fuzzy.post("/task_hello_world/")
# async def create_item(name: str):
#     task_name = "hello.task"
#     task = celery.send_task(task_name, args=[name])
#     return dict(id=task.id, url='localhost:5000/check_task/{}'.format(task.id))


@fuzzy.get("/check_task/{id}")
def check_task(id: str):
    task = celery.AsyncResult(id)
    if task.state == 'SUCCESS':
        response = {
            'status': task.state,
            'result': task.result,
            'task_id': id
        }
    elif task.state == 'FAILURE':
        response = json.loads(task.backend.get(task.backend.get_key_for_task(task.id)).decode('utf-8'))
        del response['children']
        del response['traceback']
    else:
        response = {
            'status': task.state,
            'result': task.info,
            'task_id': id
        }
    return response