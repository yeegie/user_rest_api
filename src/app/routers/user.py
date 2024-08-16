from fastapi import APIRouter, HTTPException, Depends
from typing import Annotated

from schemas.user import UserCreateDto, UserUpdateDto
from tortoise.exceptions import DoesNotExist

from repositories.user.base import BaseUserRepository

router = APIRouter()


@router.post('/', status_code=201)
async def create(
    dto: UserCreateDto,
    repository: Annotated[BaseUserRepository, Depends()],
):
    try:
        return await repository.create(dto)

    except Exception as ex:
        raise HTTPException(500, detail=str(ex))


@router.put('/{id}', status_code=201)
async def update(
    id: int,
    dto: UserUpdateDto,
    repository: Annotated[BaseUserRepository, Depends()],
):
    try:
        return await repository.update(id, dto)
    except DoesNotExist as ex:
        raise HTTPException(404, detail=str(ex))
    except Exception as ex:
        raise HTTPException(500, detail=str(ex))


@router.get('/{id}')
async def get(
    id: int,
    repository: Annotated[BaseUserRepository, Depends()]
):
    try:
        return await repository.read(user_id=id)
    except DoesNotExist as ex:
        raise HTTPException(404, detail=str(ex))
    except Exception as ex:
        raise HTTPException(500, detail=str(ex))


@router.delete('/{id}', status_code=204)
async def delete(
    id: int,
    repositiry: Annotated[BaseUserRepository, Depends()],
):
    try:
        return await repositiry.delete(id)
    except DoesNotExist as ex:
        raise HTTPException(404, detail=str(ex))
    except Exception as ex:
        raise HTTPException(500, detail=str(ex))


@router.get('/')
async def all(
    repository: Annotated[BaseUserRepository, Depends()],
):
    try:
        return await user_service._all()
    except Exception as ex:
        raise HTTPException(500, detail=str(ex))
