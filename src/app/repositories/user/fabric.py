__all__ = ["UserRepositoryFabric"]

from .base import BaseUserRepository
from logging import Logger
from . import DatabaseUserRepository, RedisUserRepository


class UserRepositoryFabric:
    @staticmethod
    def create_repository(db_type: str, session, logger: Logger):
        if db_type == "database":
            return DatabaseUserRepository(session, logger)
        elif db_type == "redis":
            return RedisUserRepository(session, logger)
        elif db_type == "memory":
            return None
        else:
            raise ValueError("Unsupported database type.")
