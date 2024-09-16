from app.repositories.BaseRepository import BaseRepository
from app.repositories.role import RedisRoleRepository
from ..BaseRepositoryFactory import BaseRepositoryFactory


class RedisRoleRepositoryFactory(BaseRepositoryFactory):
    def get_instance(self) -> BaseRepository:
        return RedisRoleRepository()
