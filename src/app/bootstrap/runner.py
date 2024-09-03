__all__ = ["init_app", "configurate_app"]

from fastapi import FastAPI
import logging

from data.database_config import database_config

from utils.container import ioc
from factories.repository_manager import RepositoryManager
from factories.repositories_factory import DatabaseUserRepositoryFactory, DatabaseRoleRepositoryFactory, MemoryRoleRepositoryFactory, MemoryUserRepositoryFactory
from services import UserService, RoleService
from repositories import BaseRoleRepository, BaseUserRepository


def init_app() -> FastAPI:
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO)

    # Repositories
    repository_manager = RepositoryManager()

    # Database type
    repository_manager.set(entity="user",
                           database_type="database",
                           repository=DatabaseUserRepositoryFactory())
    
    repository_manager.set(entity="role",
                           database_type="database",
                           repository=DatabaseRoleRepositoryFactory())
    
    # Memory type
    repository_manager.set(entity="user",
                           database_type="memory",
                           repository=MemoryUserRepositoryFactory())
    
    repository_manager.set(entity="role",
                           database_type="memory",
                           repository=MemoryRoleRepositoryFactory())

    role_repository = repository_manager.get("role", database_config.db_type)
    user_repository = repository_manager.get("user", database_config.db_type)

    # Services
    user_service = UserService(user_repository, logger)
    role_service = RoleService(role_repository, logger)

    app = FastAPI(title='USER REST API', debug=True)

    from routers import UserRouter, RoleRouter

    user_router = UserRouter(user_service)
    role_router = RoleRouter(role_service)

    app.include_router(user_router, prefix='/user', tags=['user'])
    app.include_router(role_router, prefix='/role', tags=['role'])

    # Store in IOC
    ioc.set(UserService, user_service)
    ioc.set(RoleService, role_service)
    ioc.set(logging.Logger, logger)
    # ioc.set(BaseUserRepository, user_repository)
    # ioc.set(BaseRoleRepository, role_repository)

    return app
