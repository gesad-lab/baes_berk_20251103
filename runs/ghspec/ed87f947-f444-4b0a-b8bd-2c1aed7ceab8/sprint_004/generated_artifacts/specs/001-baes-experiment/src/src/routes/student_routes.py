```python
# src/routes/student_routes.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.models import Student, Course, StudentCourse
from src.schemas import StudentCourseCreate, StudentCoursesResponse

router = APIRouter()

@router.post("/students/{student_id}/courses", response_model=StudentCoursesResponse)
def enroll_student_in_course(student_id: int, course_data: StudentCourseCreate, db: Session = Depends(get_db)):
    """Enroll a student in a course."""
    # Validate student existence
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail=f"Student with ID {student_id} not found.")

    # Validate course existence
    course = db.query(Course).filter(Course.id == course_data.course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail=f"Course with ID {course_data.course_id} not found.")

    # Check if the student is already enrolled in the course
    if db.query(StudentCourse).filter(
        StudentCourse.student_id == student_id,
        StudentCourse.course_id == course_data.course_id
    ).first():
        raise HTTPException(status_code=400, detail="Student is already enrolled in this course.")

    # Enroll student in the course
    new_enrollment = StudentCourse(student_id=student_id, course_id=course_data.course_id)
    db.add(new_enrollment)
    db.commit()
    db.refresh(new_enrollment)

    return {"student_id": student_id, "course_id": new_enrollment.course_id, "message": "Enrollment successful."}

@router.get("/students/{student_id}/courses", response_model=list[StudentCoursesResponse])
def get_student_courses(student_id: int, db: Session = Depends(get_db)):
    """Retrieve all courses for a specific student."""
    # Validate student existence
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail=f"Student with ID {student_id} not found.")

    # Retrieve courses associated with the student
    courses = db.query(Course).join(StudentCourse).filter(StudentCourse.student_id == student_id).all()
    return [{"course_id": course.id, "course_name": course.name} for course in courses]

@router.delete("/students/{student_id}/courses/{course_id}", response_model=dict)
def remove_student_from_course(student_id: int, course_id: int, db: Session = Depends(get_db)):
    """Remove a student from a course."""
    # Validate student existence
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail=f"Student with ID {student_id} not found.")

    # Validate course existence
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail=f"Course with ID {course_id} not found.")

    # Validate enrollment existence
    enrollment = db.query(StudentCourse).filter(
        StudentCourse.student_id == student_id,
        StudentCourse.course_id == course_id
    ).first()
    if not enrollment:
        raise HTTPException(status_code=404, detail="Enrollment not found.")

    # Remove enrollment
    db.delete(enrollment)
    db.commit()

    return {"message": "Student successfully removed from the course."}
```