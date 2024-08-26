__all__ = ["BaseRoleRepository"]

from ..base import BaseRepository

from abc import ABC, abstractmethod
from typing import Optional, List

from schemas.role import RoleSchema, RoleCreateDto, RoleUpdateDto


class BaseRoleRepository(BaseRepository, ABC):
    @abstractmethod
    async def create(self, create_dto: RoleCreateDto) -> RoleSchema:
        raise NotImplementedError()

    @abstractmethod
    async def read(self, role_id: int) -> Optional[RoleSchema]:
        raise NotImplementedError()

    @abstractmethod
    async def update(self, role_id: int, update_dto: RoleUpdateDto) -> bool:
        raise NotImplementedError()

    @abstractmethod
    async def delete(self, role_id: int) -> bool:
        raise NotImplementedError()

    @abstractmethod
    async def all(self) -> List[RoleSchema]:
        raise NotImplementedError()
