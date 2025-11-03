# Implementation Plan: Add Course Relationship to Student Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Email Field to Student Entity

---

## I. Overview
This implementation plan outlines the steps needed to establish a relationship between the `Student` and `Course` entities within the application. By implementing this feature, we will allow school administrators to associate students with courses, enhancing educational data organization and improving course enrollment management. The plan includes necessary architectural updates, technology decisions, module interactions, API contracts, and testing strategies.

## II. Technology Stack
- **Web Framework**: FastAPI (for building the API)
- **Database**: SQLite (lightweight and serverless)
- **ORM**: SQLAlchemy (for object-relational mapping)
- **Testing Framework**: pytest (for unit and integration testing)
- **Environment Management**: Poetry (for dependency management)
- **Documentation**: OpenAPI (auto-generated documentation through FastAPI)

## III. Architecture
### 1. Module Boundaries
- **API Module**: Introduction of new API routes for associating courses with students and retrieving course information for a specific student.
- **Service Layer**: New business logic for managing Course associations within Student records.
- **Data Access Layer**: Methods for interacting with the updated Student table and existing Course table.
- **Model Layer**: Definition of updated Student data schema, incorporating relations with Course entities.

### 2. Directory Structure
```
/student_course_management
│
├── /src
│   ├── /api
│   │   └── student.py                      # New API routes for student-course association
│   ├── /models
│   │   └── student.py                       # SQLAlchemy models for Student entity
│   ├── /services
│   │   └── student_service.py               # Business logic for student management
│   ├── /database
│   │   └── db.py                            # Existing database connection and initialization
│   └── main.py                              # Entry point of the application
│
├── /tests
│   ├── /api
│   │   └── test_student.py                  # Test cases for student API
│   └── /services
│       └── test_student_service.py          # Test cases for student service
│
├── .env.example                              # Environment variable definitions
├── pyproject.toml                            # Poetry dependency management
└── README.md                                 # Project documentation
```

## IV. Data Models
### 1. Updated Student Entity
```python
# /src/models/student.py

from sqlalchemy import Column, Integer, String, ARRAY
from database import Base

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # Existing field
    course_ids = Column(ARRAY(Integer), nullable=True)  # New relationship field
```

## V. API Contracts
### 1. Associate Courses with a Student Endpoint
- **Method**: `PATCH`
- **Endpoint**: `/students/{student_id}/courses`
- **Request Body**:
  ```json
  {
    "course_id": 1
  }
  ```
- **Success Response**:
  - **Status**: 200 OK
  - **Body**:
    ```json
    {
      "message": "Course successfully associated with student."
    }
    ```
- **Error Responses**:
  - **Status**: 400 Bad Request
  - **Body**:
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Invalid course ID."
      }
    }
    ```

### 2. Retrieve Student Courses Endpoint
- **Method**: `GET`
- **Endpoint**: `/students/{student_id}/courses`
- **Success Response**:
  - **Status**: 200 OK
  - **Body**:
    ```json
    [
      {
        "id": 1,
        "name": "Introduction to Computer Science",
        "level": "100"
      }
    ]
    ```

## VI. Implementation Approach
1. **Setup Environment**:
   - Ensure the development environment is prepared using Poetry.
   - Verify that existing dependencies are installed.

2. **Database Migration**:
   - **Strategy**: Create a new migration script to add a `course_ids` field to the `students` table, using Alembic for database migrations.

```python
# Migration Script (using Alembic)
def upgrade():
    op.add_column('students', sa.Column('course_ids', sa.ARRAY(sa.Integer), nullable=True))

def downgrade():
    op.drop_column('students', 'course_ids')
```

3. **Implement API Endpoints**:
   - Create a new `student.py` file in the API module for defining `PATCH /students/{student_id}/courses` and `GET /students/{student_id}/courses` endpoints. Implement the necessary business logic to handle course associations and retrieval.

```python
# src/api/student.py

from fastapi import APIRouter, HTTPException
from models.student import Student
from services.student_service import associate_course_with_student, get_student_courses
from pydantic import BaseModel
from typing import List

router = APIRouter()

class CourseAssociation(BaseModel):
    course_id: int

@router.patch("/students/{student_id}/courses", status_code=200)
async def associate_course_endpoint(student_id: int, course: CourseAssociation):
    return await associate_course_with_student(student_id, course.course_id)

@router.get("/students/{student_id}/courses", response_model=List[Course])
async def retrieve_courses_endpoint(student_id: int):
    return await get_student_courses(student_id)
```

4. **Business Logic Layer**:
   - Create a new `student_service.py` in the service layer that includes logic for associating courses with students and retrieving the student's courses. Validate the presence of the input course ID against the database before performing operations.

```python
# /src/services/student_service.py

from models.student import Student
from models.course import Course
from database import SessionLocal
from sqlalchemy.orm import Session
from fastapi import HTTPException

async def associate_course_with_student(student_id: int, course_id: int):
    db: Session = SessionLocal()
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found.")
    
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=400, detail="Invalid course ID.")
    
    if student.course_ids is None:
        student.course_ids = []
    
    if course_id not in student.course_ids:
        student.course_ids.append(course_id)
    
    db.commit()
    return {"message": "Course successfully associated with student."}

async def get_student_courses(student_id: int):
    db: Session = SessionLocal()
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found.")
    
    return [db.query(Course).filter(Course.id == course_id).first() for course_id in student.course_ids]
```

5. **Testing**:
   - Develop tests in `test_student.py` and `test_student_service.py` to validate the new student-course functionalities. Ensure the tests cover success cases and errors (e.g., nonexistent students or courses).

```python
# tests/api/test_student.py

def test_associate_course_success(client):
    response = client.patch("/students/1/courses", json={"course_id": 1})
    assert response.status_code == 200
    assert response.json()["message"] == "Course successfully associated with student."

def test_associate_course_invalid_student(client):
    response = client.patch("/students/999/courses", json={"course_id": 1})
    assert response.status_code == 404
    assert response.json()["detail"] == "Student not found."

def test_associate_course_invalid_id(client):
    response = client.patch("/students/1/courses", json={"course_id": 999})
    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid course ID."
```

6. **Documentation**:
   - Update the API documentation to include the new student-course association endpoints in the autogenerated OpenAPI documentation.

## VII. Success Criteria
- The application should allow a school administrator to associate a course with a student, returning a success response.
- The application should enable retrieval of a list of courses linked to a student, represented accurately in the response.
- The application should validate the course ID provided and return errors for invalid inputs.

## VIII. Security Considerations
- Inputs must be validated to prevent injection attacks. Ensure that no user-input values are logged unnecessarily and implement strict input validation in course association requests.

## IX. Performance Considerations
- Ensure that the SQLite database performs adequately during CRUD operations related to student-course associations; however, attention to scaling needs may arise as the data volume grows.

## X. Deployment Considerations
- Review the Dockerfile and configuration files to ensure they reflect the new functionality around student-course relationships. Document necessary environment variables in `.env.example`, especially regarding database migrations.

## XI. Conclusion
Implementing this plan will successfully integrate a course relationship into the `Student` entity, increasing the depth of educational data managed within the application. Following these steps ensures a robust, thoroughly tested solution that enhances course tracking for students. The next course of action involves creating the migration script and implementing the outlined API functionalities alongside thorough testing.

Existing Code Files:
File: tests/api/test_student.py
```
from fastapi.testclient import TestClient
import pytest
from src.api.student import router as student_router  # Importing the student router
from models.student import Student  # Assuming Student is defined in models
from sqlalchemy.orm import Session
from database import get_db  # Assuming this is how we get a database session

# Create a FastAPI app instance and include the student router
app = FastAPI()
app.include_router(student_router)

# Fixture for the test client
@pytest.fixture(scope="module")
...
```

File: tests/services/test_student_service.py
```
```python
import pytest
from fastapi.testclient import TestClient
from src.api.student import app  # Assuming this is where the FastAPI app instance is defined
from src.models.student import Student  # Assuming this is the Student model
from sqlalchemy.orm import Session

client = TestClient(app)

# Mock database session fixture (setup and teardown as needed)
@pytest.fixture(scope="module")
def db_session():
    # Logic to create a database session and clean up afterward
    # This is a placeholder ...
```