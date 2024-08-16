__all__ = ["BasePositionRepository"]

from abc import ABC, abstractmethod
from typing import Optional, List

from schemas.position import PositionSchema, PositionCreateDto, PositionUpdateDto
from database.models import Position


class BasePositionRepository(ABC):
    @abstractmethod
    async def create(self, create_dto: PositionCreateDto) -> PositionSchema:
        raise NotImplementedError()

    @abstractmethod
    async def read(self, user_id: int) -> Optional[PositionSchema]:
        raise NotImplementedError()

    @abstractmethod
    async def update(self, user_id: int, update_dto: PositionUpdateDto) -> bool:
        raise NotImplementedError()

    @abstractmethod
    async def delete(self, id: int) -> bool:
        raise NotImplementedError()

    @abstractmethod
    async def all(self) -> List[PositionSchema]:
        raise NotImplementedError()
