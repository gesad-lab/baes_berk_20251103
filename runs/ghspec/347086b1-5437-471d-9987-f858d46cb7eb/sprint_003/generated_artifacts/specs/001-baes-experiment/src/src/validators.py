```python
# src/validators.py

from typing import Dict, Any, Tuple

class CourseValidationError(Exception):
    """Custom exception to handle course validation errors."""
    pass

def validate_course_input(data: Dict[str, Any]) -> Tuple[bool, str]:
    """
    Validate the input data for creating a course.

    Parameters:
    - data (dict): The input data containing course details.

    Returns:
    - Tuple[bool, str]: A tuple indicating whether the input is valid and an error message if not.
    """
    if 'name' not in data or not data['name']:
        # Course name is required
        return False, "E001: Course name is required."
    if 'level' not in data or not data['level']:
        # Course level is required
        return False, "E002: Course level is required."
    
    # Input is valid
    return True, ""

def create_course(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Create a new course after validating input data.

    Parameters:
    - data (dict): The input data containing course details.

    Returns:
    - dict: The created course details.

    Raises:
    - CourseValidationError: If the course input validation fails.
    """
    is_valid, error_message = validate_course_input(data)
    if not is_valid:
        raise CourseValidationError(error_message)

    # Assuming we have a Course model defined in models/course.py
    from src.models.course import Course  # Import the Course model
    course = Course(name=data['name'], level=data['level'])
    
    # Here we would normally save the course to the database
    # db_session.add(course)
    # db_session.commit()

    return {"name": course.name, "level": course.level}
```