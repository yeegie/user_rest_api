from abc import ABC, abstractmethod
from app.repositories.BaseRepository import BaseRepository


class BaseRepositoryFactory(ABC):
    @abstractmethod
    def get_instance(self) -> BaseRepository:
        raise NotImplementedError()
