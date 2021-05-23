# -*- coding: utf-8 -*-
import os

from flask import Flask
from flask_cors import CORS

from myapi.extensions.logger import LoggerExt
from myapi.health import health_blueprint


def create_app(instance_name: str, app_name: str = "flask-tutorial") -> Flask:
    app = Flask(app_name, instance_path=os.path.join(os.getcwd(), "instance"), instance_relative_config=True)
    app.config.from_object("myapi.config")
    app.config.from_pyfile(f"{instance_name}/application.cfg", silent=True)
    initialize_extensions(app)
    initialize_blueprints(app)
    return app


def initialize_extensions(app: Flask):
    CORS(app)
    LoggerExt(app)


def initialize_blueprints(app: Flask):
    app.register_blueprint(health_blueprint, url_prefix="/myapi/health")
