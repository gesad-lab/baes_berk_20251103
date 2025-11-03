```python
# src/routes/student_course_routes.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel, validator
from src.database.database import get_db
from src.models.student import Student
from src.models.course import Course
from src.models.student_course import StudentCourse
from typing import List

router = APIRouter()

class CourseAssignmentRequest(BaseModel):
    course_ids: List[int]

    @validator('course_ids')
    def validate_course_ids(cls, v):
        """Ensure all course_ids are positive integers."""
        if not v or any(not isinstance(course_id, int) or course_id <= 0 for course_id in v):
            raise ValueError("course_ids must be a non-empty list of positive integers")
        return v

@router.post("/students/{student_id}/courses", response_model=Student)
def assign_courses_to_student(student_id: int, assignment: CourseAssignmentRequest, db: Session = Depends(get_db)):
    """Assign courses to a student by updating the student's course list."""
    
    # Validate student exists
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found.")

    # Validate each course ID and assign courses
    for course_id in assignment.course_ids:
        course = db.query(Course).filter(Course.id == course_id).first()
        if not course:
            raise HTTPException(status_code=404, detail=f"Course with id {course_id} does not exist.")
        # Create a new student-course relationship
        student_course = StudentCourse(student_id=student_id, course_id=course_id)
        db.add(student_course)
    
    db.commit()
    db.refresh(student)

    return student

@router.get("/students/{id}", response_model=Student)
def retrieve_student(id: int, db: Session = Depends(get_db)):
    """Retrieve a student by ID including assigned course IDs."""
    student = db.query(Student).filter(Student.id == id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found.")

    return student

@router.get("/students", response_model=List[Student])
def list_all_students(db: Session = Depends(get_db)):
    """List all students along with assigned course IDs."""
    return db.query(Student).all()
```