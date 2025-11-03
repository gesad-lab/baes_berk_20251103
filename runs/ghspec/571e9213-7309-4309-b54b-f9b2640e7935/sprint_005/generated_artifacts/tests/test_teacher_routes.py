```python
import pytest
from fastapi.testclient import TestClient
from main import app  # Assuming your FastAPI app is defined in main.py
from models.teacher import Teacher  # Importing the Teacher model
from schemas.teacher_schema import CreateTeacherRequestSchema, TeacherSchema  # Importing schemas
from sqlalchemy.exc import IntegrityError

client = TestClient(app)

@pytest.fixture(scope="module")
def setup_database():
    """
    Fixture to set up and tear down the database for integration tests.
    This should create a fresh database before tests and drop it afterwards.
    """
    # Setup code to create a new database for tests
    yield  # Tests will run here
    # Teardown code to drop the database

def test_create_teacher():
    """Test creating a new Teacher with valid data."""
    response = client.post("/teachers", json={"name": "John Doe", "email": "john@example.com"})
    
    assert response.status_code == 201  # Check for success response
    data = response.json()
    assert data["name"] == "John Doe"
    assert data["email"] == "john@example.com"

def test_view_teacher_details():
    """Test retrieving the details of a specific Teacher."""
    # Assuming we already have a teacher created
    teacher_id = 1  # Replace with proper id for your testing environment
    response = client.get(f"/teachers/{teacher_id}")
    
    assert response.status_code == 200  # Check for success response
    data = response.json()
    assert "name" in data
    assert "email" in data

def test_create_teacher_missing_fields():
    """Test error handling when creating a Teacher without required fields."""
    response = client.post("/teachers", json={"name": ""})  # Missing email
    assert response.status_code == 400  # Check for client error response
    assert "detail" in response.json()  # Expecting an error message

def test_retrieve_all_teachers():
    """Test retrieving a list of all Teachers."""
    response = client.get("/teachers")
    
    assert response.status_code == 200  # Check for success response
    data = response.json()
    # Expecting a list in the response
    assert isinstance(data, list)
```