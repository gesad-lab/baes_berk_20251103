```python
# src/app.py

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from models import Student, Base
from database import get_db, engine

app = FastAPI()

# Verifying and creating the database schema on startup
@app.on_event("startup")
async def startup_event():
    # Create the database tables if they do not exist
    Base.metadata.create_all(bind=engine)

    # Optional: Validate the Student table schema after startup
    check_student_table_schema()

def check_student_table_schema():
    """
    Check if the Student table contains the necessary columns,
    including the new 'email' field. Raise an exception if discrepancies are found.
    """
    # Assuming that `engine` is a SQLAlchemy engine and that the table exists.
    with engine.connect() as connection:
        result = connection.execute("SELECT column_name FROM information_schema.columns WHERE table_name='student'")
        columns = {row['column_name'] for row in result}
        
        # Check if `email` column exists
        if "email" not in columns:
            raise RuntimeError("Database schema is invalid: 'email' column is missing in 'Student' table.")

@app.post("/students")
async def create_student(student: Student, db: Session = Depends(get_db)):
    """
    Create a new student with the provided name and email.
    
    :param student: Student data containing name and email
    :param db: Database session dependency
    :return: JSON object with student creation confirmation
    """
    db.add(student)
    db.commit()
    db.refresh(student)
    return {"id": student.id, "name": student.name, "email": student.email}

@app.get("/students/{student_id}")
async def get_student(student_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a student's information based on student ID.

    :param student_id: The ID of the student to retrieve
    :param db: Database session dependency
    :return: JSON object with student details
    """
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"id": student.id, "name": student.name, "email": student.email}
```