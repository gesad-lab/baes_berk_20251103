import pytest
from fastapi.testclient import TestClient
from api.teachers import router as teachers_router
from api.models.teachers import TeacherCreateRequest, TeacherResponse

# Instantiate the TestClient with the router to be tested
client = TestClient(teachers_router)

@pytest.fixture
def clear_teachers_db():
    """Fixture to clear the teachers database before tests."""
    # Code to clear the teachers table would go here, e.g.,
    # async with aiosqlite.connect("database.db") as db:
    #     await db.execute("DELETE FROM teacher")
    #     await db.commit()
    pass  # Replace with actual logic

def test_create_teacher_with_valid_data(clear_teachers_db):
    """Test creating a new teacher with valid data."""
    response = client.post("/teachers", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,  # Replace with appropriate dynamic check
        "name": "John Doe",
        "email": "john.doe@example.com"
    }

def test_create_teacher_with_missing_name(clear_teachers_db):
    """Test creating a teacher with missing name."""
    response = client.post("/teachers", json={"email": "john.doe@example.com"})
    assert response.status_code == 422  # Validation error
    assert response.json()["detail"][0]["msg"] == "field required"

def test_create_teacher_with_invalid_email(clear_teachers_db):
    """Test creating a teacher with an invalid email format."""
    response = client.post("/teachers", json={"name": "John Doe", "email": "invalid-email"})
    assert response.status_code == 422  # Validation error
    assert response.json()["detail"][0]["msg"] == "value is not a valid email address"

def test_list_teachers(clear_teachers_db):
    """Test retrieving the list of all teachers."""
    client.post("/teachers", json={"name": "John Doe", "email": "john.doe@example.com"})
    client.post("/teachers", json={"name": "Jane Smith", "email": "jane.smith@example.com"})
    
    response = client.get("/teachers")
    assert response.status_code == 200
    assert len(response.json()) == 2  # Ensure both teachers are listed
    assert response.json()[0]["name"] == "John Doe"
    assert response.json()[1]["name"] == "Jane Smith"

def test_list_teachers_no_teachers(clear_teachers_db):
    """Test retrieving the list of teachers when none exist."""
    response = client.get("/teachers")
    assert response.status_code == 200
    assert response.json() == []  # Expect an empty list

# Include additional tests for edge cases as necessary.