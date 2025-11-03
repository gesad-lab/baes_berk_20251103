```python
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

# Import the Course model and Pydantic schemas if they exist
from models import Course
from schemas import CourseCreate, CourseList

def create_course(db: Session, course: CourseCreate):
    """
    Create a new Course in the database.

    Parameters:
    - db: Session - The database session instance.
    - course: CourseCreate - The Course data to be created.

    Returns:
    - Course - The newly created Course object.
    """
    db_course = Course(name=course.name, level=course.level)
    db.add(db_course)
    try:
        db.commit()
        db.refresh(db_course)  # Retrieve the created course with its assigned ID
        return db_course
    except IntegrityError:
        db.rollback()  # Rollback the transaction on failure
        raise ValueError("E001: Course with this name already exists.")

def get_courses(db: Session):
    """
    Retrieve a list of all Courses from the database.

    Parameters:
    - db: Session - The database session instance.

    Returns:
    - List[Course] - A list of Course objects.
    """
    return db.query(Course).all()
```