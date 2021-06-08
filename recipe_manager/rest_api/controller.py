""" Enpoint definitions for the rest api. """

from http import HTTPStatus

from rest_api import rest_api_v1


@rest_api_v1.route("/health")
def health():
    """Send the index page to the user."""

    return {"status": "ok"}, HTTPStatus.OK
