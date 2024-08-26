from abc import ABC, abstractmethod
from repositories.base import BaseRepository


class BaseRepositoryFactory(ABC):
    @abstractmethod
    def get_instance(self) -> BaseRepository:
        raise NotImplementedError()
