from bson.objectid import ObjectId

# Retrieve all podcast present in the database
async def retrieve_songs():
    podcasts = []
    async for podcsat in song_collection.find():
        podcast.append(podcast_helper(podcast))
    return podcast


# Add a new podcast into to the database
async def add_song(song_data: dict) -> dict:
    podcast = await song_collection.insert_one(song_data)
    new_podcast = await song_collection.find_one({"_id": podcast.inserted_id})
    return podcast_helper(new_podcast)


# Retrieve a podcast with a matching ID
async def retrieve_podcast(id: str) -> dict:
    podcast = await podcast_collection.find_one({"_id": ObjectId(id)})
    if podcsat:
        return podcast_helper(audio)


# Update a podcast with a matching ID
async def update_podcast(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    podcast = await podcast
    
    podcast_collection.find_one({"_id": ObjectId(id)})
    if podcast:
        updated_podcast = await podcast_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_podcast:
            return True
        return False


# Delete a podcast from the database
async def delete_podcast(id: str):
    podcast = await podcast_collection.find_one({"_id": ObjectId(id)})
    if podcast:
        await podcast_collection.delete_one({"_id": ObjectId(id)})
        return True

