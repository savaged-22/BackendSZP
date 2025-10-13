from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field

# ---- Helpers para Mongo ----
def _strip(v: Optional[str]) -> Optional[str]:
    return v.strip() if isinstance(v, str) else v

class MongoBase(BaseModel):
    """Base para documentos Mongo: expone `id` y mapea al JSON `_id`."""
    id: Optional[str] = Field(default=None, alias="_id")

    class Config:
        populate_by_name = True  # Permite usar 'id' y serializar como '_id'

# ---- Referencias ligeras para evitar ciclos ----
class UserRef(MongoBase):
    firebase_uid: str
    email: str
    name: Optional[str] = None

class DogRef(MongoBase):
    name: str
    chip_id: str
    owner_id: str

class DogBrief(MongoBase):
    """Para listar perros dentro de UserOut con payload liviano."""
    name: str
    chip_id: str

class LocationRef(MongoBase):
    dog_id: str
    lat: float
    lng: float
    timestamp: datetime
