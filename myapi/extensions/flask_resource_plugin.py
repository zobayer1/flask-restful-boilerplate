# -*- coding: utf-8 -*-
from apispec.exceptions import APISpecError
from apispec_webframeworks.flask import FlaskPlugin
from flask import current_app


class FlaskResourcePlugin(FlaskPlugin):
    @staticmethod
    def _rule_for_view(view, app=None):
        if app is None:
            app = current_app
        view_funcs = app.view_functions
        endpoint = None
        for ept, view_func in view_funcs.items():
            if hasattr(view_func, "view_class"):
                view_func = view_func.view_class
            if view_func == view:
                endpoint = ept
        if not endpoint:  # pragma: no cover
            raise APISpecError(f"Could not find endpoint for view {view}")
        for rule in app.url_map.iter_rules(endpoint):
            return rule
