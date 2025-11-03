import pytest
from fastapi.testclient import TestClient
from main import app  # Assuming your FastAPI app is instantiated in main.py

# Initialize the test client
client = TestClient(app)

@pytest.fixture(scope="module")
def create_student():
    """Fixture to create a student for testing purposes."""
    response = client.post("/students", json={"name": "John Doe", "age": 20, "class": "Math"})
    assert response.status_code == 201
    return response.json()  # Return the created student data for further use

def test_create_student():
    """Test creating a student through the API."""
    response = client.post("/students", json={"name": "Jane Smith", "age": 22, "class": "Science"})
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["name"] == "Jane Smith"
    assert data["age"] == 22
    assert data["class"] == "Science"

def test_get_student(create_student):
    """Test fetching a student by ID."""
    student_id = create_student["id"]
    response = client.get(f"/students/{student_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == student_id
    assert data["name"] == create_student["name"]
    assert data["age"] == create_student["age"]
    assert data["class"] == create_student["class"]

def test_get_non_existent_student():
    """Test fetching a non-existent student returns a 404 error."""
    response = client.get("/students/99999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Student not found"}

def test_api_response_structure(create_student):
    """Test the API response structure for fetching a student."""
    student_id = create_student["id"]
    response = client.get(f"/students/{student_id}")
    assert response.status_code == 200
    data = response.json()
    
    # Validate the structure of the response
    assert isinstance(data, dict)
    assert "id" in data
    assert "name" in data
    assert "age" in data
    assert "class" in data
    assert data["id"] == student_id

def test_create_student_invalid_data():
    """Test creating a student with invalid data returns a 422 error."""
    response = client.post("/students", json={"name": "", "age": -1, "class": ""})
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {"loc": ["body", "name"], "msg": "field required", "type": "value_error.missing"},
            {"loc": ["body", "age"], "msg": "value is not a valid integer", "type": "value_error.integer"},
            {"loc": ["body", "class"], "msg": "field required", "type": "value_error.missing"},
        ]
    }