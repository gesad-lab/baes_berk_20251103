```python
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
from src.main import app
from src.database import Base, get_db

# Set up the SQLite database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create all tables in the database
Base.metadata.create_all(bind=engine)

# Dependency override for test cases
@pytest.fixture(scope="module")
def db():
    # Create a new database session for the test
    db = TestingSessionLocal()
    try:
        yield db  # This will be the database session for the test cases
    finally:
        db.close()  # Clean up the session after tests

# Function to override get_db dependency for the FastAPI app
@pytest.fixture()
def client(db):
    # Create a FastAPI test client, overriding the database dependency
    app.dependency_overrides[get_db] = lambda: db
    with TestClient(app) as c:
        yield c  # Return the test client for use in test functions

# Sample test case for creating a student
def test_create_student(client):
    response = client.post("/students", json={"name": "John Doe"})
    assert response.status_code == 201
    assert response.json() == {"id": 1, "name": "John Doe"}

# Sample test case for retrieving students
def test_read_students(client):
    response = client.get("/students")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Verify the response is a list

# Sample test case for updating a student
def test_update_student(client):
    response = client.put("/students/1", json={"name": "John Smith"})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "John Smith"}

# Sample test case for deleting a student
def test_delete_student(client):
    response = client.delete("/students/1")
    assert response.status_code == 204
```
