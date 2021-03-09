from fastapi import FastAPI
from server.api.endpoints import router

app = FastAPI()

app.include_router(router, tags=["audiofile"], prefix="/songs")




@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this demo app!"}
