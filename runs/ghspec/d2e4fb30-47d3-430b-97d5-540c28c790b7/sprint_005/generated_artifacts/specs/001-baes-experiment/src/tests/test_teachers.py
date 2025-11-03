```python
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app, Base, get_db
from sqlalchemy.exc import IntegrityError
from src.models.teacher import Teacher

# Setup for testing
DATABASE_URL = "postgresql://user:password@localhost/test_db"

# Create a new database engine for testing
engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a fixture for getting the test client
@pytest.fixture(scope="module")
def client():
    # Create the tables in the test database
    Base.metadata.create_all(bind=engine)
    yield TestClient(app)
    # Drop the tables after tests are complete
    Base.metadata.drop_all(bind=engine)

# Test scenarios
def test_create_teacher(client):
    # Test creating a new teacher
    response = client.post("/teachers", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201
    assert response.json() == {"message": "Teacher created successfully."}

def test_create_teacher_duplicate_email(client):
    # Test creating a teacher with a duplicate email
    response = client.post("/teachers", json={"name": "Jane Smith", "email": "john.doe@example.com"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Email is already associated with another teacher."}}

def test_retrieve_teachers(client):
    # Test retrieving the list of teachers
    response = client.get("/teachers")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0  # List should not be empty if one teacher is created
    assert all('name' in teacher and 'email' in teacher for teacher in response.json())
```