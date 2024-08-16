import asyncio
import anyio
import asyncclick as click

from database import init_database

from services import UserService, PositionService
from schemas.user import UserCreateDto
from schemas.position import PositionCreateDto

from tortoise.exceptions import DoesNotExist, IntegrityError

user_service = UserService()
position_service = PositionService()

@click.group()
async def cli():
    pass

# User
@click.command()
@click.option("--interactive", default=False, help="Interactive mode, creating a user with fields step by step.")
@click.option("--fio", default="")
@click.option("--email", default="")
async def create_user(interactive: bool, fio: str, email: str):
    if interactive:
        fio = input("fio: ")
        email = input("email: ")

    user = None
    try:
        user = await user_service.create(UserCreateDto(
            fio=fio,
            email=email,
        ))
    except IntegrityError as ex:
        click.echo(str(ex))

    click.echo(user)

@click.command()
@click.option("--user_id", type=int)
async def read_user(user_id: int):
    try:
        user = await user_service.read(user_id)
        click.echo(user)
    except DoesNotExist:
        click.echo(f"id={user_id} not found!")


@click.command()
async def read_all_users():
    users = await user_service._all()
    click.echo("\n".join(map(str, users)))


@click.command()
async def update_user():
    pass


@click.command()
@click.option("--user_id", type=int)
async def delete_user(user_id: int):
    try:
        await user_service.delete(user_id)
        click.echo(f"User id={user_id} deleted!")
    except DoesNotExist as ex:
        click.echo(str(ex))

# Position
@click.command()
@click.option("--interactive", default=False, help="Interactive mode, creating a position with fields step by step.")
@click.option("--name", type=str)
@click.option("--user_id", type=int)
async def create_position(interactive: bool, fio: str, email: str):
    if interactive:
        name = input("name: ")
        user_id = int(input("user_id: "))

    position = await PositionService.create(PositionCreateDto(
        name=fio,
        user_id=email,
    ))

    click.echo(position)

cli.add_command(create_user, name="create_user")
cli.add_command(read_all_users, name="all_users")
cli.add_command(read_user, name="read_user")
cli.add_command(delete_user, name="delete_user")

cli.add_command(create_position, name="create_position")


async def main():
    await init_database()
    await cli.main()

if __name__ == '__main__':
    anyio.run(main)
