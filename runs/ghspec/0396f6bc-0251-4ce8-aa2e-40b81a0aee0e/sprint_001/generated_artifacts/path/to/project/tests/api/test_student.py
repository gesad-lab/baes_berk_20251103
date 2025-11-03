```python
import pytest
from fastapi.testclient import TestClient
from src.main import app  # Assuming app is your FastAPI app
from src.models import Student
from src.database import get_db, engine, Base

# Create a test client for the FastAPI app
client = TestClient(app)

# Set up the database before tests
@pytest.fixture(scope='module', autouse=True)
def setup_database():
    # Create the database tables
    Base.metadata.create_all(bind=engine)
    yield
    # Drop the database tables after tests
    Base.metadata.drop_all(bind=engine)

def test_create_student_success():
    """Test successful student creation."""
    response = client.post("/students", json={"name": "John Doe"})
    assert response.status_code == 200
    assert "id" in response.json()
    assert response.json()["name"] == "John Doe"

def test_create_student_without_name():
    """Test creating a student without a name returns a 400 error."""
    response = client.post("/students", json={})
    assert response.status_code == 400
    assert response.json() == {
        "error": {
            "code": "E400",
            "message": "Name is required."
        }
    }

def test_retrieve_student_success():
    """Test retrieving a student by ID."""
    # First, create a student to retrieve
    create_response = client.post("/students", json={"name": "Jane Doe"})
    student_id = create_response.json()["id"]
    
    # Then retrieve the created student
    response = client.get(f"/students/{student_id}")
    assert response.status_code == 200
    assert response.json() == {"id": student_id, "name": "Jane Doe"}

def test_retrieve_non_existing_student():
    """Test retrieving a non-existing student returns a 404 error."""
    response = client.get("/students/99999")  # Assuming this ID does not exist
    assert response.status_code == 404
    assert response.json() == {
        "error": {
            "code": "E404",
            "message": "Student not found."
        }
    }
```