```python
# src/services/student_service.py

from fastapi import HTTPException
from pydantic import BaseModel, EmailStr
from src.repository import Student, get_student_db_session  # Assuming there's a session manager for DB interactions

# Define the Pydantic model for student creation
class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Validate the email format

# Function to create a new student
def create_student(student_data: StudentCreate):
    """
    Create a new student in the database.

    Args:
        student_data (StudentCreate): The data of the student to create.

    Raises:
        HTTPException: If student creation fails or if input validation fails.

    Returns:
        Student: The created student object.
    """
    if not student_data.name.strip():
        raise HTTPException(status_code=400, detail="Name is required and cannot be empty.")
    
    # Create a Student instance and save to the database
    with get_student_db_session() as session:  # Assuming context management for sessions
        new_student = Student(name=student_data.name, email=student_data.email)
        session.add(new_student)
        session.commit()
        session.refresh(new_student)
    
    return new_student

# Function to retrieve all students
def get_students():
    """
    Retrieve a list of all students.

    Returns:
        List[Student]: A list of all student objects.
    """
    with get_student_db_session() as session:
        students = session.query(Student).all()
    return students
```