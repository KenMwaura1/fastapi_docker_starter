from typing import Optional
from pydantic import BaseModel, HttpUrl

class AnimeBaseModel(BaseModel):
    mal_id: int
    url: HttpUrl
    title: str
    image_url: str
    synopsis: str
    type: str
    airing_start: Optional[str]  # Make airing_start optional
    episodes: int
    members: int

class AnimeInBase(AnimeBaseModel):
    id: int
    class Config:
        from_attributes = True

class Anime(AnimeInBase):
    pass

class AnimeCreate(AnimeBaseModel):
    pass

class AnimeUpdate(AnimeBaseModel):
    pass
