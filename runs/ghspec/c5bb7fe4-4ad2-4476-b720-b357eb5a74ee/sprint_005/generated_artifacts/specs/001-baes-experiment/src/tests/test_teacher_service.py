```python
import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.models.teacher import Teacher  # Assuming the Teacher model is defined here
from src.services.teacher_service import create_teacher, get_teacher, update_teacher  # Import service methods
from sqlalchemy.exc import IntegrityError

# Initialize Flask app and db for testing
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # In-memory database for tests
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up in-memory database for testing
@pytest.fixture(scope='module')
def test_db():
    with app.app_context():
        db.create_all()  # Create tables
        yield db  # Provide the fixture value
        db.drop_all()  # Clean up after tests

@pytest.fixture
def teacher_data():
    return {
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    }

def test_create_teacher(test_db, teacher_data):
    # Test creating a teacher
    teacher = create_teacher(teacher_data['name'], teacher_data['email'])
    assert teacher.id is not None
    assert teacher.name == teacher_data['name']
    assert teacher.email == teacher_data['email']

def test_get_teacher(test_db, teacher_data):
    # Create a teacher for retrieval
    teacher = create_teacher(teacher_data['name'], teacher_data['email'])
    
    # Test retrieving the teacher
    retrieved_teacher = get_teacher(teacher.id)
    assert retrieved_teacher.id == teacher.id
    assert retrieved_teacher.name == teacher_data['name']
    assert retrieved_teacher.email == teacher_data['email']

def test_update_teacher(test_db, teacher_data):
    # Create a teacher to update
    teacher = create_teacher(teacher_data['name'], teacher_data['email'])
    
    # Update the teacher's information
    updated_data = {'name': 'Jane Doe', 'email': 'jane.doe@example.com'}
    updated_teacher = update_teacher(teacher.id, updated_data['name'], updated_data['email'])
    
    # Fetch the updated teacher
    retrieved_teacher = get_teacher(teacher.id)
    assert retrieved_teacher.name == updated_data['name']
    assert retrieved_teacher.email == updated_data['email']

def test_create_teacher_missing_fields(test_db):
    # Test creating a teacher with missing name
    with pytest.raises(IntegrityError):
        create_teacher('', 'missing.name@example.com')

    # Test creating a teacher with missing email
    with pytest.raises(IntegrityError):
        create_teacher('Missing Email', '')
```