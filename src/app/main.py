from fastapi import FastAPI
from uvicorn import run
from contextlib import asynccontextmanager

from data.app_config import API

from database import init_database, close_database
from services import UserService, PositionService

from container import container

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

# Registration dependencies
user_service = UserService()
position_service = PositionService()

container.attach("user_service", user_service)
container.attach("position_service", position_service)

app = FastAPI(title='USER REST API', debug=True, lifespan=lifespan)

from routers import user_router, position_router
app.include_router(user_router, prefix='/user', tags=['user'])
app.include_router(position_router, prefix='/position', tags=['position'])


if __name__ == '__main__':
    run(app, host=API.host, port=API.port)
