""" Main application module for the recipe manager api. """
import os
from flask import Flask

from rest_api import rest_api_v1

CONFIG_MAP = {
    "dev": "config.DevelopmentConfig",
    "prod": "config.ProductionConfig",
    "test": "config.TestingConfig",
}

APPLICATION_MODE = os.getenv("APPLICATION_MODE", "dev")


def create_app():
    """Create and setup the application object."""
    app = Flask("recipe-manager")

    app.config.from_object(CONFIG_MAP.get(APPLICATION_MODE))

    app.register_blueprint(rest_api_v1, url_prefix="/api/v1")

    return app
