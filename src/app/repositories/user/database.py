from .base import BaseUserRepository
from typing import List, Optional

from schemas.user import UserCreateDto, UserSchema, UserUpdateDto


class DatabaseUserRepository(BaseUserRepository):
    def __init__(self) -> None:
        pass

    async def create(self, create_dto: UserCreateDto) -> UserSchema:
        pass

    async def read(self, user_id: int) -> Optional[UserSchema]:
        pass

    async def update(self, user_id: int, update_dto: UserUpdateDto) -> bool:
        pass

    async def delete(self, id: int) -> bool:
        pass

    async def all(self) -> List[UserSchema]:
        pass
