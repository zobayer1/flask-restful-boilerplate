# -*- coding: utf-8 -*-
from flask import Blueprint
from flask_restful import Api

from myapi.extensions import apispec
from myapi.health.status import ServerStatus

health_blueprint = Blueprint("health", __name__)
api = Api(health_blueprint)

api.add_resource(ServerStatus, "/status", endpoint="status")


@health_blueprint.before_app_first_request
def register_views():
    apispec.spec.path(view=ServerStatus)


__all__ = ["health_blueprint"]
