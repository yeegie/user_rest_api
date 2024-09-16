__all__ = [
    "EmailSettings",
]


from pydantic import BaseModel, SecretStr


class EmailSettings(BaseModel):
    host: str = "localhost"
    port: int = 587
    tls: bool
    password: SecretStr
    email_from: str
