
from sqlalchemy.orm import Session

from app import crud, schema, anime_data
from app.db import base_class
from app.models import Anime
from app.db.session import engine, SessionLocal
from app.crud.base import Base


def init_db(db: Session) -> None:  # sourcery skip: merge-nested-ifs
    # Create all the tables
    Base.metadata.create_all(bind=engine)
    test_anime = crud.anime.get_multi(SessionLocal())
    # print(test_anime)
    print(anime_data.get_anime()[0])
    if not test_anime:
        for anime in anime_data.get_anime():
            if test_anime is not anime.get('mal_id'):

                new_anime = schema.AnimeCreate(
                    mal_id=anime.get('mal_id'),
                    url=anime.get('url'),
                    title=anime.get('title'),
                    image_url=anime.get('image_url'),
                    synopsis=anime.get('synopsis'),
                    type=anime.get('type'),
                    airing_start=anime.get('airing_start'),
                    episodes=anime.get('episodes'),
                    members=anime.get('members'),
                )
                # print(new_anime)
                try:
                    crud.anime.create(db, obj_in=new_anime)
                except Exception as e:
                    print(f"Problem:{e}")


