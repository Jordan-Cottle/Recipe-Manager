""" Main application module for the recipe manager api. """
import os

from flask import Flask
from werkzeug.utils import import_string

from database import Database, close_session, inject_session
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

    config = import_string(CONFIG_MAP.get(APPLICATION_MODE))()
    app.config.from_object(config)

    # Set up common database
    app.config["DATABASE"] = Database(app.config["DATABASE_CONFIG"])
    app.before_request(inject_session)
    app.after_request(close_session)

    app.register_blueprint(rest_api_v1, url_prefix="/api/v1")

    return app
