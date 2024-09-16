from app.repositories.BaseRepository import BaseRepository
from typing import List
import redis.asyncio as redis
import json
import uuid

from app.repositories.schemas import UserCreateDto, UserSchema, UserUpdateDto

import logging


class RedisUserRepository(BaseRepository):
    def __init__(self, session: redis.Redis, logger: logging.Logger) -> None:
        self._session = session
        self._logger = logger

    async def create(self, create_dto: UserCreateDto) -> UserSchema:
        item_id = str(uuid.uuid4())
        item_data = UserSchema(
            id=item_id,
            fio=create_dto.fio,
            email=create_dto.email
        ).model_dump(mode="python")

        await self._session.hmset('users', item_id, item_data)
        return item_data

    async def read(self, user_id: int) -> UserSchema | None:
        return await self._session.hmget('users', user_id)

    async def update(self, user_id: int, update_dto: UserUpdateDto) -> bool:
        """Update user by user_id"""
        try:
            # Check user exists
            existing_user_data = await self._session.hmget('users', user_id)
            if not existing_user_data:
                self._logger.warning(f"[{user_id}] UPDATE User - not found for update.")
                return False
            
            updated_data = {
                'fio': update_dto.fio,
                'email': update_dto.email,
            }

            await self._session.hmset('users', user_id, updated_data)
            return True
        except Exception as ex:
            self._logger.error(f"Failed to update user[{user_id}]: {ex}")
            return False

    async def delete(self, user_id: int) -> bool:
        """Delete user by user_id"""
        try:
            result = await self._session.hdel('users', user_id)
            if result == 1:
                return True
            else:
                self._logger.warning(f"[{user_id}] DELETE User - not found.")
                return False
        except Exception as ex:
            self._logger.error(f"Failed to delete user[{user_id}]: {ex}")
            return False

    async def is_email_unique(self, email: str) -> bool:
        """Check if the email is unique in Redis"""
        cursor = 0
        while True:
            cursor, keys = await self._session.scan(cursor=cursor)
            for key in keys:
                item_data = await self._session.hmget('users', key)
                if item_data:
                    item_dict = json.loads(item_data)
                    if item_dict.get('email') == email:
                        return False
            if cursor == 0:
                break
        return True

    async def all(self) -> List[UserSchema]:
        cursor = 0
        items = []

        while True:
            cursor, keys = await self._session.scan(cursor=cursor) 
            for key in keys:
                item_data = await self._session.hmget('users', key)
                if item_data:
                    item_dict = json.loads(item_data)
                    item = UserSchema(**item_dict)
                    items.append(item)
            if cursor == 0:
                break
        
        return items

