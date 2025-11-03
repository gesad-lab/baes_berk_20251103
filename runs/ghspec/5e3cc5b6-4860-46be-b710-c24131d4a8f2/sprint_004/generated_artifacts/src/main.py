```python
from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel
from src.models.student import Student
from src.models.course import Course
from src.models.student_course import StudentCourse
from src.database.database import get_db
from sqlalchemy.orm import Session

app = FastAPI()

# Pydantic models for Course association
class CourseAssociation(BaseModel):
    course_ids: list[int]

@app.post("/students/{id}/courses", response_model=Student)
def associate_courses(id: int, course_association: CourseAssociation, db: Session = next(get_db())):
    """
    Associate a list of courses with a specific student.

    Args:
        id (int): The Student ID to associate courses with.
        course_association (CourseAssociation): A list of Course IDs to be associated.
        db (Session): Database session used for querying.
    
    Returns:
        Student: The updated Student details including the assigned Courses.
    
    Raises:
        HTTPException: If the provided course IDs do not exist.
    """
    student = db.query(Student).filter(Student.id == id).first()
    
    if not student:
        raise HTTPException(status_code=404, detail="Student not found.")
    
    # Validate course IDs
    valid_courses = db.query(Course).filter(Course.id.in_(course_association.course_ids)).all()
    if len(valid_courses) != len(course_association.course_ids):
        raise HTTPException(status_code=400, detail="One or more invalid Course IDs.")

    # Establish relationships
    for course in valid_courses:
        student_course = StudentCourse(student_id=student.id, course_id=course.id)
        db.add(student_course)

    db.commit()
    
    # Return the updated Student object including associated courses
    return db.query(Student).filter(Student.id == id).first()

@app.get("/students/{id}/courses", response_model=Student)
def get_student_courses(id: int, db: Session = next(get_db())):
    """
    Retrieve detailed information of a student, including their associated courses.

    Args:
        id (int): The Student ID to retrieve details for.
        db (Session): Database session used for querying.
    
    Returns:
        Student: The Student details including a list of associated Course IDs.
    
    Raises:
        HTTPException: If the student is not found.
    """
    student = db.query(Student).filter(Student.id == id).first()
    
    if not student:
        raise HTTPException(status_code=404, detail="Student not found.")
    
    return student
```