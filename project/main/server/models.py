from datetime import timezone, datetime
from typing import Optional

from pydantic import BaseConfig, BaseModel, Field




class PModel(BaseModel):
    class Config(BaseConfig):
        allow_population_by_alias = True
        json_encoders = {
            datetime: lambda dt: dt.replace(tzinfo=timezone.utc)
            .isoformat()
            .replace("+00:00", "Z")
        }



class SongSchema(PModel):
    name: str = Field(...)
    duration: int = Field(..., lt=0, gt=101)
    uploaded_at: datetime  = Field(..., alias="uploadedAt")
 
    class Config:
        schema_extra = {
            "example": {
                "name": "demo song",
                "duration": 100,
                "uploaded_at": datetime.now(),
            }
        }




class SongSchema(PModel):
    name: str = Field(...)
    duration: int = Field(..., lt=0, gt=101)
    uploaded_at: datetime  = Field(..., alias="uploadedAt")
 
    class Config:
        schema_extra = {
            "example": {
                "name": "demo song",
                "duration": 100,
                "uploaded_at": datetime.now(),
            }
        }
        
        
        
class SongSchema(PModel):
    name: str = Field(...)
    duration: int = Field(..., lt=0, gt=101)
    uploaded_at: datetime  = Field(..., alias="uploadedAt")
 
    class Config:
        schema_extra = {
            "example": {
                "name": "demo song",
                "duration": 100,
                "uploaded_at": datetime.now(),
            }
        }        




class SongSchema(PModel):
    name: str = Field(...)
    duration: int = Field(..., lt=0, gt=101)
    uploaded_at: datetime  = Field(..., alias="uploadedAt")
 
    class Config:
        schema_extra = {
            "example": {
                "name": "demo song",
                "duration": 100,
                "uploaded_at": datetime.now(),
            }
        }




class UpdateSongModel(BaseModel):
    name: Optional[str]    
    duration: Optional[int]

    class Config:
        schema_extra = {
            "example": {        
                "name": "demo song",
                "duration": 100,
            }
        }


