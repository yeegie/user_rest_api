from pydantic import BaseModel
from .role import RoleSchema
from typing import Dict, Optional


class UserSchema(BaseModel):
    id: int | str
    fio: str
    email: str
    # role: Optional[RoleSchema]


class UserCreateDto(BaseModel):
    fio: str
    email: str


class UserUpdateDto(BaseModel):
    fio: str
    email: str
