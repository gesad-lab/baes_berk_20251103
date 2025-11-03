```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

Base = declarative_base()

class Course(Base):
    """ORM model representing a Course entity."""
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)

class CourseRepository:
    """Repository class for Course CRUD operations."""

    def __init__(self, db: Session):
        self.db = db

    def create_course(self, name: str, level: str) -> Course:
        """
        Create a new course record in the database.

        Args:
            name (str): The name of the course.
            level (str): The level of the course (e.g., beginner, intermediate, advanced).

        Returns:
            Course: The created course object.
        """
        new_course = Course(name=name, level=level)
        self.db.add(new_course)
        self.db.commit()
        self.db.refresh(new_course)  # Refresh instance to get updated state
        return new_course

    def get_course(self, course_id: int) -> Course:
        """
        Retrieve a course by its ID.

        Args:
            course_id (int): The ID of the course to retrieve.

        Returns:
            Course: The course object if found, None otherwise.
        """
        return self.db.query(Course).filter(Course.id == course_id).first()

    def get_all_courses(self) -> list[Course]:
        """
        Retrieve all course records.

        Returns:
            list[Course]: A list of all course objects.
        """
        return self.db.query(Course).all()
```