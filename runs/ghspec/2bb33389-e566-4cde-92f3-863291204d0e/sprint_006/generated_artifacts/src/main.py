```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from src.models import Course, Teacher  # Assuming Teacher model is defined in src/models.py
from src.database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends

app = FastAPI()

# Pydantic models for request and response
class TeacherAssignment(BaseModel):
    teacher_id: int
    course_id: int

class CourseResponse(BaseModel):
    id: int
    name: str
    teacher_id: Optional[int] = None
    teacher_name: Optional[str] = None

@app.post("/assign_teacher", response_description="Assign a Teacher to a Course")
async def assign_teacher(assignment: TeacherAssignment, db: Session = Depends(get_db)):
    """
    Assign a teacher to a specific course by providing the course ID and teacher ID.

    Parameters:
    - assignment: TeacherAssignment - Contains teacher_id and course_id

    Returns:
    - JSON confirmation response on success
    - JSON error response if course or teacher does not exist
    """

    # Check if course exists
    course = db.query(Course).filter(Course.id == assignment.course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail={"error": {"code": "E001", "message": "Course not found"}})

    # Check if teacher exists
    teacher = db.query(Teacher).filter(Teacher.id == assignment.teacher_id).first()
    if not teacher:
        raise HTTPException(status_code=404, detail={"error": {"code": "E002", "message": "Teacher not found"}})

    # Assign teacher to course and commit to database
    course.teacher_id = assignment.teacher_id
    db.commit()
    return {"message": "Teacher assigned to course successfully."}

@app.get("/courses/{course_id}", response_model=CourseResponse, response_description="Retrieve course with assigned teacher")
async def get_course(course_id: int, db: Session = Depends(get_db)):
    """
    Retrieve the details of a course including its assigned teacher.

    Parameters:
    - course_id: int - The ID of the course to retrieve

    Returns:
    - JSON response with course details and assigned teacher information
    """
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail={"error": {"code": "E001", "message": "Course not found"}})

    return CourseResponse(
        id=course.id,
        name=course.name,
        teacher_id=course.teacher_id,
        teacher_name=course.teacher.name if course.teacher else None
    )
```