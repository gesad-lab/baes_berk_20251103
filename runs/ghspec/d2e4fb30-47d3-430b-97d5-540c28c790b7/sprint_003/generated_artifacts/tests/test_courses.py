```python
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app, Base, get_db
from sqlalchemy.exc import IntegrityError

# Setup for testing
DATABASE_URL = "postgresql://user:password@localhost/test_db"

# Create a new database engine
engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the tables in the test database
Base.metadata.create_all(bind=engine)

# Dependency override for testing
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

# Test cases for Course API
@pytest.fixture()
def client():
    return TestClient(app)

def test_create_course(client):
    # Test creating a course with valid data
    response = client.post("/courses", json={"name": "Math 101", "level": "Beginner"})
    assert response.status_code == 200
    assert "id" in response.json()
    assert response.json()["name"] == "Math 101"
    assert response.json()["level"] == "Beginner"

def test_create_course_missing_info(client):
    # Test creating a course with missing name
    response = client.post("/courses", json={"level": "Beginner"})
    assert response.status_code == 422  # Unprocessable Entity
    assert response.json()["detail"][0]["msg"] == "field required"

    # Test creating a course with missing level
    response = client.post("/courses", json={"name": "Math 101"})
    assert response.status_code == 422  # Unprocessable Entity
    assert response.json()["detail"][0]["msg"] == "field required"

def test_retrieve_courses(client):
    # Test retrieving courses
    response = client.get("/courses")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Should return a list
```