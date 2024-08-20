__all__ = ["LocalRoleRepository"]

from abc import ABC
from typing import Optional, List
from logging import Logger

from schemas.role import RoleSchema, RoleCreateDto, RoleUpdateDto


class LocalRoleRepository(ABC):
    def __init__(self, logger: Logger) -> None:
        self.data: List[RoleSchema] = []
        self._logger = logger
        
    async def create(self, create_dto: RoleCreateDto) -> RoleSchema:
        pass

    async def read(self, role_id: int) -> Optional[RoleSchema]:
        pass

    async def update(self, role_id: int, update_dto: RoleUpdateDto) -> bool:
        pass

    async def delete(self, role_id: int) -> bool:
        pass

    async def all(self) -> List[RoleSchema]:
        pass
