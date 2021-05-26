# -*- coding: utf-8 -*-
import os

from flask import Flask
from flask_cors import CORS

from myapi.health import health_blueprint
from myapi.utils.logger import LoggerConfigurer


def create_app(
    app_name: str = "flask-tutorial",
    instance_name: str = "development",
    instance_path: str = os.path.join(os.getcwd(), "instance"),
) -> Flask:
    initialize_logger(f"{instance_name}/logging.yaml", instance_path=instance_path)
    app = Flask(app_name, instance_path=instance_path, instance_relative_config=True)
    app.config.from_object("myapi.config")
    app.config.from_pyfile(f"{instance_name}/application.cfg", silent=True)
    initialize_extensions(app)
    initialize_blueprints(app)
    return app


def initialize_logger(config_path: str, instance_path: str):
    LoggerConfigurer(config_path, instance_path, silent=True)


def initialize_extensions(app: Flask):
    CORS(app)


def initialize_blueprints(app: Flask):
    app.register_blueprint(health_blueprint, url_prefix="/myapi/health")
