import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from fastapi.testclient import TestClient
from models import Base, Course, Teacher  # Import Course and Teacher models
from your_app import app  # Import the FastAPI application

@pytest.fixture(scope='function')
def test_database():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)  # Create all tables for tests

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    yield SessionLocal  # Provide session to the tests
    Base.metadata.drop_all(engine)  # Cleanup after tests

@pytest.fixture(scope='function')
def client(test_database):
    """Create a test client using the FastAPI application."""
    with TestClient(app) as client:
        yield client

def test_assign_teacher_to_course(client, test_database):
    """Test assigning a teacher to a course."""
    with test_database() as db:
        # Create a sample teacher
        teacher = Teacher(name="John Doe")
        db.add(teacher)
        db.commit()
        db.refresh(teacher)

        # Create a sample course
        course = Course(title="Math 101", description="Basic Math")
        db.add(course)
        db.commit()
        db.refresh(course)

        # Assign the teacher to the course
        response = client.post(f"/courses/{course.id}/assign-teacher", json={"teacher_id": teacher.id})
        assert response.status_code == 200
        assert response.json() == {"message": "Teacher assigned successfully"}, "Response message mismatch"

        # Verify that the teacher was assigned correctly
        updated_course = db.query(Course).filter(Course.id == course.id).first()
        assert updated_course.teacher_id == teacher.id, "Teacher ID not updated in the course"

def test_get_course_with_teacher(client, test_database):
    """Test retrieving a course with its assigned teacher."""
    with test_database() as db:
        # Create a sample teacher
        teacher = Teacher(name="Jane Smith")
        db.add(teacher)
        db.commit()
        db.refresh(teacher)

        # Create a sample course and assign the teacher
        course = Course(title="Science 101", description="Basic Science", teacher_id=teacher.id)
        db.add(course)
        db.commit()
        db.refresh(course)

        # Get the course details
        response = client.get(f"/courses/{course.id}")
        assert response.status_code == 200
        assert response.json() == {
            "id": course.id,
            "title": course.title,
            "description": course.description,
            "teacher_id": teacher.id
        }, "Course details do not match expected values" 

# Add additional tests as necessary for edge cases and error handling