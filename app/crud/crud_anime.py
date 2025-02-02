from typing import Type
from app.crud.base import CRUDBase
from app.models.anime import Anime as AnimeModel
from app.schema import Anime, AnimeCreate, AnimeUpdate

class CRUDAnime(CRUDBase[AnimeModel, AnimeCreate, AnimeUpdate]):
    def __init__(self, model: Type[AnimeModel]):
        super().__init__(model)

    # Define other CRUD methods here

anime = CRUDAnime(AnimeModel)
