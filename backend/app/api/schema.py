from typing import List, Optional
from pydantic import BaseModel,Field


class FeatureIn(BaseModel):
    name: str
    Confidentiality: float
    Integrity: float
    Availability: float
    Sensitivity: Optional[float]


class UserDataIn(BaseModel):
    PA_NUMBER: str
    BENEFICIARY_NAME: str
    DISTRICT: Optional[str]
    GP_NP: Optional[str]
    WARD_NO: Optional[int]

    AREA_TOLE: Optional[str]
    HOUSE_OWNER_NAME: Optional[str]
    GENDER: Optional[str]
    Age: Optional[int]
    Citizenship_Number: Optional[int]

    PHONE_NO: Optional[int]
    LATITUDE: Optional[float]
    LONGITUDE: Optional[float]
    Nationality: Optional[str]
    Occupation: Optional[str]
    Education: Optional[str]


class FeatureOut(FeatureIn):
    Id: int
