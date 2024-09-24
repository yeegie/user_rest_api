__all__ = [
    "RootConfig"
]

from pydantic import BaseModel

# Configs
from .AppConfig import AppConfig
from .DatabaseConfig import DatabaseConfig
from .SmtpConfig import SmtpConfig

from typing import Optional


class RootConfig(BaseModel):
    app: AppConfig
    database: DatabaseConfig
    smtp: Optional[SmtpConfig]
