""" Common fixtures useful for all test modules. """

import pytest

from app import create_app


@pytest.fixture(name="client")
def create_test_client():
    """Create a test client for the flask application."""

    app = create_app()
    with app.test_client() as test_client:
        yield test_client
