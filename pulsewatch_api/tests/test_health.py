from fastapi.testclient import TestClient
from pulsewatch_api.main import app

client = TestClient(app)

def test_live():
    r = client.get("/health/live")
    assert r.status_code == 200
    assert r.json()["live"] is True

def test_ready():
    r = client.get("/health/ready")
    assert r.status_code == 200
    assert r.json()["ready"] is True
