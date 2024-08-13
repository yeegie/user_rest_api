from pydantic import BaseModel
from typing import Optional

class PositionSchema(BaseModel):
    id: int
    name: str


class PositionCreateDto(BaseModel):
    name: str
    user_id: Optional[int]


class PositionUpdateDto(BaseModel):
    name: str
    
