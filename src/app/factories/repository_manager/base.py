from abc import ABC, abstractmethod
from repositories.base import BaseRepository
from typing import Mapping


class BaseRepositoryManager(ABC):
    @abstractmethod
    def get(self, database_type: str):
        raise NotImplementedError()
    
    @abstractmethod
    def set(self, database_type: str, repository: BaseRepository):
        raise NotImplementedError()
