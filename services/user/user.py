from .crud import UserCRUD

from tortoise.exceptions import DoesNotExist

from schemas.user import UserSchema, UserUpdateDto, UserCreateDto
from database.models.user import User

import logging
logger = logging.getLogger(__name__)


class UserService(UserCRUD):
    @staticmethod
    async def read(user_id: int) -> UserSchema:
        '''### Get User by user_id'''
        user = await User.get_or_none(id=user_id)
        if user is None:
            raise DoesNotExist(f'pk={user_id} | User not found.')
        return await user.to_schema()

    @staticmethod
    async def create(dto: UserCreateDto) -> UserSchema:
        '''### Create User from'''
        user = await User.create(
            fio=dto.fio,
            email=dto.email,
        )

        return await user.to_schema()

    @staticmethod
    async def update(user_id: int, dto: UserUpdateDto) -> UserSchema:
        '''### Update User by id'''
        user = await User.get_or_none(id=user_id)

        if user is None:
            raise DoesNotExist(f'pk={user_id} | User not found.')

        user.fio = dto.fio
        user.email = dto.email

        await user.save()

        return await user.to_schema()

    @staticmethod
    async def delete(user_id: int) -> None:
        '''### Delete User by user_id'''
        user = await User.get_or_none(id=user_id)

        if user is None:
            raise DoesNotExist(f'pk={user_id} | User not found.')
        await user.delete()

        logger.info(f'[{user_id}] User - DELETE')
