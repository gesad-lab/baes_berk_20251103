```python
# src/api/student.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from db.database import SessionLocal
from models.student_courses import StudentCourse
from models.student import Student
from models.course import Course

router = APIRouter()

class Enrollment(BaseModel):
    course_id: str

@router.post("/students/{student_id}/courses")
def enroll_student(student_id: str, enrollment: Enrollment):
    """Enroll a student in a course."""
    db = SessionLocal()
    
    try:
        # Validate student and course existence
        student = db.query(Student).filter(Student.id == student_id).first()
        course = db.query(Course).filter(Course.id == enrollment.course_id).first()

        if not student or not course:
            raise HTTPException(status_code=400, detail={"error": {"code": "E002", "message": "Invalid student ID or course ID"}})

        # Create enrollment record
        new_enrollment = StudentCourse(student_id=student_id, course_id=enrollment.course_id)

        db.add(new_enrollment)
        db.commit()

        return {"message": "Student enrolled successfully", "studentId": student_id, "courseId": enrollment.course_id}
    
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail={"error": {"code": "E500", "message": "An error occurred during enrollment."}})
    
    finally:
        db.close()

@router.get("/students/{student_id}/courses")
def get_student_courses(student_id: str):
    """Retrieve all courses a student is enrolled in."""
    db = SessionLocal()
    
    try:
        student = db.query(Student).filter(Student.id == student_id).first()

        if not student:
            raise HTTPException(status_code=404, detail={"error": {"code": "E001", "message": "Student not found"}})

        # Fetch courses for the student
        courses = db.query(Course).join(StudentCourse).filter(StudentCourse.student_id == student_id).all()

        # Format course response
        course_list = [{"name": course.name, "level": course.level} for course in courses]

        return {"courses": course_list}

    except Exception as e:
        raise HTTPException(status_code=500, detail={"error": {"code": "E500", "message": "An error occurred while retrieving courses."}})
    
    finally:
        db.close()
```