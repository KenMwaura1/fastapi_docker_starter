from pydantic import BaseModel, HttpUrl
from dataclasses import dataclass


class AnimeBaseModel(BaseModel):
    mal_id: int
    url: HttpUrl
    title: str
    image_url: str
    synopsis: str
    type: str
    airing_start: str
    episodes: int
    members: int


# Properties shared by models stored in DB
class AnimeInBase(AnimeBaseModel):
    id: int
    mal_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Anime(AnimeInBase):
    pass


# Properties to create new anime
@dataclass
class AnimeCreate:
    mal_id: int
    url: HttpUrl
    title: str
    image_url: str
    synopsis: str
    type: str
    airing_start: str
    episodes: int
    members: int
