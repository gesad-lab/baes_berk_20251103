```python
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app, Base, get_db, Student  # Import the Student model
from sqlalchemy.exc import IntegrityError

# Setup for testing
DATABASE_URL = "postgresql://user:password@localhost/test_db"

# Create a new database engine
engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the database tables
Base.metadata.create_all(bind=engine)

# Override the dependency
@pytest.fixture(scope="module")
def test_client():
    # Use the FastAPI test client
    with TestClient(app) as client:
        yield client

@pytest.fixture(scope="module")
def db_session():
    # Create a new session for the tests
    connection = engine.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)
    
    yield session  # This will be the session used in tests

    session.close()
    transaction.rollback()
    connection.close()

def test_create_student_with_email(test_client):
    response = test_client.post("/students", json={"name": "John Doe", "email": "john.doe@example.com"})
    
    assert response.status_code == 201  # Check for success
    data = response.json()
    
    # Validate the response includes the student's details and email
    assert "id" in data
    assert data["name"] == "John Doe"
    assert data["email"] == "john.doe@example.com"

def test_create_student_without_email(test_client):
    response = test_client.post("/students", json={"name": "Jane Doe"})
    
    assert response.status_code == 400  # Check for error response
    assert response.json() == {"detail": "Email field is required."}

def test_retrieve_students_includes_email(test_client, db_session):
    # Create a test student with email
    test_student = Student(name="Alice Smith", email="alice.smith@example.com")
    db_session.add(test_student)
    db_session.commit()
    
    response = test_client.get("/students")
    
    assert response.status_code == 200  # Check for successful retrieval
    data = response.json()
    
    # Validate that the returned students include email
    assert len(data) > 0
    assert any(student["email"] == "alice.smith@example.com" for student in data)  # Check for specific email
```