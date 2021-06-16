# -*- coding: utf-8 -*-
from typing import Type

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask import Flask, Blueprint
from flask_apispec import FlaskApiSpec
from flask_restful import Resource

from myapi.commons.utils.app_utils import app_version


class ApiSpecExt(object):
    def __init__(self, app: Flask = None):
        self.apispec = FlaskApiSpec()
        if app:  # pragma: no cover
            self.init_app(app)

    def init_app(self, app: Flask):
        app.config.update(
            {
                "APISPEC_SPEC": APISpec(
                    title=app.name,
                    version=app_version(app.name),
                    openapi_version="3.0.2",
                    plugins=[MarshmallowPlugin()],
                )
            }
        )
        self.apispec.init_app(app)

    def register(self, resource: Type[Resource], blueprint: Blueprint):
        blueprint.before_app_first_request(lambda: self.apispec.register(resource, blueprint=blueprint.name))
