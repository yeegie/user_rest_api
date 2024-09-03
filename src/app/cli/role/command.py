__all__ = ["role_group"]

from services import RoleService
from utils.container import ioc
from cli.role.role import RoleCommands
import click


role_commands = RoleCommands(ioc.get(RoleService))

# Commands
create_role_command = click.Command(
    name="create_role",
    callback=role_commands.create,
    params=[
        click.Option(["--name"], show_default=True, help="Role name"),
    ]
)

read_role_command = click.Command(
    name="read_role",
    callback=role_commands.read,
    params=[
        click.Option(["--role_id"], show_default=True, help="Id of role"),
    ]
)

update_role_command = click.Command(
    name="update_role",
    callback=role_commands.update,
    params=[
        click.Option(["--role_id"], show_default=True, help="Id of role"),
        click.Option(["--name"], show_default=True, help="Name of role"),
        # click.Option(["--user"], show_default=True, help="User id of role"),
    ]
)

delete_role_command = click.Command(
    name="delete_role",
    callback=role_commands.delete,
    params=[
        click.Option(["--role_id"], show_default=True, help="Id of role"),
    ]
)

all_role_command = click.Command(
    name="all_role",
    callback=role_commands.all,
)

# Command group
role_group = click.Group(
    commands={
        "create": create_role_command,
        "read": read_role_command,
        "update": update_role_command,
        "delete": delete_role_command,
        "all": all_role_command,
    }
)