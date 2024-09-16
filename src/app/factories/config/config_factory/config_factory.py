__all__ = ["IniConfigFactory", "YmlConfigFactory"]

from .config_schemas import ConfigSchema
from .ConfigFactory import BaseConfigFactory

from configparser import ConfigParser
from yaml import safe_load

import os


class IniConfigFactory(BaseConfigFactory):
    @property
    def type(self) -> str:
        return "ini"

    def get_instance(self, filepath: str) -> ConfigSchema:
        parser = ConfigParser()
        parser.read(filepath)

        return ConfigSchema(
            config_type=self.type,
            settings={str.lower(section): dict(parser.items(section)) for section in parser.sections()},
        )


class YmlConfigFactory(BaseConfigFactory):
    @property
    def type(self) -> str:
        return "yml"

    def get_instance(self, filepath: str) -> ConfigSchema:
        # Check file exist
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"File {filepath} not found")
        
        # Safe open file
        with open(filepath, 'r') as file:
            try:
                data = safe_load(file)
            except Exception as e:
                raise ValueError(f"Error loading YAML file: {e}")
            
            if "type" not in data or "settings" not in data:
                raise ValueError("Invalid YAML format: missing 'type' or 'settings' fields")
            
            return ConfigSchema(
                config_type=data["type"],
                settings=data["settings"],
            )
    