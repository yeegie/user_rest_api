from fastapi import FastAPI
from uvicorn import run
from contextlib import asynccontextmanager

from data.app_config import API

from services import DatabaseService
from data.database_config import DataBase

import logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


database_service = DatabaseService(
    type=DataBase.type,
    host=DataBase.host,
    port=DataBase.port,
    user=DataBase.user,
    password=DataBase.password,
    database=DataBase.database,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info('[⭐] Starting app...')
    await database_service.init_database()

    yield
    logger.info('[👋] Bye')
    await database_service.close_database()

app = FastAPI(title='USER REST API', debug=True, lifespan=lifespan)

from routers import user_router, position_router
app.include_router(user_router, prefix='/user', tags=['user'])
app.include_router(position_router, prefix='/position', tags=['position'])


if __name__ == '__main__':
    run(app, host=API.host, port=API.port)
