# Implementation Plan: Add Teacher Relationship to Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Teacher Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Course Relationship to Student Entity

---

## I. Overview
This implementation plan outlines the steps necessary to establish a relationship between the `Course` entity and the `Teacher` entity. This will allow courses to have an associated teacher, enhancing the application’s functionality by providing clear management of course information. The plan covers architectural updates, technology decisions, module interactions, API contracts, and testing strategies for the addition of this relationship.

## II. Technology Stack
- **Web Framework**: FastAPI (for building the API)
- **Database**: SQLite (lightweight and serverless)
- **ORM**: SQLAlchemy (for object-relational mapping)
- **Testing Framework**: pytest (for unit and integration testing)
- **Environment Management**: Poetry (for dependency management)
- **Documentation**: OpenAPI (auto-generated documentation through FastAPI)

## III. Architecture
### 1. Module Boundaries
- **API Module**: New API routes for updating courses with teacher assignments and retrieving courses including teacher details.
- **Service Layer**: Business logic for managing course and teacher relationships.
- **Data Access Layer**: Methods for interacting with both the Course and Teacher tables.
- **Model Layer**: Update to the Course data schema to include a foreign key reference to the Teacher.

### 2. Directory Structure
```
/course_management
│
├── /src
│   ├── /api
│   │   └── course.py                            # Existing API routes for course management (update to include teacher)
│   ├── /models
│   │   ├── course.py                             # SQLAlchemy model for Course entity (update for teacher relationship)
│   │   └── teacher.py                            # SQLAlchemy model for Teacher entity
│   ├── /services
│   │   └── course_service.py                     # Business logic for course management (update for teacher assignment)
│   ├── /database
│   │   └── db.py                                 # Existing database connection and initialization
│   └── main.py                                   # Entry point of the application
│
├── /tests
│   ├── /api
│   │   └── test_course.py                        # Test cases for course API (update for teacher-related tests)
│   └── /services
│       └── test_course_service.py                # Test cases for course service (update for teacher assignments)
│
├── .env.example                                   # Environment variable definitions
├── pyproject.toml                                 # Poetry dependency management
└── README.md                                      # Project documentation
```

## IV. Data Models
### 1. Update Course Entity
```python
# /src/models/course.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # Required Field
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # Adding Foreign Key for Teacher

    teacher = relationship("Teacher")  # Relationship to Teacher
```
### 2. Teacher Entity
(No changes needed, referred to in the previous sprint)

## V. API Contracts
### 1. Update Course Endpoint
- **Method**: `PUT`
- **Endpoint**: `/courses/{course_id}`
- **Request Body**:
```json
{
  "teacher_id": 1
}
```
- **Success Response**:
  - **Status**: 200 OK
  - **Body**:
```json
{
  "id": 1,
  "name": "Mathematics 101",
  "teacher_id": 1
}
```
- **Error Responses**:
  - **Status**: 400 Bad Request
  - **Body**:
```json
{
  "error": {
    "code": "E001",
    "message": "Invalid teacher ID."
  }
}
```
- **404 Not Found** if the specified course does not exist.

### 2. Retrieve Course with Teacher Endpoint
- **Method**: `GET`
- **Endpoint**: `/courses/{course_id}`
- **Success Response**:
  - **Status**: 200 OK
  - **Body**:
```json
{
  "id": 1,
  "name": "Mathematics 101",
  "teacher": {
    "name": "John Doe"
  }
}
```
- **404 Not Found** if the course does not exist.

## VI. Implementation Approach
1. **Setup Environment**:
   - Ensure the development environment is prepared using Poetry.
   - Verify existing dependencies are updated.

2. **Database Migration**:
   - **Strategy**: Create a migration script that modifies the existing `courses` table to add the `teacher_id` foreign key relationship using Alembic for database migrations.

```python
# Migration Script (using Alembic)
def upgrade():
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))
    op.create_foreign_key('fk_teacher', 'courses', 'teachers', ['teacher_id'], ['id'])

def downgrade():
    op.drop_constraint('fk_teacher', 'courses', type_='foreignkey')
    op.drop_column('courses', 'teacher_id')
```

3. **Implement API Endpoints**:
   - Update the existing `course.py` file in the API module to include the functionality for updating a course with a teacher assignment and retrieving a course with its teacher details.

```python
# src/api/course.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from models.course import Course
from models.teacher import Teacher
from services.course_service import update_course_teacher, get_course_with_teacher

router = APIRouter()

class CourseTeacherUpdate(BaseModel):
    teacher_id: int

@router.put("/courses/{course_id}", response_model=Course)
async def update_course(course_id: int, teacher_update: CourseTeacherUpdate):
    return await update_course_teacher(course_id, teacher_update.teacher_id)

@router.get("/courses/{course_id}", response_model=Course)
async def get_course(course_id: int):
    return await get_course_with_teacher(course_id)
```

4. **Business Logic Layer**:
   - Update the `course_service.py` file to handle operations related to associating a teacher with a course.

```python
# /src/services/course_service.py

from models.course import Course
from models.teacher import Teacher
from database import SessionLocal
from sqlalchemy.orm import Session
from fastapi import HTTPException

async def update_course_teacher(course_id: int, teacher_id: int):
    db: Session = SessionLocal()
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found.")

    # Validate teacher ID exists
    if teacher_id is not None:
        teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
        if not teacher:
            raise HTTPException(status_code=400, detail="Invalid teacher ID.")
    
    course.teacher_id = teacher_id
    db.commit()
    db.refresh(course)
    return course

async def get_course_with_teacher(course_id: int):
    db: Session = SessionLocal()
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found.")

    return {
        "id": course.id,
        "name": course.name,
        "teacher": {
            "name": course.teacher.name if course.teacher else None
        }
    }
```

5. **Testing**:
   - Update tests in `test_course.py` and `test_course_service.py` to validate new functionalities: assigning a teacher to a course and retrieving course details including teacher information.

```python
# tests/api/test_course.py

def test_update_course_teacher_success(client):
    response = client.put("/courses/1", json={"teacher_id": 1})
    assert response.status_code == 200
    assert response.json()["teacher_id"] == 1

def test_update_course_teacher_invalid(client):
    response = client.put("/courses/1", json={"teacher_id": 999})
    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid teacher ID."

def test_get_course_with_teacher_success(client):
    response = client.get("/courses/1")
    assert response.status_code == 200
    assert response.json()["teacher"]["name"] == "John Doe"

def test_get_course_not_found(client):
    response = client.get("/courses/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Course not found."
```

6. **Documentation**:
   - Update the existing API documentation to include the new course management endpoints related to teacher assignments in the autogenerated OpenAPI documentation.

## VII. Success Criteria
- The application should allow updating a course to associate it with a valid teacher and return a success response confirming the update.
- The application should successfully retrieve a course's details, including its associated teacher's name using the new endpoint.
- The application should validate inputs during course updates and handle errors gracefully, returning clear messages for invalid teacher IDs or non-existent courses.

## VIII. Security Considerations
- Implement proper validation for the incoming requests to prevent any malicious inputs. Ensure no sensitive data (like teacher names or emails) is exposed in error messages.

## IX. Performance Considerations
- Monitor the performance of database queries, ensuring that any joins with the teacher table do not adversely impact response times, especially as data volume grows.

## X. Deployment Considerations
- Review the Dockerfile and configuration files to ensure they reflect the new database schema changes and any new dependency requirements. Update the migration instructions in `.env.example`, ensuring any necessary environment variables are documented.

## XI. Conclusion
Implementing this plan will effectively introduce the teacher relationship to the course entity, improving course management functionalities within the application. Following these steps will ensure a robust, thoroughly tested solution while maintaining compatibility with existing structures and functionality. 

Existing Code Files:
File: tests/api/test_course.py
```
```python
# /tests/api/test_course.py

from fastapi.testclient import TestClient
import pytest
from src.api.course import router as course_router  # Importing the course router
from models.course import Course  # Assuming Course is defined in models
from database import get_db  # Assuming this is how we get a database session
from fastapi import FastAPI

# Create a FastAPI app instance and include the course router
app = FastAPI()
app.include_router(course_router)

# Initialize the test...
```

File: tests/services/test_course_service.py
```
```python
# /tests/services/test_course_service.py

from fastapi.testclient import TestClient
import pytest
from src.api.course import app  # Assuming this is where the FastAPI app instance is defined
from models.course import Course  # Assuming Course is defined in models
from sqlalchemy.orm import Session
from database import get_db  # Assuming this is how we get a database session

client = TestClient(app)

# Mock database session fixture (setup and teardown as needed)
@pytest.fixture(sc...
```

The above technical plan outlines the integration of the teacher relationship into the course entity effectively while adhering to the existing infrastructure and constraints.