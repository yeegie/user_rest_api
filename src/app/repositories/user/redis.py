from .base import BaseUserRepository
from typing import List
from tortoise import BaseDBAsyncClient

from schemas.user import UserCreateDto, UserSchema, UserUpdateDto

import logging


class RedisUserRepository(BaseUserRepository):
    def __init__(self, session: BaseDBAsyncClient, logger: logging.Logger) -> None:
        self._session = session
        self._logger = logger

    async def create(self, create_dto: UserCreateDto) -> UserSchema:
        pass

    async def read(self, user_id: int) -> UserSchema | None:
        pass

    async def update(self, user_id: int, update_dto: UserUpdateDto) -> bool:
        pass

    async def delete(self, id: int) -> bool:
        pass

    async def all(self) -> List[UserSchema]:
        pass

