from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi import Depends
from . import crud, models, schemas
from .database import get_db

app = FastAPI()

@app.get("/students/{student_id}", response_model=schemas.StudentWithCourses)
def get_student_with_courses(student_id: str, db: Session = Depends(get_db)):
    """
    Retrieve a student's information along with their linked courses.

    Parameters:
    - student_id: The ID of the student to retrieve.
    - db: Database session dependency.

    Returns:
    - A Student object with a list of linked course IDs.
    
    Raises:
    - HTTPException: If the student is not found.
    """
    student = crud.get_student_with_courses(db, student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student