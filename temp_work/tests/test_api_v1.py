from fastapi.testclient import TestClient
from main import app
from models.schemas import RequestPayload, TaskName

client = TestClient(app)

def test_capabilities():
    response = client.get("/api/v1/capabilities")
    assert response.status_code == 200
    assert "models" in response.json()
    assert "capabilities" in response.json()

def test_heartbeat():
    response = client.post("/api/v1/heartbeat")
    assert response.status_code == 200
    assert response.json() == {"status": "alive"}

def test_generate_parsed():
    test_payload = {
        "task_name": "five_ws_extraction",
        "citation": True,
        "reasoning": False
    }
    response = client.post("/api/v1/generate_parsed", json=test_payload)
    assert response.status_code == 200
    data = response.json()
    assert "extraction" in data
    assert "who" in data["extraction"]
    assert "info" in data
    assert data["info"].get("citation") is not None