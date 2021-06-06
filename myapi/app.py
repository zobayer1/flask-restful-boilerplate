# -*- coding: utf-8 -*-
import os
import sys
from typing import Any

from apispec.ext.marshmallow import MarshmallowPlugin

from myapi.extensions import FlaskResourcePlugin
from myapi.extensions import apispec

from apispec import APISpec
from flask import Flask
from flask_cors import CORS
from logging_.config import YAMLConfig

from myapi.apis.admin import blueprint as admin_blueprint
from myapi.apis.apiv1 import blueprint as apiv1_blueprint
from myapi.apis.public import blueprint as public_blueprint

if sys.version_info < (3, 8):  # pragma: no cover
    # noinspection PyUnresolvedReferences
    from importlib_metadata import version
else:  # pragma: no cover
    from importlib.metadata import version


def create_app(
    instance_name: str, instance_path: str = os.path.join(os.getcwd(), "instance"), app_name: str = "flask_tutorial"
) -> Flask:
    initialize_logging(f"{instance_name}/logging.yaml", instance_path=instance_path, silent=True)
    app = Flask(app_name, instance_path=instance_path, instance_relative_config=True)
    app.config.from_object("myapi.config")
    app.config.from_pyfile(f"{instance_name}/application.cfg", silent=True)
    if app.debug or app.testing:
        initialize_apispec(app)
    initialize_extensions(app)
    initialize_blueprints(app)
    return app


def initialize_logging(filename: str, instance_path: str, **kwargs: Any):
    YAMLConfig.from_file(os.path.join(instance_path, filename), **kwargs)


def initialize_extensions(app: Flask):
    CORS(app)


def initialize_blueprints(app: Flask):
    app.register_blueprint(admin_blueprint, url_prefix="/myapi/admin")
    app.register_blueprint(public_blueprint, url_prefix="/myapi/public")
    app.register_blueprint(apiv1_blueprint, url_prefix="/myapi/v1")


def initialize_apispec(app: Flask):
    app.config.update(
        {
            "APISPEC_SPEC": APISpec(
                title=app.name,
                version=version(app.name),
                openapi_version="3.0.2",
                plugins=[FlaskResourcePlugin(), MarshmallowPlugin()],
            )
        }
    )
    apispec.init_app(app)
