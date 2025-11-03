```python
import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.models.student import Student
from src.models.course import Course
from src.models.student_course import StudentCourse
from src.database.database import get_db, Base, engine

# Create the FastAPI test client
client = TestClient(app)

# Setup the test database
@pytest.fixture(scope="module", autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)  # Create the database tables
    yield
    Base.metadata.drop_all(bind=engine)  # Drop the tables after tests


def test_associate_student_with_course():
    """
    Test associating a student with a course.
    This ensures that a student can be successfully linked to a course
    via the StudentCourse relationship.
    """
    # Create a student
    student_data = {"name": "John Doe"}
    response = client.post("/students/", json=student_data)
    assert response.status_code == 201
    student_id = response.json()["id"]
    
    # Create a course
    course_data = {"title": "Biology 101"}
    response = client.post("/courses/", json=course_data)
    assert response.status_code == 201
    course_id = response.json()["id"]
    
    # Associate student with course
    association_data = {"student_id": student_id, "course_id": course_id}
    response = client.post("/students/courses/", json=association_data)
    assert response.status_code == 201
    assert response.json() == {"message": "Student associated with course successfully."}


def test_get_student_courses():
    """
    Test retrieving courses associated with a specific student.
    This ensures that the student-course association retrieves the correct courses.
    """
    # Use the existing student ID from the previous test
    response = client.get("/students/1/courses/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Expect a list of courses
    assert len(response.json()) > 0  # At least one course should be associated


def test_invalid_student_course_association():
    """
    Test handling of invalid student-course association requests.
    Ensure that appropriate error messages are returned for invalid data.
    """
    invalid_data = {"student_id": 999, "course_id": 999}  # Non-existent IDs
    response = client.post("/students/courses/", json=invalid_data)
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E404", "message": "Student or Course not found."}}
```