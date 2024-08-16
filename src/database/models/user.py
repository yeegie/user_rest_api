from tortoise import Model, fields
from schemas.user import UserSchema


class User(Model):
    id = fields.IntField(pk=True)
    fio = fields.CharField(max_length=255, null=False)
    email = fields.CharField(max_length=255, unique=True)

    async def to_schema(self) -> UserSchema:
        return UserSchema(
            id=self.id,
            fio=self.fio,
            email=self.email,
            position=self.position,
        )
