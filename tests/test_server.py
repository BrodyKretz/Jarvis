from fastapi.testclient import TestClient

from jarvis.server import app

client = TestClient(app)


def test_index_serves_page():
    response = client.get("/")
    assert response.status_code == 200
    assert "Jarvis" in response.text


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"
