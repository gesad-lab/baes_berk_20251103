```python
import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.models.teacher import Teacher
from src.database.database import get_db, Base, engine

# Create the FastAPI test client
client = TestClient(app)

# Setup the test database
@pytest.fixture(scope="module", autouse=True)
def setup_database():
    # Create the database tables including Teacher table
    Base.metadata.create_all(bind=engine)
    
    # Add any necessary setup data for tests (if needed)
    yield
    
    # Teardown: drop all tables after tests are done
    Base.metadata.drop_all(bind=engine)

def test_create_teacher_success():
    """Test creating a Teacher with valid data."""
    response = client.post("/teachers/", json={"name": "John Doe", "email": "john@example.com"})
    assert response.status_code == 201
    assert response.json()["name"] == "John Doe"
    assert response.json()["email"] == "john@example.com"

def test_create_teacher_missing_name():
    """Test creating a Teacher without the required name field."""
    response = client.post("/teachers/", json={"email": "john@example.com"})
    assert response.status_code == 422  # Unprocessable Entity
    assert response.json()["detail"][0]["msg"] == "field required"

def test_create_teacher_missing_email():
    """Test creating a Teacher without the required email field."""
    response = client.post("/teachers/", json={"name": "John Doe"})
    assert response.status_code == 422  # Unprocessable Entity
    assert response.json()["detail"][0]["msg"] == "field required"

def test_get_teacher_success():
    """Test retrieving a Teacher's details by ID."""
    # First, create a Teacher to retrieve
    create_response = client.post("/teachers/", json={"name": "Jane Doe", "email": "jane@example.com"})
    teacher_id = create_response.json()["id"]
    
    # Now, retrieve the Teacher
    response = client.get(f"/teachers/{teacher_id}")
    assert response.status_code == 200
    assert response.json()["id"] == teacher_id
    assert response.json()["name"] == "Jane Doe"
    assert response.json()["email"] == "jane@example.com"

def test_get_teacher_not_found():
    """Test retrieving a Teacher which does not exist."""
    response = client.get("/teachers/999")
    assert response.status_code == 404  # Not Found
    assert response.json()["detail"] == "Teacher not found."
```