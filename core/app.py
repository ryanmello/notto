from contextlib import asynccontextmanager
from fastapi import FastAPI
from api import notto
from core.database import engine, Base
from models import Note  # Import to register model

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create tables on startup
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

def create_app() -> FastAPI:
    app = FastAPI(lifespan=lifespan)

    app.include_router(notto.router)

    return app
    