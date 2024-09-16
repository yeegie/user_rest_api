__all__ = [
    "AppSettings",
]


from pydantic import BaseModel


class AppSettings(BaseModel):
    repository_type: str
    host: str = "localhost"
    port: int
    debug: bool
