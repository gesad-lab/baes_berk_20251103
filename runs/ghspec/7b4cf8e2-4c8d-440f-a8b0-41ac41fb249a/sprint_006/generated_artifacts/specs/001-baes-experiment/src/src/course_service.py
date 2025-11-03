```python
from models import Course, Teacher  # Importing needed models
from app import db  # Importing the database instance

def assign_teacher_to_course(course_id: int, teacher_id: int) -> None:
    """Assign a specific teacher to the given course.

    Args:
        course_id (int): The ID of the course.
        teacher_id (int): The ID of the teacher to assign.

    Raises:
        ValueError: If the course or teacher does not exist.
    """
    course = Course.query.get(course_id)
    teacher = Teacher.query.get(teacher_id)

    if not course:
        raise ValueError(f'Course with ID {course_id} does not exist.')
    if not teacher:
        raise ValueError(f'Teacher with ID {teacher_id} does not exist.')

    course.teacher_id = teacher_id  # Assign the teacher to the course
    db.session.commit()  # Save changes to the database


def unassign_teacher_from_course(course_id: int) -> None:
    """Unassign the teacher from the specified course.

    Args:
        course_id (int): The ID of the course.

    Raises:
        ValueError: If the course does not exist.
    """
    course = Course.query.get(course_id)

    if not course:
        raise ValueError(f'Course with ID {course_id} does not exist.')

    course.teacher_id = None  # Remove the teacher assignment
    db.session.commit()  # Save changes to the database


def get_course_details(course_id: int) -> dict:
    """Retrieve course details, including the associated teacher.

    Args:
        course_id (int): The ID of the course.

    Returns:
        dict: A dictionary containing course details along with the assigned teacher information.

    Raises:
        ValueError: If the course does not exist.
    """
    course = Course.query.get(course_id)

    if not course:
        raise ValueError(f'Course with ID {course_id} does not exist.')

    return {
        'course_id': course.id,
        'course_name': course.name,
        'teacher_id': course.teacher_id,
        'teacher_name': course.teacher.name if course.teacher else None
    }


def list_courses_with_teachers() -> list:
    """Retrieve all courses with their assigned teachers.

    Returns:
        list: A list of dictionaries containing course details and associated teacher names.
    """
    courses = Course.query.all()
    course_list = [{
        'course_id': course.id,
        'course_name': course.name,
        'teacher_id': course.teacher_id,
        'teacher_name': course.teacher.name if course.teacher else None
    } for course in courses]
    
    return course_list
```