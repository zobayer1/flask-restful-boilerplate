# -*- coding: utf-8 -*-
import os

"""ENV: Flask application environment.

Examples: `development`, `production`, `testing`.
"""
ENV = os.getenv("FLASK_ENV", "development")

"""SECRET_KEY: Secret key used for signing cookies and tokens.

Application will fail to start if $FLASK_SECRET is not set.
"""
try:
    SECRET_KEY = os.getenv("FLASK_SECRET").encode("utf-8")
except AttributeError:  # pragma: no cover
    raise RuntimeError("Environment variable $FLASK_SECRET was not set")

"""LOGGING_CONFIG: Path to logging configurations.

Logger extension will read configurations from the specified file.
"""
LOGGING_CONFIG = os.getenv("LOGGING_CONFIG", f"instance/{ENV}/logging.yaml")

"""APISPEC_SWAGGER_URL: URL for swagger.json file.

Set None to disable serving this resource.
"""
APISPEC_SWAGGER_URL = "/myapi/apispec/spec"

"""APISPEC_SWAGGER_UI_URL: URL for swagger-ui.

Set None to disable serving this view.
"""
APISPEC_SWAGGER_UI_URL = "/myapi/apispec"
