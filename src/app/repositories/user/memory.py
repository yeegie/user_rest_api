__all__ = ["MemoryUserRepository"]

from abc import ABC
from typing import Optional, List
from schemas import UserSchema, UserCreateDto, UserUpdateDto


class MemoryUserRepository(ABC):
    def __init__(self) -> None:
        self._data: List[UserSchema] = []

    async def create(self, create_dto: UserCreateDto) -> UserSchema:
        id = len(self._data) + 1
        new_user = UserSchema(
            id=id,
            fio=create_dto.fio,
            email=create_dto.email,
            # role=create_dto.role,
        )
        self._data.append(new_user)

        return new_user

    async def read(self, user_id: int) -> Optional[UserSchema]:
        index = await self._binary_search(user_id)
        if index is None:
            return None
        
        return self._data[index]

    async def update(self, user_id: int, update_dto: UserUpdateDto) -> bool:
        index = await self._binary_search(user_id)
        if index is None:
            return False
        
        old_user = self._data[index]
        self._data[index] = UserSchema(
            id=old_user.id,
            fio=update_dto.fio,
            email=update_dto.email,
            # role=
        )

        return True

    async def delete(self, user_id: int) -> bool:
        index = await self._binary_search(user_id)
        if index is None:
            return False
        
        try:
            self._data.pop(index)
            return True
        except:
            return False

    async def all(self) -> List[UserSchema]:
        return self._data
    
    async def _binary_search(self, target_value: int) -> Optional[int]:
        """
        Binary search algorithm

        :return - index of data
        """
        data = self._data

        # If data is empty
        if not data:
            return None
        
        left, right = 0, len(self._data) - 1
        
        while left <= right:
            middle = (left + right) // 2
            middle_value = data[middle]

            if middle_value.id == target_value:
                return middle
            elif middle_value.id < target_value:
                left = middle + 1
            else:
                right = middle - 1        
        return None
