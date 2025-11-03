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

def test_get_teacher(client):
    """Test retrieving a teacher by ID"""
    # Assume the first teacher added has an ID of 1
    response = client.get('/teachers/1')
    assert response.status_code == 200

    response_data = response.get_json()
    assert response_data['name'] == "John Doe"
    assert response_data['email'] == "johndoe@example.com"

def test_get_teacher_not_found(client):
    """Test retrieving a teacher that does not exist"""
    response = client.get('/teachers/99')  # Assuming no teacher with ID 99
    assert response.status_code == 404
    response_data = response.get_json()
    assert response_data['error']['code'] == "E404"
    assert response_data['error']['message'] == "Teacher not found"
```