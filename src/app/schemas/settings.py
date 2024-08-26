from pydantic import BaseModel


class DatabaseSettings(BaseModel):
    type = str
    db_uri = str
