```python
# src/data_access/course_dal.py

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from src.model.course import Course  # Assuming Course model is defined in src.model.course

class CourseDAL:
    """
    Data Access Layer for Course entity.
    Responsible for interacting with the database for course-related operations.
    """

    def __init__(self, session: Session):
        self.session = session

    def create_course(self, name: str, level: str) -> Course:
        """Creates a new course entry in the database.

        Args:
            name (str): The name of the course.
            level (str): The academic level of the course.

        Returns:
            Course: The created Course object.

        Raises:
            HTTPException: If name or level is missing.
        """
        if not name:
            raise HTTPException(status_code=400, detail="E001: Course name is required.")
        if not level:
            raise HTTPException(status_code=400, detail="E002: Course level is required.")

        new_course = Course(name=name, level=level)
        self.session.add(new_course)
        try:
            self.session.commit()
            self.session.refresh(new_course)  # Refresh to get the updated state
            return new_course
        except IntegrityError:
            self.session.rollback()
            raise HTTPException(status_code=400, detail="E003: Course with this name already exists.")

    def get_course_by_id(self, course_id: int) -> Course:
        """Retrieves a course by its ID.

        Args:
            course_id (int): The ID of the course to retrieve.

        Returns:
            Course: The Course object corresponding to the given ID.

        Raises:
            HTTPException: If course not found.
        """
        course = self.session.query(Course).filter(Course.id == course_id).first()
        if not course:
            raise HTTPException(status_code=404, detail="E004: Course not found.")
        return course
```