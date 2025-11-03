```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base
from typing import Dict, Any, Optional

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}')>"


def create_student(session: Session, name: str) -> Dict[str, Any]:
    """
    Create a new student in the database.
    
    Parameters:
    - session: The SQLAlchemy session to use for the transaction.
    - name: The name of the student to create.

    Returns:
    - A dictionary containing the student's ID and name.
    
    Raises:
    - ValueError if the name is empty.
    """
    if not name:
        raise ValueError("Student name cannot be empty.")

    new_student = Student(name=name)
    session.add(new_student)
    try:
        session.commit()
        return {"id": new_student.id, "name": new_student.name}
    except IntegrityError:
        session.rollback()
        raise ValueError("Failed to create student due to integrity error.")


def fetch_student(session: Session, student_id: int) -> Optional[Dict[str, Any]]:
    """
    Fetch a student's details by their ID.
    
    Parameters:
    - session: The SQLAlchemy session to use for the transaction.
    - student_id: The ID of the student to fetch.

    Returns:
    - A dictionary containing the student's ID and name if found, otherwise None.
    """
    student = session.query(Student).filter_by(id=student_id).first()
    if student:
        return {"id": student.id, "name": student.name}
    return None


def update_student(session: Session, student_id: int, name: str) -> Dict[str, Any]:
    """
    Update a student's name by their ID.
    
    Parameters:
    - session: The SQLAlchemy session to use for the transaction.
    - student_id: The ID of the student to update.
    - name: The new name for the student.

    Returns:
    - A dictionary containing the updated student's ID and name.

    Raises:
    - ValueError if the student is not found or the name is empty.
    """
    if not name:
        raise ValueError("Student name cannot be empty.")

    student = session.query(Student).filter_by(id=student_id).first()
    if not student:
        raise ValueError(f"Student with ID {student_id} not found.")

    student.name = name
    session.commit()
    return {"id": student.id, "name": student.name}


def delete_student(session: Session, student_id: int) -> str:
    """
    Delete a student from the database by their ID.
    
    Parameters:
    - session: The SQLAlchemy session to use for the transaction.
    - student_id: The ID of the student to delete.

    Returns:
    - A confirmation message on successful deletion.

    Raises:
    - ValueError if the student is not found.
    """
    student = session.query(Student).filter_by(id=student_id).first()
    if not student:
        raise ValueError(f"Student with ID {student_id} not found.")

    session.delete(student)
    session.commit()
    return f"Student with ID {student_id} deleted successfully."
```