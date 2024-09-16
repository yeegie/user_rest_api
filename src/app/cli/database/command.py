__all__ = ["database_group"]

from cli.database.database import DatabaseCommands
import click


database_commands = DatabaseCommands()


# Commands
create_db_command = click.Command(
    name="create_db",
    callback=database_commands.create_db,
)


# Command group
database_group = click.Group(
    commands={
        "create_db": create_db_command,
    }
)