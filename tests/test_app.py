""" Test module for recipe-manager/app.py. """
from http import HTTPStatus

def test_health(client):
    response = client.get("/health")
    assert response.status_code == HTTPStatus.OK
    assert response.json == {"status": "ok"}
