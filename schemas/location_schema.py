from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field

from .common import MongoBase, DogRef

class LocationBase(BaseModel):
    dog_id: str = Field(..., description="ID (_id) del Dog")
    lat: float
    lng: float
    battery: Optional[int] = Field(default=None, ge=0, le=100)
    timestamp: datetime

class LocationCreate(LocationBase):
    pass

class LocationOut(MongoBase, LocationBase):
    # Relación N:1 -> Dog (referencia ligera)
    dog: DogRef
