```python
# src/validators/course_validation.py
from database import session  # Importing the database session for database operations
from models.course import Course  # Assuming the Course model is defined here
from models.teacher import Teacher  # Assuming the Teacher model is defined here

def validate_course_update(course_id: int, teacher_id: int) -> None:
    """
    Validate the inputs for updating a course with a new teacher.

    Parameters:
    - course_id (int): The ID of the course to be updated.
    - teacher_id (int): The ID of the teacher to be assigned to the course.

    Raises:
    - ValueError: If the course does not exist or the teacher does not exist.
    """
    # Check if Course exists
    course = session.query(Course).filter_by(id=course_id).first()
    if not course:
        raise ValueError("Course not found.")

    # Check if Teacher exists
    teacher = session.query(Teacher).filter_by(id=teacher_id).first()
    if not teacher:
        raise ValueError("Teacher does not exist.")
```