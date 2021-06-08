""" Present database logic as a unified interface to the rest of the application. """

from flask import g, current_app

from .engine import Database, DatabaseSession


def inject_session():
    """Add a new database session to the g object for each request."""

    g.session = current_app.config.get("DATABASE").session


def close_session(response):
    """Attempt to finalize transactions and close the session."""

    g.session.finalize()

    return response
