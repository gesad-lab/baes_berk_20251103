```python
# /student_management/tests/test_student.py

import pytest
from src.models import Student  # Assuming your Student model is in models.py
from src.repositories import StudentRepository  # Assuming you have a repository for handling DB operations

@pytest.fixture
def student_repository():
    """Fixture for creating an instance of the StudentRepository."""
    return StudentRepository()

def test_create_student(student_repository):
    """Test creating a new student."""
    student_data = {"name": "John Doe"}
    student = student_repository.create(student_data)
    
    assert student.id is not None  # Checking if the ID was created
    assert student.name == "John Doe"  # Check if name is correct

def test_retrieve_all_students(student_repository):
    """Test retrieving all students."""
    student_repository.create({"name": "Jane Doe"})  # Preparing data

    students = student_repository.get_all()
    
    assert len(students) > 0  # Ensure students list is not empty

def test_update_student(student_repository):
    """Test updating an existing student."""
    student = student_repository.create({"name": "Update Name"})
    updated_data = {"name": "Updated Name"}
    
    updated_student = student_repository.update(student.id, updated_data)
    
    assert updated_student.name == "Updated Name"  # Check if the name was updated

def test_delete_student(student_repository):
    """Test deleting a student."""
    student = student_repository.create({"name": "Delete Me"})
    
    result = student_repository.delete(student.id)
    
    assert result is True  # Expect a successful deletion
    assert student_repository.get(student.id) is None  # Ensure student has been deleted
```