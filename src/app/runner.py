__all__ = ["init_app"]

from data.database_config import DataBaseConfig
from services.database.service import DatabaseService

from repositories import DatabaseRoleRepository, DatabaseUserRepository

import logging
from logging import Logger

from container import container


async def init_app():
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO)

    # Services
    database_service = DatabaseService(
        type=DataBaseConfig.type,
        host=DataBaseConfig.host,
        port=DataBaseConfig.port,
        user=DataBaseConfig.user,
        password=DataBaseConfig.password,
        database=DataBaseConfig.database,
    )

    session = database_service.get_connection()

    # Repositories
    user_repository = DatabaseUserRepository(session=session, logger=logger)
    role_repository = DatabaseRoleRepository(session=session, logger=logger)

    # Store in container
    container.attach(DatabaseService, database_service)
    
    container.attach(DatabaseUserRepository, user_repository)
    container.attach(DatabaseRoleRepository, role_repository)
    
    container.attach(Logger, logger)

    await database_service.init_database()