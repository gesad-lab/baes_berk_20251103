```python
from fastapi import APIRouter, HTTPException, Path
from pydantic import BaseModel, conlist
from typing import List
from src.models.student import Student
from src.models.course import Course  # Importing Course model for validation
from src.models.student_course import StudentCourse
from sqlalchemy.orm import Session
from src.database.database import get_db

router = APIRouter()

class CourseAssociation(BaseModel):
    course_ids: conlist(int, unique_items=True)

@router.post("/students/{student_id}/courses", response_model=Student)
def associate_courses(student_id: int, course_association: CourseAssociation, db: Session = next(get_db())):
    # Validate that the student exists
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    # Validate that all course IDs provided exist
    invalid_course_ids = [course_id for course_id in course_association.course_ids if not db.query(Course).filter(Course.id == course_id).first()]
    if invalid_course_ids:
        raise HTTPException(status_code=400, detail=f"Invalid Course IDs: {invalid_course_ids}")

    # Associate courses with the student
    for course_id in course_association.course_ids:
        student_course = StudentCourse(student_id=student_id, course_id=course_id)
        db.add(student_course)
    
    db.commit()
    
    # Reload the student to include the associated courses in the response
    db.refresh(student)
    return student

@router.get("/students/{student_id}/courses", response_model=List[int])
def retrieve_student_courses(student_id: int, db: Session = next(get_db())):
    # Validate that the student exists
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    # Fetch the associated courses
    course_ids = [sc.course_id for sc in student.student_courses]  # Assuming student_courses relationship is well-defined
    return course_ids
```