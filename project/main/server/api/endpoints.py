from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from server.errors import ErrorResponseModel, ResponseModel
from server.crud.audiobook import *
from server.crud.podcast import *
from server.crud.songfile import *


from server.models.audiobook import *
from server.models.podcast import *
from server.models.songfile import *



router = APIRouter()







@router.post("/", response_description="Songfile data added into the database")
async def add_songfile_data(song: SongSchema = Body(...)):
    song = jsonable_encoder(songfile)
    new_song = await add_song(song)
    return ResponseModel(new_song, "Songfile has been added successfully.")






@router.get("/{id}", response_description="Songfile data retrieved")
async def get_songfile_data(id):
    student = await retrieve_songfile(id)
    if song:
        return ResponseModel(student, "Songfile data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Songfile doesn't exist.")



@router.put("/{id}")
async def update_songfile_data(id: str, req: UpdateSongModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_songfile = await update_songfile(id, req)
    if updated_songfile:
        return ResponseModel(
            "Songfile with ID: {} name update is successful".format(id),
            "Songfile name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the songfile data.",
    )



@router.delete("/{id}", response_description="Songfile data deleted from the database")
async def delete_songfile_data(id: int):
    deleted_songfile = await delete_songfile(id)
    if deleted_songfile:
        return ResponseModel(
            "Songfile with ID: {} removed".format(id), "Songfile deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Songfile with id {0} doesn't exist".format(id)
    )
