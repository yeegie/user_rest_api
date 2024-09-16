import asyncio
import click

from sqlalchemy.ext.asyncio import create_async_engine
from app.repositories.models import Base

from factories.config.config_schemas import DatabaseSettings


class DatabaseCommands:
    def __init__(self, config: DatabaseSettings) -> None:
        self.__config = config
        self.__connection_string = self.__build_connection_string()

    def __build_connection_string(self) -> str:
        return (
            f"{self.__config.db_type}://{self.__config.user}:"
            f"{self.__config.password}@{self.__config.host}:"
            f"{self.__config.port}/{self.__config.database}"
        )
    
    def create_db(self):
        asyncio.run(self.__create())
        click.echo(f'database created')

    async def __create(self):
        engine = create_async_engine(self.__connection_string, echo=True)
        
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
