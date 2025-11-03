```python
import pytest
from fastapi.testclient import TestClient
from myapp.main import app  # Importing the FastAPI app
from myapp.models import Course, Teacher  # Assuming Course and Teacher models are defined
from sqlalchemy.orm import clear_mappers

# Create a TestClient for making requests to the FastAPI app
client = TestClient(app)

@pytest.fixture(scope="module", autouse=True)
def setup_database():
    """Fixture to set up the database schema before running tests."""
    # Here you would typically create your database schema and any necessary initial data
    # This might involve creating the tables and some sample data as necessary
    pass

def test_assign_teacher_to_course():
    """Test assigning a teacher to a course."""
    # Create a test course and teacher in the database
    teacher = Teacher(name="John Doe", email="john@example.com")
    course = Course(title="Math 101", description="Basic Mathematics")
    
    # Assume that we're using a session to add these objects to the database
    session.add(teacher)
    session.add(course)
    session.commit()
    
    response = client.put(f"/courses/{course.id}/assign_teacher", json={"teacher_id": teacher.id})
    
    assert response.status_code == 200
    assert response.json() == {"message": "Teacher assigned successfully"}
    
    updated_course = session.query(Course).filter_by(id=course.id).first()
    assert updated_course.teacher_id == teacher.id

def test_assign_teacher_to_nonexistent_course():
    """Test assigning a teacher to a course that does not exist."""
    response = client.put("/courses/9999/assign_teacher", json={"teacher_id": 1})
    
    assert response.status_code == 400
    assert response.json() == {"detail": "Course does not exist"}

def test_assign_teacher_to_nonexistent_teacher():
    """Test assigning a nonexistent teacher to a course."""
    course = Course(title="Science 101", description="Basic Science")
    
    # Add course to the database
    session.add(course)
    session.commit()
    
    response = client.put(f"/courses/{course.id}/assign_teacher", json={"teacher_id": 9999})
    
    assert response.status_code == 400
    assert response.json() == {"detail": "Teacher does not exist"}

def test_get_course_details_with_teacher():
    """Test getting course details including assigned teacher."""
    teacher = Teacher(name="Jane Smith", email="jane@example.com")
    course = Course(title="History 101", description="Basic History", teacher_id=teacher.id)
    
    # Add teacher and course to the database
    session.add(teacher)
    session.add(course)
    session.commit()
    
    response = client.get(f"/courses/{course.id}")
    
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == course.title
    assert data["teacher"]["name"] == teacher.name
    assert data["teacher"]["email"] == teacher.email

def test_get_nonexistent_course():
    """Test getting a course that does not exist."""
    response = client.get("/courses/9999")
    
    assert response.status_code == 404
    assert response.json() == {"detail": "Course not found"}

# Clear mappers after tests to avoid conflicts
@pytest.fixture(scope="function", autouse=True)
def teardown():
    clear_mappers()
```