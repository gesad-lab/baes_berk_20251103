```python
from sqlalchemy.orm import Session
from models import Course  # Assuming models.py contains the Course class
import logging

# Set up logging
logger = logging.getLogger(__name__)

class CourseService:
    """Service class for managing courses."""

    def __init__(self, session: Session):
        """Initialize the CourseService with a SQLAlchemy session."""
        self.session = session

    def create_course(self, name: str, level: str) -> Course:
        """Create a new course in the system.

        Args:
            name (str): The name of the course.
            level (str): The level of the course (e.g., 'beginner', 'intermediate', 'advanced').

        Returns:
            Course: The created Course object.

        Raises:
            ValueError: If name or level is empty.
        """
        if not name or not level:
            raise ValueError("Course name and level cannot be empty.")

        course = Course(name=name, level=level)
        self.session.add(course)
        self.session.commit()
        
        logger.info(f"Created new course: {course}")
        return course

    def get_course(self, course_id: int) -> Course:
        """Retrieve a course by its ID.

        Args:
            course_id (int): The ID of the course to retrieve.

        Returns:
            Course: The Course object, if found.

        Raises:
            ValueError: If course_id is not positive.
            LookupError: If no course is found with the given ID.
        """
        if course_id <= 0:
            raise ValueError("Course ID must be a positive integer.")

        course = self.session.query(Course).filter(Course.id == course_id).one_or_none()

        if course is None:
            logger.error(f"Course with ID {course_id} not found.")
            raise LookupError(f"No course found with ID: {course_id}")

        logger.info(f"Retrieved course: {course}")
        return course

    def list_courses(self) -> list[Course]:
        """List all courses in the system.

        Returns:
            list: A list of Course objects.
        """
        courses = self.session.query(Course).all()
        logger.info(f"Listing all courses: {courses}")
        return courses
```