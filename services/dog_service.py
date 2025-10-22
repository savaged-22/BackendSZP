from db.mongo import Connection
from bson import ObjectId
from typing import Any, Dict, Optional, List
from datetime import datetime, timezone


def _to_object_id(value: str) -> Optional[ObjectId]:
    try:
        return ObjectId(value)
    except Exception:
        return None
    
def _serialize_dog(doc: Dict[str,Any])->Dict[str,Any]:
    out = {**doc}
    _id = out.get("_id")
    if isinstance(_id, ObjectId):
        out["_id"] = str(_id)
        

class DogService:
    @staticmethod
    def create_dog(db,dog)-> Optional[ObjectId]:
        try:
            col = db["dog"]
            now = datetime.now(timezone.utc)

            data = {
                "name": getattr(dog, "name", None),
                "chip_id": getattr(dog, "chip_id", None),
                "breed": getattr(dog, "breed", None),
                "age_years": getattr(dog, "age_years", None),
                "owner_id": getattr(dog, "powner_id", None),
                "created_at": getattr(dog, "created_at", None) or now,
                "updated_at": getattr(dog, "updated_at", None) or now,
            }

            res = col.insert_one(data)
            return res.inserted_id
        except Exception as e:
            # Loguea con tu logger si tienes
            print(f"[create_dog] DB error: {e}")
            return None


    @staticmethod
    def dog_by_id(db,uid:str)-> Optional[Dict[str, Any]]:
        try:
            oid = _to_object_id(uid)
            if not oid:
                return None
            col = db["user"]
            doc = col.find_one({"_id": oid})
            return _serialize_dog(doc) if doc else None
        except Exception as e:
            print(f"[find_by_id] DB error: {e}")
            return None
        

    @staticmethod
    def update_dog():
        pass
