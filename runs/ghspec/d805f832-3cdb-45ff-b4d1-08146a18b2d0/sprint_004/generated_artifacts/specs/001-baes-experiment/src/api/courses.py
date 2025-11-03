from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from models import Course, StudentCourse  # Ensure these models are defined in models.py
from database import get_db  # Dependency for database session

router = APIRouter()

class StudentCoursesResponseModel(BaseModel):
    """Model to represent the response format for a student's courses."""
    student_id: int
    courses: list

@router.get("/students/{student_id}/courses", response_model=StudentCoursesResponseModel)
async def get_student_courses(student_id: int, db: Session = Depends(get_db)):
    """
    Fetch the courses associated with a specific Student.

    Parameters:
    - student_id (int): The ID of the student whose courses are to be retrieved.
    - db (Session): Database session dependency.

    Returns:
    - JSON object containing the student ID and a list of associated courses with their IDs and names.
    """
    # Query the courses associated with the student
    student_courses = db.query(StudentCourse).filter(StudentCourse.student_id == student_id).all()
    
    if not student_courses:
        raise HTTPException(status_code=404, detail="No courses found for this student.")

    courses = []
    for sc in student_courses:
        course = db.query(Course).filter(Course.id == sc.course_id).first()
        if course:
            courses.append({"id": course.id, "name": course.name})

    return {"student_id": student_id, "courses": courses}