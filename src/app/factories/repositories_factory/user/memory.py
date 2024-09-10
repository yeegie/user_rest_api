from app.repositories.BaseRepository import BaseRepository
from repositories.user import MemoryUserRepository
from ..BaseRepositoryFactory import BaseRepositoryFactory


class MemoryUserRepositoryFactory(BaseRepositoryFactory):
    def get_instance(self) -> BaseRepository:
        return MemoryUserRepository()

