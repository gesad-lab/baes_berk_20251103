from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

# Declare a base class for the ORM models
Base = declarative_base()

# Define the Student model
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

# Create an SQLite database engine
ENGINE = create_engine('sqlite:///students.db')

# Initialize the database schema
Base.metadata.create_all(ENGINE)

# Create a session factory
Session = sessionmaker(bind=ENGINE)

def create_student(name: str) -> Student:
    """Create a new Student record in the database."""
    session = Session()
    new_student = Student(name=name)
    try:
        session.add(new_student)
        session.commit()
        return new_student
    except SQLAlchemyError as e:
        session.rollback()
        # Log error details (ideally using a logging framework)
        print(f"Error creating student: {e}")  # Replace with proper logging in production
        raise 
    finally:
        session.close()

def get_all_students() -> list:
    """Retrieve all Student records from the database."""
    session = Session()
    try:
        return session.query(Student).all()
    except SQLAlchemyError as e:
        # Log error details (ideally using a logging framework)
        print(f"Error retrieving students: {e}")  # Replace with proper logging in production
        raise
    finally:
        session.close()

def update_student(student_id: int, name: str) -> Student:
    """Update the name of an existing Student in the database."""
    session = Session()
    try:
        student = session.query(Student).filter(Student.id == student_id).one()
        student.name = name
        session.commit()
        return student
    except SQLAlchemyError as e:
        session.rollback()
        # Log error details
        print(f"Error updating student: {e}")  # Replace with proper logging in production
        raise
    finally:
        session.close()

def delete_student(student_id: int) -> None:
    """Remove a Student record from the database."""
    session = Session()
    try:
        student = session.query(Student).filter(Student.id == student_id).one()
        session.delete(student)
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        # Log error details
        print(f"Error deleting student: {e}")  # Replace with proper logging in production
        raise
    finally:
        session.close()