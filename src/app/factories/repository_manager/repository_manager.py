from app.factories.repositories_factory.BaseRepositoryFactory import BaseRepositoryFactory
from .BaseRepositoryManager import BaseRepositoryManager
from typing import Dict


class RepositoryManager(BaseRepositoryManager):
    def __init__(self) -> None:
        self._repositories: Dict[str, Dict[str, BaseRepositoryFactory]] = {}

    def get(self, entity: str, database_type: str):
        if entity in self._repositories and database_type in self._repositories[entity]:
            return self._repositories[entity][database_type].get_instance()
        else:
            raise KeyError(f"Repository for entity '{entity}' and database type '{database_type}' not found.")

    def set(self, entity: str, database_type: str, repository: BaseRepositoryFactory):
        if entity not in self._repositories:
            self._repositories[entity] = {}
        self._repositories[entity][database_type] = repository
