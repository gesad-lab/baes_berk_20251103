```python
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..models.course import Course
from ..models.teacher import Teacher
from ..database import get_db
from pydantic import BaseModel

router = APIRouter()

class TeacherAssignment(BaseModel):
    teacherId: int

@router.post("/courses/{course_id}/assign-teacher", status_code=200)
async def assign_teacher(course_id: int, assignment: TeacherAssignment, db: Session = Depends(get_db)):
    # Check if the course exists
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found.")
    
    # Check if the teacher exists
    teacher = db.query(Teacher).filter(Teacher.id == assignment.teacherId).first()
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found.")
    
    # Assign the teacher to the course
    course.teacher_id = assignment.teacherId
    db.commit()
    
    # Return a confirmation message
    return {"message": "Teacher assigned successfully.", "courseId": course_id, "teacherId": assignment.teacherId}

class CourseResponse(BaseModel):
    id: int
    title: str
    description: str
    teacher_name: str = None
    teacher_email: str = None

@router.get("/courses/{course_id}", response_model=CourseResponse)
async def get_course(course_id: int, db: Session = Depends(get_db)):
    # Retrieve the course with associated teacher details
    course = db.query(Course).filter(Course.id == course_id).first()
    
    if not course:
        raise HTTPException(status_code=404, detail="Course not found.")
    
    # Prepare the response data
    teacher = db.query(Teacher).filter(Teacher.id == course.teacher_id).first()
    
    return CourseResponse(
        id=course.id,
        title=course.title,
        description=course.description,
        teacher_name=teacher.name if teacher else None,
        teacher_email=teacher.email if teacher else None
    )
```