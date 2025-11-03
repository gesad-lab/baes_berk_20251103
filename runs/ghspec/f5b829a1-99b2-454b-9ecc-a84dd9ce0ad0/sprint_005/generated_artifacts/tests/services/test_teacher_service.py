```python
import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.services.teacher_service import TeacherService

# Initialize the FastAPI test client
client = TestClient(app)

@pytest.fixture(scope="module")
def setup_database():
    """Fixture to setup the in-memory database for testing."""
    # Setup logic to create required tables and seed initial data as necessary
    yield
    # Cleanup logic if necessary

def test_create_teacher_success(setup_database):
    """Test creating a teacher with valid name and email information."""
    response = client.post("/teachers", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["name"] == "John Doe"
    assert response.json()["email"] == "john.doe@example.com"

def test_create_teacher_missing_name(setup_database):
    """Test attempting to create a teacher without a name."""
    response = client.post("/teachers", json={"email": "john.doe@example.com"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Name is required."}

def test_create_teacher_missing_email(setup_database):
    """Test attempting to create a teacher without an email."""
    response = client.post("/teachers", json={"name": "John Doe"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Email is required."}

def test_create_teacher_invalid_email_format(setup_database):
    """Test creating a teacher with an invalid email format."""
    response = client.post("/teachers", json={"name": "John Doe", "email": "not-an-email"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid email format."}
```