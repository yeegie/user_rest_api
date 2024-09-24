from app.repositories.BaseRepository import BaseRepository
from app.repositories.role import DatabaseRoleRepository
from ..BaseRepositoryFactory import BaseRepositoryFactory
from app.adapters.sqlalchemy.session import SqlalchemySessionCreator
from app.infrastructure.config import DatabaseConfig


class DatabaseRoleRepositoryFactory(BaseRepositoryFactory):
    def get_instance(self, database_config: DatabaseConfig) -> BaseRepository:
        db = database_config
        connection_string = f"{db.db_type}://{db.user}:{db.password}@{db.host}:{db.port}/{db.database}"

        session_creator = SqlalchemySessionCreator(connection_string)
        session = session_creator.create_session()
        return DatabaseRoleRepository(session)

