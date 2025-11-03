```python
# src/api/student.py

from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List
from src.db.models import Student, Course, StudentCourse
from src.db.database import get_db
from src.validations.student_validators import validate_student_id
from src.validations.course_validators import validate_course_ids

router = APIRouter()

@router.patch("/students/{student_id}", response_model=Student)
def associate_courses(student_id: int, course_ids: List[int], db: Session = next(get_db())):
    """
    Associate courses with a student.

    Parameters:
    - student_id: ID of the student to associate courses with
    - course_ids: List of course IDs to associate with the student

    Returns:
    - Updated student object with associated courses

    Raises:
    - HTTPException: If the student or any of the courses do not exist
    """
    # Validate student ID
    student = validate_student_id(student_id, db)
    
    # Validate course IDs
    valid_courses = validate_course_ids(course_ids, db)
    
    # If any invalid courses were sent, raise a 400 Bad Request error
    if len(valid_courses) != len(course_ids):
        raise HTTPException(status_code=400, detail="One or more course IDs are invalid.")

    # Clear existing course associations
    db.query(StudentCourse).filter(StudentCourse.student_id == student_id).delete()
    
    # Create new associations
    for course_id in valid_courses:
        student_course = StudentCourse(student_id=student_id, course_id=course_id)
        db.add(student_course)
    
    # Commit the changes to the database
    db.commit()
    
    # Return updated student with associated courses
    return student


@router.get("/students/{student_id}/courses", response_model=List[Course])
def retrieve_student_courses(student_id: int, db: Session = next(get_db())):
    """
    Retrieve the list of courses associated with a student.

    Parameters:
    - student_id: ID of the student to retrieve courses for

    Returns:
    - List of course objects associated with the student
    """
    # Validate student ID
    validate_student_id(student_id, db)
    
    # Retrieve courses associated with the student
    courses = db.query(Course).join(StudentCourse).filter(StudentCourse.student_id == student_id).all()
    
    return courses
```
