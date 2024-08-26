from repositories.base import BaseRepository
from repositories.role import RedisRoleRepository
from ..base import BaseRepositoryFactory


class RedisRoleRepositoryFactory(BaseRepositoryFactory):
    def get_instance(self) -> BaseRepository:
        return RedisRoleRepository()
