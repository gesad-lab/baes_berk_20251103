```python
from sqlalchemy.orm import Session
from models import Course, Teacher  # Ensure proper import of models

def assign_teacher_to_course(course_id: int, teacher_id: int, db: Session) -> Course:
    """
    Assigns a teacher to a course by updating the teacher_id field in the Course model.
    
    Args:
        course_id (int): The ID of the course to assign the teacher to.
        teacher_id (int): The ID of the teacher to be assigned.
        db (Session): The database session to perform the operations.

    Returns:
        Course: The updated course with the assigned teacher.

    Raises:
        ValueError: If the course does not exist.
        ValueError: If the teacher does not exist.
    """
    # Retrieve the course by ID
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise ValueError("Course not found")

    # Check if the teacher exists
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if not teacher:
        raise ValueError("Teacher not found")

    # Assign the teacher to the course
    course.teacher_id = teacher.id
    db.commit()  # Persist changes to the database
    db.refresh(course)  # Refresh the course instance with updated data
    return course
```