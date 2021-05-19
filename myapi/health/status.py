# -*- coding: utf-8 -*-
import sys

if sys.version_info < (3, 8):  # pragma: no cover
    from importlib_metadata import version
else:  # pragma: no cover
    from importlib.metadata import version

from flask import current_app as app
from flask_restful import Resource


class ServerStatus(Resource):
    # noinspection PyMethodMayBeStatic
    def get(self):
        app.logger.info("Health status request received")
        return {"server": f"{app.name} v{version(app.name)}", "status": "running"}, 200
