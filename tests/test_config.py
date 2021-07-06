# -*- coding: utf-8 -*-
def test_env(app):
    """Test fails if app is not initialized with testing configurations"""
    assert app.env == "testing"
    assert app.testing
    assert app.name == "myapi"
