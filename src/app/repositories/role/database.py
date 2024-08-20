from .base import BaseRoleRepository
from abc import ABC

from typing import List, Union
from tortoise import BaseDBAsyncClient
from redis import Redis

from schemas.role import RoleCreateDto, RoleSchema, RoleUpdateDto

from logging import Logger


class DatabaseRoleRepository(BaseRoleRepository, ABC):
    def __init__(self, session: Union[BaseDBAsyncClient, Redis], logger: Logger) -> None:
        self._session = session
        self._logger = logger

    async def create(self, dto: RoleCreateDto) -> RoleSchema:
        query = await self._session.execute_query("INSERT INTO role (name, user_id) VALUES (?, ?)", [dto.name, dto.user_id])
        return query

    async def read(self, role_id: int) -> RoleSchema | None:
        return await self._session.execute_query_dict(f"SELECT * FROM user WHERE id={role_id}")

    async def update(self, role_id: int, dto: RoleUpdateDto) -> bool:
        pass

    async def delete(self, role_id: int) -> bool:
        try:
            await self._session.execute_query(f"DELETE FROM user WHERE id={role_id}")
            return True
        except Exception as ex:
            self._logger.error(ex)
            return False

    async def all(self):  #  -> List[RoleSchema]
        return await self._session.execute_query("SELECT * FROM role")