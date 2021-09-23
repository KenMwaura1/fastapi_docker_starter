from fastapi import FastAPI, APIRouter

app = FastAPI(title="Starter App", openapi_url="/openapi.json")

api_router = APIRouter()


@api_router.get('/', status_code=200)
def root() -> dict:
    """
    root function
    :return: welcome message
    """
    return {"msg": "Hello Zoo!"}


app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, port=8001, log_level="debug")
