from fastapi import APIRouter
from schemas.user import UserCreateDto, UserUpdateDto
from services import UserService


class UserRouter(APIRouter):
    def __init__(self, service: UserService):
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
    
    async def create(self, dto: UserCreateDto):
        return await self.__service.create(dto)

    async def read(self, id: int):
        return await self.__service.read(id)
    
    async def update(self, id: int, dto: UserUpdateDto):
        return await self.__service.update(id, dto)
    
    async def delete(self, id: int):
        return await self.__service.delete(id)
