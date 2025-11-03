import pytest
from src.models import db, Student

@pytest.fixture(scope='module')
def test_client():
    from src.app import app
    # Set up test client
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create tables
        yield client
        with app.app_context():
            db.drop_all()  # Cleanup after tests

def test_create_student_success(test_client):
    """Test creating a new student with a valid name."""
    response = test_client.post('/students', json={'name': 'John Doe'})
    assert response.status_code == 201
    assert 'id' in response.json
    assert response.json['name'] == 'John Doe'

def test_create_student_without_name(test_client):
    """Test creating a new student without a name."""
    response = test_client.post('/students', json={})
    assert response.status_code == 400
    assert response.json == {
        "error": {
            "code": "E001",
            "message": "Name is required."
        }
    }

def test_get_students_empty(test_client):
    """Test retrieving students when none exist."""
    response = test_client.get('/students')
    assert response.status_code == 200
    assert response.json == []

def test_create_multiple_students(test_client):
    """Test creating multiple students and retrieving them."""
    test_client.post('/students', json={'name': 'Jane Doe'})
    test_client.post('/students', json={'name': 'Alice Smith'})
    
    response = test_client.get('/students')
    assert response.status_code == 200
    assert len(response.json) == 2
    assert any(student['name'] == 'Jane Doe' for student in response.json)
    assert any(student['name'] == 'Alice Smith' for student in response.json)

def test_student_table_schema(test_client):
    """Test if the student table schema exists as expected."""
    result = db.session.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='students';").fetchone()
    assert result is not None and result[0] == 'students'
    
    # Verify the columns in the students table
    result = db.session.execute("PRAGMA table_info(students);").fetchall()
    columns = {column[1] for column in result}
    assert 'id' in columns
    assert 'name' in columns
