# -*- coding: utf-8 -*-
from flask import Blueprint
from flask_restful import Api

from myapi.apis.public.server_status import ServerStatus

blueprint = Blueprint("public", __name__)

api = Api(blueprint)
api.add_resource(ServerStatus, "/server/status")

__all__ = ["blueprint", "ServerStatus"]
