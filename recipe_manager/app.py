""" Main application module for the recipe manager api. """

from flask import Flask
from http import HTTPStatus

app = Flask(
    "recipe-manager",
)


@app.route("/health")
def index_page():
    """Send the index page to the user."""

    return {"status": "ok"}, HTTPStatus.OK
