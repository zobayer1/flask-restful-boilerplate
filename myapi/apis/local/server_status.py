# -*- coding: utf-8 -*-
from flask import current_app as app
from flask_apispec import MethodResource, doc

from myapi.commons.utils.app_utils import app_version


class ServerStatus(MethodResource):
    @doc(tags=["local"], description="Get server health status")
    def get(self):
        app.logger.info("Health status request received")
        return {"server": f"{app.name} v{app_version(app.name)}", "status": "running"}, 200
