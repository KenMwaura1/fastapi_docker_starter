from typing import Any, List

from fastapi import FastAPI, APIRouter, Request, Depends, HTTPException
from fastapi.templating import Jinja2Templates

from pathlib import Path

from sqlalchemy.orm import Session 
from starlette.templating import _TemplateResponse

from app import crud, deps
from app.schema import Anime

BASE_PATH = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "static/templates"))

app = FastAPI(title="Starter App", openapi_url="/openapi.json")

api_router = APIRouter()


@api_router.get('/', status_code=200)
def root() -> dict:
    """
    root function
    :return: welcome message
    """
    return {"msg": "Hello Zoo!"}


@api_router.get('/home', status_code=200, response_model=List[Anime])
def home(request: Request, db: Session = Depends(deps.get_db)) -> _TemplateResponse:
    """
    home page get
    :param db:
    :param request:
    :return: home template
    """
    all_anime = crud.anime.get_multi(db=db, limit=20)
    if not all_anime:
        # the exception is raised, not returned - you will get a validation
        # error otherwise.
        raise HTTPException(status_code=404, detail='Anime not found in db')

    # ta = [t for t in get_anime()]
    return TEMPLATES.TemplateResponse("index.html", {"request": request, "all_anime": all_anime})


@api_router.get("/anime/all", status_code=200, response_model=List[Anime]) 
def fetch_all_anime(*, db: Session = Depends(deps.get_db)) -> Any:
    """
    function to fetch all the anime in batches
    :param db:
    :return:
    """
    result = crud.anime.get_multi(db=db, limit=20)
    if not result:
        # the exception is raised, not returned - you will get a validation
        # error otherwise.
        raise HTTPException(status_code=404, detail='Anime not found in db')

    return result


@api_router.get("/anime/{anime_id}", status_code=200, response_model=Anime)
def fetch_anime(*, anime_id: int, db: Session = Depends(deps.get_db)) -> Any:
    """
    function to fetch an anime by id
    :param anime_id:
    :param db:
    :return:
    """
<<<<<<< HEAD
    result = crud.anime.get_by_id(db=db, id=anime_id)
    print(result)
=======
    result = crud.anime.get(db=db, id=anime_id)
>>>>>>> 2a967e7b928f6da9141fc7c1dafc7f5b16f6985f
    if not result:
        # the exception is raised, not returned - you will get a validation
        # error otherwise.
        raise HTTPException(
            status_code=404, detail=f"Anime with ID {anime_id} not found"
        )

    return result

# get anime by name
@api_router.get("/anime/name/{anime_name}", status_code=200, response_model=Anime)
def fetch_anime(*, anime_name: str, db: Session = Depends(deps.get_db)) -> Any:
    """
    function to fetch an anime by id
    :param anime_id:
    :param db:
    :return:
    """
    result = crud.anime.get_multi_by_name(db=db, name=anime_name)
    print(result)
    if not result:
        # the exception is raised, not returned - you will get a validation
        # error otherwise.
        raise HTTPException(
            status_code=404, detail=f"Anime with name {anime_name} not found"
        )

    return result

# get anime by genre
@api_router.get("/anime/genre/{anime_genre}", status_code=200, response_model=Anime)
def fetch_anime(*, anime_genre: str, db: Session = Depends(deps.get_db)) -> Any:
    """
    function to fetch an anime by id
    :param anime_id:
    :param db:
    :return:
    """
    result = crud.anime.get_by_genre(db=db, genre=anime_genre)
    print(result)
    if not result:
        # the exception is raised, not returned - you will get a validation
        # error otherwise.
        raise HTTPException(
            status_code=404, detail=f"Anime with genre {anime_genre} not found"
        )

    return result
app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, port=8001, log_level="debug")
