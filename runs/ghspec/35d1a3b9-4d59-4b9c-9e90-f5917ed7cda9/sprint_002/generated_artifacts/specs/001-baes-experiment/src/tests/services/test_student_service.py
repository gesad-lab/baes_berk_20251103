```python
import pytest
from fastapi.testclient import TestClient
from src.services.student_service import create_student, get_students
from src.repository import models, create_db

# Setup for tests
@pytest.fixture(scope="module")
def client():
    # Create an instance of the TestClient
    app = create_db()  # Assuming create_db initializes and sets up the FastAPI app
    yield TestClient(app)

@pytest.fixture(scope="module", autouse=True)
def setup_database():
    # Initialize the database schema for tests
    models.Base.metadata.create_all(bind=models.engine)  # Create DB schema
    yield
    models.Base.metadata.drop_all(bind=models.engine)  # Cleanup DB after tests

def test_create_student_with_valid_email(client):
    """Test creating a student with valid name and email."""
    response = client.post("/students/", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201  # Check if creation was successful
    assert "id" in response.json()       # Ensure the response contains an ID
    assert response.json()["name"] == "John Doe"
    assert response.json()["email"] == "john.doe@example.com"

def test_create_student_with_invalid_email(client):
    """Test creating a student with invalid email."""
    response = client.post("/students/", json={"name": "Jane Doe", "email": "not-an-email"})
    assert response.status_code == 400  # Check if it fails with a bad request
    assert response.json() == {"detail": "Invalid email format"}

def test_create_student_without_email(client):
    """Test creating a student without an email."""
    response = client.post("/students/", json={"name": "Alice"})
    assert response.status_code == 400  # Check for bad request due to missing email
    assert response.json() == {"detail": "Field 'email' is required."}

def test_get_students_includes_email(client):
    """Test retrieval of students to ensure emails are included."""
    # Create a student to retrieve later
    client.post("/students/", json={"name": "Bob Smith", "email": "bob.smith@example.com"})
    
    response = client.get("/students/")
    assert response.status_code == 200  # Check if the retrieval was successful
    students = response.json()
    assert len(students) > 0
    assert any(student['email'] == "bob.smith@example.com" for student in students)  # Validate email is present
```