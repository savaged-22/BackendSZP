from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, field_validator
from .common import MongoBase, _strip, UserRef, LocationRef


class DogBase(BaseModel):
    name: str
    chip_id: str = Field(..., description="Identificador único del collar/chip")
    breed: Optional[str] = None
    age_years: Optional[int] = Field(default=None, ge=0)
    owner_id: str = Field(..., description="ID (_id) del User propietario")
    trainer_id: str = Field(..., description="ID (_id) del User trainer")
    created_at: datetime
    updated_at: datetime
    @field_validator("name", "chip_id", "breed", "owner_id", mode="before")
    @classmethod
    def _clean(cls, v):
        return _strip(v)

class DogCreate(DogBase):
    pass

class DogUpdate(BaseModel):
    name: Optional[str] = None
    breed: Optional[str] = None
    age_years: Optional[int] = Field(default=None, ge=0)
    trainer_id: Optional[str] = Field(defaul=None)

    @field_validator("name", "breed", mode="before")
    @classmethod
    def _clean(cls, v):
        return _strip(v)

class DogOut(MongoBase, DogBase):
    created_at: datetime
    updated_at: datetime
    # Relaciones
    owner: UserRef                       # N:1 -> User
    last_location: Optional[LocationRef] # 1:1 (denormalizada para rapidez)
