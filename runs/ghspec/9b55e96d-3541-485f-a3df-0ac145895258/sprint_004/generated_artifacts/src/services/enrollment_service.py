from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models import Student, Course, Enrollment
from database import get_db

router = APIRouter()

@router.post("/students/{student_id}/enroll")
def enroll_student(student_id: int, course_id: int, db: Session = Depends(get_db)):
    # Check if the student exists
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    # Check if the course exists
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    # Create a new enrollment record
    enrollment = Enrollment(student_id=student_id, course_id=course_id)
    db.add(enrollment)
    db.commit()
    db.refresh(enrollment)

    return {"message": "Student enrolled in course successfully"}

@router.get("/students/{student_id}/courses")
def get_student_courses(student_id: int, db: Session = Depends(get_db)):
    # Check if the student exists
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    # Retrieve courses the student is enrolled in
    courses = db.query(Course).join(Enrollment).filter(Enrollment.student_id == student_id).all()
    
    return [{"id": course.id, "name": course.name} for course in courses]

@router.delete("/students/{student_id}/courses/{course_id}")
def remove_student_from_course(student_id: int, course_id: int, db: Session = Depends(get_db)):
    # Check if the student exists
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    # Check if the course exists
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    # Find the enrollment record to delete
    enrollment = db.query(Enrollment).filter(Enrollment.student_id == student_id, Enrollment.course_id == course_id).first()
    if not enrollment:
        raise HTTPException(status_code=404, detail="Enrollment record not found")

    db.delete(enrollment)
    db.commit()

    return {"message": "Student removed from course successfully"}