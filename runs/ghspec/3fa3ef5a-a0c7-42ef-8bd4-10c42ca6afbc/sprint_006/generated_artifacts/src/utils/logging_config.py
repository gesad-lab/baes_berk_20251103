```python
import logging

# Configure the logging settings
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)

# Create a logger for this module
logger = logging.getLogger(__name__)

def log_teacher_assignment(course_id: int, teacher_id: int) -> None:
    """
    Log the event of assigning a teacher to a course.

    Args:
        course_id (int): The ID of the course to which the teacher is being assigned.
        teacher_id (int): The ID of the teacher being assigned to the course.
    """
    logger.info("Assigned teacher ID %d to course ID %d.", teacher_id, course_id)

def log_teacher_removal(course_id: int, teacher_id: int) -> None:
    """
    Log the event of removing a teacher from a course.

    Args:
        course_id (int): The ID of the course from which the teacher is being removed.
        teacher_id (int): The ID of the teacher being removed from the course.
    """
    logger.info("Removed teacher ID %d from course ID %d.", teacher_id, course_id)

```
