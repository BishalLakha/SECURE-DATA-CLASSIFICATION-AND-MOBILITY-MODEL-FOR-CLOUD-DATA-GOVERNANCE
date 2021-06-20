from .add_rule import system
from typing import List
from fastapi import Query
from fastapi import APIRouter, HTTPException
from .schema import FeatureIn,FeatureOut
from .db_manager import *


#
# print(output)




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


@fuzzy.get('/all-features', response_model=List[FeatureOut])
async def get_all_results():
    return await get_all_features()
