```python
# src/routes.py

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from src.database import get_db, init_db
from src.models import Student, Course, StudentCourse
from pydantic import BaseModel

app = FastAPI()

class EnrollRequest(BaseModel):
    course_id: int

@app.post("/students/{id}/enroll")
def enroll_student(id: int, enroll_request: EnrollRequest, db: Session = Depends(get_db)):
    """Enroll a student in a specific course."""
    
    # Fetch the student by ID
    student = db.query(Student).filter(Student.id == id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    # Fetch the course by ID
    course = db.query(Course).filter(Course.id == enroll_request.course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    # Check if the enrollment already exists
    existing_enrollment = db.query(StudentCourse).filter(
        StudentCourse.student_id == id,
        StudentCourse.course_id == enroll_request.course_id
    ).first()
    
    if existing_enrollment:
        raise HTTPException(status_code=400, detail="Student already enrolled in this course")
    
    # Create the new enrollment
    new_enrollment = StudentCourse(student_id=id, course_id=enroll_request.course_id)
    db.add(new_enrollment)
    db.commit()
    db.refresh(new_enrollment)
    
    return {"message": "Enrollment successful", "enrollment_id": new_enrollment.id}

@app.get("/students/{id}/courses")
def get_student_courses(id: int, db: Session = Depends(get_db)):
    """Retrieve a list of courses a student is enrolled in."""
    
    # Fetch the student by ID
    student = db.query(Student).filter(Student.id == id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    # Fetch the courses linked to the student
    courses = db.query(Course).join(StudentCourse).filter(StudentCourse.student_id == id).all()
    
    return {"courses": [{"id": course.id, "name": course.name} for course in courses]}

def init_db():
    """Initialize the database, including handling new migrations."""
    # Call existing migration logic
    existing_migration_logic()
    
    # New logic to handle the `student_courses` table
    # Check if `student_courses` table exists, if not, create it
    if not check_table_exists("student_courses"):
        create_student_courses_table()
    
    # Perform any other necessary migration steps
    update_existing_student_data()
    update_existing_course_data()
    # Log successful database initialization
    print("Database initialized with all necessary migrations.")
```
