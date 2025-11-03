```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)

def create_course(db: Session, course_data: dict) -> Course:
    """
    Create a new course record in the database.

    Args:
        db (Session): The database session.
        course_data (dict): A dictionary containing course details.

    Returns:
        Course: The created course object.
    """
    new_course = Course(name=course_data["name"], level=course_data["level"])
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return new_course

def get_courses(db: Session):
    """
    Retrieve all courses from the database.

    Args:
        db (Session): The database session.

    Returns:
        list: A list of all course objects.
    """
    return db.query(Course).all()

def update_course(db: Session, course_id: int, course_data: dict) -> Course:
    """
    Update an existing course's name or level based on provided course ID.

    Args:
        db (Session): The database session.
        course_id (int): The unique identifier for the course.
        course_data (dict): A dictionary containing updated course details.

    Returns:
        Course: The updated course object.
    
    Raises:
        ValueError: If the course ID does not exist in the database.
    """
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise ValueError("Course not found")

    if "name" in course_data and course_data["name"]:
        course.name = course_data["name"]
    if "level" in course_data and course_data["level"]:
        course.level = course_data["level"]

    db.commit()
    db.refresh(course)
    return course

def delete_course(db: Session, course_id: int):
    """
    Delete a course from the database by ID.

    Args:
        db (Session): The database session.
        course_id (int): The unique identifier for the course.

    Returns:
        bool: True if deletion was successful, False otherwise.
    """
    course = db.query(Course).filter(Course.id == course_id).first()
    if course:
        db.delete(course)
        db.commit()
        return True
    return False
```