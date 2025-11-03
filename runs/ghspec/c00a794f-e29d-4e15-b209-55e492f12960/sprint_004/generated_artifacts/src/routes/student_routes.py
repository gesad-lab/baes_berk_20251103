from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.models import Student, Course, StudentCourse

router = APIRouter()

@router.post("/students/{student_id}/courses/{course_id}", response_model=Student)
async def associate_student_with_course(student_id: int, course_id: int, db: Session = Depends(get_db)):
    # Attempt to retrieve the student
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    # Attempt to retrieve the course
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        # If the course does not exist, raise an exception with a clear error message
        raise HTTPException(status_code=404, detail={"error": {"code": "E001", "message": "Course does not exist"}})

    # Associate the student with the course if both exist
    student_course_association = StudentCourse(student_id=student.id, course_id=course.id)
    db.add(student_course_association)
    db.commit()
    db.refresh(student)

    # Return the updated student record
    return student

@router.get("/students/{student_id}", response_model=Student)
async def get_student_with_courses(student_id: int, db: Session = Depends(get_db)):
    # Retrieve the student along with associated courses
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    # Here you could include a mechanism to return the associated courses as well,
    # e.g., using a join to fetch courses related to the student.

    return student