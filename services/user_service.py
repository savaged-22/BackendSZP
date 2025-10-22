from db.mongo import Connection
from bson import ObjectId
from typing import Any, Dict, Optional, List
from datetime import datetime, timezone



def _to_object_id(value: str) -> Optional[ObjectId]:
    try:
        return ObjectId(value)
    except Exception:
        return None

def _serialize_user(doc: Dict[str, Any]) -> Dict[str, Any]:
    out = {**doc}
    _id = out.get("_id")
    if isinstance(_id, ObjectId):
        out["_id"] = str(_id)
    # Asegurar que dog exista como lista
    if "dog" not in out or out["dog"] is None:
        out["dog"] = []
    return out


class UserService:

    @staticmethod
    def create_user(db,user)-> Optional[ObjectId]:
        try:
            col = db["user"]
            now = datetime.now(timezone.utc)

            data = {
                "username": getattr(user, "username", None),
                "email": getattr(user, "email", None),
                "phone": getattr(user, "phone", None),
                "address": getattr(user, "address", None),
                "password_hash": getattr(user, "password_hash", None),
                "created_at": getattr(user, "created_at", None) or now,
                "updated_at": getattr(user, "updated_at", None) or now,
                "dog": [],
                "role": getattr(user, "role", "Owner"),
            }

            res = col.insert_one(data)
            return res.inserted_id
        except Exception as e:
            # Loguea con tu logger si tienes
            print(f"[create_user] DB error: {e}")
            return None


    @staticmethod
    def find_by_id(db,uid:str)-> Optional[Dict[str, Any]]:
        try:
            oid = _to_object_id(uid)
            if not oid:
                return None
            col = db["user"]
            doc = col.find_one({"_id": oid})
            return _serialize_user(doc) if doc else None
        except Exception as e:
            print(f"[find_by_id] DB error: {e}")
            return None
        
    
    def update_user_dogs(uid:str,dog:list):
        try:
            database = Connection.db_connection()
            collection = database["user"]
            data = {
                'dog':dog
            }
            dogs = collection.update_one({'_id': uid}, {"$set": data})
            return dogs
        except Exception  as e:
            print(f"Error updating user in the database: {e}")


