from abc import ABC, abstractmethod


class BaseEmailService(ABC):
    @abstractmethod
    async def send_welcome_message(self, recipient: str) -> None:
        raise NotImplementedError()
    

    async def send_code(self, recipient: str, code: int) -> None:
        raise NotImplementedError()
