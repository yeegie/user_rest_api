from abc import ABC, abstractmethod
from typing import List, Optional


class BaseRepository(ABC):
    @abstractmethod
    async def create(self, dto: any) -> any:
        raise NotImplementedError()

    @abstractmethod
    async def read(self, id: int) -> Optional[any]:
        raise NotImplementedError()

    @abstractmethod
    async def update(self, id: int, dto: any) -> bool:
        raise NotImplementedError()

    @abstractmethod
    async def delete(self, id: int) -> bool:
        raise NotImplementedError()

    @abstractmethod
    async def all(self) -> List[any]:
        raise NotImplementedError()
