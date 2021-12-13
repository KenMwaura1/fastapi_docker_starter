from app.crud.base import CRUDBase
from app.models import Anime
from app.schema import AnimeCreate


class CRUDAnime(CRUDBase[Anime, AnimeCreate]):
    ...


anime = CRUDAnime(Anime)
