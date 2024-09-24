__all__ = [
    "DatabaseConfig"
]


from pydantic import BaseModel, SecretStr


class DatabaseConfig(BaseModel):
    db_type: str
    host: str = "localhost"
    port: int
    user: str
    password: SecretStr
    database: str
