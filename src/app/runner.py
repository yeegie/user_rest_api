__all__ = ["init_app"]

import logging
from logging import Logger

from data import DataBaseConfig

from services import UserService, RoleService, DatabaseServiceFactory, BaseDatabaseService

from repositories import RoleRepositoryFabric, UserRepositoryFabric

from utils.container import container

from fastapi import FastAPI

from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    database_service = container.get(BaseDatabaseService)
    logger = container.get(Logger)

    # DataBase
    await database_service.init_database()
    session = await database_service.get_session()

    # Repositories
    user_repository = UserRepositoryFabric().create_repository(
        DataBaseConfig.db_type,
        session,
        logger
    )
    
    role_repository = RoleRepositoryFabric().create_repository(
        DataBaseConfig.db_type,
        session,
        logger
    )

    # Services
    user_service = UserService(user_repository, logger)
    role_service = RoleService(role_repository, logger)

    # Store in container
    container.attach(key=RoleService, instance=role_service)
    container.attach(key=UserService, instance=user_service)

    yield

    await database_service.close_database()


def init_app() -> FastAPI:
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO)

    logger.info("[⭐] Starting app...")

    # DataBase
    database_service = DatabaseServiceFactory().create_service(
        db_type=DataBaseConfig.db_type,
        db_uri=DataBaseConfig.db_uri,
        logger=logger,
    )

    # Store in container
    container.attach(key=BaseDatabaseService, instance=database_service)
    container.attach(key=Logger, instance=logger)

    # FastAPI app
    app = FastAPI(title='USER REST API', debug=True, lifespan=lifespan)

    from routers import user_router, role_router
    app.include_router(user_router, prefix='/user', tags=['user'])
    app.include_router(role_router, prefix='/role', tags=['role'])

    return app
