# -*- coding: utf-8 -*-
import json

from openapi_spec_validator import validate_spec


def test_apispec_returns_json_with_success(client):
    """Test fails if /myapi/apispec/spec does not return a valid openapi spec"""
    response = client.get("/myapi/apispec/spec")
    assert response.status_code == 200
    validate_spec((json.loads(response.data)))
