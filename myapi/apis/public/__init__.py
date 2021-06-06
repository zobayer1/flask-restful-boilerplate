# -*- coding: utf-8 -*-
from flask import Blueprint
from flask_restful import Api

from myapi.extensions import apispec
from myapi.apis.public.server_status import ServerStatus

blueprint = Blueprint("public", __name__)
api = Api(blueprint)

api.add_resource(ServerStatus, "/server/status", endpoint="status")


@blueprint.before_app_first_request
def register_views():
    apispec.spec.path(view=ServerStatus, endpoint="status")


__all__ = ["blueprint"]
