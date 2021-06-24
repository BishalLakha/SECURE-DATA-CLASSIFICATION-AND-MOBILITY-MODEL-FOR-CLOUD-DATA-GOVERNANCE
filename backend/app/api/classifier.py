from .add_rule import system
from typing import List
from fastapi import Query
from fastapi import APIRouter, HTTPException
from .schema import FeatureIn,FeatureOut
from .db_manager import *
from .encrypt import AESCipher,ECCAESCipher
import pandas as pd
from fastapi import FastAPI, File, UploadFile



aes = AESCipher("1234")
ecc = ECCAESCipher(1234)


fuzzy = APIRouter()


@fuzzy.post('/save-and-predict', status_code=201)
async def predict_single(features: FeatureIn):
    try:
        output = system.evaluate_output(features)
        features.update({"Sensitivity":output})

        await add_feature(features)

        return {"prediction":output,
                "message": "Successfully predicted",
                "success": True}
    except Exception as E:
        return {"prediction": None, "message": str(E),
                "success": False}




@fuzzy.post("/save-data/")
def upload_csv(csv_file: UploadFile = File(...,media_type="csv")):
    dataframe = pd.read_csv(csv_file.file)
    print(dataframe)
    return {"filename": csv_file.filename}

@fuzzy.post('/save-and-predict', status_code=201)
async def predict_single(features: FeatureIn):
    try:
        output = system.evaluate_output(features)
        features.update({"Sensitivity":output})

        await add_feature(features)

        return {"prediction":output,
                "message": "Successfully predicted",
                "success": True}
    except Exception as E:
        return {"prediction": None, "message": str(E),
                "success": False}


@fuzzy.get('/all-features', response_model=List[FeatureOut])
async def get_all_results():
    return await get_all_features()
