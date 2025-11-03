```python
import pytest
from app import create_app, db
from models.student import Student

@pytest.fixture(scope='module')
def test_client():
    app = create_app('testing')  # Initialize app with testing configuration
    testing_client = app.test_client()

    # Establish an application context
    with app.app_context():
        # Create the database and the database table(s)
        db.create_all()

        yield testing_client  # This is where the testing happens!

        # Teardown the database after tests
        db.session.remove()
        db.drop_all()

def test_add_student_with_email(test_client):
    """Test adding a student with a valid email."""
    response = test_client.post('/students', json={
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    })
    
    # Check if the response is 201 Created
    assert response.status_code == 201
    json_data = response.get_json()

    # Validate the response data
    assert json_data['name'] == 'John Doe'
    assert json_data['email'] == 'john.doe@example.com'

def test_add_student_without_email(test_client):
    """Test adding a student without an email."""
    response = test_client.post('/students', json={
        'name': 'Jane Doe'
    })
    
    # Check if the response is 400 Bad Request
    assert response.status_code == 400
    json_data = response.get_json()

    # Validate the error message
    assert json_data['error']['message'] == 'Email field is required'

def test_retrieve_all_students_with_email(test_client):
    """Test retrieving all students including their email addresses."""
    # Ensure there is at least one student to retrieve
    test_client.post('/students', json={
        'name': 'Alice Smith',
        'email': 'alice.smith@example.com'
    })

    response = test_client.get('/students')
    assert response.status_code == 200
    json_data = response.get_json()

    # Check the response contains the student we added
    assert len(json_data) > 0
    assert any(student['email'] == 'alice.smith@example.com' for student in json_data)
```