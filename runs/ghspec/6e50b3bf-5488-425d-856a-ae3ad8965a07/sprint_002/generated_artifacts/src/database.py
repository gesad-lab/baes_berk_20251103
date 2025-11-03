```python
# src/database.py

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the base class for declarative models
Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)  # New column for storing email addresses

# Initialize the database connection
DATABASE_URL = "sqlite:///students.db"  # Example SQLite database URL
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """Creates the database tables if they don't already exist."""
    Base.metadata.create_all(bind=engine)

def get_student_by_id(student_id: int):
    """Retrieve a student record by ID.
    
    Args:
        student_id: ID of the student to retrieve.

    Returns:
        Student: The student record if found, None otherwise.
    """
    session = SessionLocal()
    try:
        return session.query(Student).filter(Student.id == student_id).first()
    except Exception as e:
        # Log exception details here (e.g., using a logging library)
        raise e
    finally:
        session.close()

def create_student(name: str, email: str):
    """Create a new student record in the database.
    
    Args:
        name: The name of the student.
        email: The email of the student.

    Returns:
        Student: The created student object with an auto-generated ID.
    """
    session = SessionLocal()
    new_student = Student(name=name, email=email)
    try:
        session.add(new_student)
        session.commit()
        session.refresh(new_student)  # Load the ID of the new student
        return new_student
    except Exception as e:
        session.rollback()  # Roll back the transaction on error
        # Log exception details here (e.g., using a logging library)
        raise e
    finally:
        session.close()
```