# -*- coding: utf-8 -*-
import os

import pytest

from myapi.app import create_app
from tests.envvars import variables


@pytest.fixture(scope="session")
def app():
    """A flask app with testing configurations"""
    os.environ.update(variables)
    return create_app("myapi")


@pytest.fixture(scope="session")
def client(app):
    """An HTTP test client to test api endpoints"""
    return app.test_client()


@pytest.fixture(scope="session")
def runner(app):
    """A CLI test client to test shell commands"""
    return app.test_cli_runner()
