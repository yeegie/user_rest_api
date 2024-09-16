from app.repositories.BaseRepository import BaseRepository
from app.repositories.role import DatabaseRoleRepository
from ..BaseRepositoryFactory import BaseRepositoryFactory
from app.adapters.sqlalchemy.session import SqlalchemySessionCreator
from app.factories.config.config_schemas import DatabaseSettings


class DatabaseRoleRepositoryFactory(BaseRepositoryFactory):
    def get_instance(self, database_config: DatabaseSettings) -> BaseRepository:
        db = database_config
        connection_string = f"{db.db_type}://{db.user}:{db.password}@{db.host}:{db.port}/{db.database}"

        session_creator = SqlalchemySessionCreator(connection_string)
        session = session_creator.create_session()
        return DatabaseRoleRepository(session)

