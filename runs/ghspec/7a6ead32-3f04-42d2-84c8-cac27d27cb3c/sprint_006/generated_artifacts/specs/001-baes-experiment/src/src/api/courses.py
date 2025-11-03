```python
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models import Course, Teacher
from database import get_db

router = APIRouter()

@router.put("/api/v1/courses/{course_id}/assign_teacher")
async def assign_teacher(course_id: int, teacher_id: int, db: Session = Depends(get_db)):
    """Assign a teacher to a course.

    Args:
        course_id (int): The ID of the course to which the teacher will be assigned.
        teacher_id (int): The ID of the teacher to be assigned to the course.

    Raises:
        HTTPException: If the course not found, teacher not found, or if the course already has a teacher.

    Returns:
        dict: Response with a success message and the updated course information.
    """
    course = db.query(Course).filter(Course.id == course_id).first()
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")

    if course.teacher_id is not None:
        raise HTTPException(status_code=400, detail="A teacher is already assigned to this course")
    
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")

    # Assign the teacher to the course
    course.teacher_id = teacher_id
    db.commit()
    
    return {
        "message": "Teacher successfully assigned to course",
        "course": {
            "id": course.id,
            "name": course.name,
            "teacher_id": course.teacher_id,
            "teacher_name": teacher.name,
            "teacher_email": teacher.email
        }
    }

@router.get("/api/v1/courses/{course_id}")
async def get_course(course_id: int, db: Session = Depends(get_db)):
    """Retrieve course details including assigned teacher information.

    Args:
        course_id (int): The ID of the course to retrieve.

    Raises:
        HTTPException: If the course not found.

    Returns:
        dict: Course details along with associated teacher information if assigned.
    """
    course = db.query(Course).filter(Course.id == course_id).first()
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")

    response = {
        "id": course.id,
        "name": course.name,
        "teacher_id": course.teacher_id,
    }
    
    if course.teacher_id is not None:
        teacher = db.query(Teacher).filter(Teacher.id == course.teacher_id).first()
        response.update({
            "teacher_name": teacher.name,
            "teacher_email": teacher.email
        })

    return response
```