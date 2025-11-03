import pytest
from fastapi.testclient import TestClient
from src.services.student_service import app, list_students, create_student, update_student, delete_student

client = TestClient(app)

@pytest.fixture
def sample_student():
    return {
        "name": "John Doe",
        "age": 20,
        "grade": "Sophomore"
    }

def test_create_student(sample_student):
    """Test successful student creation with valid data."""
    response = client.post("/students/", json=sample_student)
    assert response.status_code == 201
    assert response.json().get("name") == sample_student["name"]

def test_list_students(sample_student):
    """Test listing of students."""
    # First, create a student to ensure there is at least one record to retrieve
    client.post("/students/", json=sample_student)
    
    response = client.get("/students/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0

def test_get_student_by_id(sample_student):
    """Test retrieving a student by ID."""
    # Create a student to retrieve
    create_response = client.post("/students/", json=sample_student)
    student_id = create_response.json().get("id")
    
    # Now attempt to retrieve that student
    response = client.get(f"/students/{student_id}")
    assert response.status_code == 200
    assert response.json().get("id") == student_id

def test_update_student(sample_student):
    """Test successful update of a student."""
    # Create a student to update
    create_response = client.post("/students/", json=sample_student)
    student_id = create_response.json().get("id")
    
    updated_data = {"name": "Jane Doe", "age": 21, "grade": "Junior"}
    response = client.put(f"/students/{student_id}", json=updated_data)
    assert response.status_code == 200
    assert response.json().get("name") == updated_data["name"]

def test_delete_student():
    """Test successful deletion of a student."""
    # Create a student to delete
    create_response = client.post("/students/", json={"name": "Mark Smith", "age": 22, "grade": "Senior"})
    student_id = create_response.json().get("id")
    
    # Now delete the student
    delete_response = client.delete(f"/students/{student_id}")
    assert delete_response.status_code == 204  # No content on successful delete

    # Try to retrieve the deleted student (should result in 404)
    get_response = client.get(f"/students/{student_id}")
    assert get_response.status_code == 404  # Not found after deletion
