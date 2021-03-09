# Retrieve all songs present in the database
async def retrieve_audiofiles():
    audiofiles = []
    async for files in audiobook_collection.find():
        audiofiles.append(audiobook_helper(audio))
    return audiofiles


# Add a new song into to the database
async def add_audiofile(audio_data: dict) -> dict:
    audio = await audiobook_collection.insert_one(audio_data)
    new_audio = await audiobook_collection.find_one({"_id": audio.inserted_id})
    return audiobook_helper(new_audio)




# Update a song with a matching ID
async def update_audio(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    audio = await audiobook_collection.find_one({"_id": ObjectId(id)})
    if audio:
        updated_audio = await audiobook_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_audio:
            return True
        return False


# Delete a song from the database
async def delete_audio(id: str):
    song = await audiobook_collection.find_one({"_id": ObjectId(id)})
    if song:
        await audiobook_collection.delete_one({"_id": ObjectId(id)})
        return True

