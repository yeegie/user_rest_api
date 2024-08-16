from .base import BaseRoleRepository
from typing import List
from tortoise import BaseDBAsyncClient

from schemas.role import RoleCreateDto, RoleSchema, RoleUpdateDto

import logging


class DatabaseRoleRepository(BaseRoleRepository):
    def __init__(self, session: BaseDBAsyncClient, logger: logging.Logger) -> None:
        self._session = session
        self._logger = logger

    async def create(self, dto: RoleCreateDto) -> RoleSchema:
        pass

    async def read(self, user_id: int) -> RoleSchema | None:
        pass

    async def update(self, user_id: int, dto: RoleUpdateDto) -> bool:
        pass

    async def delete(self, user_id: int) -> bool:
        pass

    async def all(self) -> List[RoleSchema]:
        pass
