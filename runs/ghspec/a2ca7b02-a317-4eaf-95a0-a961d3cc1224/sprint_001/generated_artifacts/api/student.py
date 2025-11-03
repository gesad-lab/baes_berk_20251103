from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from services.student_service import get_all_students
from models.student import Student

app = FastAPI()

@app.get("/students", response_model=list[Student])
def read_students(db: Session = next(get_db())):
    """
    Retrieve all students from the database.

    Parameters:
    db (Session): The database session.

    Returns:
    list[Student]: A list of students' names.
    """
    students = get_all_students(db)
    if not students:
        # If no students found, return an empty list
        return []
    
    return students

