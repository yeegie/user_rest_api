from .BaseRoleRepository import BaseRoleRepository
from abc import ABC
from typing import List, Optional
from schemas.role import RoleCreateDto, RoleSchema, RoleUpdateDto

import redis.asyncio as redis
from logging import Logger

import json


class RedisRoleRepository(BaseRoleRepository, ABC):
    def __init__(self, session: redis.Redis, logger: Logger) -> None:
        self._session = session
        self._logger = logger
        
    async def create(self, dto: RoleCreateDto) -> RoleSchema:
        length = await self._session.llen("database")
        self._session.hmset(length + 1, dto.model_dump())
        return dto

    async def read(self, user_id: int) -> Optional[RoleSchema]:
        pass

    async def update(self, user_id: int, dto: RoleUpdateDto) -> bool:
        pass

    async def delete(self, user_id: int) -> bool:
        await self._session.delete(user_id)

    async def all(self) -> List[RoleSchema]:
        cursor = 0
        items = []

        while True:
            cursor, keys = await self._session.scan(cursor=cursor) 
            for key in keys:
                item_data = await self._session.get(key)
                if item_data:
                    item_dict = json.loads(item_data)
                    item = RoleSchema(**item_dict)
                    items.append(item)
            if cursor == 0:
                break
        
        return items
