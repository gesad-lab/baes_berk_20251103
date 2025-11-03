```python
import pytest
from app import app, db, Student

@pytest.fixture
def client():
    """Create a test client for the Flask application."""
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the database schema for testing
        yield client
        with app.app_context():
            db.drop_all()  # Clean up after the tests

def test_retrieve_students(client):
    """Test the retrieval of student records from the /students endpoint."""
    
    # Setup: Create sample students in the database
    student1 = Student(name='Alice', email='alice@example.com')
    student2 = Student(name='Bob', email='bob@example.com')
    db.session.add(student1)
    db.session.add(student2)
    db.session.commit()
    
    # Act: Send a GET request to fetch all students
    response = client.get('/students')
    
    # Assert: Check the response status code and data
    assert response.status_code == 200  # Expecting HTTP 200 OK
    data = response.get_json()
    
    # Verify that email fields are included in the retrieved student records
    assert isinstance(data, list)  # Ensure the response is a list
    assert len(data) == 2  # Ensure we have two students
    assert 'email' in data[0]  # Ensure email field is present in student 1
    assert 'email' in data[1]  # Ensure email field is present in student 2
    assert data[0]['email'] == student1.email  # Check email matches
    assert data[1]['email'] == student2.email  # Check email matches
```