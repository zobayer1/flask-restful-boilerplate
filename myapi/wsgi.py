# -*- coding: utf-8 -*-
import os

from myapi.app import create_app

app = create_app(instance_name=os.getenv("FLASK_ENV", "development"))
