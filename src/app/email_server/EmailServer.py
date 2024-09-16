from abc import ABC, abstractmethod


class BaseEmailServer(ABC):
    @abstractmethod
    def send_email(self, recipient: str) -> None:
        raise NotImplementedError()
    
    @abstractmethod
    def connect(self) -> None:
        raise NotImplementedError()
    
    @abstractmethod
    def disconnect(self) -> None:
        pass
