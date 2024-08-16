from .base import BaseUserRepository
from typing import List

from schemas.user import UserCreateDto, UserSchema, UserUpdateDto


class RedisUserRepository(BaseUserRepository):
    async def create(self, create_dto: UserCreateDto) -> UserSchema:
        raise NotImplementedError

    async def read(self, user_id: int) -> UserSchema | None:
        raise NotImplementedError

    async def update(self, user_id: int, update_dto: UserUpdateDto) -> bool:
        raise NotImplementedError

    async def delete(self, id: int) -> bool:
        raise NotImplementedError

    async def all(self) -> List[UserSchema]:
        raise NotImplementedError

