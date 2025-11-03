```python
# tests/test_database.py

import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.models import Base, Course, Enrollment, Teacher  # Import the new Teacher model
from app.database import engine

# Set up the test database
@pytest.fixture(scope="module")
def test_db():
    # Create the database schema, including the Course, Enrollment, and Teacher tables
    Base.metadata.create_all(bind=engine)
    yield
    # Drop the database schema after tests are done
    Base.metadata.drop_all(bind=engine)

# Test creating a teacher with valid data
def test_create_teacher_valid():
    client = TestClient(app)
    response = client.post("/teachers", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201
    assert response.json() == {"id": 1, "name": "John Doe", "email": "john.doe@example.com"}

# Test creating a teacher without a name
def test_create_teacher_missing_name():
    client = TestClient(app)
    response = client.post("/teachers", json={"email": "john.doe@example.com"})
    assert response.status_code == 422  # Unprocessable Entity
    assert response.json() == {"detail": [{"loc": ["body", "name"], "msg": "field required", "type": "value_error.missing"}]}

# Test creating a teacher without an email
def test_create_teacher_missing_email():
    client = TestClient(app)
    response = client.post("/teachers", json={"name": "John Doe"})
    assert response.status_code == 422  # Unprocessable Entity
    assert response.json() == {"detail": [{"loc": ["body", "email"], "msg": "field required", "type": "value_error.missing"}]}

# Additional tests for retrieving teacher details would go here...
```