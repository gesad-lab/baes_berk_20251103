```python
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models.student import Base, Student  # Assuming Student model is defined in models/student.py
from src.app import app  # Assuming your Flask app is defined in src/app.py

@pytest.fixture(scope='module')
def test_client():
    # Set up the test client
    app.config['TESTING'] = True
    yield app.test_client()

@pytest.fixture(scope='module')
def init_database():
    # Create a new SQLite database for testing
    engine = create_engine('sqlite:///test_students.db')  # Create a test database
    Base.metadata.create_all(engine)  # Create the schema
    yield
    Base.metadata.drop_all(engine)  # Drop the test database after tests are done

def test_database_initialization(init_database):
    """ Test case to verify the database schema creation functionality. """
    
    # Verify that the Student table exists
    engine = create_engine('sqlite:///test_students.db')
    inspector = inspect(engine)
    assert 'student' in inspector.get_table_names(), "The Student table should exist in the database."

def test_adding_student(test_client, init_database):
    """ Test case to add a new student and check if it's created successfully. """
    response = test_client.post('/students', json={'name': 'John Doe'})
    assert response.status_code == 201
    json_data = response.get_json()
    assert json_data['name'] == 'John Doe'

def test_retrieving_student(test_client, init_database):
    """ Test case to retrieve a student by ID. """
    # First, add a student
    response = test_client.post('/students', json={'name': 'Jane Doe'})
    student_id = response.get_json()['id']

    # Now, retrieve the student by ID
    response = test_client.get(f'/students/{student_id}')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['name'] == 'Jane Doe'

def test_error_handling_missing_name(test_client, init_database):
    """ Test case to handle errors when name is missing. """
    response = test_client.post('/students', json={})
    assert response.status_code == 400
    json_data = response.get_json()
    assert json_data == {"error": {"code": "E001", "message": "Name is required"}}
```