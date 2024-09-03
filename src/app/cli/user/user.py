import asyncio
import click
from services import UserService
from schemas.user import RoleSchema, RoleCreateDto, UserUpdateDto
from typing import List

class UserCommands:
    def __init__(self, service: UserService):
        self.__service = service

    def create(self, fio: str, email: str):
        dto = RoleCreateDto(
            fio=fio,
            email=email,
        )

        new_user: RoleSchema = asyncio.run(
            self.__service.create(dto)
        )
        click.echo(f'[{new_user.id}] User added\nfio={new_user.fio}\nemail={new_user.email}')

    def read(self, user_id: int):
        user = asyncio.run(
            self.__service.read(user_id)
        )
        click.echo(f'[{user.id}] User\nfio={user.fio}\nemail={user.email}')

    def update(self, user_id: int, fio: str, email: str):
        dto = UserUpdateDto(
            fio=fio,
            email=email,
        )
        user = asyncio.run(
            self.__service.update(user_id, dto)
        )
        click.echo(f'[{user.id}] User\nfio={user.fio}\nemail={user.email}')

    def delete(self, user_id: int):
        user = asyncio.run(
            self.__service.delete(user_id)
        )
        click.echo(f'User deleted.')

    def all(self):
        users = asyncio.run(
            self.__service.all()
        )
        
        for user in users:
            click.echo(user)
