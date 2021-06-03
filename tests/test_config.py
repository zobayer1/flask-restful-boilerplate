# -*- coding: utf-8 -*-
import sys

if sys.version_info < (3, 8):
    # noinspection PyUnresolvedReferences
    from importlib_metadata import version
else:
    from importlib.metadata import version


def test_env(app):
    """Test fails if app was not initialized with testing configurations"""
    assert app.env == "testing"
    assert app.testing


def test_application_version(app):
    """Test fails if importlib metadata could not be loaded from metadata"""
    assert app.name == "flask_tutorial"
    assert len(version(app.name)) > 0
