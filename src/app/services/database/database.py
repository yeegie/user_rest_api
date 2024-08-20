__all__ = ["DatabaseService"]

from .base import BaseDatabaseService
from tortoise import Tortoise, connections
from logging import Logger


class DatabaseService(BaseDatabaseService):
    def __init__(self, db_uri: str, logger: Logger) -> None:
        self._db_uri = db_uri
        self._logger = logger

        self._session = None

    async def init_database(self) -> None:
        await Tortoise.init(
            db_url=self._db_uri,
            modules={'models': ['database.models']}
        )
        await Tortoise.generate_schemas()
        self._session = connections.get("default")
        self._logger.info(f"[📦] Database[{self._db_uri.split(':')[0]}] connected...")

    async def close_database(self) -> None:
        await Tortoise.close_connections()

    async def get_session(self):
        if self._session is None:
            self._logger.critical("Session is None")
            raise ValueError("Session is None")
        
        return self._session
