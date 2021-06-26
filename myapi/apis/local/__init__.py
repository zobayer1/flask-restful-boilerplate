# -*- coding: utf-8 -*-
from flask import Blueprint
from flask_restful import Api

from myapi.apis.local.server_status import ServerStatus

blueprint = Blueprint("local", __name__)

api = Api(blueprint)
api.add_resource(ServerStatus, "/server/status")

__all__ = ["blueprint", "ServerStatus"]
