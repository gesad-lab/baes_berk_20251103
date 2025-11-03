```python
import json
import pytest
from your_application import app, db, Teacher, Course  # Adjust import based on your structure

# Reinitialize the Flask application and SQLAlchemy for testing
@pytest.fixture(scope='module')
def test_client():
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the database and tables for testing
            yield client  # Provide the test client to the tests
            db.drop_all()  # Clean up the database after tests


def test_create_teacher_valid(test_client):
    """Test creating a teacher with valid details."""
    response = test_client.post('/teachers', 
                                 data=json.dumps({"name": "John Doe", "email": "john.doe@example.com"}),
                                 content_type='application/json')
    assert response.status_code == 201  # Check for successful creation
    assert b'Teacher created successfully.' in response.data  # Validate success message

    # Verify the teacher is in the database
    teacher = Teacher.query.filter_by(email="john.doe@example.com").first()
    assert teacher is not None
    assert teacher.name == "John Doe"


def test_create_teacher_missing_fields(test_client):
    """Test creating a teacher without required fields."""
    response = test_client.post('/teachers', 
                                 data=json.dumps({"name": "", "email": ""}),
                                 content_type='application/json')
    assert response.status_code == 400  # Check for validation error
    assert b'Error: Name and email are required.' in response.data  # Validate error message


def test_get_teacher_by_id(test_client):
    """Test retrieving teacher information by ID."""
    # First create a teacher to retrieve
    create_response = test_client.post('/teachers', 
                                        data=json.dumps({"name": "Jane Doe", "email": "jane.doe@example.com"}),
                                        content_type='application/json')
    teacher = Teacher.query.filter_by(email="jane.doe@example.com").first()

    # Now retrieve the teacher's information
    response = test_client.get(f'/teachers/{teacher.id}')
    assert response.status_code == 200  # Check for successful retrieval
    data = json.loads(response.data)
    assert data['id'] == teacher.id
    assert data['name'] == teacher.name
    assert data['email'] == teacher.email


def test_create_teacher_with_existing_email(test_client):
    """Test creating a teacher with an existing email."""
    # Create the first teacher
    test_client.post('/teachers',
                     data=json.dumps({"name": "Alice", "email": "alice@example.com"}),
                     content_type='application/json')

    # Attempt to create a second teacher with the same email
    response = test_client.post('/teachers', 
                                 data=json.dumps({"name": "Alice Duplicate", "email": "alice@example.com"}),
                                 content_type='application/json')
    assert response.status_code == 400  # Check for duplicate entry error
    assert b'Error: Email already exists.' in response.data  # Validate error message


def test_migration_data_integrity(test_client):
    """Test to ensure data integrity post-migration."""
    # Check existing Course records before migration
    existing_courses = Course.query.all()
    existing_course_count = len(existing_courses)

    # Run the migration to ensure the Teachers table is created
    db.engine.execute("CREATE TABLE IF NOT EXISTS teachers (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT NOT NULL UNIQUE);")

    # Ensure Courses data still exists
    assert len(Course.query.all()) == existing_course_count  # Validate that course count remains the same
```