from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os

load_dotenv()
URL = os.getenv("MONGODB_URL")
PASSWD = os.getenv("MONGODB_PASSWORD")

print(f'SECRET_KEY: {PASSWD}')
print(f'DATABASE_URL: {URL}')


class Connection:
    
    @staticmethod
    def db_connection():
        try:
            client = MongoClient(URL, server_api=ServerApi('1'))
            client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
            database =  client["SafeZonePet"]
            print("Connected to MongoDB")
            return database
        except Exception as e:
            print(e)