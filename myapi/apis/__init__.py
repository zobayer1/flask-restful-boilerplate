# -*- coding: utf-8 -*-
from myapi.apis.admin import blueprint as admin_blueprint
from myapi.apis.apiv1 import blueprint as apiv1_blueprint
from myapi.apis.public import blueprint as public_blueprint

__all__ = ["admin_blueprint", "apiv1_blueprint", "public_blueprint"]
