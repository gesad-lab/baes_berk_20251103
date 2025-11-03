from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

Base = declarative_base()

class Student(Base):
    """Database model for a student."""
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

def create_student(db: Session, name: str):
    """Create a new student in the database.

    Args:
        db (Session): The database session.
        name (str): The name of the student.

    Returns:
        Student: The created student instance.
    """
    student = Student(name=name)
    db.add(student)  # Add the student instance to the session
    db.commit()      # Commit the current transaction
    db.refresh(student)  # Refresh the instance with new data from the database
    return student

def get_students(db: Session):
    """Retrieve all students from the database.

    Args:
        db (Session): The database session.

    Returns:
        List[Student]: A list of student instances.
    """
    return db.query(Student).all()  # Query all students from the table

def get_student_by_id(db: Session, student_id: int):
    """Retrieve a student by ID.

    Args:
        db (Session): The database session.
        student_id (int): The ID of the student.

    Returns:
        Student: The student instance if found, else None.
    """
    return db.query(Student).filter(Student.id == student_id).first()  # Query a specific student by ID

def delete_student(db: Session, student_id: int):
    """Delete a student from the database by ID.

    Args:
        db (Session): The database session.
        student_id (int): The ID of the student.

    Returns:
        bool: True if the student was deleted, False otherwise.
    """
    student = db.query(Student).filter(Student.id == student_id).first()  # Find student by ID
    if student:
        db.delete(student)  # Delete the student instance
        db.commit()         # Commit the changes to the database
        return True
    return False  # Return False if the student was not found