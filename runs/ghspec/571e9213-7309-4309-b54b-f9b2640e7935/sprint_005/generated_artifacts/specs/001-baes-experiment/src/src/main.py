```python
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db  # Assuming this is your database session retrieval function
from models import Teacher  # Importing the Teacher model
from schemas import TeacherCreate, TeacherResponse  # Assuming these schemas are defined
from typing import List

app = FastAPI()

# Dependency to get the database session
def get_db_session():
    db: Session = get_db()
    try:
        yield db
    finally:
        db.close()

# Route to create a new Teacher
@app.post("/teachers", response_model=TeacherResponse)
def create_teacher(teacher: TeacherCreate, db: Session = Depends(get_db_session)):
    """
    Create a new Teacher entry in the system.
    
    Args:
        teacher (TeacherCreate): The data for the new Teacher.
        db (Session): The database session dependency.

    Returns:
        TeacherResponse: The created Teacher details.
    """
    new_teacher = Teacher(name=teacher.name, email=teacher.email)
    
    db.add(new_teacher)
    db.commit()
    db.refresh(new_teacher)
    
    return new_teacher

# Route to retrieve a specific Teacher's details
@app.get("/teachers/{teacher_id}", response_model=TeacherResponse)
def get_teacher(teacher_id: int, db: Session = Depends(get_db_session)):
    """
    Retrieve the details of a specific Teacher.
    
    Args:
        teacher_id (int): The ID of the Teacher.
        db (Session): The database session dependency.

    Returns:
        TeacherResponse: The Teacher's details.

    Raises:
        HTTPException: If the Teacher is not found.
    """
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return teacher

# Route to list all Teachers
@app.get("/teachers", response_model=List[TeacherResponse])
def list_teachers(db: Session = Depends(get_db_session)):
    """
    List all Teachers available in the system.
    
    Args:
        db (Session): The database session dependency.

    Returns:
        List[TeacherResponse]: A list of Teachers.
    """
    teachers = db.query(Teacher).all()
    return teachers
```