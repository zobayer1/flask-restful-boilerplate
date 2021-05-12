# -*- coding: utf-8 -*-
import os

ENV = os.getenv("FLASK_ENV", "development")
SECRET_KEY = os.getenv("FLASK_SECRET", "bb9ba2817ef62e261d3adaf90c2727bb").encode("utf-8")
LOGGING_ROOT = os.getenv("LOGGING_ROOT", "logs")
LOGGING_CONFIG = os.getenv("LOGGING_CONFIG", f"instance/{ENV}/logging.yaml")
