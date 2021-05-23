# -*- coding: utf-8 -*-
import logging
import logging.config
import os
import re
from typing import Any

import yaml
from yaml.parser import ParserError


class LoggerExt(object):
    def __init__(self, app: Any = None, **kwargs):
        self.logger_name = "myapi_logger"
        self._path_matcher = re.compile(r"\${([^}^{]+)}")
        self._options = kwargs
        if app:
            self.init_app(app)

    def init_app(self, app: Any):
        self._create_logger(app)

    def _create_logger(self, app: Any):
        yaml.add_implicit_resolver("!path", self._path_matcher, None, yaml.SafeLoader)
        yaml.add_constructor("!path", self._path_constructor, yaml.SafeLoader)
        try:
            with open(app.config["LOGGING_CONFIG"], "r") as f:
                log_cfg = yaml.safe_load(f.read())
                logging.config.dictConfig(log_cfg)
        except (FileNotFoundError, PermissionError, ParserError):  # pragma: no cover
            pass
        app.logger = logging.getLogger(self.logger_name)

    def _path_constructor(self, _: Any, node: Any):
        match = self._path_matcher.match(node.value)
        env_var = match.group()[2:-1]
        env_value = os.environ.get(env_var)
        return env_value + node.value[match.end() :]
