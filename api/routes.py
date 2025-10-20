from fastapi import APIRouter, HTTPException, Depends
from schemas.user_schema import UserBase,UserUpdate

router = APIRouter()

#Create a user
@router.post("/user/new")
async def crear_usuario(user:UserBase):
    pass

#Get user information
@router.get("/user/{uid}")
async def get_user(uid:str):
    pass

#Update the dog list
@router.patch("/user/{uid}")
async def update_dogs(uid:str, data:UserUpdate):
    pass

#Method to get every dog of every owner
@router.get("/user/dogs")
async def get_dogs(uid:str):
    pass


