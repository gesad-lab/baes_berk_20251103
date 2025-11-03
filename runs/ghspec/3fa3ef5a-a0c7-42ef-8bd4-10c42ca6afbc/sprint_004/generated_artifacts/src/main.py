```python
# src/main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.services.student_service import StudentService
from src.services.course_service import CourseService

app = FastAPI()

class CourseAssignment(BaseModel):
    student_id: int
    course_ids: list[int]

class CourseRemoval(BaseModel):
    student_id: int
    course_id: int

@app.post("/students/{student_id}/courses")
async def assign_courses(student_id: int, course_assignment: CourseAssignment):
    """Assign courses to a student."""
    try:
        student = await StudentService.assign_courses(student_id, course_assignment.course_ids)
        return student
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.get("/students/{student_id}")
async def get_student(student_id: int):
    """Retrieve a student's details along with their associated courses."""
    student = await StudentService.get_student_with_courses(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.delete("/students/{student_id}/courses")
async def remove_course(student_id: int, course_removal: CourseRemoval):
    """Remove a course from a student's list."""
    try:
        student = await StudentService.remove_course(student_id, course_removal.course_id)
        return student
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

# Additional application logic and route definitions...
```
