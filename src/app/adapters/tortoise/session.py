from ..base import BaseSessionCreator
from tortoise import Tortoise
import asyncio


class TortoiseSessionCreator(BaseSessionCreator):
    def __init__(self, db_uri) -> None:
        self._db_uri = db_uri
        asyncio.run(self.init_db())


    async def init_db(self) -> None:
        await Tortoise.init(
            db_url=self._db_uri,
            modules={"models": ["adapters.tortoise.models"]}
        )
        await Tortoise.generate_schemas()


    def create_session(self):
        return Tortoise.get_connection("default")
