from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    fio: str
    email: str


class UserCreateDto(BaseModel):
    fio: str
    email: str


class UserUpdateDto(BaseModel):
    fio: str
    email: str
