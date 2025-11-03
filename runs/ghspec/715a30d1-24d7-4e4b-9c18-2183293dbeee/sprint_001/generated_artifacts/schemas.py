from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
from models import Student  # Assuming models.py contains the Student model
from database import SessionLocal, engine  # Assuming database.py handles session management
from pydantic import BaseModel

app = FastAPI()

class StudentResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/students/{id}", response_model=StudentResponse)
def read_student(id: int, db: Session = next(get_db())):
    """
    Retrieve a student by ID.

    :param id: The ID of the student to retrieve.
    :param db: Database session to use for the query.
    :return: The student data.
    :raises HTTPException: If the student is not found.
    """
    student = db.query(Student).filter(Student.id == id).first()  # Query the student by ID
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")  # Raise a 404 error if not found
    return student  # Return the student data as a response