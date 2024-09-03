__all__ = ["user_group"]

from services import UserService
from utils.container import ioc
from cli.user.user import UserCommands
import click


user_commands = UserCommands(ioc.get(UserService))

# Commands
create_user_command = click.Command(
    name="create_user",
    callback=user_commands.create,
    params=[
        click.Option(["--fio"], show_default=True, help="Full name of user"),
        click.Option(["--email"], show_default=True, help="User email"),
        # click.Option(["--role"], show_default=True, help="Role id of user"),
    ]
)

read_user_command = click.Command(
    name="read_user",
    callback=user_commands.read,
    params=[
        click.Option(["--user_id"], show_default=True, help="Id of user"),
    ]
)

update_user_command = click.Command(
    name="update_user",
    callback=user_commands.update,
    params=[
        click.Option(["--user_id"], show_default=True, help="Id of user"),
        click.Option(["--fio"], show_default=True, help="Full name of user"),
        click.Option(["--email"], show_default=True, help="User email"),
    ]
)

delete_user_command = click.Command(
    name="delete_user",
    callback=user_commands.delete,
    params=[
        click.Option(["--user_id"], show_default=True, help="Id of user"),
    ]
)

all_user_command = click.Command(
    name="all_user",
    callback=user_commands.all,
)

# Command group
user_group = click.Group(
    commands={
        "create": create_user_command,
        "read": read_user_command,
        "update": update_user_command,
        "delete": delete_user_command,
        "all": all_user_command,
    }
)
