__all__ = ["UserCRUD"]

from abc import ABC, abstractmethod
from schemas.user import UserCreateDto, UserUpdateDto


class UserCRUD(ABC):
    @abstractmethod
    async def create(self, dto: UserCreateDto):
        pass

    @abstractmethod
    async def read(self, id: int):
        pass

    @abstractmethod
    async def update(self, id: int, dto: UserUpdateDto):
        pass

    @abstractmethod
    async def delete(self, id: int):
        pass

    @abstractmethod
    async def _all(self):
        """Get all users"""
        pass
    