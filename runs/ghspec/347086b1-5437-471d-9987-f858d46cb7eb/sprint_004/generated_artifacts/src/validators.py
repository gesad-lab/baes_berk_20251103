```python
# src/routes/course.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from src.models.student import Student, StudentCourse
from src.models.course import Course
from src.database import get_db

router = APIRouter()

@router.post("/students/{student_id}/courses/{course_id}", response_model=Student)
def associate_student_with_course(student_id: int, course_id: int, db: Session = Depends(get_db)):
    """
    Associate a Student with a Course.

    Args:
        student_id: The ID of the student to associate with a course.
        course_id: The ID of the course to associate with the student.
        db: Database session.

    Returns:
        The updated Student entity with course associations.

    Raises:
        HTTPException: If the student or course does not exist.
    """
    student = db.query(Student).filter(Student.id == student_id).first()
    course = db.query(Course).filter(Course.id == course_id).first()
    
    # Check if the Student and Course exist
    if not student:
        raise HTTPException(status_code=404, detail={"code": "E404", "message": "Student not found"})
    if not course:
        raise HTTPException(status_code=404, detail={"code": "E404", "message": "Course not found"})
    
    # Associate the course to the student
    student.courses.append(course)
    db.commit()
    db.refresh(student)

    return student

@router.get("/students/{student_id}/courses", response_model=list[Course])
def get_associated_courses(student_id: int, db: Session = Depends(get_db)):
    """
    Retrieve all courses associated with a specific Student.

    Args:
        student_id: The ID of the student to retrieve courses for.
        db: Database session.

    Returns:
        A list of Course entities associated with the Student.

    Raises:
        HTTPException: If the student does not exist.
    """
    student = db.query(Student).filter(Student.id == student_id).first()
    
    if not student:
        raise HTTPException(status_code=404, detail={"code": "E404", "message": "Student not found"})
    
    return student.courses
```