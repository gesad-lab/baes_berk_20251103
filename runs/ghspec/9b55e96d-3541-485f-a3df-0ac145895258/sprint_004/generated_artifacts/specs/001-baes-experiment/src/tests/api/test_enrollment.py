```python
from fastapi import APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from models import Student, Course, Enrollment
from database import get_db

router = APIRouter()

@router.post("/students/{student_id}/enroll", response_model=dict)
async def enroll_student(student_id: int, course_id: int, db: Session = Depends(get_db)):
    # Check if the student exists
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")

    # Check if the course exists
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")

    # Enroll the student in the course
    enrollment = Enrollment(student_id=student_id, course_id=course_id)
    db.add(enrollment)
    db.commit()

    return {"message": "Student enrolled in course successfully"}
```