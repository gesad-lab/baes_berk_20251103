```python
import pytest
from app import create_app, db
from app.models import Teacher  # Ensure Teacher model is imported
from http import HTTPStatus

@pytest.fixture
def client():
    app = create_app({'TESTING': True})
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create schema for testing
            yield client
            db.drop_all()  # Clean up after testing

def test_create_teacher(client):
    """Test creating a new teacher with valid name and email."""
    response = client.post('/teachers', json={'name': 'Jane Doe', 'email': 'janedoe@example.com'})
    assert response.status_code == HTTPStatus.CREATED
    assert 'id' in response.json  # Ensure that the created teacher has an ID

def test_create_teacher_without_name(client):
    """Test creating a teacher without providing a name."""
    response = client.post('/teachers', json={'email': 'janedoe@example.com'})
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json['error']['code'] == 'E001'  # Check for the correct error code

def test_get_teachers(client):
    """Test retrieving all teachers; should return a list of teachers."""
    client.post('/teachers', json={'name': 'John Doe', 'email': 'johndoe@example.com'})  # Create a teacher for retrieval
    response = client.get('/teachers')
    assert response.status_code == HTTPStatus.OK
    assert len(response.json['teachers']) > 0  # Ensure the list is not empty
```