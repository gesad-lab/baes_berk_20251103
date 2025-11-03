```python
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app, Base, get_db
from sqlalchemy.exc import IntegrityError
from src.models.student import Student
from src.models.course import Course

# Setup for testing
DATABASE_URL = "postgresql://user:password@localhost/test_db"

# Create a new database engine for testing
engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the tables in the test database
Base.metadata.create_all(bind=engine)

# Create a TestClient instance
client = TestClient(app)

# Dependency override for testing
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

# Apply the dependency override
app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(scope="module")
def setup_data():
    # Insert test data before running tests
    db = TestingSessionLocal()
    
    # Create a student
    student = Student(name="Test Student")
    db.add(student)
    db.commit()
    db.refresh(student)

    # Create a course
    course = Course(name="Test Course")
    db.add(course)
    db.commit()
    db.refresh(course)

    yield student, course

    # Cleanup after tests
    db.query(Student).delete()
    db.query(Course).delete()
    db.commit()

def test_assign_courses_success(setup_data):
    student, course = setup_data
    course_ids = [course.id]

    response = client.post(f"/students/{student.id}/courses", json={"courseIds": course_ids})

    assert response.status_code == 200
    assert response.json() == {"assignedCourses": course_ids}

def test_assign_courses_student_not_found():
    course_ids = [1]  # Assuming course with id 1 exists
    response = client.post("/students/999/courses", json={"courseIds": course_ids})  # 999 is a non-existing student ID

    assert response.status_code == 404
    assert response.json() == {"detail": "Student not found"}

def test_assign_courses_invalid_course():
    student = setup_data[0]  # Use existing student ID
    response = client.post(f"/students/{student.id}/courses", json={"courseIds": [999]})  # Non-existing course ID

    assert response.status_code == 400  # Assuming invalid course returns a 400
    assert "detail" in response.json()  # Further validation can be added based on error handling implementation
```