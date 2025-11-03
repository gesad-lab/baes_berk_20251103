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

def test_create_student_success(test_client):
    """Test creating a student with a valid name."""
    response = test_client.post('/students', json={'name': 'John Doe'})
    assert response.status_code == 201  # Expect a 201 Created response
    json_data = response.get_json()
    assert 'id' in json_data  # Check if the response contains the student ID
    assert json_data['name'] == 'John Doe'  # Check if the name matches

def test_create_student_missing_name(test_client):
    """Test creating a student without a name."""
    response = test_client.post('/students', json={'name': ''})
    assert response.status_code == 400  # Expect a 400 Bad Request response
    json_data = response.get_json()
    assert json_data['error']['code'] == 'E001'  # Check for specific error code
    assert json_data['error']['message'] == 'Name is required'  # Check for error message

def test_retrieve_students(test_client):
    """Test retrieving all students."""
    test_client.post('/students', json={'name': 'Alice'})
    test_client.post('/students', json={'name': 'Bob'})
    response = test_client.get('/students')
    assert response.status_code == 200  # Expect a 200 OK response
    json_data = response.get_json()
    assert len(json_data) == 2  # Check if there are two students in the response
    assert 'Alice' in [student['name'] for student in json_data]  # Verify students' names are returned
    assert 'Bob' in [student['name'] for student in json_data]  # Verify students' names are returned