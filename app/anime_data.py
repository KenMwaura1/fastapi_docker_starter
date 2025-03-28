from jikanpy import Jikan

jikan = Jikan()

def get_anime():
    response = jikan.search('anime',query='', page=1)
    return response['data']

def get_top_anime():
    response = jikan.top(type='anime', page=2)
    return response['data']

def get_current_season():
    response = jikan.seasons()
    return response['data']

def get_anime_by_id(id):
    response = jikan.anime(id)
    return response

def get_anime_by_name(name):
    response = jikan.search(type='anime', query=name, page=1)
    return response['data']

def get_anime_by_genre(genre_id):
    response = jikan.genre(type='anime', genre_id=genre_id)
    return response['data']

def get_anime_by_season(year, season):
    response = jikan.seasons(year=year, season=season)
    return response['data']

def get_anime_by_year(year):
    response = jikan.seasons(year=year, season='winter')
    return response['data']

def get_anime_by_producer(producer_id):
    response = jikan.producer(producer_id)
    return response['data']

def search_anime_by_name(name: str):
    response = jikan.search('anime', query=name, page=1)
    return response['data']
