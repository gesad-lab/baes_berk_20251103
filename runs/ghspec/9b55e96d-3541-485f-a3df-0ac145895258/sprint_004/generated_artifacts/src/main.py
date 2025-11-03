from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from models import Student, Course, Enrollment  # Assuming these models are defined in models.py
from database import SessionLocal, engine  # Assuming database session management is setup in database.py
from sqlalchemy.orm import Session

app = FastAPI()

# Pydantic schemas
class EnrollRequest(BaseModel):
    course_id: int

class CourseResponse(BaseModel):
    course_id: int
    course_name: str  # Assuming Course has a name attribute

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/students/{student_id}/enroll")
def enroll_student(student_id: int, enroll_request: EnrollRequest, db: Session = next(get_db())):
    """Enroll a student in a course."""
    student = db.query(Student).filter(Student.id == student_id).first()
    course = db.query(Course).filter(Course.id == enroll_request.course_id).first()
    
    if not student or not course:
        raise HTTPException(status_code=404, detail="Student or Course not found")
    
    # Create the enrollment association
    enrollment = Enrollment(student_id=student_id, course_id=enroll_request.course_id)
    db.add(enrollment)
    db.commit()
    
    return {"message": "Student enrolled in course successfully"}

@app.get("/students/{student_id}/courses", response_model=List[CourseResponse])
def get_student_courses(student_id: int, db: Session = next(get_db())):
    """Retrieve courses a student is enrolled in."""
    student = db.query(Student).filter(Student.id == student_id).first()
    
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    # Retrieve courses associated with the student
    courses = db.query(Course).join(Enrollment).filter(Enrollment.student_id == student_id).all()
    
    return [{"course_id": course.id, "course_name": course.name} for course in courses]

@app.delete("/students/{student_id}/courses/{course_id}")
def remove_student_from_course(student_id: int, course_id: int, db: Session = next(get_db())):
    """Remove a student from a course."""
    enrollment = db.query(Enrollment).filter(Enrollment.student_id == student_id, Enrollment.course_id == course_id).first()
    
    if not enrollment:
        raise HTTPException(status_code=404, detail="Student or Course not found")
    
    db.delete(enrollment)
    db.commit()
    
    return {"message": "Student removed from course successfully"}

# Make sure to initialize the database models and tables as needed.
def init_db():
    # Create tables
    from models import Base  # Assuming Base is defined in models.py
    Base.metadata.create_all(bind=engine)

# Call this function on startup if needed, otherwise ensure it's handled in your app setup
# init_db()