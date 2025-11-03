```python
import pytest
from fastapi.testclient import TestClient
from src.app import app
from src.db import get_db
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from src.models import Base, Student

# Setting up the test database in memory
@pytest.fixture(scope="module")
def test_db():
    # Create a new SQLite database in memory
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(bind=engine)

    # Create a new session for testing
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    yield SessionLocal

    # Cleanup
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="module")
def test_client(test_db):
    # Dependency override to use the in-memory database
    app.dependency_overrides[get_db] = lambda: test_db()
    with TestClient(app) as client:
        yield client

def test_create_student_with_email(test_client):
    """Test creating a new student with an email."""
    response = test_client.post("/students/", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["name"] == "John Doe"
    assert data["email"] == "john.doe@example.com"

def test_create_student_missing_email(test_client):
    """Test error handling when the email is missing."""
    response = test_client.post("/students/", json={"name": "Jane Doe"})
    assert response.status_code == 422  # Unprocessable Entity
    assert response.json() == {"detail": [{"loc": ["body", "email"], "msg": "field required", "type": "value_error.missing"}]}

def test_retrieve_student_with_email(test_client):
    """Test retrieving student information including email."""
    response = test_client.get("/students/1/")  # Assuming the newly created student has ID 1
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "John Doe"
    assert data["email"] == "john.doe@example.com"

def test_existing_students_preserved(test_client):
    """Test that existing student data is retained after migration."""
    # Ensure there's at least one existing student
    response = test_client.post("/students/", json={"name": "Existing Student", "email": "existing@example.com"})
    assert response.status_code == 201

    # Retrieve to verify integrity
    response = test_client.get("/students/2/")  # Assuming this is the ID of the existing student
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Existing Student"
    assert data["email"] == "existing@example.com"
```