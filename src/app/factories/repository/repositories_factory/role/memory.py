from app.repositories.BaseRepository import BaseRepository
from app.repositories.role import MemoryRoleRepository
from ..BaseRepositoryFactory import BaseRepositoryFactory


class MemoryRoleRepositoryFactory(BaseRepositoryFactory):
    def get_instance(self) -> BaseRepository:
        return MemoryRoleRepository()

