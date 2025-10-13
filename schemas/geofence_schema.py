from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, field_validator

from .common import MongoBase, _strip, DogRef

class GeofenceBase(BaseModel):
    dog_id: str = Field(..., description="ID (_id) del Dog")
    name: str = Field(..., description='Ej: "Casa", "Parque"')
    center_lat: float
    center_lng: float
    radius_meters: float = Field(..., gt=0)
    active: bool = True

    @field_validator("dog_id", "name", mode="before")
    @classmethod
    def _clean(cls, v):
        return _strip(v)

class GeofenceCreate(GeofenceBase):
    pass

class GeofenceUpdate(BaseModel):
    name: Optional[str] = None
    center_lat: Optional[float] = None
    center_lng: Optional[float] = None
    radius_meters: Optional[float] = Field(default=None, gt=0)
    active: Optional[bool] = None

    @field_validator("name", mode="before")
    @classmethod
    def _clean(cls, v):
        return _strip(v)

class GeofenceOut(MongoBase, GeofenceBase):
    created_at: datetime
    updated_at: datetime
    # Relación N:1 -> Dog
    dog: DogRef
