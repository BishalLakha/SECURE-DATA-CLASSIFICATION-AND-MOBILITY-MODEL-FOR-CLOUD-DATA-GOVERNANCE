from .db import  database, feature_data, user_data
from .schema import FeatureIn


async def add_feature(payload: FeatureIn):
    query = feature_data.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get_all_features():
    query = feature_data.select()
    return await database.fetch_all(query=query)


async def add_user_data(payload: FeatureIn):
    query = user_data.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get_all_user_data():
    query = user_data.select()
    return await database.fetch_all(query=query)