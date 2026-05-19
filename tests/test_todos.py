from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root_endpoint():
    """Test root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert "Todo API" in response.json().get("message", "")


def test_create_todo():
    """Test creating a new todo"""
    response = client.post(
        "/api/todos/",
        json={
            "title": "Test Todo from CI",
            "description": "Testing in GitHub Actions"
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test Todo from CI"
    assert "id" in data