```python
from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
from models import Teacher
from database import get_db  # Assuming a database module for handling DB sessions

app = FastAPI()

@app.get("/teachers/{teacher_id}", response_model=Teacher)
def get_teacher(teacher_id: int, db: Session = next(get_db())):
    """
    Retrieve the details of a specific teacher by their ID.
    
    :param teacher_id: The ID of the teacher to retrieve.
    :param db: The database session to use for the query.
    :return: The details of the teacher.
    :raises HTTPException: 404 if the teacher is not found.
    """
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return teacher
```