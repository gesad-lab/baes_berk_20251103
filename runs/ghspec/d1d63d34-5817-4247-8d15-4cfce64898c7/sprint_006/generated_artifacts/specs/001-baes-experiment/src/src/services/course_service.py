```python
from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends
from pydantic import BaseModel, Field
from .database import get_db
from .models import Course  # Assuming Course model is imported from models

# Request model for assigning/updating a teacher
class AssignTeacherRequest(BaseModel):
    teacher_id: str = Field(..., description="The ID of the teacher to assign to the course")

@app.put("/courses/{course_id}/update-teacher")
async def update_teacher_assignment(course_id: int, request: AssignTeacherRequest, db: Session = Depends(get_db)):
    """
    Update the teacher assigned to a specific course.

    :param course_id: The ID of the course to update
    :param request: Request object containing the new teacher ID
    :param db: Database session dependency
    :return: JSON response confirming the update
    """
    # Fetch the course from the database
    course = db.query(Course).filter(Course.id == course_id).first()
    
    if not course:
        raise HTTPException(status_code=404, detail=f"Course with ID {course_id} not found.")
    
    # Update the teacher ID for the course
    course.teacher_id = request.teacher_id
    
    try:
        db.commit()  # Commit the changes to the database
        db.refresh(course)  # Refresh the instance to get updated data
    except Exception as e:
        db.rollback()  # Rollback in case of error
        raise HTTPException(status_code=500, detail=f"An error occurred while updating teacher assignment: {str(e)}")

    return {"message": "Teacher assignment has been updated successfully.", "course_id": course.id, "teacher_id": course.teacher_id}
```