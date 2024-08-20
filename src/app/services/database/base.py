from abc import ABC, abstractmethod
from tortoise import BaseDBAsyncClient

from logging import Logger


class BaseDatabaseService(ABC):
    @abstractmethod
    def __init__(self, db_uri: str, logger: Logger) -> None:
        raise NotImplementedError()

    @abstractmethod
    async def init_database(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    async def close_database(self) -> None:
        raise NotImplementedError()
    
    @abstractmethod
    async def get_session(self):
        raise NotImplementedError()
