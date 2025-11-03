```python
from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel
from src.repositories.course_repository import CourseRepository
from src.repositories.teacher_repository import TeacherRepository
from src.models.course import Course
from src.models.teacher import Teacher

app = FastAPI()

class AssignTeacherRequest(BaseModel):
    teacher_id: int

class CourseResponse(BaseModel):
    id: int
    name: str
    description: str
    teacher_id: int
    teacher: Teacher

@app.post("/api/v1/courses/{course_id}/assign_teacher")
async def assign_teacher_to_course(course_id: int, request: AssignTeacherRequest):
    """
    Assign a Teacher to a Course by Course ID.
    
    - **course_id**: The ID of the course to which the teacher is to be assigned.
    - **request**: Body containing the teacher ID.
    """
    # Validate if the Course exists
    course = await CourseRepository.get_course_by_id(course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    # Validate if the Teacher exists
    teacher = await TeacherRepository.get_teacher_by_id(request.teacher_id)
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")

    # Assign the teacher to the course
    course.teacher_id = request.teacher_id
    await CourseRepository.update_course(course)

    return {"message": "Teacher assigned successfully", "course_id": course_id, "teacher_id": request.teacher_id}

@app.get("/api/v1/courses/{course_id}", response_model=CourseResponse)
async def get_course_with_teacher(course_id: int):
    """
    Retrieve Course details including the assigned Teacher's information by Course ID.
    
    - **course_id**: The ID of the course to fetch.
    """
    course = await CourseRepository.get_course_with_teacher(course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    
    return course
```