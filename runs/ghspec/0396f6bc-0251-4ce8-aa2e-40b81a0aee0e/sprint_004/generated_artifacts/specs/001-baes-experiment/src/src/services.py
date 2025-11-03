```python
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, constr
from sqlalchemy.orm import Session
from models import Student, Course, StudentCourse  # Import StudentCourse for the relationship
from database import get_db  # Assuming there's a function to get the database session

router = APIRouter()

class EnrollRequest(BaseModel):
    course_id: int  # Ensure course_id is required and of type integer

@router.post("/students/{student_id}/enroll")
async def enroll_student(student_id: int, enroll_request: EnrollRequest, db: Session = Depends(get_db)):
    # Validate that the student exists
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail={"error": {"code": "E404", "message": "Student not found."}})

    # Validate that the course exists
    course = db.query(Course).filter(Course.id == enroll_request.course_id).first()
    if not course:
        raise HTTPException(status_code=400, detail={"error": {"code": "E400", "message": "Invalid course ID."}})

    # Enroll the student in the course by creating a new StudentCourse entry
    student_course = StudentCourse(student_id=student_id, course_id=enroll_request.course_id)
    db.add(student_course)
    db.commit()
    db.refresh(student_course)

    return {"message": "Student enrolled successfully in the course."}
```