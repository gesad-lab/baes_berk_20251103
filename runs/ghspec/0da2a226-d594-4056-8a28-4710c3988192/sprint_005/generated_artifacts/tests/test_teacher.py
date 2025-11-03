```python
import pytest
from fastapi.testclient import TestClient
from main import app
from models import Teacher
from sqlalchemy.orm import Session
from database import get_db, Base, engine

# Create the test client used for sending requests to the application
client = TestClient(app)

# Dependency override for the database session
def override_get_db():
    db = Session(bind=engine)
    yield db
    db.close()

# Setup the test database and create the necessary tables
@pytest.fixture(scope="module", autouse=True)
def setup_database():
    # Create the database tables
    Base.metadata.create_all(bind=engine)
    yield  # This allows tests to run
    # Drop the database tables after tests are complete
    Base.metadata.drop_all(bind=engine)

# Test the creation of a new Teacher entity
def test_create_teacher():
    response = client.post("/teachers/", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201
    assert response.json()["name"] == "John Doe"
    assert response.json()["email"] == "john.doe@example.com"

# Test creating a Teacher without required fields
def test_create_teacher_missing_fields():
    response = client.post("/teachers/", json={"name": ""})
    assert response.status_code == 422  # Unprocessable Entity
    assert "detail" in response.json()

# Test creating a Teacher with duplicate email
def test_create_teacher_duplicate_email():
    client.post("/teachers/", json={"name": "John Doe", "email": "john.doe@example.com"})
    response = client.post("/teachers/", json={"name": "Jane Doe", "email": "john.doe@example.com"})
    assert response.status_code == 400  # Bad Request
    assert "detail" in response.json()

# Test retrieving the list of existing Teachers
def test_get_teachers():
    response = client.get("/teachers/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Ensure response is a list
    assert len(response.json()) > 0  # Ensure there's at least one Teacher

# Test retrieval of teachers when no records exist
def test_get_teachers_empty():
    # Drop all teachers (if any created in prior tests)
    with Session(bind=engine) as db:
        db.query(Teacher).delete()
        db.commit()
    
    response = client.get("/teachers/")
    assert response.status_code == 200
    assert response.json() == []  # Ensure the response is an empty list
```