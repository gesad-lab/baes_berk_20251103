```python
# tests/controllers/test_course_controller.py

import pytest
from unittest.mock import MagicMock
from src.controllers.course_controller import CourseController
from src.services.course_service import CourseService
from src.models.course import Course

@pytest.fixture
def course_service():
    """Mock CourseService for testing CourseController."""
    return MagicMock(spec=CourseService)

@pytest.fixture
def course_controller(course_service):
    """Initialize CourseController with mocked CourseService."""
    return CourseController(course_service)

def test_assign_teacher_to_course(course_controller, course_service):
    """Test assigning a teacher to an existing course."""
    course_id = 1
    teacher_id = 2
    course_service.assign_teacher_to_course.return_value = True

    response = course_controller.assign_teacher(course_id, teacher_id)
    
    # Assert that the service was called with the correct parameters
    course_service.assign_teacher_to_course.assert_called_once_with(course_id, teacher_id)
    
    # Assert response (Assuming it returns a success message)
    assert response == {'message': 'Teacher assigned successfully'}

def test_get_course_with_teacher_details(course_controller, course_service):
    """Test retrieving course details with teacher information."""
    course_id = 1
    course_data = Course(id=course_id, name='Math 101', teacher_id=2)
    teacher_data = {'id': 2, 'name': 'John Doe', 'email': 'john@example.com'}
    
    # Mock the service return value
    course_service.get_course_with_teacher.return_value = {**course_data.__dict__, 'teacher': teacher_data}

    response = course_controller.get_course(course_id)

    # Assert that the service was called with the correct parameters
    course_service.get_course_with_teacher.assert_called_once_with(course_id)

    # Assert response contains course and teacher details
    expected_response = {
        'id': 1,
        'name': 'Math 101',
        'teacher': teacher_data
    }
    assert response == expected_response

def test_assign_teacher_with_invalid_id(course_controller, course_service):
    """Test assigning a teacher with an invalid ID returns an error."""
    course_id = 1
    invalid_teacher_id = None
    course_service.assign_teacher_to_course.side_effect = ValueError("Invalid teacher ID")

    with pytest.raises(ValueError) as exc_info:
        course_controller.assign_teacher(course_id, invalid_teacher_id)
    
    # Validate the error message
    assert str(exc_info.value) == "Invalid teacher ID"

# Additional tests can be added here to cover more scenarios
```