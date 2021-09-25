from typing import Any, List

from fastapi import FastAPI, APIRouter, Request, Depends, HTTPException
from fastapi.templating import Jinja2Templates

from pathlib import Path

from sqlalchemy.orm import Session

from app import crud, deps
from app.schema import Anime
from .anime_data import get_anime

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
def home(request: Request, db: Session = Depends(deps.get_db)) -> dict:
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
    return TEMPLATES.TemplateResponse("index.html", {"request": request, "all_anime": all_anime}, )


@api_router.get("/anime/all", status_code=200, response_model=List[Anime])
def fetch_anime(*, db: Session = Depends(deps.get_db)) -> Any:
    """
    function to fetch all the anime in batches
    :param anime_id:
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
    result = crud.anime.get(db=db, id=anime_id)
    print(result)
    if not result:
        # the exception is raised, not returned - you will get a validation
        # error otherwise.
        raise HTTPException(
            status_code=404, detail=f"Anime with ID {anime_id} not found"
        )

    return result


app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, port=8001, log_level="debug")
