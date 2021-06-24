from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.db import metadata, database, engine
from app.api.classifier import fuzzy

metadata.create_all(engine)


app = FastAPI(openapi_url="/api/v1/fuzzy/openapi.json", docs_url="/api/v1/fuzzy/docs")

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(fuzzy, prefix='/api/v1/fuzzy/classify', tags=['fuzzy classification'])