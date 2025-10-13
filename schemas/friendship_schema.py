from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, field_validator

from .common import MongoBase, _strip, UserRef

class FriendshipBase(BaseModel):
    user_id: str = Field(..., description="ID (_id) del usuario A")
    friend_id: str = Field(..., description="ID (_id) del usuario B")
    can_view: bool = Field(True, description="Si B puede ver ubicaciones de A")

    @field_validator("user_id", "friend_id", mode="before")
    @classmethod
    def _clean(cls, v):
        return _strip(v)

class FriendshipCreate(FriendshipBase):
    pass

class FriendshipUpdate(BaseModel):
    can_view: Optional[bool] = None

class FriendshipOut(MongoBase, FriendshipBase):
    since: datetime
    # Relación N:M -> User-User (materializada)
    user: UserRef
    friend: UserRef
