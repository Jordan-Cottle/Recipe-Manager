""" Common fixtures useful for all test modules. """

import pytest

from app import create_app

from config import get_config


@pytest.fixture(name="client")
def create_test_client():
    """Create a test client for the flask application."""

    app = create_app()
    with app.test_client() as test_client:
        yield test_client


@pytest.fixture(name="config")
def get_configuration():
    """Fixture for easily providing config object to tests"""

    return get_config()
