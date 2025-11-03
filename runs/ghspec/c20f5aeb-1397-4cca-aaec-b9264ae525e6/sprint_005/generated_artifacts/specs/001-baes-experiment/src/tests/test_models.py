```python
import pytest
from src.models import Teacher  # Import the Teacher model
from src.database import get_db, init_db
from src.app import create_app

@pytest.fixture
def app():
    """Create a new Flask application instance for testing."""
    app = create_app({"TESTING": True})
    with app.app_context():
        init_db()  # Initialize the database with the schema
    yield app

@pytest.fixture
def client(app):
    """Create a test client for the Flask application."""
    with app.test_client() as client:
        yield client

def test_teacher_model():
    """Test that creating a Teacher instance works as expected."""
    teacher = Teacher(name="John Doe", email="john.doe@example.com")
    assert teacher.name == "John Doe"
    assert teacher.email == "john.doe@example.com"

def test_create_teacher_success(client):
    """Test that creating a teacher with valid data succeeds."""
    response = client.post('/teachers', json={"name": "Jane Doe", "email": "jane.doe@example.com"})
    assert response.status_code == 200
    assert response.get_json()['name'] == "Jane Doe"
    assert 'id' in response.get_json()  # Assuming ID is returned

def test_create_teacher_missing_name(client):
    """Test creating a teacher without a name returns error."""
    response = client.post('/teachers', json={"email": "jane.doe@example.com"})
    assert response.status_code == 400
    assert 'missing' in response.get_json()['error']['message']

def test_get_teacher_details(client):
    """Test fetching details of a specific teacher."""
    client.post('/teachers', json={"name": "Jane Doe", "email": "jane.doe@example.com"})
    response = client.get('/teachers/1')
    assert response.status_code == 200
    assert response.get_json()['name'] == "Jane Doe"
```