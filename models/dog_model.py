from datetime import datetime
from pydantic import BaseModel

class Dog(BaseModel):
    id:int
    name:str
    raze: str | None
    age: str | None
    chip_id: str | None 

