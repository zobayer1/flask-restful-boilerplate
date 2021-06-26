# -*- coding: utf-8 -*-
import json


def test_server_status_returns_success(client):
    """Test fails if /myapi/local/server/status does not return success"""
    response = client.get("/myapi/local/server/status")
    assert response.status_code == 200
    assert json.loads(response.data).get("status") == "running"
