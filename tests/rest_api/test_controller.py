""" Test module for recipe-manager/app.py. """
from http import HTTPStatus


def test_health(client):
    """Test that the api is registered properly and responds to health checks."""

    response = client.get("/api/v1/health")
    assert response.status_code == HTTPStatus.OK, response.get_data(as_text=True)
    assert response.json == {"status": "ok"}
