```python
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.models import StudentCourse, Course, Student  # Import necessary models

router = APIRouter()

@router.get("/courses/{course_id}/students", response_model=list)
def list_students_in_course(course_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a list of students enrolled in a specified course.

    Args:
        course_id (int): The ID of the course to list students for.
        db (Session, optional): The database session. Defaults to dependency injection.

    Raises:
        HTTPException: If the course does not exist or no students are enrolled.

    Returns:
        list: A list of students enrolled in the specified course.
    """
    # Check if the course exists
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    # Query to retrieve students associated with the course
    student_courses = db.query(StudentCourse).filter(StudentCourse.course_id == course_id).all()
    
    student_ids = [sc.student_id for sc in student_courses]
    students = db.query(Student).filter(Student.id.in_(student_ids)).all()

    if not students:
        raise HTTPException(status_code=404, detail="No students are enrolled in this course")

    return students
```