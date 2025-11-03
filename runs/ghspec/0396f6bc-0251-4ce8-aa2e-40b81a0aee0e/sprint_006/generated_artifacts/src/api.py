```python
from fastapi import FastAPI, HTTPException, Path
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field
from typing import Optional
from models import Course, Teacher
from database import get_db  # Assuming you have a database.py for session management

app = FastAPI()

class TeacherAssignment(BaseModel):
    teacher_id: int = Field(..., description="ID of the teacher to be assigned")
    course_id: int = Field(..., description="ID of the course to be assigned a teacher")

class CourseDetail(BaseModel):
    course_id: int
    teacher_id: Optional[int]
    teacher_name: Optional[str]

@app.patch("/courses/{course_id}/assign_teacher", response_model=CourseDetail)
def assign_teacher(course_id: int, assignment: TeacherAssignment, db: Session = next(get_db())):
    """
    Assign a teacher to a specified course.

    :param course_id: ID of the course to which the teacher will be assigned
    :param assignment: Contains teacher_id and course_id
    :param db: Database session
    :return: Updated course details with the assigned teacher
    """
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    teacher = db.query(Teacher).filter(Teacher.id == assignment.teacher_id).first()
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")

    # Assign the teacher to the course
    course.teacher_id = assignment.teacher_id
    db.commit()
    
    # Prepare response model
    response = CourseDetail(course_id=course.id, teacher_id=course.teacher_id, teacher_name=teacher.name)
    return response

@app.get("/courses/{course_id}", response_model=CourseDetail)
def get_course_details(course_id: int, db: Session = next(get_db())):
    """
    Retrieve course details along with the assigned teacher.

    :param course_id: ID of the course
    :param db: Database session
    :return: Course details with assigned teacher information
    """
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    
    teacher = db.query(Teacher).filter(Teacher.id == course.teacher_id).first() if course.teacher_id else None
    teacher_name = teacher.name if teacher else None

    response = CourseDetail(course_id=course.id, teacher_id=course.teacher_id, teacher_name=teacher_name)
    return response
```