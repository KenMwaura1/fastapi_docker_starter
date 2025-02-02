from pydantic import BaseModel, HttpUrl
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
    class Config:
        orm_mode = True


# Properties to return to client
class Anime(AnimeInBase):
    pass


# Properties to create new anime
class AnimeCreate(AnimeBaseModel):
    pass


# Properties to update existing anime
class AnimeUpdate(AnimeBaseModel):
    pass
