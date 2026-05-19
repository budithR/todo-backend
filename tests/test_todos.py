from fastapi.testclient import TestClient
from app.main import app
import pytest

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert "Todo API" in response.json()["message"]

def test_create_todo():
    response = client.post(
        "/api/todos/",
        json={
            "title": "Test Todo from CI",
            "description": "Testing CI pipeline"
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test Todo from CI"
    assert "id" in data