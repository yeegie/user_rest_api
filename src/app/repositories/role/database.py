from .base import BaseRoleRepository
from typing import List

from schemas.role import RoleCreateDto, RoleSchema, RoleUpdateDto


class DatabaseRoleRepository(BaseRoleRepository):
    async def create(self, dto: RoleCreateDto) -> RoleSchema:
        raise NotImplementedError

    async def read(self, user_id: int) -> RoleSchema | None:
        raise NotImplementedError

    async def update(self, user_id: int, dto: RoleUpdateDto) -> bool:
        raise NotImplementedError

    async def delete(self, user_id: int) -> bool:
        raise NotImplementedError

    async def all(self) -> List[RoleSchema]:
        raise NotImplementedError
