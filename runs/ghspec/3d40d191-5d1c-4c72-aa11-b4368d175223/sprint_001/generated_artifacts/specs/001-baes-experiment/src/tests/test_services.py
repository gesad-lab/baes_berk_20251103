```python
import pytest
from fastapi.testclient import TestClient
from src.api import app
from src.models import Student
from src.database import get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create a new SQLite database for testing
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Fixture to provide a test client and database session
@pytest.fixture(scope="module")
def client():
    # Create the FastAPI test client
    with TestClient(app) as test_client:
        yield test_client

# Fixture to set up the database for the tests
@pytest.fixture(scope="module")
def db():
    db = TestingSessionLocal()
    yield db
    db.close()

# Test creating a student with a valid name
def test_create_student(client, db):
    response = client.post("/students", json={"name": "John Doe"})
    assert response.status_code == 201
    assert response.json()["name"] == "John Doe"

    # Verify that the student has been added to the database
    student = db.query(Student).filter(Student.name == "John Doe").first()
    assert student is not None
    assert student.name == "John Doe"

# Test creating a student without a name
def test_create_student_without_name(client):
    response = client.post("/students", json={})
    assert response.status_code == 400
    assert "detail" in response.json()  # Ensure the error response contains a detail field

# Test creating a student with an empty name
def test_create_student_with_empty_name(client):
    response = client.post("/students", json={"name": ""})
    assert response.status_code == 400
    assert "detail" in response.json()  # Ensure the error response contains a detail field

# Test creating a student with a name that's too short (assuming min length is 3)
def test_create_student_with_short_name(client):
    response = client.post("/students", json={"name": "JD"})
    assert response.status_code == 400
    assert "detail" in response.json()  # Ensure the error response contains a detail field
```