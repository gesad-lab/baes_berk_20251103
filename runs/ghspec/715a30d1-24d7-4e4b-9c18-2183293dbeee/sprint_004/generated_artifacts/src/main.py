```python
from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
from models import Student, Course  # Assuming Student and Course models are defined
from pydantic import BaseModel
from typing import List
from database import get_db  # Assuming there's a database connection utility

app = FastAPI()

class StudentEnrollmentRequest(BaseModel):
    student_id: int
    course_ids: List[int]

class StudentEnrollmentResponse(BaseModel):
    student_id: int
    enrolled_courses: List[int]

class StudentResponse(BaseModel):
    id: int
    name: str
    enrolled_courses: List[Course]  # Assuming Course is defined with appropriate fields

@app.post("/students/enroll", response_model=StudentEnrollmentResponse)
def enroll_student(enrollment: StudentEnrollmentRequest, db: Session = next(get_db())):
    """
    Enroll a student in one or more courses.
    
    Parameters:
    - enrollment (StudentEnrollmentRequest): The enrollment data containing student ID and course IDs.
    
    Returns:
    - StudentEnrollmentResponse: The updated student information with enrolled courses.
    
    Raises:
    - HTTPException: If the student or any course is not found.
    """
    # Validate the student exists
    student = db.query(Student).filter(Student.id == enrollment.student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    # Validate courses exist and enroll student
    courses = []
    for course_id in enrollment.course_ids:
        course = db.query(Course).filter(Course.id == course_id).first()
        if not course:
            raise HTTPException(status_code=404, detail=f"Course with ID {course_id} not found")
        courses.append(course)

    # Associate courses with the student
    student.courses.extend(courses)
    db.commit()

    return StudentEnrollmentResponse(student_id=student.id, enrolled_courses=[course.id for course in courses])

@app.get("/students/{id}", response_model=StudentResponse)
def get_student(id: int, db: Session = next(get_db())):
    """
    Retrieve student information along with their enrolled courses.
    
    Parameters:
    - id (int): The ID of the student to retrieve.
    
    Returns:
    - StudentResponse: The student details including enrolled courses.
    
    Raises:
    - HTTPException: If the student is not found.
    """
    student = db.query(Student).filter(Student.id == id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    return StudentResponse(id=student.id, name=student.name, enrolled_courses=student.courses)  # Assuming courses are linked appropriately
```