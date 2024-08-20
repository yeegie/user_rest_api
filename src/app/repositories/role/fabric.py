__all__ = ["RoleRepositoryFabric"]

from .base import BaseRoleRepository
from logging import Logger
from . import DatabaseRoleRepository, RedisRoleRepository


class RoleRepositoryFabric:
    @staticmethod
    def create_repository(db_type: str, session, logger: Logger):
        if db_type == "database":
            return DatabaseRoleRepository(session, logger)
        elif db_type == "redis":
            return RedisRoleRepository(session, logger)
        elif db_type == "memory":
            return None
        else:
            raise ValueError("Unsupported database type.")
