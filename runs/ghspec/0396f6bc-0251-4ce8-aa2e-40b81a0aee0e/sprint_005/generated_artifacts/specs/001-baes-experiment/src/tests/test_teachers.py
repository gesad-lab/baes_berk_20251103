```python
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
from models import Base, Teacher  # Import the Teacher model
from your_app import app  # Import the FastAPI application

# Setup for SQLite in-memory database for testing
@pytest.fixture(scope='module')
def test_database():
    # Create a new SQLite database (in-memory)
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(bind=engine)  # Create all tables
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # Setup the FastAPI TestClient
    with TestingSessionLocal() as session:
        yield session  # Provide the session to the tests

# Initialize Test Client
@pytest.fixture(scope='module')
def client(test_database):
    app.dependency_overrides[YourDatabaseSessionDependency] = lambda: test_database  # Override database dependency
    with TestClient(app) as c:
        yield c  # Provide the TestClient to the tests

def test_create_teacher(client):
    response = client.post("/teachers", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 200
    assert response.json() == {"message": "Teacher created successfully."}

def test_create_teacher_missing_name(client):
    response = client.post("/teachers", json={"email": "john.doe@example.com"})
    assert response.status_code == 400
    assert "name" in response.json()["error"]["message"]

def test_create_teacher_invalid_email(client):
    response = client.post("/teachers", json={"name": "John Doe", "email": "invalid-email"})
    assert response.status_code == 400
    assert "email" in response.json()["error"]["message"]

def test_retrieve_teachers(client):
    # First, create a teacher to retrieve
    client.post("/teachers", json={"name": "Jane Doe", "email": "jane.doe@example.com"})
    response = client.get("/teachers")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert "teachers" in response.json()
    assert len(response.json()["teachers"]) > 0  # Ensure at least one teacher is returned
```