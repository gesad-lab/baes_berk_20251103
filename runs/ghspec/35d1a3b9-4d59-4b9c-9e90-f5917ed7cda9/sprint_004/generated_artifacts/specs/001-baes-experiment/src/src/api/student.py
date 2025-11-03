```python
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from src.repository import Student, Course, StudentCourse, get_db
from sqlalchemy.orm import Session

router = APIRouter()

class EnrollmentRequest(BaseModel):
    student_id: int
    course_ids: list[int]

@router.post("/enroll", status_code=201)
async def enroll_student(enrollment: EnrollmentRequest, db: Session = Depends(get_db)):
    # Check if the student exists
    student = db.query(Student).filter(Student.id == enrollment.student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    # Enroll student in courses without duplicating enrollments
    for course_id in enrollment.course_ids:
        course = db.query(Course).filter(Course.id == course_id).first()
        if not course:
            continue  # Skip non-existent courses

        existing_enrollment = db.query(StudentCourse).filter(
            StudentCourse.student_id == enrollment.student_id,
            StudentCourse.course_id == course_id
        ).first()
        if not existing_enrollment:
            # Create a new enrollment record
            new_enrollment = StudentCourse(student_id=enrollment.student_id, course_id=course_id)
            db.add(new_enrollment)
    
    db.commit()  # Commit the transaction to save changes
    return {"message": "Student enrolled successfully"}

@router.get("/students/{student_id}/courses", response_model=list[Course])
async def get_student_courses(student_id: int, db: Session = Depends(get_db)):
    # Retrieve courses for the given student ID
    courses = db.query(Course).join(StudentCourse).filter(StudentCourse.student_id == student_id).all()
    return courses
```