from tortoise import Model, fields
from schemas.role import RoleSchema
from .user import User


class Role(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=64)
    user = fields.ForeignKeyField(
        "models.User",
        "role",
        null=True,
        on_delete=fields.CASCADE,
    )

    async def to_schema(self) -> RoleSchema:
        return RoleSchema(
            id=self.id,
            name=self.name,
        )
