from pydantic import BaseModel
from typing import Optional

class RoleSchema(BaseModel):
    id: int
    name: str


class RoleCreateDto(BaseModel):
    name: str
    user_id: Optional[int] = None


class RoleUpdateDto(BaseModel):
    name: str
    
