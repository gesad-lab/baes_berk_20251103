from fastapi import FastAPI, HTTPException, Path
from sqlalchemy.orm import Session
from typing import List

from models.student import Student as StudentModel
from database.database import get_db

app = FastAPI()

@app.post("/students/", response_model=StudentModel)
async def create_student(student: StudentModel, db: Session = next(get_db())):
    """Create a new student."""
    try:
        db.add(student)
        db.commit()
        db.refresh(student)
        return student
    except Exception as e:  # Catching generic exception for demonstration; ideally, catch specific exceptions
        db.rollback()  # Roll back the transaction on error
        raise HTTPException(status_code=400, detail="Error creating student")

@app.get("/students/", response_model=List[StudentModel])
async def read_students(skip: int = 0, limit: int = 10, db: Session = next(get_db())):
    """Retrieve a list of students."""
    try:
        students = db.query(StudentModel).offset(skip).limit(limit).all()
        return students
    except Exception as e:  # Catching generic exception for demonstration
        raise HTTPException(status_code=500, detail="Error retrieving students")

@app.get("/students/{student_id}", response_model=StudentModel)
async def read_student(student_id: int = Path(..., title="The ID of the student to retrieve"), db: Session = next(get_db())):
    """Retrieve a student by ID."""
    try:
        student = db.query(StudentModel).filter(StudentModel.id == student_id).first()
        if student is None:
            raise HTTPException(status_code=404, detail="Student not found")
        return student
    except Exception as e:  # Catching generic exception for demonstration
        raise HTTPException(status_code=500, detail="Error retrieving student")

@app.put("/students/{student_id}", response_model=StudentModel)
async def update_student(student_id: int, student: StudentModel, db: Session = next(get_db())):
    """Update a student."""
    try:
        db_student = db.query(StudentModel).filter(StudentModel.id == student_id).first()
        if db_student is None:
            raise HTTPException(status_code=404, detail="Student not found")
        
        db_student.name = student.name
        db.commit()
        return db_student
    except Exception as e:  # Catching generic exception for demonstration
        db.rollback()
        raise HTTPException(status_code=400, detail="Error updating student")

@app.delete("/students/{student_id}", response_model=dict)
async def delete_student(student_id: int, db: Session = next(get_db())):
    """Delete a student."""
    try:
        db_student = db.query(StudentModel).filter(StudentModel.id == student_id).first()
        if db_student is None:
            raise HTTPException(status_code=404, detail="Student not found")
        
        db.delete(db_student)
        db.commit()
        return {"detail": "Student deleted"}
    except Exception as e:  # Catching generic exception for demonstration
        db.rollback()
        raise HTTPException(status_code=400, detail="Error deleting student")