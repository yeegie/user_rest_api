from app.repositories.schemas import RoleSchema, RoleCreateDto, RoleUpdateDto
from app.repositories import BaseRoleRepository
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
        return await self.__repository.read(id)

    async def update(self, id: int, dto: RoleUpdateDto):
        """### Update user from dto by id"""
        return await self.__repository.update(id, dto)

    async def delete(self, id: int):
        """### Delete Role by role_id"""
        return await self.__repository.delete(id)

    async def all(self):
        """### Get all roles"""
        return await self.__repository.all()
