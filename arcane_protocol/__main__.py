import click
from platformdirs import user_data_dir

from .vault.commands import secrets


@click.group()
def entry_point():
    pass

@entry_point.group(name="vault")
def entry_vault():
    pass

entry_vault.add_command(secrets)