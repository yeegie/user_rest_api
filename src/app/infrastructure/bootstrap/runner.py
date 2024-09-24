__all__ = ["init_app"]

from fastapi import FastAPI
import logging

from .config import get_config
from app.infrastructure.config import RootConfig

from app.utils.ioc import ioc
from app.factories.repository.repository_manager import RepositoryManager
from app.factories.repository.repositories_factory import DatabaseUserRepositoryFactory, DatabaseRoleRepositoryFactory, MemoryRoleRepositoryFactory, MemoryUserRepositoryFactory
from app.services import UserService, RoleService
from app.email_server import EmailServer


def init_app(
        app_config_path: str,
        database_config_path: str,
        smtp_config_path: str,
) -> None:
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO)

    # Config
    config = get_config(
        app_config_path=app_config_path,
        database_config_path=database_config_path,
        smtp_config_path=smtp_config_path,
    )

    # Repositories
    repository_manager = RepositoryManager(config.database)

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

    
    repository_type = config.app.repository_type
    role_repository = repository_manager.get("role", repository_type)
    user_repository = repository_manager.get("user", repository_type)

    # Services
    user_service = UserService(user_repository, logger)
    role_service = RoleService(role_repository, logger)

    # SMTP
    if config.smtp:
        email_server = EmailServer(
            logger=logger,
            config=config.smtp,
        )
        email_server.connect()
        ioc.set(EmailServer, email_server)

    # Store in IOC
    ioc.set(logging.Logger, logger)
    ioc.set(RootConfig, config)
    ioc.set(UserService, user_service)
    ioc.set(RoleService, role_service)
