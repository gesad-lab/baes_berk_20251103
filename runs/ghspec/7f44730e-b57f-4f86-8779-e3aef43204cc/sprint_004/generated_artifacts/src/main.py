```python
# src/main.py
from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
from models.student import Student
from models.course import Course  # Assuming Course model is defined similarly to Student
from models.student_courses import StudentCourse
from database import get_db  # Assuming this function provides a database session

app = FastAPI()

@app.post("/students/{student_id}/courses")
def enroll_student_in_course(student_id: str, course_id: str, db: Session = Depends(get_db)):
    # Validate student existence
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail={"error": {"code": "E001", "message": "Student not found"}})

    # Validate course existence
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail={"error": {"code": "E002", "message": "Course not found"}})

    # Check if the enrollment already exists
    existing_enrollment = db.query(StudentCourse).filter(
        StudentCourse.student_id == student_id,
        StudentCourse.course_id == course_id
    ).first()
    if existing_enrollment:
        raise HTTPException(status_code=400, detail={"error": {"code": "E003", "message": "Student is already enrolled in this course"}})

    # Enroll student in course
    enrollment = StudentCourse(student_id=student_id, course_id=course_id)
    db.add(enrollment)
    db.commit()

    return {"message": "Student enrolled successfully", "studentId": student_id, "courseId": course_id}

@app.get("/students/{student_id}/courses")
def get_student_courses(student_id: str, db: Session = Depends(get_db)):
    # Validate student existence
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail={"error": {"code": "E001", "message": "Student not found"}})

    # Retrieve courses for the student
    courses = db.query(Course).join(StudentCourse).filter(StudentCourse.student_id == student_id).all()
    
    course_list = [{"name": course.name, "level": course.level} for course in courses]

    return {"courses": course_list}
```