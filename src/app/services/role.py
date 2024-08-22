from schemas.role import RoleSchema, RoleCreateDto, RoleUpdateDto
from repositories import BaseRoleRepository
from logging import Logger


class RoleService():
    def __init__(self, role_repository: BaseRoleRepository, logger: Logger) -> None:
        self.__repository = role_repository
        self.__logger = logger

    async def create(self, dto: RoleCreateDto):
        """### Create position from dto"""
        return await self.__repository.create(dto)

    async def read(self, id: int) -> RoleSchema:
        """### Get positon from id"""
        return await self.__repository.read(role_id=id)

    async def update(self, id: int, dto: RoleUpdateDto):
        """### Update user from dto by id"""
        return await self.__repository.update(role_id=id, dto=dto)

    async def delete(self, id: int):
        """### Delete Role by role_id"""
        return await self.__repository.delete(role_id=id)

    async def all(self):
        """### Get all roles"""
        return await self.__repository.all()
