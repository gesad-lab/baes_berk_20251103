```python
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models import Student, Course, Enrollment
from database import get_db
from services.enrollment_service import enroll_student_in_course, get_student_courses

router = APIRouter()

@router.post("/enroll")
async def enroll_student(student_id: int, course_id: int, db: Session = Depends(get_db)):
    """
    Enroll a student in a course.

    - **student_id**: ID of the student to enroll.
    - **course_id**: ID of the course to enroll the student in.
    """
    try:
        enrollment = enroll_student_in_course(db, student_id, course_id)
        if enrollment:
            return {"message": f"Student {student_id} enrolled in course {course_id}."}
        else:
            raise HTTPException(status_code=400, detail="Enrollment failed. Check if the course exists.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

@router.get("/students/{student_id}/courses")
async def get_courses_for_student(student_id: int, db: Session = Depends(get_db)):
    """
    Retrieve courses for a specific student.

    - **student_id**: ID of the student whose courses are being retrieved.
    """
    try:
        courses = get_student_courses(db, student_id)
        if courses:
            return {"student_id": student_id, "courses": courses}
        else:
            raise HTTPException(status_code=404, detail="No courses found for this student.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
```