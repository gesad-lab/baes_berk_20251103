```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.repositories.course_repository import CourseRepository
from src.repositories.teacher_repository import TeacherRepository

app = FastAPI()
course_repository = CourseRepository()
teacher_repository = TeacherRepository()

class AssignTeacherRequest(BaseModel):
    course_id: int
    teacher_id: int

class CourseDetailsResponse(BaseModel):
    id: int
    name: str
    teacher: dict

@app.post("/api/v1/courses/assign-teacher")
async def assign_teacher_to_course(assign_teacher_request: AssignTeacherRequest):
    # Validate that the Course and Teacher exist
    if not course_repository.exists(assign_teacher_request.course_id):
        raise HTTPException(status_code=404, detail=f"Course ID {assign_teacher_request.course_id} does not exist.")
    if not teacher_repository.exists(assign_teacher_request.teacher_id):
        raise HTTPException(status_code=404, detail=f"Teacher ID {assign_teacher_request.teacher_id} does not exist.")
    
    # Assign the Teacher to the Course
    course_repository.assign_teacher(assign_teacher_request.course_id, assign_teacher_request.teacher_id)
    return {"message": "Teacher assigned successfully."}

@app.get("/api/v1/courses/{course_id}", response_model=CourseDetailsResponse)
async def get_course_details(course_id: int):
    course = course_repository.get_course_with_teacher(course_id)
    
    if not course:
        raise HTTPException(status_code=404, detail="Course not found.")
    
    return CourseDetailsResponse(id=course.id, name=course.name, teacher=course.teacher)
```