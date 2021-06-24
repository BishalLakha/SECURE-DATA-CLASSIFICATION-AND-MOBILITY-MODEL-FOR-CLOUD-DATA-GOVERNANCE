import os

from sqlalchemy import (Column, Integer, MetaData, String, Table,
                        create_engine, ARRAY,FLOAT)

from databases import Database

DATABASE_URI = os.getenv('DATABASE_URI')

engine = create_engine(DATABASE_URI)
metadata = MetaData()

feature_data = Table(
    'features',
    metadata,
    Column('Id', Integer, primary_key=True),
    Column('Name', String(length=150),unique=True),
    Column('Confidentiality',FLOAT),
    Column('Integrity', FLOAT),
    Column('Availability', FLOAT),
    Column('Sensitivity', FLOAT)
)

user_data = Table(
    'user_data',
    metadata,
    Column('Id', Integer, primary_key=True),
    Column('PA_NUMBER', String(length=500),unique=True),
    Column('BENEFICIARY_NAME',String(length=500)),
    Column('DISTRICT', String(length=500),nullable=True),
    Column('GP_NP', String(length=500),nullable=True),
    Column('WARD_NO', String(length=500),nullable=True),
    Column('AREA_TOLE', String(length=500),nullable=True),
    Column('HOUSE_OWNER_NAME',String(length=500),nullable=True),
    Column('GENDER', String(length=500),nullable=True),
    Column('Age', String(length=500),nullable=True),
    Column('Citizenship_Number ', String(length=500),nullable=True,unique=True),
    Column('PHONE_NO',String(length=500),nullable=True),
    Column('LATITUDE', String(length=500),nullable=True),
    Column('LONGITUDE', String(length=500),nullable=True),
    Column('Nationality', String(length=500),nullable=True),
    Column('Occupation', String(length=500),nullable=True),
    Column('Education', String(length=500),nullable=True)

)
database = Database(DATABASE_URI)