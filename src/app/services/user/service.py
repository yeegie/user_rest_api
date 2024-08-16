from tortoise.exceptions import DoesNotExist, IntegrityError

from schemas.user import UserSchema, UserUpdateDto, UserCreateDto

from container import container
from repositories import DatabaseUserRepository
from services.email import EmailService

import logging


class UserService():
    def __init__(self) -> None:
        self._user_repository = container.get(DatabaseUserRepository)
        self._logger = container.get(logging.Logger)
        self._email_service = EmailService()

    async def read(self, user_id: int) -> UserSchema:
        '''### Get User by user_id'''
        user = await self._user_repository.get_or_none(id=user_id).prefetch_related("position")

        if user is None:
            raise DoesNotExist(f'pk={user_id} | User not found.')
        
        return await user.to_schema()

    async def create(self, dto: UserCreateDto) -> UserSchema:
        '''### Create User from'''
        user = await self._user_repository.create(dto=dto)
        await self.email_service.send_welcome_message(dto.email)

        return await user.to_schema()

    async def update(self, user_id: int, dto: UserUpdateDto) -> UserSchema:
        '''### Update User by id'''
        user = self._user_repository.get_or_none(id=user_id)

        if user is None:
            raise DoesNotExist(f'pk={user_id} | User not found.')

        user.fio = dto.fio
        user.email = dto.email

        await user.save()

        return await user.to_schema()

    async def delete(self, user_id: int) -> None:
        '''### Delete User by user_id'''
        user = await self._user_repository.get_or_none(id=user_id)

        if user is None:
            raise DoesNotExist(f'pk={user_id} | User not found.')
        await user.delete()

        self._logger.info(f'[{user_id}] User - DELETE')

    async def _all(self):
        users = await self._user_repositoryuser.all()
        return [await users.to_schema() for users in users]
