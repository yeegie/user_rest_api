__all__ = ["UserRepository"]

from ..BaseRepository import BaseRepository

from abc import ABC, abstractmethod
from typing import Optional, List

from app.repositories.schemas import UserSchema, UserCreateDto, UserUpdateDto


class BaseUserRepository(BaseRepository, ABC):
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
    async def is_email_unique(self, email: str) -> bool:
        raise NotImplementedError()

    @abstractmethod
    async def all(self) -> List[UserSchema]:
        raise NotImplementedError()
