from typing import List, Optional
from tortoise.exceptions import DoesNotExist

from schemas.user import UserSchema, UserUpdateDto, UserCreateDto
from database.models.User import User
import logging

logger = logging.getLogger(__name__)


class UserService:
    @staticmethod
    async def get(id: int) -> UserSchema:
        '''### Get User by id'''
        user = await User.get_or_none(id=id)
        if user is None:
            raise DoesNotExist(f'pk={id} | User not found.')
        return await user.to_schema()

    @staticmethod
    async def create(dto: UserCreateDto) -> UserSchema:
        '''### Create User by id'''
        user = await User.create(
            fio=dto.fio,
        )

        return await user.to_schema()

    @staticmethod
    async def update(id: int, dto: UserUpdateDto) -> UserSchema:
        '''### Update User by id'''
        user = await User.get_or_none(id=id)

        if user is None:
            raise DoesNotExist(f'pk={id} | User not found.')

        user.fio = dto.fio
        await user.save()

        return await user.to_schema()

    @staticmethod
    async def delete(id: int) -> None:
        '''### Delete User by id'''
        user = await User.get_or_none(id=id)

        if user is None:
            raise DoesNotExist(f'pk={id} | User not found.')
        await user.delete()

        logger.info(f'[{id}] User - DELETE')
