```python
import pytest
from fastapi.testclient import TestClient
from main import app  # Assuming your FastAPI app is instantiated in main.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Teacher, Course  # Assuming your models are defined in models.py

# Initialize the test client
client = TestClient(app)

# Set up the database for the test
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="module")
def setup_database():
    """Fixture to set up the database state before tests and clean up afterwards."""
    Base.metadata.create_all(bind=engine)  # Create tables

    # Seed data for testing
    with SessionLocal() as session:
        # Create a sample teacher
        teacher = Teacher(name="John Doe")
        session.add(teacher)
        session.commit()
        session.refresh(teacher)

        # Create a sample course and associate it with the teacher
        course = Course(title="Introduction to Testing", teacher_id=teacher.id)
        session.add(course)
        session.commit()
    
    yield  # Run tests

    # Drop all tables after tests
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="module")
def create_teacher():
    """Fixture to create a teacher and return the associated id."""
    with SessionLocal() as session:
        teacher = Teacher(name="Jane Smith")
        session.add(teacher)
        session.commit()
        session.refresh(teacher)
        return teacher.id

def test_create_course_with_teacher(setup_database, create_teacher):
    """Test creating a course and assigning it to a teacher."""
    response = client.post("/courses/", json={"title": "Advanced Testing", "teacher_id": create_teacher})
    assert response.status_code == 201
    assert response.json()["title"] == "Advanced Testing"
    assert response.json()["teacher_id"] == create_teacher

def test_get_courses_with_teacher(setup_database):
    """Test retrieving courses along with their associated teacher details."""
    response = client.get("/courses/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0  # Ensure there is at least one course returned

    # Check the structure of the returned data for courses
    for course in response.json():
        assert "id" in course
        assert "title" in course
        assert "teacher_id" in course
        assert "teacher" in course  # Ensure teacher details are included
        assert isinstance(course["teacher"], dict)  # Teacher should be a dictionary
        assert "id" in course["teacher"]
        assert "name" in course["teacher"]
```