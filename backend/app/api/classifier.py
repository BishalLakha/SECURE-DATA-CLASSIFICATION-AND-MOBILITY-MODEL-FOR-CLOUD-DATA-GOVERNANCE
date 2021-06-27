from .add_rule import system
from typing import List
from fastapi import APIRouter, HTTPException
from .schema import FeatureIn,FeatureOut
from .db_manager import *
from .encrypt import AESCipher,ECCAESCipher
import pandas as pd
from fastapi import File, UploadFile,Body
from io import StringIO
from fastapi import BackgroundTasks
from celery.result import AsyncResult
from .worker import celery
import json


aes = AESCipher("1234")
ecc = ECCAESCipher(1234)


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




@fuzzy.post("/save-data")
async def upload_csv(background_tasks: BackgroundTasks, csv_file: UploadFile = File(...)):
    if csv_file.filename.split(".")[-1] != "csv":
        return {"message":"Please use csv file","success":False, "status":400}

    dataframe = pd.read_csv(StringIO(str(csv_file.file.read(), 'utf-8')), encoding='utf-8')
    dataframe = dataframe.astype(str)

    return {"Message": "Started encryption and saving data"}


@fuzzy.get('/all-features', response_model=List[FeatureOut])
async def get_all_results():
    return await get_all_features()



@fuzzy.post("/task_hello_world/")
async def create_item(name: str):
    task_name = "hello.task"
    task = celery.send_task(task_name, args=[name])
    return dict(id=task.id, url='localhost:5000/check_task/{}'.format(task.id))


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