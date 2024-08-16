__all__ = ["BaseRoleRepository"]

from abc import ABC, abstractmethod
from typing import Optional, List

from schemas.role import RoleSchema, RoleCreateDto, RoleUpdateDto


class BaseRoleRepository(ABC):
    @abstractmethod
    async def create(self, create_dto: RoleCreateDto) -> RoleSchema:
        raise NotImplementedError()

    @abstractmethod
    async def read(self, user_id: int) -> Optional[RoleSchema]:
        raise NotImplementedError()

    @abstractmethod
    async def update(self, user_id: int, update_dto: RoleUpdateDto) -> bool:
        raise NotImplementedError()

    @abstractmethod
    async def delete(self, id: int) -> bool:
        raise NotImplementedError()

    @abstractmethod
    async def all(self) -> List[RoleSchema]:
        raise NotImplementedError()
