from .base import BasePositionRepository
from typing import List

from schemas.position import PositionCreateDto, PositionSchema, PositionUpdateDto


class PositionRepository(BasePositionRepository):
    async def create(self, create_dto: PositionCreateDto) -> PositionSchema:
        raise NotImplementedError

    async def read(self, user_id: int) -> PositionSchema | None:
        raise NotImplementedError

    async def update(self, user_id: int, update_dto: PositionUpdateDto) -> bool:
        raise NotImplementedError

    async def delete(self, id: int) -> bool:
        raise NotImplementedError

    async def all(self) -> List[PositionSchema]:
        raise NotImplementedError
