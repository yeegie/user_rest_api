__all__ = ["DatabaseServiceFactory"]

from logging import Logger
from . import DatabaseService, RedisDatabaseService


class DatabaseServiceFactory:
    @staticmethod
    def create_service(db_type: str, db_uri: str, logger: Logger):
        if db_type == "database":
            return DatabaseService(db_uri, logger)
        elif db_type == "redis":
            return RedisDatabaseService(db_uri, logger)
        elif db_type == "memory":
            return None
