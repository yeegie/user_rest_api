from .BaseConfigManager import BaseConfigManager
from ..config_factory.config_factory import BaseConfigFactory
from ..config_factory.config_schemas import ConfigSchema
from typing import Dict
import os


class ConfigFactoryManager(BaseConfigManager):
    def __init__(self):
        self.storage_: Dict[str, BaseConfigFactory] = {}

    def set(self, config: BaseConfigFactory):
        if config.type not in self.storage_:
            self.storage_[config.type] = config
        else:
            raise Exception(f"Config {config} already registered")


    def get(self, filepath: str) -> ConfigSchema:
        file_extension = os.path.splitext(filepath)[-1].lower().lstrip('.')
        if file_extension in self.storage_:
            return self.storage_[file_extension].get_instance(filepath=filepath)

        raise Exception(f"Config for format .{file_extension} not found.")