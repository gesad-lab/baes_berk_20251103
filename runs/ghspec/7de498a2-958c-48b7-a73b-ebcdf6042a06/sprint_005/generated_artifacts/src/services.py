```python
# src/api.py

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from . import services, models
from .database import get_db

app = FastAPI()

@app.post("/teachers/", response_model=models.Teacher, status_code=201)
def create_teacher(teacher: models.TeacherCreate, db: Session = Depends(get_db)):
    """
    Create a new teacher record.

    Args:
        teacher: TeacherCreate object containing teacher name and email.
        db: Database session dependency.

    Returns:
        The created Teacher object.
    """
    existing_teacher = services.get_teacher_by_email(db, email=teacher.email)
    if existing_teacher:
        raise HTTPException(status_code=400, detail="Teacher with this email already exists.")

    return services.create_teacher(db=db, name=teacher.name, email=teacher.email)


@app.get("/teachers/{teacher_id}", response_model=models.Teacher)
def read_teacher(teacher_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a teacher by ID.

    Args:
        teacher_id: ID of the teacher to retrieve.
        db: Database session dependency.

    Returns:
        The Teacher object if found, otherwise raises 404 error.
    """
    teacher = services.get_teacher(db=db, teacher_id=teacher_id)
    if teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found.")
    return teacher


@app.put("/teachers/{teacher_id}", response_model=models.Teacher)
def update_teacher(teacher_id: int, teacher: models.TeacherUpdate, db: Session = Depends(get_db)):
    """
    Update an existing teacher's details.

    Args:
        teacher_id: ID of the teacher to update.
        teacher: TeacherUpdate object containing updated teacher details.
        db: Database session dependency.

    Returns:
        The updated Teacher object if successful, otherwise raises 404 error.
    """
    updated_teacher = services.update_teacher(db=db, teacher_id=teacher_id, name=teacher.name, email=teacher.email)
    if updated_teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found.")
    return updated_teacher


@app.delete("/teachers/{teacher_id}", status_code=204)
def delete_teacher(teacher_id: int, db: Session = Depends(get_db)):
    """
    Delete a teacher record by ID.

    Args:
        teacher_id: ID of the teacher to delete.
        db: Database session dependency.

    Returns:
        No content status if deleted successfully, otherwise raises 404 error.
    """
    if not services.delete_teacher(db=db, teacher_id=teacher_id):
        raise HTTPException(status_code=404, detail="Teacher not found.")

```