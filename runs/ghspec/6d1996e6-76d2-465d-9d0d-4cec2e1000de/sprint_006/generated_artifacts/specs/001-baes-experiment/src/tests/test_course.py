```python
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from services.course import CourseService
from services.teacher import TeacherService

app = FastAPI()

# Dependency Injection for Course Service
course_service = CourseService()
teacher_service = TeacherService()

class RemoveTeacherRequest(BaseModel):
    """Request model for removing a teacher from a course."""
    teacher_id: int

@app.delete("/courses/{id}/remove-teacher")
def remove_teacher_from_course(id: int, request: RemoveTeacherRequest):
    """Remove a teacher from a course by course ID."""
    # Validate that the course exists
    course = course_service.get_course_by_id(id)
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found.")

    # Check if the teacher exists before removing
    teacher = teacher_service.get_teacher_by_id(request.teacher_id)
    if teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found.")

    # Proceed to remove the teacher from the course
    course_service.remove_teacher(id, request.teacher_id)
    
    return {"message": "Teacher removed successfully."}
```