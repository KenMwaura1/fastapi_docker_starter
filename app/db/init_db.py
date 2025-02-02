from pprint import pprint
from sqlalchemy.orm import Session

from app import crud, schema, anime_data
from app.db import base_class
from app.models import Anime
from app.db.session import engine, SessionLocal
from app.crud.base import Base
from datetime import datetime as dt

current_year = dt.now().year
print(current_year)

def init_db(db: SessionLocal) -> None:
    # Create all the tables
    Base.metadata.create_all(bind=engine)
    test_anime = crud.anime.get_multi(db)
    # Add logic to initialize the database with test data if needed

    top_anime = anime_data.get_top_anime()
    all_anime = anime_data.get_anime()
    search_anime = anime_data.search_anime_by_name('naruto')
    
    if not test_anime:
        for anime in top_anime:
            mal_id = anime.get('mal_id')
            if not any(existing.mal_id == mal_id for existing in test_anime):
                new_anime = schema.AnimeCreate(
                    mal_id=mal_id,
                    url=anime.get('url'),
                    title=anime.get('title'),
                    image_url=anime.get('images', {}).get('webp', {}).get('large_image_url'),
                    synopsis=anime.get('synopsis'),
                    type=anime.get('type'),
                    airing_start=anime.get('aired', {}).get('from'),  # Extracting 'aired' -> 'from'
                    episodes=anime.get('episodes'),
                    members=anime.get('members'),
                )
                try:
                    crud.anime.create(db, obj_in=new_anime)
                except Exception as e:
                    print(f"Problem: {e}")
