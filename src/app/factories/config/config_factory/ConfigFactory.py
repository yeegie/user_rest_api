__all__ = ["BaseConfigFactory"]

from abc import ABC, abstractmethod
from .config_schemas import ConfigSchema


class BaseConfigFactory(ABC):
    @classmethod
    @abstractmethod
    def type(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def get_instance(self, filepath: str) -> ConfigSchema:
        raise NotImplementedError
