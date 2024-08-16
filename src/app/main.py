from fastapi import FastAPI
from uvicorn import run
from contextlib import asynccontextmanager

from data.app_config import AppConfig

from runner import init_app


@asynccontextmanager
async def lifespan(app: FastAPI):
    # logger.info('[⭐] Starting app...')
    # await database_service.init_database()
    await init_app()

    yield
    
    # logger.info('[👋] Bye')
    # await database_service.close_database()

app = FastAPI(title='USER REST API', debug=True, lifespan=lifespan)

from routers import user_router, role_router
app.include_router(user_router, prefix='/user', tags=['user'])
app.include_router(role_router, prefix='/role', tags=['role'])


if __name__ == '__main__':
    run(app, host=AppConfig.host, port=AppConfig.port)
