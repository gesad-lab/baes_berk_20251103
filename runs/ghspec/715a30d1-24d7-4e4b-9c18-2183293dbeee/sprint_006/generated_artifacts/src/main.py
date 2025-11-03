```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import Optional

from database import get_db
from models import Course, Teacher  # Ensure Teacher model is available
from repository import assign_teacher_to_course, get_course_details

app = FastAPI()

# API request model for assigning a teacher to a course
class TeacherCourseAssignmentRequest(BaseModel):
    course_id: int
    teacher_id: int

# API response model for course details including teacher
class CourseDetailsResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    teacher: Optional[Teacher]  # Reference to Teacher model

@app.post("/courses/assign-teacher", response_model=CourseDetailsResponse)
def assign_teacher(assignment: TeacherCourseAssignmentRequest, db: Session = next(get_db())):
    """
    Assign a teacher to a course by updating the course's teacher_id.
    
    :param assignment: Details of the teacher and course assignment
    :param db: Database session
    :return: Updated course details with teacher information
    :raises HTTPException: If the teacher ID or course ID is invalid
    """
    course = assign_teacher_to_course(db, assignment.course_id, assignment.teacher_id)
    return course

@app.get("/courses/{id}", response_model=CourseDetailsResponse)
def get_course(id: int, db: Session = next(get_db())):
    """
    Retrieve detailed information about a specific course, 
    including the assigned teacher if available.
    
    :param id: The ID of the course to fetch
    :param db: Database session
    :return: Course details along with teacher information
    :raises HTTPException: If the course ID does not exist
    """
    course = get_course_details(db, id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course
```