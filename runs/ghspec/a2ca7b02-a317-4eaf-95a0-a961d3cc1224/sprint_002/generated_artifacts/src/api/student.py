```python
from fastapi import FastAPI, HTTPException, Body
from sqlalchemy.orm import Session
import re
from db.database import get_db
from services.student_service import create_student, get_all_students
from models.student import Student

app = FastAPI()

# Regular expression for validating email format
EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

def validate_email(email: str) -> None:
    """
    Validate the format of the email address.
    
    Parameters:
    email (str): The email address to validate.

    Raises:
    HTTPException: If the email format is invalid.
    """
    if not re.match(EMAIL_REGEX, email):
        raise HTTPException(
            status_code=400,
            detail={"error": {"code": "E001", "message": "Invalid email format."}}
        )

@app.post("/students", response_model=Student)
def create_student_endpoint(
    name: str = Body(..., embed=True),
    email: str = Body(..., embed=True),
    db: Session = next(get_db())
):
    """
    Create a new student in the database.

    Parameters:
    name (str): The name of the student.
    email (str): The email of the student.
    db (Session): The database session.

    Returns:
    Student: The newly created student object.
    """
    if not name:
        raise HTTPException(
            status_code=400,
            detail={"error": {"code": "E002", "message": "Name is required."}}
        )

    validate_email(email)  # Validate email format

    student = create_student(db=db, name=name, email=email)  # Call service to create student
    return student

@app.get("/students", response_model=list[Student])
def read_students(db: Session = next(get_db())):
    """
    Retrieve all students from the database.

    Parameters:
    db (Session): The database session.

    Returns:
    list[Student]: A list of students' names and emails.
    """
    return get_all_students(db=db)
```