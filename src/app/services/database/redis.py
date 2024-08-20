__all__ = ["RedisDatabaseService"]

from .base import BaseDatabaseService
from logging import Logger

from redis import asyncio as redis


class RedisDatabaseService(BaseDatabaseService):
    def __init__(self, db_uri: str, logger: Logger) -> None:
        self._db_uri = db_uri
        self._logger = logger
        self._session = None

    async def init_database(self) -> None:
        self._session = redis.from_url(url=self._db_uri)
        self._logger.info(f"[📦] Database[{self._db_uri.split(':')[0]}] connected...")

    
    async def close_database(self) -> None:
        await self._session.close()

    async def get_session(self):
        return self._session
    