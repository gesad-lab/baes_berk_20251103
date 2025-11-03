```python
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models import Student, Course, StudentCourse
from database import get_db
from pydantic import BaseModel
from typing import List

router = APIRouter()

class CourseAssignment(BaseModel):
    course_ids: List[int]

@router.post("/api/v1/students/{student_id}/courses")
async def assign_courses_to_student(student_id: int, assignment: CourseAssignment, db: Session = Depends(get_db)):
    """
    Assign multiple courses to a student.

    Parameters:
    - student_id: ID of the student to whom courses will be assigned.
    - assignment: contains a list of course IDs to be assigned.

    Returns:
    - JSON response confirming the assignment with student ID and course IDs.
    Raises:
    - HTTPException if the student or any course does not exist.
    """
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail={"error": {"code": "E404", "message": "Student not found"}})

    # Validate that all courses exist
    courses = db.query(Course).filter(Course.id.in_(assignment.course_ids)).all()
    if len(courses) != len(assignment.course_ids):
        raise HTTPException(status_code=404, detail={"error": {"code": "E404", "message": "One or more courses not found"}})

    # Assign courses to student
    for course in courses:
        student_course = StudentCourse(student_id=student_id, course_id=course.id)
        db.add(student_course)

    db.commit()

    return {
        "student_id": student.id,
        "course_ids": [course.id for course in courses],
        "course_names": [course.name for course in courses]
    }

@router.get("/api/v1/students/{student_id}/courses")
async def get_student_courses(student_id: int, db: Session = Depends(get_db)):
    """
    Retrieve the list of courses for a specified student.

    Parameters:
    - student_id: ID of the student

    Returns:
    - JSON response with student ID and list of enrolled courses.
    Raises:
    - HTTPException if the student does not exist.
    """
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail={"error": {"code": "E404", "message": "Student not found"}})

    student_courses = db.query(StudentCourse).filter(StudentCourse.student_id == student_id).all()
    course_ids = [sc.course_id for sc in student_courses]

    return {
        "student_id": student.id,
        "course_ids": course_ids
    }

@router.delete("/api/v1/students/{student_id}/courses/{course_id}")
async def remove_course_from_student(student_id: int, course_id: int, db: Session = Depends(get_db)):
    """
    Remove a course assignment from a student.

    Parameters:
    - student_id: ID of the student
    - course_id: ID of the course to remove

    Returns:
    - JSON response confirming removal.
    Raises:
    - HTTPException if the student or course does not exist.
    """
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail={"error": {"code": "E404", "message": "Student not found"}})

    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail={"error": {"code": "E404", "message": "Course not found"}})

    # Remove the course assignment
    db.query(StudentCourse).filter(StudentCourse.student_id == student_id, StudentCourse.course_id == course_id).delete()
    db.commit()

    return {"message": "Course successfully removed from student.", "student_id": student_id, "course_id": course_id}
```