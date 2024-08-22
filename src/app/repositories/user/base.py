__all__ = ["UserRepository"]

from abc import ABC, abstractmethod
from typing import Optional, List

from schemas.user import UserSchema, UserCreateDto, UserUpdateDto
from adapters.tortoise.models import User


class BaseUserRepository(ABC):
    @abstractmethod
    async def create(self, create_dto: UserCreateDto) -> UserSchema:
        raise NotImplementedError()

    @abstractmethod
    async def read(self, user_id: int) -> Optional[UserSchema]:
        raise NotImplementedError()

    @abstractmethod
    async def update(self, user_id: int, update_dto: UserUpdateDto) -> bool:
        raise NotImplementedError()

    @abstractmethod
    async def delete(self, user_id: int) -> bool:
        raise NotImplementedError()

    @abstractmethod
    async def all(self) -> List[UserSchema]:
        raise NotImplementedError()
