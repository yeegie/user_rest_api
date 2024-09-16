from .BaseRoleRepository import BaseRoleRepository
from abc import ABC

from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from app.repositories.schemas import RoleCreateDto, RoleSchema, RoleUpdateDto

from logging import Logger


class DatabaseRoleRepository(BaseRoleRepository, ABC):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def create(self, dto: RoleCreateDto) -> RoleSchema:
        sql = text("INSERT INTO roles (name) "
                   "VALUES (:name) "
                   "RETURNING id")
        async with self._session.begin():
            result = await self._session.execute(sql, {
                "name": dto.name,
            })
            role_id = result.scalar_one()
            return RoleSchema(id=role_id, **dto.model_dump())

    async def read(self, id: int) -> Optional[RoleSchema]:
        sql = text("SELECT * " 
                   "FROM roles "
                   "WHERE id = :id")
        async with self._session.begin():
            result = await self._session.execute(sql, {'id': id})
            row = result.fetchone()
            if row:
                return RoleSchema(id=row[0], name=row[1])
        return None

    async def update(self, id: int, dto: RoleUpdateDto) -> bool:
        pass

    async def delete(self, id: int) -> bool:
        try:
            sql = text("DELETE FROM roles "
                       "WHERE id = :id")
            async with self._session.begin():
                result = await self._session.execute(sql, {"id": id})
                return True
        except Exception as ex:
            return False

    async def all(self) -> List[RoleSchema]:
        sql = text("SELECT * "
                   "FROM roles ")
        async with self._session.begin():
            result = await self._session.execute(sql)
            rows = result.fetchall()
            return [RoleSchema(id=row[0], name=row[1]) for row in rows]
