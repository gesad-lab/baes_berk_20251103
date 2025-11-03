```python
# /src/services/course_service.py

from models.course import Course
from models.teacher import Teacher
from database import SessionLocal
from sqlalchemy.orm import Session
from fastapi import HTTPException

async def update_course_teacher(course_id: int, teacher_id: int) -> Course:
    """
    Updates the course with the specified course_id to associate it with a teacher_id.
    
    Args:
        course_id (int): The ID of the course to update.
        teacher_id (int): The ID of the teacher to assign to the course.
    
    Raises:
        HTTPException: If the course does not exist or the teacher ID is invalid.
    
    Returns:
        Course: The updated course object.
    """
    with SessionLocal() as session:
        # Fetch the course by ID
        course = session.get(Course, course_id)
        if not course:
            raise HTTPException(status_code=404, detail="Course not found.")

        # Fetch the teacher by ID to validate the existence
        teacher = session.get(Teacher, teacher_id)
        if not teacher:
            raise HTTPException(status_code=400, detail="Invalid teacher ID.")
        
        # Assign the teacher to the course
        course.teacher_id = teacher_id
        
        # Commit the changes to the database
        session.commit()
        session.refresh(course)  # Refresh the course instance with the latest data

        return course

async def get_course_with_teacher(course_id: int) -> Course:
    """
    Retrieves the course with the specified course_id, including associated teacher information.
    
    Args:
        course_id (int): The ID of the course to retrieve.
    
    Raises:
        HTTPException: If the course does not exist.
    
    Returns:
        Course: The course object with the associated teacher info.
    """
    with SessionLocal() as session:
        # Fetch the course by ID
        course = session.query(Course).filter(Course.id == course_id).options(
            joinedload(Course.teacher)  # Assuming teacher relationship is set up in the Course model
        ).first()

        if not course:
            raise HTTPException(status_code=404, detail="Course not found.")

        return course
```