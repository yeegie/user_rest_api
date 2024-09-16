from app.repositories.schemas import UserSchema, UserUpdateDto, UserCreateDto
from app.repositories import BaseUserRepository

from app.email_server import EmailServer
from utils.ioc import ioc

from logging import Logger


class UserService():
    def __init__(self, user_repository: BaseUserRepository, logger: Logger) -> None:
        self.__repository = user_repository
        self.__logger = logger

    async def create(self, dto: UserCreateDto) -> UserSchema:
        """### Create User from"""
        unique = await self.__repository.is_email_unique(dto.email)
        if unique is False:
            raise ValueError(f"User with email {dto.email} already exists.")

        created_user = await self.__repository.create(dto)
        
        email_server = ioc.get(EmailServer)
        email_server.send_email(
            dto.email,
            "Welcome Message",
            f"Hello, {dto.fio}!",
        )

        return created_user
    
    async def read(self, id: int) -> UserSchema:
        """### Get User by user id"""
        return await self.__repository.read(id)

    async def update(self, id: int, dto: UserUpdateDto) -> UserSchema:
        """### Update User by user id"""
        return await self.__repository.update(id, dto)

    async def delete(self, id: int) -> None:
        """### Delete User by user id"""
        return await self.__repository.delete(id)

    async def all(self):
        """### Get all users"""
        return await self.__repository.all()
