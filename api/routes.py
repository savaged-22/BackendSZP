from fastapi import APIRouter, HTTPException, Depends, status
from schemas.user_schema import UserBase,UserUpdate
from schemas.dog_schema import DogBase
from services.user_service import UserService
from db.mongo import Connection

router = APIRouter()

def get_db():
    return Connection.get_db()

#Create a user
@router.post("/user/new",status_code=status.HTTP_201_CREATED)
async def crear_usuario(user:UserBase,db=Depends(get_db)):
    sid = UserService.create_user(db, user)
    if not sid:
        raise HTTPException(500, "No se pudo crear el usuario")
    return {"id": str(sid)}


#Get user information
@router.get("/user/{uid}")
async def get_user(uid:str,db=Depends(get_db)):
    print(type(uid))
    user_info= UserService.find_by_id(db,uid)
    if not user_info:
        raise HTTPException(404, "Usuario no encontrado")
    return user_info


#Update the dog list
@router.patch("/user/{uid}")
async def update_dogs(uid:str, data:UserUpdate, db=Depends(get_db)):
    dogs_list = getattr(data, "dog", None) or getattr(data, "dogs", None)
    if dogs_list is None or not isinstance(dogs_list, list):
        raise HTTPException(400, "Debes enviar un arreglo 'dog' (o 'dogs')")
    ok = UserService.update_user_dogs(db, uid, dogs_list)
    if not ok:
        raise HTTPException(404, "Usuario no encontrado")
    return {"updated": True, "count": ok}

#Method to get every dog of every owner
@router.get("/user/{uid}/dogs")
async def get_dogs(uid:str, db=Depends(get_db)):
    pass
   
@router.get("/dog/new",status_code=status.HTTP_201_CREATED)
async def create_dog(dog:DogBase):
    pass

@router.post("/dog/{uid}")
async def get_dog(uid:str):
    pass
