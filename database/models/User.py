from tortoise import Model, fields
from schemas.user import UserSchema


class User(Model):
    id = fields.IntField(pk=True)
    fio = fields.CharField(max_length=255, null=False)

    async def to_schema(self) -> UserSchema:
        return UserSchema(
            id=self.id,
            fio=self.fio,
        )
