```python
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from models import Course, Teacher  # Assuming these models exist and are imported correctly
from database import SessionLocal, engine  # Assuming SessionLocal is a callable that returns a database session
from pydantic import BaseModel

app = FastAPI()

# Dependency for getting the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Request model for assigning a teacher
class AssignTeacherRequest(BaseModel):
    teacher_id: str

@app.post("/courses/{course_id}/assign-teacher")
def assign_teacher_to_course(course_id: int, request: AssignTeacherRequest, db: Session = Depends(get_db)):
    # Fetch the course by its ID
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    
    # Assign the teacher to the course
    course.teacher_id = request.teacher_id
    db.commit()
    
    return {"message": "Teacher assigned to course successfully", "course_id": course_id}

@app.get("/courses/{course_id}")
def get_course_details(course_id: int, db: Session = Depends(get_db)):
    # Fetch the course by its ID
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    
    # Prepare course details along with teacher info
    teacher = db.query(Teacher).filter(Teacher.id == course.teacher_id).first() if course.teacher_id else None
    course_details = {
        "id": course.id,
        "title": course.title,
        "teacher": {
            "id": teacher.id if teacher else None,
            "name": teacher.name if teacher else None,
            "email": teacher.email if teacher else None,
        } if teacher else None
    }
    
    return course_details
```