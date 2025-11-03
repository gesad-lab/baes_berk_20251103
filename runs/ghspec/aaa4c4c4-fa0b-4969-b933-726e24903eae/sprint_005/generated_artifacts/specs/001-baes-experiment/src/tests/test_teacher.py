```python
import pytest
from fastapi.testclient import TestClient
from main import app  # Assuming your FastAPI app is instantiated in main.py

# Initialize the test client
client = TestClient(app)

@pytest.fixture(scope="module")
def setup_database():
    """Fixture to set up the database state before tests and clean up afterwards."""
    # Set up the database for tests
    # Here we can create the Teacher table and any necessary seed data
    pass

@pytest.fixture(scope="module")
def create_teacher(setup_database):
    """Fixture to create a teacher for testing purposes."""
    response = client.post("/teachers", json={"name": "Jane Smith", "email": "jane.smith@example.com"})
    assert response.status_code == 201
    return response.json()  # Return the created teacher data for further tests

def test_create_teacher():
    """Test the creation of a new teacher."""
    response = client.post("/teachers", json={"name": "Alice Johnson", "email": "alice.johnson@example.com"})
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["name"] == "Alice Johnson"
    assert data["email"] == "alice.johnson@example.com"

def test_create_teacher_missing_fields():
    """Test creating a teacher without required fields."""
    response = client.post("/teachers", json={"name": "Incomplete Teacher"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Missing required fields", "details": {"email": "This field is required."}}}

def test_get_teacher_details(create_teacher):
    """Test retrieval of teacher details."""
    teacher_id = create_teacher["id"]
    response = client.get(f"/teachers/{teacher_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == teacher_id
    assert data["name"] == create_teacher["name"]
    assert data["email"] == create_teacher["email"]

def test_get_teacher_not_found():
    """Test retrieval of a teacher that does not exist."""
    response = client.get("/teachers/9999")  # Assuming this ID does not exist
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E002", "message": "Teacher not found", "details": {}}}
```