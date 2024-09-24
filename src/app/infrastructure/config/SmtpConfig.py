__all__ = [
    "SmtpConfig"
]


from pydantic import BaseModel, SecretStr, EmailStr


class SmtpConfig(BaseModel):
    host: str = "localhost"
    port: int = 587
    tls: bool = True
    password: SecretStr
    email_from: EmailStr
