from app.repositories.BaseRepository import BaseRepository
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from schemas import UserCreateDto, UserSchema, UserUpdateDto


class DatabaseUserRepository(BaseRepository):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def create(self, dto: UserCreateDto) -> UserSchema:
        sql = text("INSERT INTO users (fio, email) "
                   "VALUES (:fio, :email) "
                   "RETURNING id")
        async with self._session.begin():
            result = await self._session.execute(sql, {
                'fio': dto.fio,
                'email': dto.email,
            })
            user_id = result.scalar_one()
            return UserSchema(id=user_id, **dto.model_dump())

    async def read(self, id: int) -> Optional[UserSchema]:
        sql = text("SELECT * " 
                   "FROM users "
                   "WHERE id = :id")
        async with self._session.begin():
            result = await self._session.execute(sql, {'id': id})
            row = result.fetchone()
            if row:
                return UserSchema(id=row[0], fio=row[1], email=row[2])
        return None

    async def update(self, id: int, dto: UserUpdateDto) -> bool:
        pass

    async def delete(self, id: int) -> bool:
        try:
            sql = text("DELETE FROM users "
                       "WHERE id = :id")
            async with self._session.begin():
                result = await self._session.execute(sql, {"id": id})
                return True
        except Exception as ex:
            return False

    async def all(self) -> List[UserSchema]:
        sql = text("SELECT * "
                   "FROM users "
                   "LEFT JOIN roles ON users.role_id = roles.id")
        async with self._session.begin():
            result = await self._session.execute(sql)
            rows = result.fetchall()
            return [UserSchema(id=row[0], fio=row[1], email=row[2]) for row in rows]
