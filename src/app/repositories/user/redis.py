from repositories.base import BaseRepository
from typing import List
import redis.asyncio as redis
import json
import uuid

from schemas.user import UserCreateDto, UserSchema, UserUpdateDto

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
        pass

    async def delete(self, id: int) -> bool:
        pass

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

