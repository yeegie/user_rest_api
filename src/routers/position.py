from fastapi import APIRouter, HTTPException

from schemas.position import PositionCreateDto, PositionUpdateDto
from services.position.position import PositionService
from container import container

from tortoise.exceptions import DoesNotExist


router = APIRouter()
position_service: PositionService = container.get("position_service")


@router.post('/', status_code=201)
async def create(dto: PositionCreateDto):
    try:
        await position_service.create(dto)
    except Exception as ex:
        raise HTTPException(500, detail=str(ex))


@router.put('/{id}', status_code=201)
async def update(id: int, dto: PositionUpdateDto):
    pass


@router.get('/{id}')
async def get(id: int):
    try:
        return await position_service.read(position_id=id)
    except DoesNotExist as ex:
        raise HTTPException(404, detail=str(ex))
    except Exception as ex:
        raise HTTPException(500, detail=str(ex))


@router.delete('/{id}', status_code=204)
async def delete(id: int):
    pass
