from fastapi.testclient import TestClient
from graphkb.api.main import app

client = TestClient(app)


def test_add_node():
    response = client.post(
        "/nodes", json={"id": "alice", "type": "person", "properties": {"age": 30}}
    )
    assert response.status_code == 200
    assert response.json()["message"] == "Node alice added"
