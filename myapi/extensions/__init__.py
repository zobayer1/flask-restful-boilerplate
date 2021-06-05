# -*- coding: utf-8 -*-
from flask_apispec.extension import FlaskApiSpec

from myapi.extensions.flask_resource_plugin import FlaskResourcePlugin

apispec = FlaskApiSpec()

__all__ = ["apispec", "FlaskResourcePlugin"]
