```python
from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel
from sqlalchemy.orm import Session
from models import Course, Teacher  # Assuming these are defined in models.py
from database import get_db  # Assuming a database utility for session handling

app = FastAPI()

class TeacherAssignment(BaseModel):
    teacher_id: int

@app.patch("/courses/{course_id}/assign-teacher")
def assign_teacher(course_id: int, assignment: TeacherAssignment, db: Session = next(get_db())):
    """Assign a teacher to a course by course_id."""
    # Validate if the teacher_id exists in the Teacher table
    teacher = db.query(Teacher).filter(Teacher.id == assignment.teacher_id).first()
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found: Invalid teacher_id provided.")

    # Update the course with the teacher_id
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found: Invalid course_id provided.")

    course.teacher_id = assignment.teacher_id
    db.commit()
    return {"message": "Teacher assigned successfully to the course."}

@app.get("/courses/{course_id}")
def get_course(course_id: int, db: Session = next(get_db())):
    """Retrieve details of a specific course including assigned teacher."""
    course = db.query(Course).filter(Course.id == course_id).first()
    
    if not course:
        raise HTTPException(status_code=404, detail="Course not found: Invalid course_id provided.")
    
    return {
        "course_id": course.id,
        "course_name": course.name,
        "teacher_id": course.teacher_id
    }
```