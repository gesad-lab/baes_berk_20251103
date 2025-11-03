```python
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models import Course, Teacher
from database import get_db

router = APIRouter()

@router.get("/api/v1/courses/{course_id}")
async def get_course(course_id: int, db: Session = Depends(get_db)):
    """
    Retrieve course details along with the assigned teacher's information.
    
    Parameters:
    - course_id (int): The ID of the course to retrieve.

    Returns:
    - JSON response with course details including assigned Teacher's name and email.
    
    Raises:
    - HTTPException: If the course does not exist.
    """
    # Query the course by ID
    course = db.query(Course).filter(Course.id == course_id).first()
    
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    
    # Prepare response data
    response_data = {
        "id": course.id,
        "name": course.name,
        "description": course.description,
        "teacher_id": course.teacher_id,
    }
    
    # Include teacher information if assigned
    if course.teacher_id:
        teacher = db.query(Teacher).filter(Teacher.id == course.teacher_id).first()
        if teacher:
            response_data["teacher_name"] = teacher.name
            response_data["teacher_email"] = teacher.email
    
    return response_data
```