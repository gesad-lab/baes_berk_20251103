```python
# src/services.py

from fastapi import HTTPException
from sqlalchemy.orm import Session
from .models import Student  # Assuming Student model is defined in models.py
from .database import get_db  # Assuming a function that provides a database session

def update_student(student_id: int, name: str = None, email: str = None, db: Session = None):
    """
    Update an existing Student's name and/or email.

    Parameters:
    student_id (int): The ID of the student to update.
    name (str): The updated name of the student (optional).
    email (str): The updated email of the student (optional, must be valid).

    Returns:
    Student: The updated Student object.

    Raises:
    HTTPException: If the student is not found or if the email is invalid.
    """
    if db is None:
        db = get_db()
        
    # Fetch student from the database
    student = db.query(Student).filter(Student.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    # Validate email if provided
    if email is not None:
        if not isinstance(email, str) or "@" not in email:
            raise HTTPException(status_code=400, detail="Invalid email format")
        student.email = email

    # Update name if provided
    if name is not None:
        student.name = name

    # Commit changes to the database
    db.commit()
    db.refresh(student)  # Refresh the student instance to get the updated data

    return student
```