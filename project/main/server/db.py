from bson.objectid import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient

import motor.motor_asyncio
from .db_crud import *


class DataBase:
    client: AsyncIOMotorClient = None


db = DataBase()


async def get_database() -> AsyncIOMotorClient:
    return db.client

songfile_collection = database.get_collection("audiobook_collection")
podcast_collection = database.get_collection("podcast_collection")
audiobook_collection = database.get_collection("audiobook_collection")
songfile_collection_name = "songs"
audiobook_collection_name = "podcast"
podcast_collection_name = "podcast"




# for parsing the results from a database query into a Python dict.
def songfile_helper(song) -> dict:
    return {
        "id": int(song["_id"]),
        "name": song["name"],
        "duration": song["duration"],
        "uploaded_at": song["uploaded_at"],
    }


def audiobookfile_helper(audio) -> dict:
    return {
        "id": int(audio["_id"]),
        "name": audio["name"],
        "duration": audio["duration"],
        "uploaded_at": audio["uploaded_at"],
    }
    
def podcastfile_helper(podcast) -> dict:
    return {
        "id": int(podcast["_id"]),
        "name": podcast["name"],
        "host": podcast["host"]
        "duration": podcast["duration"],
        "uploaded_at": podcast["uploaded_at"],
        "participants":podcast["participants"]
    }    

