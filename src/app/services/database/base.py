from abc import ABC, abstractmethod
from tortoise import BaseDBAsyncClient


class BaseDatabaseService(ABC):
    @abstractmethod
    def __init__(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    async def init_database(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    async def close_database(self) -> None:
        raise NotImplementedError()
    
    @abstractmethod
    def create_connection_string(self, database_type: str) -> str:
        raise NotImplementedError()
    
    @abstractmethod
    async def get_connection(self) -> BaseDBAsyncClient:
        raise NotImplementedError()
