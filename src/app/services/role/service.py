from tortoise.exceptions import DoesNotExist, IntegrityError

from schemas.role import RoleSchema, RoleCreateDto, RoleUpdateDto
from repositories import DatabaseRoleRepository

import logging
from container import container


class RoleService():
    def __init__(self) -> None:
        self._role_repository = container.get(DatabaseRoleRepository)
        self._logger = container.get(logging.Logger)

    async def create(self, dto: RoleCreateDto):
        "### Create position from dto"
        role = await self._role_repository.create(dto=dto)
        return await role.to_schema()

    async def read(self, position_id: int) -> RoleSchema:
        "### Get positon from id"
        position = await self._role_repository.get_or_none(id=position_id)

        if position is None:
            raise DoesNotExist(f'pk={position_id} | Position not found.')
        return await position.to_schema()

    async def update(self, position_id: int, dto: RoleUpdateDto):
        pass

    async def delete(self, position_id: int):
        '''### Delete Position by position_id'''
        position = await self._role_repository.get_or_none(id=position_id)

        if position is None:
            raise DoesNotExist(f'pk={position_id} | Position not found.')
        await position.delete()

        logger.info(f'[{position_id}] Position - DELETE')
