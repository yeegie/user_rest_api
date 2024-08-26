from repositories.base import BaseRepository
from repositories.role import MemoryRoleRepository
from ..base import BaseRepositoryFactory


class MemoryRoleRepositoryFactory(BaseRepositoryFactory):
    def get_instance(self) -> BaseRepository:
        return MemoryRoleRepository()

