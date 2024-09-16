from abc import ABC, abstractmethod
from ..config_factory.ConfigFactory import BaseConfigFactory


class BaseConfigManager(ABC):
    @abstractmethod
    def set(self, config: BaseConfigFactory):
        raise NotImplementedError
    
    @abstractmethod
    def get(self, filepath: str):
        raise NotImplementedError
    
