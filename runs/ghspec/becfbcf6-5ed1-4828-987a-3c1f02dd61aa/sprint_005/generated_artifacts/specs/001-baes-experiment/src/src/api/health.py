```python
import pytest
from app import app, db, Teacher

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the database schema for testing

            # Creating sample teachers for tests
            teacher1 = Teacher(name="John Doe", email="johndoe@example.com")
            db.session.add(teacher1)
            db.session.commit()

        yield client

def test_create_teacher_success(client):
    """Test successful creation of a Teacher."""
    response = client.post('/teachers', json={'name': 'Jane Smith', 'email': 'janesmith@example.com'})
    
    assert response.status_code == 201  # Confirm that it's a successful creation
    data = response.get_json()
    
    assert 'id' in data  # Ensure that an ID is returned
    assert data['name'] == 'Jane Smith'
    assert data['email'] == 'janesmith@example.com'

def test_create_teacher_missing_fields(client):
    """Test error response when required fields are missing."""
    response = client.post('/teachers', json={'name': ''})  # Missing email

    assert response.status_code == 400  # Should return a Bad Request
    error_data = response.get_json()
    
    assert error_data['error']['code'] == 'E001'
    assert error_data['error']['message'] == 'Missing required fields: name, email.'

def test_create_teacher_duplicate_email(client):
    """Test error response for duplicate email."""
    client.post('/teachers', json={'name': 'John Doe', 'email': 'johndoe@example.com'})  # Create first teacher

    response = client.post('/teachers', json={'name': 'Another John', 'email': 'johndoe@example.com'})  # Duplicate email

    assert response.status_code == 400  # Should return a Bad Request for duplicate email
    error_data = response.get_json()
    
    assert error_data['error']['code'] == 'E002'  # Assuming E002 is the code for duplicate email errors
    assert error_data['error']['message'] == 'Email already exists.'

def test_retrieve_teacher_success(client):
    """Test retrieval of a Teacher by ID."""
    response = client.post('/teachers', json={'name': 'Alice Wonderland', 'email': 'alice@example.com'})
    
    teacher_id = response.get_json()['id']
    retrieval_response = client.get(f'/teachers/{teacher_id}')

    assert retrieval_response.status_code == 200  # Confirm successful retrieval
    data = retrieval_response.get_json()
    
    assert data['id'] == teacher_id
    assert data['name'] == 'Alice Wonderland'
    assert data['email'] == 'alice@example.com'
```