__all__ = ['PositionCRUD']

from abc import ABC, abstractmethod
from schemas.position import PositionCreateDto, PositionUpdateDto


class PositionCRUD(ABC):
    @abstractmethod
    async def create(dto: PositionCreateDto):
        pass

    @abstractmethod
    async def read(id: int):
        pass

    @abstractmethod
    async def update(id: int, dto: PositionUpdateDto):
        pass

    @abstractmethod
    async def delete(id: int):
        pass
