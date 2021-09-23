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


class AnimeInBase(AnimeBaseModel):
    id: int
    mal_id: int

    class Config:
        orm_mode = True


class Anime(AnimeInBase):
    pass
