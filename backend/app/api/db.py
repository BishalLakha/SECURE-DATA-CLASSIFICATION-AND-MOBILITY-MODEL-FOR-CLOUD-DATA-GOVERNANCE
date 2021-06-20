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

database = Database(DATABASE_URI)