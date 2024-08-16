from tortoise.exceptions import DoesNotExist, IntegrityError

from schemas.user import UserSchema, UserUpdateDto, UserCreateDto
from database.models import User

import logging
logger = logging.getLogger(__name__)


class UserService():
    def __init__(self) -> None:
        self.user = User

    async def read(self, user_id: int) -> UserSchema:
        '''### Get User by user_id'''
        user = await self.user.get_or_none(id=user_id).prefetch_related("position")

        print(user)

        if user is None:
            raise DoesNotExist(f'pk={user_id} | User not found.')
        
        return await user.to_schema()

    async def create(self, dto: UserCreateDto) -> UserSchema:
        '''### Create User from'''
        user = await self.user.create(
            fio=dto.fio,
            email=dto.email,
        )

        return await user.to_schema()

    async def update(self, user_id: int, dto: UserUpdateDto) -> UserSchema:
        '''### Update User by id'''
        user = self.user.get_or_none(id=user_id)

        if user is None:
            raise DoesNotExist(f'pk={user_id} | User not found.')

        user.fio = dto.fio
        user.email = dto.email

        await user.save()

        return await user.to_schema()

    async def delete(self, user_id: int) -> None:
        '''### Delete User by user_id'''
        user = await self.user.get_or_none(id=user_id)

        if user is None:
            raise DoesNotExist(f'pk={user_id} | User not found.')
        await user.delete()

        logger.info(f'[{user_id}] User - DELETE')

    async def _all(self):
        users = await self.user.all()
        return [await users.to_schema() for users in users]
