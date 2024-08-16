from tortoise.exceptions import DoesNotExist, IntegrityError

from schemas.position import PositionSchema, PositionCreateDto, PositionUpdateDto
from database.models import Position

import logging
logger = logging.getLogger(__name__)


class PositionService():
    def __init__(self) -> None:
        self.position = Position

    async def create(self, dto: PositionCreateDto):
        "### Create position from dto"
        position = await self.position.create(
            name=dto.name,
        )

        return await position.to_schema()

    async def read(self, position_id: int):
        "### Get positon from id"
        position = await self.position.get_or_none(id=position_id)

        if position is None:
            raise DoesNotExist(f'pk={position_id} | Position not found.')
        return await position.to_schema()

    async def update(self, position_id: int, dto: PositionUpdateDto):
        pass

    async def delete(self, position_id: int):
        '''### Delete Position by position_id'''
        position = await self.position.get_or_none(id=position_id)

        if position is None:
            raise DoesNotExist(f'pk={position_id} | Position not found.')
        await position.delete()

        logger.info(f'[{position_id}] Position - DELETE')
