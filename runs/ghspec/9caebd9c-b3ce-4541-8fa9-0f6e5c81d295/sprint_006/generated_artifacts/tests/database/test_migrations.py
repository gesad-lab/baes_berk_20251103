```python
import json
import pytest
from your_application import app, db, Teacher, Course  # Ensure imports fit your structure
from sqlalchemy.exc import IntegrityError

# Reinitialize the Flask application and SQLAlchemy for testing
@pytest.fixture(scope='module')
def test_client():
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the database and tables for testing
            yield client
            db.drop_all()  # Clean up the database after tests


def test_migration_preserves_data(test_client):
    """Test that data remains intact after migration."""
    # Create initial data
    teacher = Teacher(name="John Doe")
    course = Course(name="Physics 101")
    
    db.session.add(teacher)
    db.session.add(course)
    db.session.commit()

    # Check data before migration
    assert Teacher.query.count() == 1
    assert Course.query.count() == 1

    # Apply migration (assuming a function `apply_migration` exists)
    apply_migration()  # This function should run the migration script

    # Check data after migration
    assert Teacher.query.count() == 1
    assert Course.query.count() == 1

    # Verify that the course can still be accessed
    assert Course.query.first().name == "Physics 101"
    assert Teacher.query.first().name == "John Doe"


def test_assign_teacher_to_course_success(test_client):
    """Test assigning a teacher to a course successfully."""
    teacher = Teacher(name="Jane Smith")
    course = Course(name="Math 101")
    
    db.session.add(teacher)
    db.session.add(course)
    db.session.commit()

    # Assign the teacher to the course
    response = test_client.put(
        f"/courses/{course.id}/assign-teacher",
        data=json.dumps({"teacher_id": teacher.id}),
        content_type='application/json'
    )
    
    # Check the response and that the relationship is established
    assert response.status_code == 200
    assert json.loads(response.data)["message"] == "Teacher assigned successfully."
    assert course.teacher_id == teacher.id  # Check relationship


def test_assign_teacher_to_course_invalid_teacher(test_client):
    """Test assigning a teacher with an invalid ID returns an error."""
    course = Course(name="History 101")
    db.session.add(course)
    db.session.commit()

    # Attempt to assign an invalid teacher ID
    response = test_client.put(
        f"/courses/{course.id}/assign-teacher",
        data=json.dumps({"teacher_id": 9999}),  # Invalid ID
        content_type='application/json'
    )

    # Check response for invalid ID
    assert response.status_code == 400
    assert json.loads(response.data)["error"]["code"] == "E001"
    assert "Invalid teacher ID" in json.loads(response.data)["error"]["message"]


def test_assign_teacher_to_course_missing_teacher_id(test_client):
    """Test that an error is returned if teacher_id is missing."""
    course = Course(name="Chemistry 101")
    db.session.add(course)
    db.session.commit()

    # Attempt to assign a teacher without providing teacher_id
    response = test_client.put(
        f"/courses/{course.id}/assign-teacher",
        data=json.dumps({}),  # Missing teacher ID
        content_type='application/json'
    )

    # Check response for missing ID
    assert response.status_code == 400
    assert json.loads(response.data)["error"]["code"] == "E002"
    assert "Teacher ID is required" in json.loads(response.data)["error"]["message"]
```