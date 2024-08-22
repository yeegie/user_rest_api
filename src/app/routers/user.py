from fastapi import APIRouter, HTTPException, Depends
from typing import Annotated

from schemas.user import UserCreateDto, UserUpdateDto
from services import UserService

from utils.container import container


class UserRouter:
    def __init__(self, service: UserService):
        self.__service = service
        self.__router = APIRouter()

        self.__router.add_api_route("/", self.all, methods=["GET"])
        self.__router.add_api_route("/", self.create, methods=["POST"])
        self.__router.add_api_route("/{id}", self.read, methods=["GET"])
        self.__router.add_api_route("/{id}", self.update, methods=["PUT"])
        self.__router.add_api_route("/{id}", self.delete, methods=["DELETE"])

    # Routes
    async def all(self):
        return await self.__service.__all()
    
    async def create(self, dto: UserCreateDto):
        return await self.__service.create(dto)

    async def read(self, id: int):
        return await self.__service.read(id)
    
    async def update(self, id: int, dto: UserUpdateDto):
        return await self.__service.update(id, dto)
    
    async def delete(self, id: int):
        return await self.__service.delete(id)
