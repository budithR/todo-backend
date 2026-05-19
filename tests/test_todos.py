import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200

def test_create_todo():
    response = client.post("/api/todos/", json={
        "title": "Test Todo",
        "description": "This is a test"
    })
    assert response.status_code == 201
    assert response.json()["title"] == "Test Todo"