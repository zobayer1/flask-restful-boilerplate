# -*- coding: utf-8 -*-
import sys

from flask import current_app as app
from flask_apispec import MethodResource, doc

if sys.version_info < (3, 8):  # pragma: no cover
    # noinspection PyUnresolvedReferences
    from importlib_metadata import version
else:  # pragma: no cover
    from importlib.metadata import version


class ServerStatus(MethodResource):
    @doc(tags=["health"], description="Get server health status")
    def get(self):
        app.logger.info("Health status request received")
        return {"server": f"{app.name} v{version(app.name)}", "status": "running"}, 200
