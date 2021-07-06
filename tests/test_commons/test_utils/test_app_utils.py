# -*- coding: utf-8 -*-
from myapi.commons.utils.app_utils import app_version


def test_application_version(app):
    """Test fails if importlib metadata cannot be loaded from metadata"""
    assert len(app_version(app.name)) > 0
