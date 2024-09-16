from app.repositories.BaseRepository import BaseRepository
from app.repositories.user import DatabaseUserRepository
from ..BaseRepositoryFactory import BaseRepositoryFactory
from app.adapters.sqlalchemy.session import SqlalchemySessionCreator
from app.factories.config import DatabaseSettings

class DatabaseUserRepositoryFactory(BaseRepositoryFactory):
    def get_instance(self, database_config: DatabaseSettings) -> BaseRepository:
        db = database_config
        connection_string = f"{db.db_type}://{db.user}:{db.password}@{db.host}:{db.port}/{db.database}"

        session_creator = SqlalchemySessionCreator(database_config.db_uri)
        session = session_creator.create_session()
        return DatabaseUserRepository(session)
