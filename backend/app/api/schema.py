from typing import List, Optional
from pydantic import BaseModel,Field


class FeatureIn(BaseModel):
    name: str
    Confidentiality: float
    Integrity: float
    Availability: float
    Sensitivity: Optional[float]


class FeatureOut(FeatureIn):
    Id: int
