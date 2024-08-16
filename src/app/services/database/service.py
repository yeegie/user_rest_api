from .base import BaseDatabaseService

from tortoise import Tortoise, BaseDBAsyncClient, connections
from tortoise.exceptions import DBConnectionError

import logging
logger = logging.getLogger(__name__)


class DatabaseService(BaseDatabaseService):
    def __init__(
        self,
        type: str,
        host: str,
        port: int,
        user: str,
        password: str,
        database: str,
    ) -> None:
        self._type = type
        self._host = host
        self._port = port
        self.__user = user
        self.__password = password
        self._database = database

        self._connection_string = self.create_connection_string(type)

        self._connection = None

    async def init_database(self) -> None:
        try:
            await Tortoise.init(
                db_url=self._connection_string,
                modules={'models': ['database.models']}
            )
            await Tortoise.generate_schemas()
            self._connection = connections.get("default")
        except DBConnectionError as ex:
            logger.critical(f'Data base connection error to {self._connection_string}')
        except Exception as ex:
            logger.critical(f'DATABASE CONNECTION ERROR: {str(ex)}. {self._connection_string}')

    async def close_database(self) -> None:
        await Tortoise.close_connections()

    def create_connection_string(self, database_type: str) -> str:
        # Create connection string for sqlite and other db types
        connection_string = None

        if self._type == 'local':
            db_path = f'database/'
            db_file = f'{self._database}.sqlite3'
            connection_string = f'sqlite://{db_path}{db_file}'
        else:
            if len(self.__password) == 0:
                connection_string = f'{self._type}://{self.__user}@{self._host}:{self._port}/{self._database}'
            else:
                connection_string = f'{self._type}://{self.__user}:{self.__password}@{self._host}:{self._port}/{self._database}'

        return connection_string

    async def get_connection(self) -> BaseDBAsyncClient:
        return self._connection
