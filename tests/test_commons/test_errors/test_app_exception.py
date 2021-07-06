# -*- coding: utf-8 -*-
import json
from http import HTTPStatus

import pytest

from myapi.commons.errors import Errors
from myapi.commons.errors.app_exception import AppException


@pytest.fixture(scope="module")
def cls(app):
    """A test exception class inherited from AppException"""
    with app.app_context():

        class TestException(AppException):
            """A test exception class"""

            pass

        yield TestException


def test_exception_handler_sets_properties(cls):
    """Test fails if handler does not use subclass attributes when they are set"""
    obj = cls(subtype=Errors.SERVER_ERROR, detail="Test exception details")
    response = cls.handle(obj)
    error_response = json.loads(response.data).get("error")
    assert response.status_code == obj.status
    assert error_response["type"] == Errors.SERVER_ERROR.name
    assert error_response["code"] == Errors.SERVER_ERROR.value[0]


def test_handler_uses_superclass_attributes(cls):
    """Test fails if handler does not use superclass attributes when they are not set in subclass"""
    obj = cls()
    response = cls.handle(obj)
    error_response = json.loads(response.data).get("error")
    assert response.status_code == obj.status
    assert error_response["title"] == HTTPStatus(value=obj.status).phrase


def test_exception_handler_ignores_other_errors(cls):
    """Test fails if handler does not ignore error objects not inherited from AppException"""
    response = cls.handle(RuntimeError("Test"))
    assert isinstance(response, RuntimeError)
