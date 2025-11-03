```python
import pytest
from src.models.student import Student, StudentError

@pytest.fixture
def student():
    """Fixture to create a sample student instance for testing."""
    return Student(name="John Doe")

def test_student_creation(student):
    """Test that a student can be created with a valid name."""
    assert student.name == "John Doe", "Student name should be 'John Doe'"

def test_student_creation_without_name():
    """Test that creating a student without a name raises an error."""
    with pytest.raises(StudentError) as excinfo:
        Student(name="")
    assert str(excinfo.value) == "Name cannot be empty", "Should raise error for empty name"

def test_update_student_name(student):
    """Test that a student's name can be updated successfully."""
    student.update_name("Jane Doe")
    assert student.name == "Jane Doe", "Student name should be updated to 'Jane Doe'"

def test_update_student_name_with_empty_string(student):
    """Test that updating a student’s name to an empty string raises an error."""
    with pytest.raises(StudentError) as excinfo:
        student.update_name("")
    assert str(excinfo.value) == "Name cannot be empty", "Should raise error for empty name"

def test_delete_student(student):
    """Test that a student can be deleted properly."""
    student.delete()
    assert student.is_deleted, "Student should be marked as deleted"

def test_invalid_student_deletion(student):
    """Test that deleting a student that is already deleted raises an error."""
    student.delete()
    with pytest.raises(StudentError) as excinfo:
        student.delete()
    assert str(excinfo.value) == "Student is already deleted", "Should raise error for double deletion"
```