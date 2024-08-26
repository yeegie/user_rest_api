from repositories.base import BaseRepository
from repositories.user import RedisUserRepository
from ..base import BaseRepositoryFactory


class RedisUserRepositoryFactory(BaseRepositoryFactory):
    def get_instance(self) -> BaseRepository:
        return RedisUserRepository()
