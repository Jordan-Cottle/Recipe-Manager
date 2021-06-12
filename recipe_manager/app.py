""" Main application module for the recipe manager api. """

from flask import Flask

from config import get_config
from database import Database, close_session, inject_session
from rest_api import rest_api_v1


def create_app():
    """Create and setup the application object."""
    app = Flask("recipe-manager")

    config = get_config()
    app.config.from_object(config)

    # Set up common database
    app.config["DATABASE"] = Database(app.config["DATABASE_CONFIG"])
    app.before_request(inject_session)
    app.after_request(close_session)

    app.register_blueprint(rest_api_v1, url_prefix="/api/v1")

    return app
