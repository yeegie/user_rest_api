__all__ = ["database_group"]

import click
from app.cli.database.database import DatabaseCommands
from app.utils.ioc import ioc
from app.factories.config import ConfigSchema, DatabaseSettings


config = ioc.get(ConfigSchema)
database_commands = DatabaseCommands(
    config=DatabaseSettings(
        **config.settings["database"]
    )
)


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