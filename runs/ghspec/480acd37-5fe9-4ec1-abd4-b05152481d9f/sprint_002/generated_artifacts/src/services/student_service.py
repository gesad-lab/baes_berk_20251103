```python
# src/services/student_service.py

from typing import List, Optional
from pydantic import EmailStr, BaseModel, ValidationError
from src.models import Student  # Assuming there's a Student model in models.py
from src.database import db_session  # Assuming there's a database session management in database.py


class StudentCreateRequest(BaseModel):
    name: str
    email: EmailStr  # Pydantic will handle the validation of the email format


class StudentUpdateRequest(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None  # Pydantic validation for optional email


def create_student(student_data: StudentCreateRequest) -> Student:
    """
    Create a new student record in the database.

    Args:
        student_data (StudentCreateRequest): The data to create the student.

    Returns:
        Student: The created student object.

    Raises:
        ValidationError: If the student data is invalid.
    """
    try:
        new_student = Student(name=student_data.name, email=student_data.email)
        db_session.add(new_student)
        db_session.commit()
        db_session.refresh(new_student)
        return new_student
    except Exception as e:
        db_session.rollback()  # Rollback in case of an error
        raise ValidationError(f"Error creating student: {str(e)}")


def update_student(student_id: int, update_data: StudentUpdateRequest) -> Student:
    """
    Update an existing student record by the student's ID.

    Args:
        student_id (int): The ID of the student to update.
        update_data (StudentUpdateRequest): The new data for the student.

    Returns:
        Student: The updated student object.

    Raises:
        ValueError: If the student ID is invalid or if the update fails.
    """
    student = db_session.query(Student).filter(Student.id == student_id).first()
    
    if not student:
        raise ValueError(f"Student with ID {student_id} not found.")

    if update_data.name is not None:
        student.name = update_data.name
    if update_data.email is not None:
        student.email = update_data.email  # Pydantic will validate this

    try:
        db_session.commit()
        return student
    except Exception as e:
        db_session.rollback()  # Rollback in case of an error
        raise ValueError(f"Error updating student: {str(e)}")


def get_all_students() -> List[Student]:
    """
    Retrieve all student records from the database.

    Returns:
        List[Student]: A list of all student objects.
    """
    return db_session.query(Student).all()
```