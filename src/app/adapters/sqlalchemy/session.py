from ..BaseSessionCreator import BaseSessionCreator
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker


class SqlalchemySessionCreator(BaseSessionCreator):
    def __init__(self, db_uri: str) -> None:
        self._db_uri = db_uri
        self._engine = create_async_engine(self._db_uri, echo=True)
        self._SessionLocal = sessionmaker(
            bind=self._engine,
            class_=AsyncSession,
            expire_on_commit=False
        )
    
    def create_session(self) -> AsyncSession:
        return self._SessionLocal()