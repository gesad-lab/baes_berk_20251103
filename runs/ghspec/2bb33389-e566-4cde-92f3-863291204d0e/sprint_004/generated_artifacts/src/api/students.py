```python
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.models import Student, Course, StudentCourses  # Ensure the join table is imported
from typing import List

router = APIRouter()

@router.get("/students/{student_id}/courses", response_model=List[Course])
async def get_student_courses(student_id: int, db: Session = Depends(get_db)):
    db_student = db.query(Student).filter(Student.id == student_id).first()
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    # Retrieve the courses associated with the student through the join table
    courses = db.query(Course).join(StudentCourses).filter(StudentCourses.student_id == student_id).all()
    return courses
```