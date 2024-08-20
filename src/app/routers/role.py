from fastapi import APIRouter, Depends

from schemas.role import RoleCreateDto, RoleUpdateDto

from container import container
from typing import Annotated
from services import RoleService

router = APIRouter()

def get_service():
    return container.get(RoleService)


@router.post('/', status_code=201)
async def create(
    dto: RoleCreateDto,
    service: Annotated[RoleService, Depends(get_service)]
):
    return await service.create(dto)


@router.put('/{id}', status_code=201)
async def update(
    id: int,
    dto: RoleUpdateDto,
    service: Annotated[RoleService, Depends()],
):
    return await service.update(update_dto=dto)


@router.get('/{id}')
async def read(
    id: int,
    service: Annotated[RoleService, Depends()],
):
    return await service.read(role_id=id)


@router.delete('/{id}', status_code=204)
async def delete(
    id: int,
    service: Annotated[RoleService, Depends(get_service)],
):
    return await service.delete(id=id)

@router.get('/')
async def all(
    service: Annotated[RoleService, Depends(get_service)],
):
    return await service.all()
