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

        # Teardown the database after the tests are complete
        db.drop_all()


def test_add_student_with_email(test_client):
    """Test adding a student with valid name and email"""
    response = test_client.post('/students', json={
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    })
    assert response.status_code == 201  # Check that the response is created
    assert 'id' in response.json  # Check that a student ID is returned
    assert response.json['name'] == 'John Doe'  # Validate the name
    assert response.json['email'] == 'john.doe@example.com'  # Validate the email


def test_add_student_without_email(test_client):
    """Test adding a student without email should return a 400 error"""
    response = test_client.post('/students', json={
        'name': 'Jane Doe'
        # Missing email
    })
    assert response.status_code == 400  # Check for bad request
    assert response.json['error']['code'] == 'E001'  # Check for specific error code
    assert 'email' in response.json['error']['details']  # Validate that details mention email


def test_get_all_students(test_client):
    """Test retrieving all students including their emails"""
    response = test_client.get('/students')
    assert response.status_code == 200  # Check for successful retrieval
    assert isinstance(response.json, list)  # Verify the response is a list
    for student in response.json:
        assert 'name' in student  # Validate presence of name
        assert 'email' in student  # Validate presence of email
```