# -*- coding: utf-8 -*-
import os
import sys
from typing import Any

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask import Flask
from flask_cors import CORS
from logging_.config import YAMLConfig

from myapi.apis import admin_blueprint, apiv1_blueprint, public_blueprint
from myapi.extensions import apispec

if sys.version_info < (3, 8):  # pragma: no cover
    # noinspection PyUnresolvedReferences
    from importlib_metadata import version
else:  # pragma: no cover
    from importlib.metadata import version


def create_app(
    instance_name: str, instance_path: str = os.path.join(os.getcwd(), "instance"), app_name: str = "flask_tutorial"
) -> Flask:
    """Creates a Flask app"""
    _initialize_logging(f"{instance_name}/logging.yaml", instance_path=instance_path, silent=True)
    app = Flask(app_name, instance_path=instance_path, instance_relative_config=True)
    app.config.from_object("myapi.config")
    app.config.from_pyfile(f"{instance_name}/application.cfg", silent=True)
    _initialize_extensions(app)
    _initialize_blueprints(app)
    return app


def _initialize_logging(filename: str, instance_path: str, **kwargs: Any):
    """Initializes logging, must be done before creating Flask app"""
    YAMLConfig.from_file(os.path.join(instance_path, filename), **kwargs)


def _initialize_extensions(app: Flask):
    """Initializes extensions with app config"""
    CORS(app)
    if app.debug or app.testing:
        _initialize_apispec(app)


def _initialize_blueprints(app: Flask):
    """Initializes blueprints with URL prefixes"""
    app.register_blueprint(admin_blueprint, url_prefix="/myapi/admin")
    app.register_blueprint(public_blueprint, url_prefix="/myapi/public")
    app.register_blueprint(apiv1_blueprint, url_prefix="/myapi/v1")


def _initialize_apispec(app: Flask):
    """Initializes apispec with plugins"""
    app.config.update(
        {
            "APISPEC_SPEC": APISpec(
                title=app.name,
                version=version(app.name),
                openapi_version="3.0.2",
                plugins=[MarshmallowPlugin()],
            )
        }
    )
    apispec.init_app(app)
