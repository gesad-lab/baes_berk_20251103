```python
from fastapi import FastAPI, HTTPException, Path, Body
from sqlalchemy.orm import Session
from myapp.database import get_session
from myapp.models import Student, Course, StudentCourses

app = FastAPI()

@app.post("/students/{student_id}/enroll")
def enroll_student(student_id: int = Path(..., title="The ID of the student to enroll"),
                   course_id: int = Body(..., title="The ID of the course to enroll the student in"),
                   db: Session = get_session()):
    """
    Enroll a student in a course.

    Args:
        student_id (int): The ID of the student.
        course_id (int): The ID of the course.

    Returns:
        JSON response with success message and HTTP status 201 if enrollment is successful.

    Raises:
        HTTPException: If the student or course does not exist.
    """
    # Check if the student exists
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    # Check if the course exists
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    # Perform enrollment
    enrollment = StudentCourses(student_id=student_id, course_id=course_id)
    db.add(enrollment)
    db.commit()
    db.refresh(enrollment)

    return {"message": "Enrollment successful"}, 201

@app.get("/students/{student_id}/courses")
def get_student_courses(student_id: int = Path(..., title="The ID of the student to retrieve courses for"),
                        db: Session = get_session()):
    """
    Retrieve a list of courses for a specific student.

    Args:
        student_id (int): The ID of the student.

    Returns:
        JSON response with a list of courses if the student exists, otherwise HTTP 404.
    """
    # Check if the student exists
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    # Retrieve courses associated with the student
    courses = db.query(Course).join(StudentCourses).filter(StudentCourses.student_id == student_id).all()
    return {"courses": courses}  # Returning a list of courses
```