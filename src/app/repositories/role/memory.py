__all__ = ["LocalRoleRepository"]

from abc import ABC
from typing import Optional, List
from logging import Logger

from schemas.role import RoleSchema, RoleCreateDto, RoleUpdateDto


class MemoryRoleRepository(ABC):
    def __init__(self) -> None:
        self._data: List[RoleSchema] = []
        
    async def create(self, create_dto: RoleCreateDto) -> RoleSchema:
        id = len(self._data) + 1
        new_role = RoleSchema(
            id=id,
            name=create_dto.name,
        )
        self._data.append(new_role)

        return new_role

    async def read(self, role_id: int) -> Optional[RoleSchema]:
        index = await self._binary_search(role_id)
        if index is None:
            return None
        
        return self._data[index]

    async def update(self, role_id: int, update_dto: RoleUpdateDto) -> bool:
        index = await self._binary_search(role_id)
        if index is None:
            return False
        
        old_role = self._data[index]
        self._data[index] = RoleSchema(
            id=old_role.id,
            name=update_dto.name,
            # user=
        )

        return True

    async def delete(self, role_id: int) -> bool:
        index = await self._binary_search(role_id)
        if index is None:
            return False
        
        try:
            self._data.pop(index)
            return True
        except:
            return False

    async def all(self) -> List[RoleSchema]:
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
