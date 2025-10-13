from datetime import datetime
from pydantic import BaseModel

class User(BaseModel):
    Uid:int
    name:str
    email:str
    passw:str
    phone:int
    address:str
    signup_ts: datetime | None
