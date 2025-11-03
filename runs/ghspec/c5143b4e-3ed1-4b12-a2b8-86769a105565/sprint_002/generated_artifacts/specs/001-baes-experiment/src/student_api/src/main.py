from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
from src.database import get_db
from src import crud, models

app = FastAPI()


class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Validate email format


@app.post("/students", response_model=models.Student)
async def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    """
    Create a new student with a name and email address.
    
    Parameters:
    - student: StudentCreate - The student information to be created.
    - db: Session - The database session.

    Returns:
    - The created student object.
    
    Raises:
    - HTTPException: 400 if the email is not valid or if the creation failed.
    """
    # Validate email is provided (handled by Pydantic)
    if not student.email:
        raise HTTPException(status_code=400, detail="Email must be provided.")

    # Call CRUD function to create student
    db_student = crud.create_student(db=db, name=student.name, email=student.email)
    
    if db_student is None:
        raise HTTPException(status_code=500, detail="Failed to create student.")
    
    return db_student


@app.get("/students", response_model=list[models.Student])
async def get_students(db: Session = Depends(get_db)):
    """
    Retrieve a list of all students.

    Parameters:
    - db: Session - The database session.

    Returns:
    - A list of all student objects.
    """
    students = crud.get_students(db)
    return students