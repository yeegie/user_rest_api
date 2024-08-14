from fastapi import APIRouter, HTTPException
from schemas.user import UserCreateDto, UserUpdateDto
from tortoise.exceptions import DoesNotExist

from container import container
from services import UserService

router = APIRouter()
user_service: UserService = container.get("user_service")


@router.post('/', status_code=201)
async def create(dto: UserCreateDto):
    try:
        return await user_service.create(dto)
    except Exception as ex:
        raise HTTPException(500, detail=str(ex))


@router.put('/{id}', status_code=201)
async def update(id: int, dto: UserUpdateDto):
    try:
        return await user_service.update(id, dto)
    except DoesNotExist as ex:
        raise HTTPException(404, detail=str(ex))
    except Exception as ex:
        raise HTTPException(500, detail=str(ex))


@router.get('/{id}')
async def get(id: int):
    try:
        return await user_service.read(user_id=id)
    except DoesNotExist as ex:
        raise HTTPException(404, detail=str(ex))
    except Exception as ex:
        raise HTTPException(500, detail=str(ex))


@router.delete('/{id}', status_code=204)
async def delete(id: int):
    try:
        await user_service.delete(id)
        return 'ok'
    except DoesNotExist as ex:
        raise HTTPException(404, detail=str(ex))
    except Exception as ex:
        raise HTTPException(500, detail=str(ex))


@router.get('/')
async def all():
    try:
        return await user_service._all()
    except Exception as ex:
        raise HTTPException(500, detail=str(ex))
