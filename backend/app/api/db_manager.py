from .db import  database, feature_data, user_data
from .schema import FeatureInDb,UserDataIn


async def add_feature(payload):
    query = feature_data.insert().values(**payload)
    return await database.execute(query=query)


async def get_all_features():
    query = feature_data.select()
    return await database.fetch_all(query=query)

async def get_features(feature_name):
    query = feature_data.select().where(feature_data.c.Name == feature_name)
    return await database.fetch_one(query=query)


async def add_user_data(payload: UserDataIn):
    query = user_data.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get_all_user_data():
    query = user_data.select()
    return await database.fetch_all(query=query)