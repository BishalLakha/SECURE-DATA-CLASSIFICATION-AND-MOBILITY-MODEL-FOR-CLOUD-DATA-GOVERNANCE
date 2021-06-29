from typing import List, Optional
from pydantic import BaseModel,Field


class FeatureIn(BaseModel):
    Name: str
    Confidentiality: float
    Integrity: float
    Availability: float


class FeatureInDb(BaseModel):
    Name: str
    Confidentiality: float
    Integrity: float
    Availability: float
    Sensitivity: float


class UserDataIn(BaseModel):
    PA_NUMBER: str
    BENEFICIARY_NAME: str
    DISTRICT: Optional[str]
    GP_NP: Optional[str]
    WARD_NO: Optional[str]
    AREA_TOLE: Optional[str]
    HOUSE_OWNER_NAME: Optional[str]
    GENDER: Optional[str]
    Age: Optional[str]
    Citizenship_Number: Optional[str]
    PHONE_NO: Optional[str]
    LATITUDE: Optional[str]
    LONGITUDE: Optional[str]
    Nationality: Optional[str]
    Occupation: Optional[str]
    Education: Optional[str]


class FeatureOut(FeatureIn):
    Id: int
    Sensitivity: float


class UserDataOut(UserDataIn):
    Id: int
