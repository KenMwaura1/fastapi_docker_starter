from typing import Any, Dict
import asyncio
from jikanpy import AioJikan, Jikan

jikan = Jikan()


def get_anime():
    sn = jikan.seasons(extension='now')
    data = sn.get('data')
    print("Here")
    print(data)
    return data

def get_top_anime():
    sn = jikan.top(type='anime')
    data = sn.get('data')
    print("Here")
    print(data)
    return data

def get_anime_by_id(id):
    sn = jikan.anime(id)
    data = sn
    print(data)
    return data

def get_anime_by_name(name):
    sn = jikan.search('anime', name)
    data = sn.get('results')
    print(data)
    return data

def get_anime_by_genre(genre):
    sn = jikan.genres(type='anime', filter=genre)
    data = sn.get('data')
    print(data)
    return data

def get_anime_by_season(year, season):
    sn = jikan.seasons(year=year,
        season='winter',
        # page=2,
        parameters={'filter': 'tv'})
    data = sn.get('data')
    print(data)
    return data

def get_anime_by_year(year):
    sn = jikan.seasons(year=year)
    data = sn.get('data')
    print(data)
    return data

def get_anime_by_producer(producer):
    sn = jikan.producer(producer)
    data = sn.get('data')
    print(data)
    return data

def search_anime_by_name(name):
    sn = jikan.search('anime', name)
    data = sn.get('data')
    print(data)
    return data
# search_anime_by_name('jojo')
# print(get_top_anime()[0].get('images').get('webp').get('large_image_url'))


"""
async def main() -> Any:
    async with AioJikan() as aiojikan:
        latest_season: Any = await aiojikan.season()
        print(latest_season.get('anime')[0])
        print("here")
        return await latest_season


# asyncio.run(main())
# fn = main()
loop = asyncio.get_event_loop()


async def get_anime():
    fn = asyncio.run(main())
    t1 = main()
    await fn
    print(t1)
    return await t1

m = asyncio.wait(get_anime())
print(m)"""
