from fastapi import APIRouter, HTTPException
from models.student_course_association import StudentCourseAssociation
from models.student import Student
from models.course import Course
from database.db import SessionLocal
from pydantic import BaseModel
from typing import List

router = APIRouter()

class CourseAssignment(BaseModel):
    course_ids: List[int]

@router.post("/students/{student_id}/courses", status_code=200)
def assign_courses(student_id: int, assignment: CourseAssignment):
    """Assign one or more courses to an existing student."""
    db = SessionLocal()
    student = db.query(Student).filter(Student.id == student_id).first()
    
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    # Query to check if all provided course_ids exist
    courses = db.query(Course).filter(Course.id.in_(assignment.course_ids)).all()
    if len(courses) != len(assignment.course_ids):
        raise HTTPException(status_code=404, detail="One or more courses not found")

    # Iterate and create course associations
    for course in courses:
        association = StudentCourseAssociation(student_id=student_id, course_id=course.id)
        db.add(association)
    db.commit()
    
    return {"student_id": student_id, "assigned_courses": [course.id for course in courses]}

@router.get("/students/{student_id}", status_code=200)
def get_student_info(student_id: int):
    """Retrieve student information along with their associated courses."""
    db = SessionLocal()
    student = db.query(Student).filter(Student.id == student_id).first()
    
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    # Join to retrieve courses associated with the student
    courses = db.query(Course).join(StudentCourseAssociation).filter(StudentCourseAssociation.student_id == student_id).all()
    
    return {
        "student_id": student.id,
        "courses": [{"id": course.id, "name": course.name, "level": course.level} for course in courses]
    }