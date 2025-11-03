```python
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session
from src.models.course import Course
from src.models.teacher import Teacher

class CourseService:
    """Service class to handle business logic related to Course and Teacher assignments."""

    def __init__(self, session: Session):
        """
        Initializes the CourseService with a SQLAlchemy session.

        :param session: The SQLAlchemy session to use for database operations.
        """
        self.session = session

    def assign_teacher_to_course(self, course_id: int, teacher_id: int):
        """
        Assigns a Teacher to a Course.

        :param course_id: ID of the course to which the teacher will be assigned.
        :param teacher_id: ID of the teacher to be assigned.
        :raises ValueError: If the course or teacher does not exist.
        """
        # Retrieve the course
        course = self.session.query(Course).filter(Course.id == course_id).one_or_none()
        if course is None:
            raise ValueError(f"Course with ID {course_id} does not exist.")
        
        # Retrieve the teacher
        teacher = self.session.query(Teacher).filter(Teacher.id == teacher_id).one_or_none()
        if teacher is None:
            raise ValueError(f"Teacher with ID {teacher_id} does not exist.")
        
        # Assign the teacher to the course
        course.teacher_id = teacher_id
        self.session.commit()

    def get_course_with_teacher(self, course_id: int):
        """
        Retrieves a Course along with its assigned Teacher.

        :param course_id: ID of the course to retrieve.
        :return: Course object including teacher details.
        :raises ValueError: If the course does not exist.
        """
        # Retrieve the course, including the teacher relationship
        course = self.session.query(Course).filter(Course.id == course_id).one_or_none()
        if course is None:
            raise ValueError(f"Course with ID {course_id} does not exist.")
        
        return course
```