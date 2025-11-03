```python
import pytest
from app import create_app, db
from app.models import Student

@pytest.fixture(scope='module')
def test_client():
    app = create_app('testing')  # create the app with the testing configuration
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # create the database tables
        yield client
        with app.app_context():
            db.drop_all()  # drop the database tables after tests

def test_create_student_with_email_success(test_client):
    """Test creating a Student with a name and email."""
    response = test_client.post('/students', json={'name': 'John Doe', 'email': 'john.doe@example.com'})
    assert response.status_code == 201  # check for success status code
    data = response.get_json()
    assert data['name'] == 'John Doe'
    assert data['email'] == 'john.doe@example.com'

def test_create_student_without_email_success(test_client):
    """Test creating a Student with a name but without an email."""
    response = test_client.post('/students', json={'name': 'Jane Doe'})
    assert response.status_code == 201  # check for success status code
    data = response.get_json()
    assert data['name'] == 'Jane Doe'
    assert data['email'] is None  # check for None email

def test_create_student_without_name_failure(test_client):
    """Test creating a Student without a name."""
    response = test_client.post('/students', json={'email': 'invalid@example.com'})
    assert response.status_code == 400  # check for bad request status code
    data = response.get_json()
    assert data['error']['code'] == 'E002'  # assuming E002 is the error code for missing name
    assert 'name is required' in data['error']['message']  # check for correct error message

def test_retrieve_students_with_email(test_client):
    """Test retrieving all Students."""
    response = test_client.get('/students')
    assert response.status_code == 200  # check for success status code
    data = response.get_json()
    assert isinstance(data, list)  # check if response is a list
    assert len(data) > 0  # check that there is at least one student in the response
```
