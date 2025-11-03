```python
# src/service.py

from sqlalchemy.orm import Session
from models import Course
from schemas import CourseCreate, CourseRead  # Assuming these are defined in schemas.py

class CourseService:
    """
    Service layer for managing course data.

    This class provides methods to create and retrieve courses,
    encapsulating business logic related to course management.
    """

    def __init__(self, db: Session):
        self.db = db

    def create_course(self, course_data: CourseCreate) -> CourseRead:
        """
        Create a new course in the database.

        Parameters:
            course_data (CourseCreate): The data for the new course.

        Returns:
            CourseRead: The created course with its attributes.
        """
        # Create a new Course instance
        new_course = Course(name=course_data.name, level=course_data.level)
        
        # Add the new course to the session
        self.db.add(new_course)
        self.db.commit()  # Commit the transaction
        self.db.refresh(new_course)  # Refresh instance to obtain the stored data

        return CourseRead.from_orm(new_course)  # Return the newly created course

    def get_courses(self) -> list[CourseRead]:
        """
        Retrieve all courses from the database.

        Returns:
            list[CourseRead]: A list of all courses in the database.
        """
        courses = self.db.query(Course).all()
        return [CourseRead.from_orm(course) for course in courses]  # Convert to Pydantic schema


def get_course_service(db: Session) -> CourseService:
    """
    Dependency injection for CourseService.

    Parameters:
        db (Session): The database session.

    Returns:
        CourseService: An instance of the CourseService.
    """
    return CourseService(db)
```