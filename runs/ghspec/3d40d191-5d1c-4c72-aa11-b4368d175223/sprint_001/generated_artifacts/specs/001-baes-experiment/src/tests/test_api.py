```python
import pytest
from fastapi.testclient import TestClient
from src.api import app  # Import your FastAPI app instance

@pytest.fixture()
def client():
    """Create a test client for the FastAPI app."""
    return TestClient(app)

def test_create_student(client):
    """Test creating a student with a valid name."""
    response = client.post("/students", json={"name": "John Doe"})
    assert response.status_code == 201
    assert response.json()["name"] == "John Doe"

def test_create_student_without_name(client):
    """Test creating a student without a name returns a validation error."""
    response = client.post("/students", json={})
    assert response.status_code == 400
    assert "detail" in response.json()  # Check that the response contains an error detail

def test_create_student_with_empty_name(client):
    """Test creating a student with an empty name returns a validation error."""
    response = client.post("/students", json={"name": ""})
    assert response.status_code == 400
    assert "detail" in response.json()  # Verify that the error detail is present

def test_get_student(client):
    """Test retrieving a student by ID, assuming a student is already created with ID 1."""
    # This test assumes that there is already a student created with ID 1
    response = client.get("/students/1")
    assert response.status_code == 200
    assert "name" in response.json()  # Ensure that the response contains a name field

def test_get_student_not_found(client):
    """Test retrieving a student by ID that does not exist returns a 404 error."""
    response = client.get("/students/999")  # Assuming ID 999 does not exist
    assert response.status_code == 404
    assert "detail" in response.json()  # Check that the response contains an error detail
```