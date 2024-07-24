from fastapi import APIRouter, HTTPException

from schemas.user import UserCreateDto, UserUpdateDto
from services.user import UserService

from tortoise.exceptions import DoesNotExist

router = APIRouter()


@router.post('/', status_code=201)
async def create(dto: UserCreateDto):
    try:
        return await UserService.create(dto)
    except Exception as ex:
        raise HTTPException(500, detail=str(ex))


@router.put('/{id}', status_code=201)
async def update(id: int, dto: UserUpdateDto):
    try:
        return await UserService.update(id, dto)
    except DoesNotExist as ex:
        raise HTTPException(404, detail=str(ex))
    except Exception as ex:
        raise HTTPException(500, detail=str(ex))


@router.get('/{id}')
async def get(id: int):
    try:
        return await UserService.get(id)
    except DoesNotExist as ex:
        raise HTTPException(404, detail=str(ex))
    except Exception as ex:
        raise HTTPException(500, detail=str(ex))


@router.delete('/{id}', status_code=204)
async def delete(id: int):
    try:
        await UserService.delete(id)
        return 'ok'
    except DoesNotExist as ex:
        raise HTTPException(404, detail=str(ex))
    except Exception as ex:
        raise HTTPException(500, detail=str(ex))
