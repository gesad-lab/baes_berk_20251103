```python
import pytest
from app import app, db, Student

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the database schema for testing
        yield client
        with app.app_context():
            db.drop_all()  # Clean up after the tests

def test_retrieve_students(client):
    # Setup: Create sample students in the database
    student1 = Student(name="John Doe")
    student2 = Student(name="Jane Smith")
    db.session.add(student1)
    db.session.add(student2)
    db.session.commit()

    # Act: Send a GET request to retrieve students
    response = client.get('/students')

    # Assert: Verify the response format and contents
    assert response.status_code == 200
    students_data = response.get_json()
    assert isinstance(students_data, list)
    assert len(students_data) == 2
    assert any(student['name'] == "John Doe" for student in students_data)
    assert any(student['name'] == "Jane Smith" for student in students_data)
```