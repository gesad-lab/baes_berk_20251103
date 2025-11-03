```python
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel
from ..models.course import Course
from ..models.student import Student
from ..models.student_course import StudentCourse
from ..database import get_db

router = APIRouter()

class CourseAssignment(BaseModel):
    courseIds: List[int]  # expecting a list of course IDs

@router.post("/students/{student_id}/courses", status_code=200)
async def assign_courses(student_id: int, course_assignment: CourseAssignment, db: Session = Depends(get_db)):
    # Check if the student exists
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    assigned_courses = []
    
    for course_id in course_assignment.courseIds:
        # Check if the course exists
        course = db.query(Course).filter(Course.id == course_id).first()
        if not course:
            raise HTTPException(status_code=404, detail=f"Course with ID {course_id} not found")
        
        # Create a link between student and course
        student_course = StudentCourse(student_id=student_id, course_id=course_id)
        db.add(student_course)
        assigned_courses.append(course)

    # Commit the transaction to save changes to the database
    db.commit()

    return {"assigned_courses": [course.id for course in assigned_courses]}

@router.get("/students/{student_id}/courses", status_code=200)
async def retrieve_enrolled_courses(student_id: int, db: Session = Depends(get_db)):
    # Check if the student exists
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    # Retrieve courses assigned to the student
    enrolled_courses = (
        db.query(Course)
        .join(StudentCourse)
        .filter(StudentCourse.student_id == student_id)
        .all()
    )

    return {"enrolled_courses": [course.id for course in enrolled_courses]}
```