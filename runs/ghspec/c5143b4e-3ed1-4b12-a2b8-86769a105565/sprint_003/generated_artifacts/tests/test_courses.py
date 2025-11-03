```python
import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.models import Course
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.database import Base


# Setup the test client
@pytest.fixture(scope="module")
def test_client():
    engine = create_engine("sqlite:///./test.db")
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
    # Create the database tables
    Base.metadata.create_all(bind=engine)
    
    with TestClient(app) as client:
        yield client

    # Drop the database tables after tests
    Base.metadata.drop_all(bind=engine)


def test_create_course(test_client):
    # Test creating a course with valid input
    response = test_client.post("/courses", json={"name": "Mathematics", "level": "Beginner"})
    assert response.status_code == 200
    assert response.json() == {"name": "Mathematics", "level": "Beginner"}


def test_create_course_missing_name(test_client):
    # Test creating a course without a name
    response = test_client.post("/courses", json={"level": "Beginner"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Validation error", "details": {"name": "Field required"}}}


def test_create_course_missing_level(test_client):
    # Test creating a course without a level
    response = test_client.post("/courses", json={"name": "Mathematics"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Validation error", "details": {"level": "Field required"}}}


def test_get_courses(test_client):
    # Test retrieving courses
    test_client.post("/courses", json={"name": "Mathematics", "level": "Beginner"})
    test_client.post("/courses", json={"name": "Science", "level": "Intermediate"})
    
    response = test_client.get("/courses")
    assert response.status_code == 200
    assert len(response.json()) == 2
    assert {"name": "Mathematics", "level": "Beginner"} in response.json()
    assert {"name": "Science", "level": "Intermediate"} in response.json()
```