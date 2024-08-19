from configparser import ConfigParser
from .config_parser import get_parser


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
        self.__section = 'DataBase'
        self._avaiable_types = ['local', 'mysql', 'postgres']

        self.type = parser.get(self.__section, 'type')
        self.host = parser.get(self.__section, 'host')
        self.port = parser.getint(self.__section, 'port')
        self.user = parser.get(self.__section, 'user')
        self.password = parser.get(self.__section, 'password')
        self.database = parser.get(self.__section, 'database')

        # If type database is incorrect
        if self.type not in self._avaiable_types:
            raise ValueError(f'database type must be {self._avaiable_types}, your value: {type}')

        # Create connection string for sqlite and other db types
        if self.type == 'local':
            db_path = f'database/'
            db_file = f'{self.database}.sqlite3'
            connection_string = f'sqlite://{db_path}{db_file}'
        else:
            if len(self.password) == 0:
                connection_string = f'{self.type}://{self.user}@{self.host}:{self.port}/{self.database}'
            else:
                connection_string = f'{self.type}://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}'


database_config = DataBaseConfig(parser=get_parser())
