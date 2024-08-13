__all__ = ["UserCRUD"]

from abc import ABC, abstractmethod
from schemas.user import UserCreateDto, UserUpdateDto


class UserCRUD(ABC):
    @abstractmethod
    async def create(dto: UserCreateDto):
        pass

    @abstractmethod
    async def read(id: int):
        pass

    @abstractmethod
    async def update(id: int, dto: UserUpdateDto):
        pass

    @abstractmethod
    async def delete(id: int):
        pass
