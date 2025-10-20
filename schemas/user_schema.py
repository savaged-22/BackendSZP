from __future__ import annotations
from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel, Field, field_validator
from .common import MongoBase, _strip, DogBrief

class UserBase(BaseModel):
    firebase_uid: str = Field(..., description="UID emitido por Firebase Auth")
    email: str
    name: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    role:Optional[str] = None
    # Compatibilidad: si alguna vez existió password_hash, se marca deprecado.
    password_hash: Optional[str] = Field(
        default=None,
        description="DEPRECATED: No usar con Firebase Auth."
    )

    @field_validator("firebase_uid", "email", "name", "phone", "address", "password_hash", mode="before")
    @classmethod
    def _clean(cls, v):
        return _strip(v)

class UserCreate(UserBase):
    """Creación de usuario; password se gestiona en Firebase (no aquí)."""
    pass

class UserUpdate(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    dogs:List[DogBrief] = []

    @field_validator("name", "phone", "address", "dogs", mode="before")
    @classmethod
    def _clean(cls, v):
        return _strip(v)

class UserOut(MongoBase, UserBase):
    created_at: datetime
    updated_at: datetime
    # Relación 1:N -> Dog (listado liviano)
    dogs: List[DogBrief] = []
