from schemas.user import UserSchema, UserUpdateDto, UserCreateDto
from repositories import BaseUserRepository

from logging import Logger


class UserService():
    def __init__(self, user_repository: BaseUserRepository, logger: Logger) -> None:
        self.__repository = user_repository
        self.__logger = logger

    async def create(self, dto: UserCreateDto) -> UserSchema:
        """### Create User from"""
        return await self.__repository.create(create_dto=dto)
    
    async def read(self, id: int) -> UserSchema:
        """### Get User by user id"""
        return await self.__repository.read(user_id=id)

    async def update(self, id: int, dto: UserUpdateDto) -> UserSchema:
        """### Update User by user id"""
        return await self.__repository.update(user_id=id, update_dto=dto)

    async def delete(self, id: int) -> None:
        """### Delete User by user id"""
        return await self.__repository.delete(user_id=id)

    async def all(self):
        """### Get all users"""
        return await self.__repository.all()
