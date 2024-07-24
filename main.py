from fastapi import FastAPI
from uvicorn import run
from contextlib import asynccontextmanager

from data.config import API

from database import init_database, close_database
from routers import user_router

import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info('[⭐] Starting app...')
    await init_database()

    yield
    logger.info('[👋] Bye')
    await close_database()

app = FastAPI(title='USER REST API', debug=True, lifespan=lifespan)
app.include_router(user_router, prefix='/user', tags=['user'])

if __name__ == '__main__':
    run(app, host=API.host, port=API.port)
    pass
