__all__ = ["MemoryUserRepository"]

from abc import ABC
from typing import Optional, List
from logging import Logger

from schemas.user import UserSchema, UserCreateDto, UserUpdateDto


class MemoryUserRepository(ABC):
    def __init__(self, logger: Logger) -> None:
        self._logger = logger

    async def create(self, create_dto: UserCreateDto) -> UserSchema:
        pass

    async def read(self, user_id: int) -> Optional[UserSchema]:
        pass

    async def update(self, user_id: int, update_dto: UserUpdateDto) -> bool:
        pass

    async def delete(self, user_id: int) -> bool:
        pass

    async def all(self) -> List[UserSchema]:
        pass
