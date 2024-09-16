__all__ = [
    "ConfigSchema",
]


from pydantic import BaseModel
from typing import Mapping, Any


class ConfigSchema(BaseModel):
    config_type: str
    settings: Mapping[str, Any]
