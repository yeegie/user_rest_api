from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    fio: str


class UserCreateDto(BaseModel):
    fio: str


class UserUpdateDto(BaseModel):
    fio: str
