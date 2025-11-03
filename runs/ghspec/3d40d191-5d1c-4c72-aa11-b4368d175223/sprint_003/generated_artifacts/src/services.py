```python
from sqlalchemy.orm import Session
from src.models import Course  # Import the Course model

def create_course_service(name: str, level: str, db: Session):
    """Create a new Course and persist it to the database.
    
    Args:
        name (str): The name of the course.
        level (str): The level of the course.
        db (Session): The database session.

    Raises:
        ValueError: If either the name or level is missing.

    Returns:
        Course: The created course object.
    """
    if not name or not level:
        raise ValueError("Both name and level must be provided for the Course.")

    course = Course(name=name, level=level)
    db.add(course)
    db.commit()
    db.refresh(course)
    return course

def get_all_courses_service(db: Session):
    """Retrieve all courses from the database.

    Args:
        db (Session): The database session.

    Returns:
        List[Course]: A list of Course objects.
    """
    return db.query(Course).all()
```