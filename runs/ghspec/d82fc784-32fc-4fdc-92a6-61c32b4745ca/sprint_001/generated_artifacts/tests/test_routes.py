```python
import pytest
from app import create_app, db
from app.models import Student

@pytest.fixture
def client():
    """A test client for the Flask application."""
    app = create_app('testing')  # Use the testing configuration
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the database tables
        yield client
        with app.app_context():
            db.drop_all()  # Clean up the database after tests

def test_create_student(client):
    """Test creating a new student."""
    response = client.post('/students', json={"name": "Test Student"})
    assert response.status_code == 201  # Verify resource was created
    data = response.get_json()
    # Check if the response contains the correct data
    assert data['name'] == "Test Student"
    assert 'id' in data  # Ensure an id is returned for the created resource

def test_get_students(client):
    """Test retrieving a list of students."""
    # Pre-populate with a student in the database
    student = Student(name="Existing Student")
    db.session.add(student)
    db.session.commit()

    response = client.get('/students')
    assert response.status_code == 200  # Verify successful retrieval
    data = response.get_json()
    assert isinstance(data, list)  # Ensure response is a list
    assert len(data) > 0  # Ensure there are items in the list

def test_update_student(client):
    """Test updating an existing student."""
    # Create a student for testing
    student = Student(name="Old Name")
    db.session.add(student)
    db.session.commit()
    
    # Perform the update
    response = client.put(f'/students/{student.id}', json={"name": "Updated Name"})
    assert response.status_code == 200  # Verify successful update
    updated_student = Student.query.get(student.id)
    assert updated_student.name == "Updated Name"  # Verify name was updated

def test_delete_student(client):
    """Test deleting an existing student."""
    # Create a student for testing
    student = Student(name="Student to Delete")
    db.session.add(student)
    db.session.commit()
    
    response = client.delete(f'/students/{student.id}')
    assert response.status_code == 204  # Verify successful deletion (No Content)

    # Check that the student is no longer in the database
    deleted_student = Student.query.get(student.id)
    assert deleted_student is None  # Verify student was deleted
```