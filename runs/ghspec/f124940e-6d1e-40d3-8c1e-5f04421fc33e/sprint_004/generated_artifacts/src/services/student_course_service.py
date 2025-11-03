```python
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from src.models import StudentCourse, Course, Student
from src.database import get_db  # Assuming a function to get DB session

router = APIRouter()

class Enrollment(BaseModel):
    course_id: int

@router.post("/students/{student_id}/enroll")
def enroll_student(student_id: int, enrollment: Enrollment, db: Session = Depends(get_db)):
    """
    Enroll a student in a course by linking student and course.
    
    Args:
        student_id (int): ID of the student.
        enrollment (Enrollment): Enrollment data containing course_id.
        db (Session): Database session dependency.
        
    Raises:
        HTTPException: If the course is not found or the student is already enrolled.
        
    Returns:
        dict: Confirmation message upon successful enrollment.
    """
    # Check if the course exists
    course = db.query(Course).filter(Course.id == enrollment.course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    
    # Check if the student is already enrolled in the course
    existing_enrollment = db.query(StudentCourse).filter(
        StudentCourse.student_id == student_id,
        StudentCourse.course_id == enrollment.course_id
    ).first()
    if existing_enrollment:
        raise HTTPException(status_code=400, detail="Student already enrolled in this course")
    
    # Create a new StudentCourse relationship
    new_enrollment = StudentCourse(student_id=student_id, course_id=enrollment.course_id)
    db.add(new_enrollment)
    db.commit()
    
    return {"message": "Student enrolled successfully"}

@router.get("/students/{student_id}/courses")
def get_student_courses(student_id: int, db: Session = Depends(get_db)):
    """
    Retrieve all courses a student is enrolled in.
    
    Args:
        student_id (int): ID of the student.
        db (Session): Database session dependency.
    
    Returns:
        List[Course]: List of courses that the student is enrolled in.
    """
    # Get all courses for the student
    courses = db.query(Course).join(StudentCourse).filter(StudentCourse.student_id == student_id).all()
    return courses
```