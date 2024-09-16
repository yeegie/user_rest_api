from pydantic import BaseModel, IPvAnyAddress, SecretStr
from typing import Mapping, Any, Union


class ConfigSchema(BaseModel):
    config_type: str
    settings: Mapping[str, Any]


class DatabaseSettings(BaseModel):
    db_type: str
    host: Union[IPvAnyAddress, str]
    port: int
    user: str
    password: SecretStr
    database: str


class AppSettings(BaseModel):
    repository_type: str
    host: str
    port: int
    debug: bool
