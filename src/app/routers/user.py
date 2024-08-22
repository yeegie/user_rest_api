from fastapi import APIRouter, HTTPException, Depends
from typing import Annotated

from schemas.user import UserCreateDto, UserUpdateDto
from services import UserService

from utils.container import container


router = APIRouter()

def get_service():
    return container.get(UserService)


@router.post('/', status_code=201)
async def create(
    dto: UserCreateDto,
    service: Annotated[UserService, Depends(get_service)],
):
    return await service.create(dto)


@router.put('/{id}', status_code=201)
async def update(
    id: int,
    dto: UserUpdateDto,
    service: Annotated[UserService, Depends(get_service)],
):
    return await service.update(id, dto)


@router.get('/{id}')
async def get(
    id: int,
    service: Annotated[UserService, Depends(get_service)]
):
    return await service.read(id)


@router.delete('/{id}', status_code=204)
async def delete(
    id: int,
    service: Annotated[UserService, Depends(get_service)],
):
    return await service.delete(id)


@router.get('/')
async def all(
    service: Annotated[UserService, Depends(get_service)],
):
    return await service.all()
