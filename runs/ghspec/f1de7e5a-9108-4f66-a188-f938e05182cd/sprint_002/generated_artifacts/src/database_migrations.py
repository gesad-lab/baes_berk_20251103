```python
from sqlalchemy import Column, Integer, String, create_engine, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
import re

Base = declarative_base()

# Database connection setup
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Student(Base):
    """Database model for the Student entity."""
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(Text, unique=True, nullable=False)  # Email field added

def validate_email(email: str) -> bool:
    """Validate the format of the email address."""
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

def create_student(db_session, name: str, email: str):
    """
    Create a new student in the database.

    Parameters:
    - db_session: SQLAlchemy session for database operations.
    - name: Name of the student.
    - email: Email address of the student.

    Returns:
    - The created student object if successful.
    - Raises ValueError for invalid input and IntegrityError for unique constraint violation.
    """
    if not name or not isinstance(name, str):
        raise ValueError("Invalid input: Name must be a non-empty string.")
    
    if not validate_email(email):
        raise ValueError("Invalid input: Email format is not correct.")
    
    new_student = Student(name=name, email=email)
    db_session.add(new_student)
    
    try:
        db_session.commit()
        return new_student
    except IntegrityError:
        db_session.rollback()
        raise ValueError("An error occurred: The email address must be unique.")

# Create the database table if it doesn't exist
Base.metadata.create_all(bind=engine)
```