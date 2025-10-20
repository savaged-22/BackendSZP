from datetime import datetime
from pydantic import BaseModel

class User(BaseModel):
    Uid:int
    firebase_uid:str 
    name:str
    email:str
    passw:str
    phone:int
    address:str
    signup_ts: datetime | None
    role:str = "Owner" | None