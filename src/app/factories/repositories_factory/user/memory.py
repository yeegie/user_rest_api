from repositories.base import BaseRepository
from repositories.user import MemoryUserRepository
from ..base import BaseRepositoryFactory


class MemoryUserRepositoryFactory(BaseRepositoryFactory):
    def get_instance(self) -> BaseRepository:
        return MemoryUserRepository()

