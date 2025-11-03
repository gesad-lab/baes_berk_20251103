```python
import pytest
from src.services.student_service import create_student, get_student_by_id
from src.models import Student
from unittest.mock import patch

@pytest.fixture
def mock_student():
    """Create mock student data for testing."""
    return Student(id=1, name="John Doe", email="john.doe@example.com")

def test_create_student_creates_student_successfully():
    """Test creating a student successfully."""
    name = "Jane Doe"
    email = "jane.doe@example.com"

    with patch('src.services.student_service.Student') as mock_student_class:
        mock_student_class.return_value = mock_student()
        created_student = create_student(name, email)

        assert created_student.name == name
        assert created_student.email == email

def test_get_student_by_email_successfully():
    """Test retrieving a student by ID successfully."""
    student_id = 1
    expected_email = "john.doe@example.com"
    expected_name = "John Doe"

    # Mocking the get_student_by_id function to return the mock student
    with patch('src.services.student_service.get_student_by_id') as mock_get_student:
        mock_get_student.return_value = mock_student()

        student = get_student_by_id(student_id)

        # Asserting that the fetched student's details are correct
        assert student.id == student_id
        assert student.name == expected_name
        assert student.email == expected_email
```