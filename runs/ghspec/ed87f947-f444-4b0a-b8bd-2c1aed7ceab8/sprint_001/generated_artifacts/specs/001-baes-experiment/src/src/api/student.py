from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
import logging
from .database import get_db, Student as StudentModel # Assuming existence of database and student model

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Pydantic model for Student input validation
class Student(BaseModel):
    name: str

@app.post("/students", status_code=201)
def create_student(student: Student, db: Session = Depends(get_db)):
    if not student.name:
        logger.error("Invalid input: Student name is required")
        raise HTTPException(status_code=400, detail="E400: Student name is required")
    
    new_student = StudentModel(name=student.name)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return {"id": new_student.id}

@app.get("/students/{student_id}", response_model=Student)
def read_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(StudentModel).filter(StudentModel.id == student_id).first()
    if not student:
        logger.error(f"Student with ID {student_id} not found")
        raise HTTPException(status_code=404, detail="E404: Student not found")

    return student

@app.put("/students/{student_id}", response_model=Student)
def update_student(student_id: int, student: Student, db: Session = Depends(get_db)):
    db_student = db.query(StudentModel).filter(StudentModel.id == student_id).first()
    if not db_student:
        logger.error(f"Update failed: Student with ID {student_id} not found")
        raise HTTPException(status_code=404, detail="E404: Student not found")
    
    db_student.name = student.name
    db.commit()
    return db_student

@app.delete("/students/{student_id}", status_code=204)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    db_student = db.query(StudentModel).filter(StudentModel.id == student_id).first()
    if not db_student:
        logger.error(f"Delete failed: Student with ID {student_id} not found")
        raise HTTPException(status_code=404, detail="E404: Student not found")

    db.delete(db_student)
    db.commit()
    return {}  # No content on successful deletion