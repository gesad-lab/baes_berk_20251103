import pytest
from fastapi.testclient import TestClient
from src.main import app  # Ensure this imports your FastAPI application

client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_database():
    # Here you would set up your database for testing
    # This can involve creating tables and seeding data if necessary
    pass  # Implement database setup and teardown as needed

def test_create_student_success():
    response = client.post("/students", json={"name": "John Doe"})
    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["name"] == "John Doe"

def test_create_student_missing_name():
    response = client.post("/students", json={})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Name is required"}}

def test_retrieve_student_success():
    creation_response = client.post("/students", json={"name": "Alice"})
    student_id = creation_response.json()["id"]

    response = client.get(f"/students/{student_id}")
    assert response.status_code == 200
    assert response.json()["id"] == student_id
    assert response.json()["name"] == "Alice"

def test_retrieve_student_not_found():
    response = client.get("/students/99999")  # Assuming this ID does not exist
    assert response.status_code == 404
    assert "error" in response.json()

# Add more tests as needed to ensure full coverage of endpoints and error states.