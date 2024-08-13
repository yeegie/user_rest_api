from tortoise import Model, fields
from schemas.position import PositionSchema
from .user import User


class Position(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=64)
    user = fields.ForeignKeyField(
        "models.User",
        "position",
        on_delete=fields.CASCADE,
    )

    async def to_schema(self) -> PositionSchema:
        return PositionSchema(
            id=self.id,
            name=self.name,
        )
