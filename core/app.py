from fastapi import FastAPI
from api import notto

def create_app() -> FastAPI:
    app = FastAPI()

    app.include_router(notto.router)

    return app
    