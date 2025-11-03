```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

# Define the SQLite database connection
DATABASE_URL = 'sqlite:///./test.db'
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)

def init_db():
    """Initialize the database and create tables if they don't exist."""
    Base.metadata.create_all(bind=engine)

def create_course(db: SessionLocal, name: str, level: str):
    """Create a new course in the database.

    Args:
        db: The database session.
        name: The name of the course.
        level: The level of the course.

    Returns:
        The created course object.
    """
    course = Course(name=name, level=level)
    try:
        db.add(course)
        db.commit()
        db.refresh(course)
    except IntegrityError as e:
        db.rollback()
        raise ValueError("Course creation failed due to integrity issue.") from e
    return course

def get_course(db: SessionLocal, course_id: int):
    """Retrieve a course by its ID.

    Args:
        db: The database session.
        course_id: The ID of the course.

    Returns:
        The course object if found, otherwise None.
    """
    return db.query(Course).filter(Course.id == course_id).first()

# Create the database structure
if __name__ == "__main__":
    init_db()
```