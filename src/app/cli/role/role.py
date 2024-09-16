import asyncio
import click
from app.services import RoleService
from app.repositories.schemas import RoleSchema, RoleCreateDto, RoleUpdateDto


class RoleCommands:
    def __init__(self, service: RoleService):
        self.__service = service

    def create(self, name: str):
        dto = RoleCreateDto(
            name=name
        )

        new_role: RoleSchema = asyncio.run(
            self.__service.create(dto)
        )
        click.echo(f'[{new_role.id}] Role added\nname={new_role.name}')

    def read(self, role_id: int):
        role = asyncio.run(
            self.__service.read(role_id)
        )
        click.echo(f'[{role.id}] Role\nfio={role.fio}\nemail={role.email}')

    def update(self, role_id: int, name: str):
        dto = RoleUpdateDto(
            name=name,
        )
        role = asyncio.run(
            self.__service.update(role_id, dto)
        )
        click.echo(f'[{role.id}] Role\nname={role.name}')

    def delete(self, role_id: int):
        user = asyncio.run(
            self.__service.delete(role_id)
        )
        click.echo(f'Role deleted.')

    def all(self):
        users = asyncio.run(
            self.__service.all()
        )
        
        for user in users:
            click.echo(user)
