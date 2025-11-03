import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.models.student import Student
from src.db.database import SessionLocal
from src.schemas.student_schemas import StudentCreate, StudentResponse

client = TestClient(app)

@pytest.fixture(scope="module")
def setup_database():
    """Setup database for testing."""
    # Create database connection and tables
    db = SessionLocal()
    yield db
    db.close()

@pytest.fixture(scope="module")
def create_student(setup_database):
    """Create a student fixture."""
    student_data = {
        "name": "John Doe",
        "email": "johndoe@example.com"  # Ensure to test with email field
    }
    response = client.post("/students/", json=student_data)
    return response.json()

def test_create_student(create_student):
    """Test creating a student."""
    assert create_student["name"] == "John Doe"
    assert create_student["email"] == "johndoe@example.com"
    assert create_student["id"] is not None

def test_get_student(create_student):
    """Test retrieving the created student."""
    student_id = create_student["id"]
    response = client.get(f"/students/{student_id}")
    student = response.json()
    
    assert response.status_code == 200
    assert student["id"] == student_id
    assert student["name"] == "John Doe"
    assert student["email"] == "johndoe@example.com"

def test_update_student(create_student):
    """Test updating the created student."""
    student_id = create_student["id"]
    updated_data = {
        "name": "Johnathan Doe",
        "email": "johnathan.doe@example.com"  # Update email to test email field
    }
    response = client.put(f"/students/{student_id}", json=updated_data)
    updated_student = response.json()
    
    assert response.status_code == 200
    assert updated_student["name"] == "Johnathan Doe"
    assert updated_student["email"] == "johnathan.doe@example.com"

def test_delete_student(create_student):
    """Test deleting the created student."""
    student_id = create_student["id"]
    response = client.delete(f"/students/{student_id}")
    
    assert response.status_code == 204  # No content
    assert client.get(f"/students/{student_id}").status_code == 404  # Not found after deletion

def test_create_student_invalid_email():
    """Test creating a student with an invalid email."""
    invalid_student_data = {
        "name": "Invalid Student",
        "email": "invalid-email"  # Invalid email format
    }
    response = client.post("/students/", json=invalid_student_data)
    
    assert response.status_code == 422  # Unprocessable Entity as per FastAPI response for validation errors
    assert "email" in response.json()["detail"][0]["loc"]  # Check that the error is related to the email field
    assert response.json()["detail"][0]["msg"] == "value is not a valid email address"