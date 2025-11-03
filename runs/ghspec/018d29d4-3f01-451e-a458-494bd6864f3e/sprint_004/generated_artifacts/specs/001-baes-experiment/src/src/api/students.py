from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy.orm import Session
from .database import get_db  # Presuming you have a get_db function to manage DB sessions
from .models import Student, Course, StudentCourse  # Make sure these models exist in the models file

router = APIRouter()

class CourseResponse(BaseModel):
    id: int
    name: str

class CoursesResponse(BaseModel):
    courses: List[CourseResponse]

@router.get("/students/{student_id}/courses", response_model=CoursesResponse)
def get_student_courses(student_id: int, db: Session = next(get_db())):
    """
    Retrieve courses associated with a specific student.

    Parameters:
    - student_id: ID of the student to retrieve courses for.
    - db: Database session.

    Returns:
    - A list of courses with their IDs and names.
    """
    # Fetch the student from the database
    student = db.query(Student).filter(Student.id == student_id).first()
    
    # Check if the student exists
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    # Get associated courses
    student_courses = db.query(StudentCourse).filter(StudentCourse.student_id == student.id).all()

    # If not enrolled in any courses, return an empty list
    if not student_courses:
        return CoursesResponse(courses=[])

    # Construct response data
    courses = []
    for sc in student_courses:
        course = db.query(Course).filter(Course.id == sc.course_id).first()
        if course:
            courses.append(CourseResponse(id=course.id, name=course.name))
    
    return CoursesResponse(courses=courses)