```python
from typing import List
from fastapi import HTTPException
from models.course import Course
from db.database import Database

class CourseService:
    def __init__(self, db: Database):
        self.db = db

    def create_course(self, name: str, level: str) -> Course:
        """
        Create a new course with the provided name and level.

        Args:
            name (str): The name of the course.
            level (str): The level of the course.

        Returns:
            Course: The created Course object.

        Raises:
            HTTPException: If the course creation fails due to invalid data or database errors.
        """
        try:
            # Create a new course instance
            course = Course(name=name, level=level)

            # Add the course to the database
            self.db.add(course)

            # Commit the transaction
            self.db.commit()

            return course
        except Exception as e:
            # Rollback in case of an error
            self.db.rollback()
            raise HTTPException(status_code=500, detail=f"Could not create course: {str(e)}")

    def get_all_courses(self) -> List[Course]:
        """
        Retrieve all courses from the database.

        Returns:
            List[Course]: A list of Course objects.
        """
        try:
            courses = self.db.query(Course).all()
            return courses
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Could not retrieve courses: {str(e)}")
```