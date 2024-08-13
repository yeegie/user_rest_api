from .crud import PositionCRUD

from tortoise.exceptions import DoesNotExist, IntegrityError

from schemas.position import PositionSchema, PositionCreateDto, PositionUpdateDto
from database.models import Position

import logging
logger = logging.getLogger(__name__)


class PositionService(PositionCRUD):
    async def create(dto: PositionCreateDto):
        "### Create position from dto"
        position = await Position.create(
            name=dto.name,
        )

        return await position.to_schema()

    async def read(position_id: int):
        "### Get positon from id"
        position = await Position.get_or_none(id=id)

        if position is None:
            raise DoesNotExist(f'pk={position_id} | Position not found.')
        return await position.to_schema()

    async def update(position_id: int, dto: PositionUpdateDto):
        pass

    async def delete(position_id: int):
        '''### Delete Position by position_id'''
        position = await Position.get_or_none(id=position_id)

        if position is None:
            raise DoesNotExist(f'pk={position_id} | Position not found.')
        await position.delete()

        logger.info(f'[{position_id}] Position - DELETE')
