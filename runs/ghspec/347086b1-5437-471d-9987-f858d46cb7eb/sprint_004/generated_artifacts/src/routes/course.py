```python
# src/routes/course.py

from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from models.student import Student  # Import Student model
from models.course import Course  # Import Course model
from database import get_db  # Import database session
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()

# Documentation for the new API endpoints

"""
API Endpoints for Course Management

## Endpoints

### Associate a Student with a Course
**POST** `/students/{student_id}/courses`

- Associate a student with a specific course. 
- This endpoint requires that the student already exists in the system and the course is valid.

#### Request Body
- `course_id`: The ID of the course to associate with the student.

#### Responses
- **201 Created:** If the association is successful.
  - Example:
    ```json
    {
      "message": "Course associated successfully"
    }
    ```
- **404 Not Found:** If the student or course does not exist.
  - Example:
    ```json
    {
      "error": {
        "code": "E404",
        "message": "Student or course not found"
      }
    }
    ```

### Retrieve Courses for a Student
**GET** `/students/{student_id}/courses`

- Retrieve a list of courses associated with a specific student.

#### Responses
- **200 OK:** Returns a list of courses.
  - Example:
    ```json
    [
      {
        "id": 1,
        "name": "Introduction to Programming",
        "level": "Beginner"
      },
      {
        "id": 2,
        "name": "Data Structures",
        "level": "Intermediate"
      }
    ]
    ```
- **404 Not Found:** If the student does not exist.
  - Example:
    ```json
    {
      "error": {
        "code": "E404",
        "message": "Student not found"
      }
    }
    ```

### Handle When No Course is Associated with a Student
**GET** `/students/{student_id}/courses`

- If a student has no associated courses, the API will return an empty array.

#### Responses
- **200 OK:** Indicates no courses are associated.
  - Example:
    ```json
    []
    ```

### Retain Existing Student Data
- Ensure that the migration and relationship setup does not affect existing student data.
"""

# Define Pydantic models for input validation
class CourseAssociation(BaseModel):
    course_id: int

@router.post("/students/{student_id}/courses")
def associate_student_with_course(student_id: int, association: CourseAssociation, db: Session = next(get_db())):
    """Associate a student with a course."""
    student = db.query(Student).filter(Student.id == student_id).first()
    course = db.query(Course).filter(Course.id == association.course_id).first()
    
    if not student or not course:
        raise HTTPException(status_code=404, detail="Student or course not found")
    
    student.courses.append(course)
    db.commit()
    return {"message": "Course associated successfully"}

@router.get("/students/{student_id}/courses", response_model=List[Course])
def get_student_courses(student_id: int, db: Session = next(get_db())):
    """Retrieve courses for a given student."""
    student = db.query(Student).filter(Student.id == student_id).first()
    
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    return student.courses
```