from fastapi import APIRouter, HTTPException
from typing import List
from src.models.student_model import Student
from src.database.db_setup import get_database

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = get_database()
    try:
        yield db
    finally:
        db.close()

@router.get("/students", response_model=List[Student])
async def read_students(db=next(get_db())):
    """
    Retrieve a list of all students from the database.

    Args:
        db: The database session.

    Returns:
        A list of Student objects representing all students.
    """
    try:
        students = db.query(Student).all()  # Fetch all students from the database
        return students
    except Exception as e:
        # Log the exception context here if needed
        raise HTTPException(status_code=500, detail="Could not retrieve students")