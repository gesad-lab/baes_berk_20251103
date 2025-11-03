from teacher_management.models import Teacher
import pytest

@pytest.fixture
def teacher_data():
    return {
        'name': 'John Doe',
        'email': 'john@example.com'
    }

@pytest.fixture
def create_teacher(client, teacher_data):
    """Fixture to create a teacher for testing purposes."""
    response = client.post('/teachers', json=teacher_data)
    assert response.status_code == 201  # Ensure teacher is created
    return response.json  # Return created teacher data

def test_create_teacher(client, teacher_data):
    """Test creating a new teacher."""
    response = client.post('/teachers', json=teacher_data)
    assert response.status_code == 201
    assert response.json['name'] == teacher_data['name']
    assert response.json['email'] == teacher_data['email']

def test_create_teacher_with_existing_email(client, create_teacher):
    """Test attempting to create a teacher with an existing email."""
    response = client.post('/teachers', json={
        'name': 'Jane Doe',
        'email': create_teacher['email']  # Use the existing email
    })
    assert response.status_code == 400  # Expecting a bad request
    assert response.json['error']['code'] == 'E002'  # Assume unique email error code

def test_get_teacher(client, create_teacher):
    """Test retrieving a teacher's information."""
    teacher_id = create_teacher['id']
    response = client.get(f'/teachers/{teacher_id}')
    assert response.status_code == 200
    assert response.json['name'] == create_teacher['name']
    assert response.json['email'] == create_teacher['email']

def test_update_teacher(client, create_teacher):
    """Test updating a teacher's information."""
    teacher_id = create_teacher['id']
    updated_data = {
        'name': 'John Smith',
        'email': 'johnsmith@example.com'
    }

    response = client.put(f'/teachers/{teacher_id}', json=updated_data)
    assert response.status_code == 200
    assert response.json['name'] == updated_data['name']
    assert response.json['email'] == updated_data['email']

def test_retrieve_updated_teacher(client, create_teacher):
    """Test that updated teacher information is retrieved correctly."""
    teacher_id = create_teacher['id']
    updated_data = {
        'name': 'John Smith',
        'email': 'johnsmith@example.com'
    }
    # Update teacher first
    client.put(f'/teachers/{teacher_id}', json=updated_data)

    # Now retrieve and check
    response = client.get(f'/teachers/{teacher_id}')
    assert response.status_code == 200
    assert response.json['name'] == updated_data['name']
    assert response.json['email'] == updated_data['email']