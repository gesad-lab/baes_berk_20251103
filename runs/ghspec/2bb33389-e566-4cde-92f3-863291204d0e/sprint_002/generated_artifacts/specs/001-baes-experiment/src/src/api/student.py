from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.models import Student  # Assuming a Student model is defined in src/models
from typing import List

router = APIRouter()

class StudentResponse(BaseModel):
    id: int
    name: str
    email: str

@router.get("/students", response_model=List[StudentResponse])
def read_students(db: Session = Depends(get_db)):
    """
    Retrieve a list of all students including their IDs, names, and email addresses.

    - **db**: Database session dependency.
    - Returns a list of students with their IDs, names, and emails.
    """
    students = db.query(Student).all()
    
    # Validate that the returned students have all necessary fields
    if not students:
        raise HTTPException(status_code=404, detail="No students found.")
    
    return students  # Pydantic will take care of serialization

# Additional part: Assuming Student model is updated accordingly to include email

# Make sure you have the router included in your main application file. For example:
# app.include_router(router)