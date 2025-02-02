<<<<<<< HEAD

from pprint import pprint
=======
>>>>>>> 2a967e7b928f6da9141fc7c1dafc7f5b16f6985f
from sqlalchemy.orm import Session

from app import crud, schema, anime_data
from app.db import base_class
from app.models import Anime
from app.db.session import engine, SessionLocal
from app.crud.base import Base
from datetime import datetime as dt

current_year = dt.now().year
print(current_year)

def init_db(db: Session) -> None:
    # Create all the tables
    Base.metadata.create_all(bind=engine)
<<<<<<< HEAD
    test_anime = crud.anime.get_multi(SessionLocal())

    # print(test_anime)
    print('test')
    #print(anime_data.get_anime())
    top_anime = anime_data.get_top_anime()
    all_anime = anime_data.get_anime()
    search_anime = anime_data.search_anime_by_name('naruto')
    shounnen_anime = anime_data.get_anime_by_genre('shounen')
    yearly_anime = anime_data.get_anime_by_season(f"{current_year}",season='winter')
    for anime in top_anime:
            if test_anime is not anime.get('mal_id'):

=======
    test_anime = crud.anime.get_multi(db)
    # Add logic to initialize the database with test data if needed
    
    top_anime = anime_data.get_top_anime()
    
    if not test_anime:
        for anime in top_anime:
            print(anime)
            print(f"Adding {anime.get('title')} to the database")
            crud.anime.create(db, obj_in=schema.AnimeCreate(title=anime.get('title')))
            mal_id = anime.get('mal_id')
            if not any(existing.mal_id == mal_id for existing in test_anime):
>>>>>>> 2a967e7b928f6da9141fc7c1dafc7f5b16f6985f
                new_anime = schema.AnimeCreate(
                    mal_id=mal_id,
                    url=anime.get('url'),
                    title=anime.get('title'),
                    image_url=anime.get('images', {}).get('webp', {}).get('large_image_url'),
                    synopsis=anime.get('synopsis'),
                    type=anime.get('type'),
                    airing_start=anime.get('airing_start'),  # This field is now optional
                    episodes=anime.get('episodes'),
                    members=anime.get('members'),
                )
                try:
                    crud.anime.create(db, obj_in=new_anime)
                except Exception as e:
                    print(f"Problem: {e}")

    for anime in all_anime:
        if test_anime is not anime.get('mal_id'):
            new_anime = schema.AnimeCreate(
                mal_id=anime.get('mal_id'),
                url=anime.get('url'),
                title=anime.get('title'),
                image_url=anime.get('images').get('webp').get('large_image_url'),
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

    for anime in search_anime:
        new_anime = schema.AnimeCreate(
            mal_id=anime.get('mal_id'),
            url=anime.get('url'),
            title=anime.get('title'),
            image_url=anime.get('images').get('webp').get('large_image_url'),
            synopsis=anime.get('synopsis'),
            type=anime.get('type'),
            airing_start=anime.get('airing_start'),
            episodes=anime.get('episodes'),
            members=anime.get('members'),
        )
        #pprint(new_anime)
        try:
            crud.anime.create(db, obj_in=new_anime)
        except Exception as e:
            print(f"Problem:{e}")
    
    for anime in shounnen_anime:
        new_anime = schema.AnimeCreate(
            mal_id=anime.get('mal_id'),
            url=anime.get('url'),
            title=anime.get('title'),
            image_url=anime.get('images').get('webp').get('large_image_url'),
            synopsis=anime.get('synopsis'),
            type=anime.get('type'),
            airing_start=anime.get('airing_start'),
            episodes=anime.get('episodes'),
            members=anime.get('members'),
        )
        pprint(new_anime)
        try:
            crud.anime.create(db, obj_in=new_anime)
        except Exception as e:
            print(f"Problem:{e}")
    
    for anime in yearly_anime:
        new_anime = schema.AnimeCreate(
            mal_id=anime.get('mal_id'),
            url=anime.get('url'),
            title=anime.get('title'),
            image_url=anime.get('images').get('webp').get('large_image_url'),
            synopsis=anime.get('synopsis'),
            type=anime.get('type'),
            airing_start=anime.get('airing_start'),
            episodes=anime.get('episodes'),
            members=anime.get('members'),
        )
        pprint(new_anime)
        try:
            crud.anime.create(db, obj_in=new_anime)
        except Exception as e:
            print(f"Problem:{e}")
    
