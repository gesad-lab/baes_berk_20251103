```python
import pytest
from sqlalchemy.orm import Session
from src.models import Course  # Import the Course model
from src.services.course_service import delete_course  # New import for course deletion
from src.database import get_db

@pytest.fixture
def test_db():
    # Set up a test database connection and session
    db = get_db()
    yield db
    db.rollback()  # Ensure rollback after tests to maintain isolation
    db.close()

def test_delete_course(test_db: Session):
    # First, create a course to ensure there is a course to delete
    course_to_delete = {"name": "Math 101", "level": "Intermediate"}
    created_course = create_course(test_db, course_to_delete)

    # Check that the course was created successfully
    assert created_course.name == course_to_delete["name"]
    assert created_course.level == course_to_delete["level"]

    # Now, test the delete functionality
    delete_course(test_db, created_course.id)  # Call the delete function with the course ID

    # Attempt to retrieve the course to verify it has been deleted
    deleted_course = test_db.query(Course).filter(Course.id == created_course.id).first()
    
    # Assert that the deleted course no longer exists in the database
    assert deleted_course is None
```