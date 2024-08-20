from .base import BaseUserRepository
from typing import List, Optional, Union
from tortoise import BaseDBAsyncClient
from redis import Redis

from schemas.user import UserCreateDto, UserSchema, UserUpdateDto

import logging


class DatabaseUserRepository(BaseUserRepository):
    def __init__(self, session: Union[BaseDBAsyncClient, Redis], logger: logging.Logger) -> None:
        self._session = session
        self._logger = logger

    async def create(self, create_dto: UserCreateDto) -> UserSchema:
        query = await self._session.ex("INSERT INTO user (fio, email) VALUES (?, ?)", [create_dto.fio, create_dto.email])
        return query

    async def read(self, user_id: int) -> Optional[UserSchema]:
        return await self._session.execute_query(f"SELECT * FROM user WHERE id={user_id}")

    async def update(self, user_id: int, update_dto: UserUpdateDto) -> bool:
        pass

    async def delete(self, user_id: int) -> bool:
        try:
            await self._session.execute_query(f"DELETE FROM user WHERE id={user_id}")
            return True
        except Exception as ex:
            self._logger.error(ex)
            return False

    async def all(self) -> List[UserSchema]:
        return await self._session.execute_query_dict("SELECT * FROM user")
