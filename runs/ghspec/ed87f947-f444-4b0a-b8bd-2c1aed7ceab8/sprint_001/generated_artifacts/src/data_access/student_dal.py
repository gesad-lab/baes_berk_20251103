```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# Define the base for declarative model definitions
Base = declarative_base()

# Define the Student model with declarative syntax
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

# Set up the SQLite database engine
DATABASE_URL = "sqlite:///students.db"
engine = create_engine(DATABASE_URL)

# Create a session factory bound to the engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db() -> None:
    """
    Create the database schema for the Student entity.
    This should be called at application startup to ensure
    the required database tables are created.
    """
    # Create all tables in the database
    Base.metadata.create_all(bind=engine)

def create_student(db: Session, name: str) -> Student:
    """
    Create a new student record in the database.

    Args:
        db (Session): The database session.
        name (str): The name of the student to be created.
    
    Returns:
        Student: The created student object.
    
    Raises:
        ValueError: If the name is invalid or empty.
    """
    if not name or not isinstance(name, str):
        raise ValueError("Student name must be a non-empty string")

    # Create a new Student instance
    student = Student(name=name)
    db.add(student)
    db.commit()  # Save the changes
    db.refresh(student)  # Refresh the instance to get the latest data
    return student

def get_student(db: Session, student_id: int) -> Student:
    """
    Retrieve a student record by its ID.

    Args:
        db (Session): The database session.
        student_id (int): The ID of the student to retrieve.
    
    Returns:
        Student: The student object, if found.
    
    Raises:
        ValueError: If the student ID is not found.
    """
    student = db.query(Student).filter(Student.id == student_id).first()
    if student is None:
        raise ValueError(f"Student with ID {student_id} does not exist")
    return student

def update_student(db: Session, student_id: int, new_name: str) -> Student:
    """
    Update an existing student's name by ID.

    Args:
        db (Session): The database session.
        student_id (int): The ID of the student to update.
        new_name (str): The new name for the student.
    
    Returns:
        Student: The updated student object.
    
    Raises:
        ValueError: If the student ID is not found or name is invalid.
    """
    student = get_student(db, student_id)  # Check if student exists
    if not new_name or not isinstance(new_name, str):
        raise ValueError("Student name must be a non-empty string")

    student.name = new_name  # Update name
    db.commit()  # Save changes
    db.refresh(student)  # Refresh to get updated data
    return student

def delete_student(db: Session, student_id: int) -> None:
    """
    Delete a student record by its ID.

    Args:
        db (Session): The database session.
        student_id (int): The ID of the student to delete.
    
    Raises:
        ValueError: If the student ID does not exist.
    """
    student = get_student(db, student_id)  # Check if student exists
    db.delete(student)  # Delete the student record
    db.commit()  # Save changes
```
