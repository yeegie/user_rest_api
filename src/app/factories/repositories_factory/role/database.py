from app.repositories.BaseRepository import BaseRepository
from repositories.role import DatabaseRoleRepository
from ..BaseRepositoryFactory import BaseRepositoryFactory
from adapters.sqlalchemy.session import SqlalchemySessionCreator
from data.database_config import database_config


class DatabaseRoleRepositoryFactory(BaseRepositoryFactory):
    def get_instance(self) -> BaseRepository:
        session_creator = SqlalchemySessionCreator(database_config.db_uri)
        session = session_creator.create_session()
        return DatabaseRoleRepository(session)

