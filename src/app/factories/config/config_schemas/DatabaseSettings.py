__all__ = [
    "DatabaseSettings",
]


from pydantic import BaseModel, SecretStr


class DatabaseSettings(BaseModel):
    db_type: str
    host: str = "localhost"
    port: int
    user: str
    password: SecretStr
    database: str
