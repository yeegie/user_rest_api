from app.repositories.BaseRepository import BaseRepository
from app.repositories.user import RedisUserRepository
from ..BaseRepositoryFactory import BaseRepositoryFactory


class RedisUserRepositoryFactory(BaseRepositoryFactory):
    def get_instance(self) -> BaseRepository:
        return RedisUserRepository()
