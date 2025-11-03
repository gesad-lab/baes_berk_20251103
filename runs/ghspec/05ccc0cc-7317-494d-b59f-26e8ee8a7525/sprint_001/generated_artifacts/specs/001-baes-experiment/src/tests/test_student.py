```python
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.models import Base, Student
from app.database import engine

# Set up the test database
@pytest.fixture(scope="module")
def test_db():
    # Create the database schema
    Base.metadata.create_all(bind=engine)
    yield
    # Drop the database schema after tests are done
    Base.metadata.drop_all(bind=engine)

# Test client instance for making API requests
@pytest.fixture(scope='module')
def client(test_db):
    with TestClient(app) as c:
        yield c

def test_create_student_success(client):
    """Test successful creation of a student."""
    response = client.post("/students", json={"name": "John Doe"})
    assert response.status_code == 201
    assert "id" in response.json()  # Ensure an ID is returned
    assert response.json()["name"] == "John Doe"  # Check that the name is correct

def test_retrieve_all_students(client):
    """Test retrieval of all students."""
    response = client.get("/students")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Expect a list response
    assert len(response.json()) > 0  # At least one student should be in the list

def test_create_student_missing_name(client):
    """Test error handling for missing name when creating a student."""
    response = client.post("/students", json={})
    assert response.status_code == 422  # Unprocessable Entity
    assert response.json() == {
        "detail": [{
            "loc": ["body", "name"],
            "msg": "field required",
            "type": "value_error.missing"
        }]
    }  # Check for the specific validation error

def test_database_schema_on_startup(client):
    """Test if the database schema is created on application startup."""
    response = client.get("/students")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Ensure we can retrieve students
```