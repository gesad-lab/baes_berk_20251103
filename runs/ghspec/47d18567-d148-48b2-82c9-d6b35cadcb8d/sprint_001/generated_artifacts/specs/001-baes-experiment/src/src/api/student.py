from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from src.db.database import get_db
from src.db.models import Student

router = APIRouter()

@router.post("/students", response_model=dict)
async def create_student(name: str, db: Session = Depends(get_db)):
    """
    Create a new student with the given name.

    Parameters:
    - name (str): The name of the student to create.

    Returns:
    - dict: The created student's ID and name.
    
    Raises:
    - HTTPException: If the name field is invalid.
    """
    if not name or not isinstance(name, str):
        raise HTTPException(status_code=400, detail="E001: Invalid name format. Name must be a non-empty string.")

    # Create a new student instance
    new_student = Student(name=name)

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return {"id": new_student.id, "name": new_student.name}

@router.get("/students", response_model=list)
async def get_students(db: Session = Depends(get_db)):
    """
    Retrieve a list of all students.

    Parameters:
    - db (Session): Database session to query the student table.

    Returns:
    - list: A list of dictionaries containing student IDs and names.
    """
    students = db.query(Student).all()  # Retrieve all students from the database
    return [{"id": student.id, "name": student.name} for student in students]  # Return a list of student data

# The above code implements the functionality to create and retrieve students. 
# Ensure the Student model is in place for data interaction with the database.