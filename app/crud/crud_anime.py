from typing import Type
from app.crud.base import CRUDBase
from app.schema import Anime, AnimeCreate, AnimeUpdate

class CRUDAnime(CRUDBase[Anime, AnimeCreate, AnimeUpdate]):
    def __init__(self, model: Type[Anime]):
        super().__init__(model)

    # Define other CRUD methods here

anime = CRUDAnime(Anime)
