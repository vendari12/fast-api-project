from typing import Optional, List
from pydantic import BaseModel, BaseConfig, Field
from datetime import datetime

class AudioBookBase(BaseModel):
    title: str = Field(..., max_length=100)
    author: str = Field(..., max_length=100)
    narator: str = Field(..., max_length=100)
    duration: int = Field(lt=101, gt=0)
    uploaded_at: datetime = Field(..., alias="uploaded time")
    
    
    
    
class AudioBook(AudioBookBase):
    pass


class AudioBookInCreate(BaseModel):
    title : str
    narator : str


class AudioBookInResponse(BaseModel):
    audiobook: AudioBook


class ManyAudioBookInResponse(BaseModel):
    audiobook: List[AudioBook]
    
   









