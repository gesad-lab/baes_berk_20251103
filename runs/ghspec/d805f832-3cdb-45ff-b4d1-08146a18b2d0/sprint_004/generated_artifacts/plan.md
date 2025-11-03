# Implementation Plan: Add Course Relationship to Student Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Course Entity

---

## Version
**Version**: 1.0.0  

## Purpose
This implementation plan details the enhancements to the Student Management Web Application, focusing on establishing a many-to-many relationship between `Student` and `Course` entities. By implementing this feature, the system will improve its ability to manage student course enrollments, enabling better tracking of academic progress and facilitating enhanced reporting and analytics.

## Architecture Overview
The application architecture follows a microservices pattern using FastAPI and SQLAlchemy, where the functionality for managing student-course relationships will be integrated into the existing API and database schema without disrupting current operations.

## Technology Stack
- **Programming Language**: Python 3.11+
- **Web Framework**: FastAPI
- **ORM**: SQLAlchemy
- **Database**: SQLite
- **API Testing Tool**: Postman / cURL

## Module Boundaries and Responsibilities
1. **API Layer**:
   - New Endpoints:
     - `POST /students/{student_id}/courses`: Associate a Course with a Student.
     - `GET /students/{student_id}/courses`: Retrieve all courses associated with a Student.

2. **Business Logic Layer**:
   - Implement validation checks for course existence before associations.
   - Handle CRUD operations related to course associations using the new `student_courses` junction table.

3. **Data Access Layer**:
   - Update existing models for `Student` and introduce a junction table model for `student_courses`.

## Data Models
### Junction Table Model
Definition of the new `student_courses` junction table to establish relationships between students and courses:
```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models import Base

class StudentCourse(Base):
    __tablename__ = 'student_courses'
    
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    student = relationship('Student', back_populates='courses')
    course = relationship('Course', back_populates='students')
```

### Modifications to Existing Models
- Ensure *Student* and *Course* models have relationships defined to allow bi-directional access:
```python
class Student(Base):
    # Existing attributes...

    courses = relationship('StudentCourse', back_populates='student')

class Course(Base):
    # Existing attributes...

    students = relationship('StudentCourse', back_populates='course')
```

## API Contracts
### 1. Associate a Course with a Student
- **Endpoint**: `POST /students/{student_id}/courses`
- **Request Body**:
  ```json
  {
    "course_id": 1
  }
  ```
- **Response**:
  - **Success (201)**:
    ```json
    {
      "message": "Course associated successfully.",
      "courses": [
        {
          "course_id": 1,
          "name": "Math 101"
        },
        {
          "course_id": 2,
          "name": "Science 101"
        }
      ]
    }
    ```
  - **Error (404)**:
    For non-existing course:
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Course not found."
      }
    }
    ```
  
### 2. Retrieve All Courses for a Student
- **Endpoint**: `GET /students/{student_id}/courses`
- **Response**:
  - **Success (200)**:
    ```json
    {
      "courses": [
        {
          "course_id": 1,
          "name": "Math 101"
        },
        {
          "course_id": 2,
          "name": "Science 101"
        }
      ]
    }
    ```

## Implementation Approach
1. **Environment Setup**:
   - Ensure Python 3.11+ is installed.
   - Create a virtual environment if not already done.
   - Install necessary dependencies:
     ```bash
     pip install fastapi[all] sqlalchemy
     ```

2. **Database Migration**:
   - Create a migration script to add the `student_courses` table to maintain relationships while ensuring existing student and course data is intact:
   ```python
   from sqlalchemy import create_engine
   from sqlalchemy.orm import sessionmaker
   from models import Base, StudentCourse

   engine = create_engine('sqlite:///./database.db')
   Base.metadata.create_all(engine)  # This includes running migrations for any new models.
   ```

3. **Endpoint Implementation**:
   - Modify the `api/students.py` file to add functionality for associating courses with students:
   ```python
   from fastapi import APIRouter, Depends, HTTPException
   from sqlalchemy.orm import Session
   from models import StudentCourse, Course, Student  # Include necessary models
   from database import get_db  # Dependency for DB session
   from pydantic import BaseModel

   class CourseAssociationModel(BaseModel):
       course_id: int

   router = APIRouter()

   @router.post("/students/{student_id}/courses")
   async def associate_course(student_id: int, course: CourseAssociationModel, db: Session = Depends(get_db)):
       # Verify if course exists
       existing_course = db.query(Course).filter(Course.id == course.course_id).first()
       if not existing_course:
           raise HTTPException(status_code=404, detail="Course not found.")
       
       # Create association
       student_course = StudentCourse(student_id=student_id, course_id=course.course_id)
       db.add(student_course)
       db.commit()
       db.refresh(student_course)

       # Retrieve updated list of courses for the student
       student_courses = db.query(StudentCourse).filter(StudentCourse.student_id == student_id).all()
       return {"message": "Course associated successfully.", "courses": student_courses}
   ```

4. **Testing**:
   - Create tests in `tests/test_student_courses.py`:
   - Verify API functionality for associating courses and retrieving student courses using pytest.
   - Check various scenarios, including successful associations and error handling for non-existing courses.

```python
def test_associate_course(client):
    response = client.post("/students/1/courses", json={"course_id": 1})
    assert response.status_code == 201
    assert response.json()["message"] == "Course associated successfully."
```

## Scalability and Security Considerations
- **Scalability**:
  - The application is designed to be stateless and easily scaled horizontally.
- **Security**:
  - Inputs are validated and sanitized to prevent injection attacks.
  - Ensure proper permission checks are implemented in a future update for user authorization.

## Implementation Timeline
- **Week 1**:
  - Environment setup and model adjustments for `student_courses`.
- **Week 2**:
  - Implement API endpoints for associating courses and retrieving courses.
- **Week 3**:
  - Write unit tests to cover new functionality thoroughly and ensure regression coverage on existing functionality.
- **Week 4**:
  - Conduct full integration testing, update documentation, and prepare for deployment.

## Documentation and References
- **Code Documentation**:
  - Include relevant docstrings in new and modified classes and functions.
- **README.md**:
  - Update the main README to include details of the new endpoints and usage instructions.

## Trade-offs and Decisions
- **Junction Table**:
  - Implemented a new `student_courses` table to effectively establish a many-to-many relationship while preserving existing entities and data.
- **Backward Compatibility**:
  - The migration preserves existing student and course records, ensuring current functionalities remain intact while enhancing the overall system capabilities.

This implementation plan outlines the necessary steps to enhance the Student Management Web Application by adding the capability to relate students with courses, thereby improving its functionality and providing valuable insights into student performances.