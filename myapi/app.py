# -*- coding: utf-8 -*-
import os

from flask import Flask
from flask_cors import CORS
from logging_.config import YAMLConfig

from myapi.apis import admin, apiv1, local
from myapi.extensions import apispec


def create_app(app_name: str, instance_name: str = None, instance_path: str = None):
    """Creates a Flask app"""
    instance_name = instance_name or os.getenv("FLASK_ENV", "development")
    instance_path = instance_path or os.path.join(os.getcwd(), "instance")
    _initialize_logging(f"{instance_name}/logging.yaml", instance_path, silent=True)
    app = Flask(
        app_name,
        instance_path=instance_path,
        static_url_path="/myapi/static",
        static_folder="myapi/static",
        instance_relative_config=True,
    )
    app.config.from_object("myapi.config")
    app.config.from_pyfile(f"{instance_name}/application.cfg", silent=True)
    if app.debug or app.testing:
        _register_apispec(app)
    _register_extensions(app)
    _register_blueprints(app)
    return app


def _initialize_logging(filename: str, instance_path: str, **kwargs: bool):
    """Initializes logging, must be done before creating Flask app"""
    YAMLConfig.from_file(os.path.join(instance_path, filename), **kwargs)


def _register_extensions(app: Flask):
    """Registers extensions with app config"""
    CORS(app)


def _register_blueprints(app: Flask):
    """Registers blueprints with URL prefixes"""
    app.register_blueprint(admin.blueprint, url_prefix="/myapi/admin")
    app.register_blueprint(local.blueprint, url_prefix="/myapi/local")
    app.register_blueprint(apiv1.blueprint, url_prefix="/myapi/v1")


def _register_apispec(app: Flask):
    """Registers apispec plugin and registers resources for swagger"""
    apispec.init_app(app)
    apispec.register(local.ServerStatus, blueprint=local.blueprint)
