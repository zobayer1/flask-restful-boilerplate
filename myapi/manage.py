# -*- coding: utf-8 -*-
import os

import click
from flask.cli import FlaskGroup

from myapi.app import create_app


cli = FlaskGroup(create_app=lambda: create_app("myapi"))


@cli.command()
def env():
    """Check env variables for the app."""
    env_vars = ["FLASK_ENV", "FLASK_SECRET", "LOGGING_ROOT", "LOGGING_CONFIG"]
    for var in env_vars:
        click.echo(f"${var}={os.getenv(var)}")
