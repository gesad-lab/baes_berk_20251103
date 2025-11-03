from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Student, Base

DATABASE_URL = "sqlite:///students.db"  # Connection string for SQLite

# Set up the database connection
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Function to create the database schema
def init_db():
    """Create the database schema for the application."""
    Base.metadata.create_all(bind=engine)

def create_student(name: str) -> Student:
    """Creates a new student with the provided name.

    Args:
        name (str): The name of the student to be created.

    Returns:
        Student: The created Student object.
    """
    session = SessionLocal()
    try:
        new_student = Student(name=name)
        session.add(new_student)
        session.commit()
        session.refresh(new_student)
        return new_student
    except Exception as e:
        session.rollback()
        raise RuntimeError(f"Error creating student: {str(e)}")
    finally:
        session.close()

def get_student(student_id: int) -> Student:
    """Retrieves a student by their ID.

    Args:
        student_id (int): The ID of the student to retrieve.

    Returns:
        Student: The retrieved Student object.
    
    Raises:
        ValueError: If the student is not found.
    """
    session = SessionLocal()
    try:
        student = session.query(Student).filter(Student.id == student_id).first()
        if student is None:
            raise ValueError("Student not found")
        return student
    finally:
        session.close()

def update_student(student_id: int, new_name: str) -> Student:
    """Updates a student's name by their ID.

    Args:
        student_id (int): The ID of the student to update.
        new_name (str): The new name for the student.

    Returns:
        Student: The updated Student object.
    
    Raises:
        ValueError: If the student is not found.
    """
    session = SessionLocal()
    try:
        student = session.query(Student).filter(Student.id == student_id).first()
        if student is None:
            raise ValueError("Student not found")
        student.name = new_name
        session.commit()
        return student
    except Exception as e:
        session.rollback()
        raise RuntimeError(f"Error updating student: {str(e)}")
    finally:
        session.close()

def delete_student(student_id: int) -> None:
    """Deletes a student by their ID.

    Args:
        student_id (int): The ID of the student to delete.

    Raises:
        ValueError: If the student is not found.
    """
    session = SessionLocal()
    try:
        student = session.query(Student).filter(Student.id == student_id).first()
        if student is None:
            raise ValueError("Student not found")
        session.delete(student)
        session.commit()
    except Exception as e:
        session.rollback()
        raise RuntimeError(f"Error deleting student: {str(e)}")
    finally:
        session.close()