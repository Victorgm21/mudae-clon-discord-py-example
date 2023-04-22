import pymongo
import os
from dotenv import load_dotenv


load_dotenv()
db_uri = os.getenv("mongo_uri")


def get_connection():
    client = pymongo.MongoClient(db_uri)
    db = client["discord_server"]
    return db