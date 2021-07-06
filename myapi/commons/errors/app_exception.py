# -*- coding: utf-8 -*-
from enum import Enum
from http import HTTPStatus
from typing import Any

from flask import jsonify, make_response


class AppException(RuntimeError):
    """Base exception class for custom app exceptions"""

    status = 500
    title = HTTPStatus(value=status).phrase

    def __init__(self, **kwargs: Any):
        _subtype = kwargs.get("subtype")
        _type = _code = _title = None
        if issubclass(type(_subtype), Enum):
            _type, _code, _title = _subtype.name, _subtype.value[0], _subtype.value[1]
        self.status = kwargs.get("status", getattr(self, "status", None))
        self.title = kwargs.get("title", getattr(self, "title", _title))
        self.type = kwargs.get("type", getattr(self, "type", _type))
        self.code = kwargs.get("code", getattr(self, "code", _code))
        self.detail = kwargs.get("detail", getattr(self, "detail", None))
        self.instance = kwargs.get("instance", getattr(self, "instance", None))

    @staticmethod
    def handle(e: Any) -> Any:
        if not isinstance(e, AppException) or not issubclass(type(e), AppException):
            return e
        return make_response(jsonify({"error": e.__dict__}), e.status)
