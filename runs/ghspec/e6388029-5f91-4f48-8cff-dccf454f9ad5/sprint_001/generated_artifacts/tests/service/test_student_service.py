```python
import pytest
from sqlalchemy.orm import Session
from src.models import Student
from src.services.student_service import create_student, get_student, update_student, delete_student
from src.database import get_db

@pytest.fixture
def test_db():
    # Set up a test database connection and session
    db = get_db()
    yield db
    db.rollback()  # Ensure rollback after tests to maintain isolation
    db.close()

def test_create_student(test_db: Session):
    # Test data for creating a student
    student_data = {
        'name': 'John Doe',
        'age': 21,
        'email': 'johndoe@example.com'
    }
    
    student = create_student(test_db, student_data)
    
    assert student.id is not None  # Ensure the student has been created with an id
    assert student.name == student_data['name']
    assert student.age == student_data['age']
    assert student.email == student_data['email']

def test_get_student(test_db: Session):
    # First create a student to retrieve
    student_data = {
        'name': 'Jane Doe',
        'age': 22,
        'email': 'janedoe@example.com'
    }
    created_student = create_student(test_db, student_data)
    
    # Now fetching the created student
    fetched_student = get_student(test_db, created_student.id)
    
    assert fetched_student is not None  # Ensure student is fetched successfully
    assert fetched_student.id == created_student.id

def test_update_student(test_db: Session):
    # Create a student for testing
    student_data = {
        'name': 'Alice Smith',
        'age': 23,
        'email': 'alicesmith@example.com'
    }
    student = create_student(test_db, student_data)
    
    # Prepare updated data
    update_data = {
        'name': 'Alice Johnson',
        'age': 24,
        'email': 'alicejohnson@example.com'
    }
    
    updated_student = update_student(test_db, student.id, update_data)
    
    assert updated_student.name == update_data['name']
    assert updated_student.age == update_data['age']
    assert updated_student.email == update_data['email']

def test_delete_student(test_db: Session):
    # Create a student to delete
    student_data = {
        'name': 'Bob Blue',
        'age': 20,
        'email': 'bobblue@example.com'
    }
    student = create_student(test_db, student_data)
    
    # Now delete the student
    delete_student(test_db, student.id)
    
    # Try fetching the deleted student
    fetched_student = get_student(test_db, student.id)
    
    assert fetched_student is None  # Student should be deleted and not found
```