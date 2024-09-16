__all__ = ["init_app"]

from fastapi import FastAPI
import logging

from app.utils.ioc import ioc
from app.factories.config import ConfigFactoryManager, IniConfigFactory, DatabaseSettings
from app.factories.repository.repository_manager import RepositoryManager
from app.factories.repository.repositories_factory import DatabaseUserRepositoryFactory, DatabaseRoleRepositoryFactory, MemoryRoleRepositoryFactory, MemoryUserRepositoryFactory
from app.services import UserService, RoleService


def init_app(
        config_path: str
) -> None:
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO)

    # Config
    config_manager = ConfigFactoryManager()
    config_manager.set(IniConfigFactory())
    config = config_manager.get(config_path)

    # Repositories
    repository_manager = RepositoryManager(DatabaseSettings(**config.settings["database"]))

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

    
    repository_type = config.settings["application"]["repository_type"]
    role_repository = repository_manager.get("role", repository_type)
    user_repository = repository_manager.get("user", repository_type)

    # Services
    user_service = UserService(user_repository, logger)
    role_service = RoleService(role_repository, logger)

    # Store in IOC
    ioc.set(logging.Logger, logger)
    ioc.set(UserService, user_service)
    ioc.set(RoleService, role_service)
    # ioc.set(BaseUserRepository, user_repository)
    # ioc.set(BaseRoleRepository, role_repository)
