from .base import BaseDatabaseService
from logging import Logger


class MemoryDatabaseService(BaseDatabaseService):
    def __init__(self, logger: Logger) -> None:
        self._data = []
        self._logger = logger

    async def init_database(self) -> None:
        self._logger.info("[📦] Database[Memory] is runned...")

    async def close_database(self) -> None:
        pass

    async def get_session(self):
        pass
