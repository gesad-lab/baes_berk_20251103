```python
import os
from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
from src.database import get_db, engine
from src.models import Student, Course, Enrollment
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

# Initialize FastAPI app
app = FastAPI()

# Apply database migrations on startup
@app.on_event("startup")
async def apply_migrations():
    # Import Base to generate tables
    from src.database import Base
    # Create all tables in the database (if not exist)
    Base.metadata.create_all(bind=engine)

# API endpoint to enroll a Student in a Course
@app.post("/students/{student_id}/enroll")
async def enroll_student(student_id: int, course_id: str, db: Session = Depends(get_db)):
    # Validate input
    if not course_id:
        raise HTTPException(status_code=400, detail={"error": {"code": "E002", "message": "Course ID is required."}})

    # Check if student exists
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail={"error": {"code": "E003", "message": "Student not found."}})

    # Check if course exists
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail={"error": {"code": "E001", "message": "Specified course not found."}})

    # Create enrollment relationship
    enrollment = Enrollment(student_id=student.id, course_id=course.id)
    db.add(enrollment)
    db.commit()
    
    # Return updated courses for the student
    courses = db.query(Course).join(Enrollment).filter(Enrollment.student_id == student.id).all()
    return {"message": "Student enrolled successfully.", "courses": [course.id for course in courses]}

# API endpoint to retrieve all Courses for a specific Student
@app.get("/students/{student_id}/courses")
async def get_student_courses(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail={"error": {"code": "E003", "message": "Student not found."}})

    # Query courses for the student
    courses = db.query(Course).join(Enrollment).filter(Enrollment.student_id == student.id).all()
    return {"courses": [{"id": course.id, "name": course.name} for course in courses]}

# The remaining application logic...
```
