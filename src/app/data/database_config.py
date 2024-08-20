from configparser import ConfigParser
from .config_parser import get_parser

from enum import StrEnum


class DatabaseTypes(StrEnum):
        DATABASE = "database"
        REDIS = "redis"
        MEMORY = "memory"


class DataBaseConfig:
    """
    ### Store the database settings

    @properties:
    1. type
    2. host
    3. port
    4. user
    5. pasword
    6. database
    """        
    def __init__(self, parser: ConfigParser) -> None:
        self.__parser = parser
        self.__section = "DataBase"

        self.db_type = parser.get(self.__section, "db_type")
        self.db_uri = parser.get(self.__section, "db_uri")

        # If type database is incorrect
        if self.db_type not in DatabaseTypes.__members__.values():
            raise ValueError(f'database type must be [database, redis, memory], your value: {self.type}')

database_config = DataBaseConfig(parser=get_parser())
