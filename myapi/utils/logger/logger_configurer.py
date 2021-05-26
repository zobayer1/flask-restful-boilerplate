# -*- coding: utf-8 -*-
import logging
import logging.config
import os
import re
from typing import Any

import yaml
from yaml.parser import ParserError


class LoggerConfigurer(object):
    _path_matcher = re.compile(r"\${([^}^{]+)}")

    def __init__(self, config_path: str, instance_path: str, **kwargs: Any):
        yaml.add_implicit_resolver("!path", self._path_matcher, None, yaml.SafeLoader)
        yaml.add_constructor("!path", self._path_constructor, yaml.SafeLoader)
        try:
            with open(os.path.join(instance_path, config_path), "r") as f:
                log_cfg = yaml.safe_load(f.read())
                logging.config.dictConfig(log_cfg)
        except (FileNotFoundError, PermissionError, ParserError):  # pragma: no cover
            if kwargs.get("silent") is not True:
                raise RuntimeError(f"Error reading file: {config_path}")

    def _path_constructor(self, _: Any, node: Any):
        match = self._path_matcher.match(node.value)
        env_var = match.group()[2:-1]
        env_value = os.environ.get(env_var)
        return (env_value if env_value else "") + node.value[match.end() :]
