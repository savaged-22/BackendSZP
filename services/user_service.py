from db.mongo import Connection
from bson import ObjectId


def create_user(user):
    try:
        database = Connection.db_connection()
        collection = database["user"]
        data = {
            'username': user.username,
            'email': user.email,
            'phone':user.phone,
            'address':user.address,
            'password_hash':user.password_hash,
            'created_at':user.created_at,
            'updated_at':user.update_at,
            'dog':[],
            'role':user.role
        }

        # Inserting the user data into the 'users' collection and obtaining the inserted ID
        sid = collection.insert_one(data).inserted_id
        print(f"usuario creado:{sid}")
        return sid
    except Exception  as e:
        print(f"Error creating user in the database: {e}")

def find_by_id(uid:str):
    try:
        database = Connection.db_connection()
        collection = database["user"]
        user = collection.find({"_id" : ObjectId("uid")})
        return user
    except Exception as e:
        print(f"Error updating user in the database: {e}")


def update_user_dogs(uid:str,dog:list):
    try:
        database = Connection.db_connection()
        collection = database["user"]
        data = {
            'dog':dog
        }
        collection.update_one({'_id': uid}, {"$set": data})
    except Exception  as e:
        print(f"Error updating user in the database: {e}")


