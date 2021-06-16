# -*- coding: utf-8 -*-
from flask import Blueprint
from flask_restful import Api

blueprint = Blueprint("apiv1", __name__)

api = Api(blueprint)

__all__ = ["blueprint"]
