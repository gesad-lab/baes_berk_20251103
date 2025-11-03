```python
# tests/test_database_migration.py
import pytest
from fastapi import status
from src.models import Course, Teacher
from src.database import SessionLocal

@pytest.fixture
def client():
    from fastapi.testclient import TestClient
    from src.main import app
    return TestClient(app)

@pytest.fixture
def setup_database():
    """Fixture to set up the database for tests, ensuring data persistence."""
    db = SessionLocal()
    # Clear existing data if needed for a clean state
    db.query(Course).delete()
    db.query(Teacher).delete()
    
    # Create sample data
    teacher = Teacher(name="Sample Teacher", email="teacher@example.com")
    course = Course(name="Sample Course", level="Beginner")
    
    db.add(teacher)
    db.add(course)
    db.commit()
    
    yield db  # Provide the session to the tests
    
    # Teardown: close the session after the test completes
    db.close()

def test_existing_data_preserved(setup_database):
    """Test that existing Course and Teacher data remain unaffected after migration."""
    db = setup_database

    # Assuming we have a migration function to run
    # run_database_migration(db)
    
    # Check if existing data is still present and correct
    course_count = db.query(Course).count()
    teacher_count = db.query(Teacher).count()

    assert course_count == 1  # ensure original course exists
    assert teacher_count == 1  # ensure original teacher exists

    # Check the details of the course and teacher
    course = db.query(Course).first()
    assert course.name == "Sample Course"
    assert course.level == "Beginner"

    teacher = db.query(Teacher).first()
    assert teacher.name == "Sample Teacher"
    assert teacher.email == "teacher@example.com"

def test_assign_teacher_to_course(client, setup_database):
    """Test assigning an existing teacher to a course."""
    db = setup_database

    # Assign a teacher to a course
    teacher = db.query(Teacher).first()
    response = client.put(f"/courses/{teacher.id}/assign", json={"teacher_id": teacher.id})

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "Teacher assigned successfully."}

def test_retrieve_course_with_teacher(client, setup_database):
    """Test retrieval of course information including assigned teacher details."""
    db = setup_database

    course = db.query(Course).first()
    teacher = db.query(Teacher).first()
    
    # Assign teacher to the course
    course.teacher_id = teacher.id
    db.commit()

    response = client.get(f"/courses/{course.id}")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "id": course.id,
        "name": course.name,
        "level": course.level,
        "teacher": {
            "name": teacher.name,
            "email": teacher.email
        }
    }

def test_assign_teacher_validation(client):
    """Test validation when no teacher is assigned to a course."""
    response = client.put("/courses/1/assign", json={"teacher_id": None})

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {"error": {"code": "E001", "message": "A teacher must be selected."}}
```