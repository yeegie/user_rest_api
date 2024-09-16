from fastapi import APIRouter
from app.repositories.schemas import RoleCreateDto, RoleUpdateDto
from app.services import RoleService


class RoleRouter(APIRouter):
    def __init__(self, service: RoleService) -> None:
        super().__init__()
        self.__service = service

        self.add_api_route("/", self.all, methods=["GET"])
        self.add_api_route("/", self.create, methods=["POST"])
        self.add_api_route("/{id}", self.read, methods=["GET"])
        self.add_api_route("/{id}", self.update, methods=["PUT"])
        self.add_api_route("/{id}", self.delete, methods=["DELETE"])

    # Routes
    async def all(self):
        return await self.__service.all()
    
    async def create(self, dto: RoleCreateDto):
        return await self.__service.create(dto)

    async def read(self, id: int):
        return await self.__service.read(id)
    
    async def update(self, id: int, dto: RoleUpdateDto):
        return await self.__service.update(id, dto)
    
    async def delete(self, id: int):
        return await self.__service.delete(id)
