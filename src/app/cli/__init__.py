from .user import user_group
from .role import role_group
from .database import database_group

import click


def register_commands() -> click.Group:
    return click.Group(
        commands={
            "user": user_group,
            "role": role_group,
            "database": database_group,
        }
    )