from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, BaseConfig, Field



class Participants(BaseModel):
    username: str
    bio: Optional[str] = ""


class ParticipantsInResponse(BaseModel):
    participants: Participants



class PodcastInDB(BaseModel):
    name: str = Field(...,max_length=100)
    duration:int = Field(..., lt=101,gt=0)
    uploaded_at : datetime = Field(..., alias="uploaded time")
    host: str = Field(..., maxlength=100)
    
    participants: Participants = Field(...,)


class Podcast(PodcastInDB):
    pass


class PodcastInCreate(BaseModel):
    name : str
    host : str


class PodcastInResponse(BaseModel):
    podcast: Podcast


class ManyPodcastInResponse(BaseModel):
    podcast: List[Podcast]
