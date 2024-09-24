from ..repositories_factory.BaseRepositoryFactory import BaseRepositoryFactory
from .BaseRepositoryManager import BaseRepositoryManager
from typing import Dict
from app.infrastructure.config import DatabaseConfig


class RepositoryManager(BaseRepositoryManager):
    def __init__(self, database_config: DatabaseConfig) -> None:
        self._database_config = database_config
        self._repositories: Dict[str, Dict[str, BaseRepositoryFactory]] = {}

    def get(self, entity: str, database_type: str):
        if entity in self._repositories and database_type in self._repositories[entity]:
            return self._repositories[entity][database_type].get_instance(self._database_config)
        else:
            raise KeyError(f"Repository for entity '{entity}' and database type '{database_type}' not found.")

    def set(self, entity: str, database_type: str, repository: BaseRepositoryFactory):
        if entity not in self._repositories:
            self._repositories[entity] = {}
        self._repositories[entity][database_type] = repository
