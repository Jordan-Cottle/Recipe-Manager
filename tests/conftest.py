import pytest

from recipe_manager.app import app


@pytest.fixture(name="client")
def test_client():
    return app.test_client()
