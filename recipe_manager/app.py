""" Main application module for the recipe manager api. """

from flask import Flask

from rest_api import rest_api_v1


def create_app():
    """Create and setup the application object."""
    app = Flask(
        "recipe-manager",
    )

    app.register_blueprint(rest_api_v1, url_prefix="/api/v1")

    return app
