# Implementation Plan: Add Teacher Relationship to Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Teacher Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Course Relationship to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Student Entity Management

## Version
1.0.0

## Purpose
To establish a relationship between the Course and Teacher entities within the existing educational management system. This will allow for effective tracking of which Teachers are assigned to which Courses, thereby improving resource management within the system.

## Architecture Overview
The system continues to utilize a microservices architecture with RESTful APIs developed using Python and FastAPI. SQLite will serve as the database. The addition of the Teacher relationship to the Course entity will be implemented while ensuring integration with existing functionalities, maintaining modularity, and adhering to best practices of maintainability and security.

## Technology Stack
- **Backend Framework**: FastAPI
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Testing**: pytest

## Module Boundaries and Responsibilities
1. **API Layer**:
   - Implement new endpoints for assigning, retrieving, and removing Teachers from Courses.

2. **Service Layer**:
   - Encapsulate business logic related to Course and Teacher relations, including validation and interaction with the persistence layer.

3. **Persistence Layer**:
   - Modify the existing Course data model to include the foreign key relation to the Teacher.

## Data Models and API Contracts

### Data Model: Course (Updated)
```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)

    teacher = relationship("Teacher", back_populates="courses")
```

### Data Model: Teacher
*(Refer to the previous sprint plan for Teacher details)*

### API Endpoints
1. **Assign Teacher to Course**
   - **Endpoint**: `PUT /courses/{course_id}/assign_teacher`
   - **Request Body**:
     ```json
     {
       "teacher_id": 1
     }
     ```
   - **Response**:
     - 200 OK with JSON representation of the updated Course object, or 404 Not Found if Course or Teacher does not exist.

2. **Retrieve Course Information Including Teacher**
   - **Endpoint**: `GET /courses/{course_id}`
   - **Response**:
     - 200 OK with JSON representation of the Course details including Teacher's information, or 404 Not Found if the course ID does not exist.

3. **Remove Teacher from Course**
   - **Endpoint**: `PUT /courses/{course_id}/remove_teacher`
   - **Response**:
     - 200 OK with JSON representation of the updated Course object, confirming Teacher has been removed.

## Implementation Approach

### 1. Project Structure Update
- In the existing FastAPI project structure, include modifications related to Course and Teacher entities:
```
src/
├── main.py            # Integrate new Course routes for handling teachers
├── models.py          # Update Course model to include teacher_id
├── services.py        # Add logic for Course-Teacher relationship management
├── api.py             # Define Course-Teacher API endpoints
├── database.py        # Handle migrations for the Course-Teacher relationship
tests/
├── test_api.py        # Test Course-Teacher API endpoints
└── test_services.py    # Test Course-Teacher business logic
```

### 2. Database Migration Strategy
- Utilize **Alembic** to create a migration updating the Course table to add the `teacher_id` foreign key:
```python
from alembic import op
import sqlalchemy as sa

def upgrade():
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), sa.ForeignKey('teachers.id'), nullable=True))

def downgrade():
    op.drop_column('courses', 'teacher_id')
```

### 3. API Implementation
- In `api.py`, implement the new methods for assigning and removing teachers from courses:
```python
@app.put("/courses/{course_id}/assign_teacher")
async def assign_teacher(course_id: int, teacher_id: int):
    # Logic to handle assigning a teacher via service layer
    pass

@app.put("/courses/{course_id}/remove_teacher")
async def remove_teacher(course_id: int):
    # Logic to handle removing a teacher via service layer
    pass
```

### 4. Business Logic Implementation
- Write service functions in `services.py` to manage the Course-Teacher relationship:
```python
def assign_teacher_to_course(db: Session, course_id: int, teacher_id: int):
    course = db.query(Course).filter(Course.id == course_id).first()
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if course is None or teacher is None:
        raise HTTPException(status_code=404, detail="Course or Teacher not found")
    
    course.teacher_id = teacher_id
    db.commit()
    db.refresh(course)
    return course

def remove_teacher_from_course(db: Session, course_id: int):
    course = db.query(Course).filter(Course.id == course_id).first()
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    
    course.teacher_id = None
    db.commit()
    return course
```

### 5. Input Validation
- Utilize Pydantic models for validating input during API requests:
```python
from pydantic import BaseModel

class AssignTeacher(BaseModel):
    teacher_id: int

class RemoveTeacher(BaseModel):
    # No fields needed for removal
    pass
```

### 6. Testing
- Implement tests for Course-Teacher functionalities in `test_api.py` and `test_services.py`:
```python
def test_assign_teacher():
    response = client.put("/courses/1/assign_teacher", json={"teacher_id": 1})  # Assuming course ID 1, teacher ID 1 exists
    assert response.status_code == 200
    assert response.json()["teacher_id"] == 1

def test_remove_teacher():
    response = client.put("/courses/1/remove_teacher")  # Assuming course ID 1 exists
    assert response.status_code == 200
    assert response.json()["teacher_id"] is None
```

### 7. Docker Setup
- Ensure Docker configurations are updated to reflect changes in application setup, particularly for migrations.

## Scalability, Security, and Maintainability Considerations
- Use environmental variables for sensitive configuration.
- Ensure robust error handling across all endpoints and service methods to provide actionable feedback to users on errors.

## Trade-Offs and Decisions
- Allow `teacher_id` to be nullable in the Course model to accommodate Courses without assigned Teachers.
- Provide clear error responses to maintain informative API interactions.

### Success Criteria
- Confirm that all API endpoints return the appropriate HTTP status codes and payloads as specified.
- Target at least 70% unit test coverage for the Course-Teacher relationship features.

## Deployment Considerations
- Ensure the database migration is run upon deployment to reflect the new relationships in the data models.
- Validate that the application maintains the functionality of existing features while integrating the new Course-Teacher relationships.

## Conclusion
This implementation plan provides details on establishing a Teacher relationship with the Course entity, ensuring adherence to existing structural norms and enhancing educational management capabilities through seamless integration with current functionalities. It covers project structure updates, API specifications, business logic, testing methodologies, and deployment strategies. 

Existing Code Files:
### File: tests/test_api.py
```python
import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

@pytest.fixture(scope="module")
def setup_database():
    # Set up necessary database state before tests
    yield
    # Clean up database state after tests

def test_assign_teacher_success(setup_database):
    response = client.put("/courses/1/assign_teacher", json={"teacher_id": 1})  # Assuming course 1 exists
    assert response.status_code == 200
    assert response.json()["teacher_id"] == 1

def test_remove_teacher_success(setup_database):
    response = client.put("/courses/1/remove_teacher")  # Assuming course 1 exists
    assert response.status_code == 200
    assert response.json()["teacher_id"] is None
```

### File: tests/test_services.py
```python
import pytest
from sqlalchemy.orm import Session
from src.services import assign_teacher_to_course, remove_teacher_from_course
from src.models import Course, Teacher

@pytest.fixture(scope="module")
def db_session():
    """Set up a test database session."""
    yield db_session  # Replace with actual session setup

def test_assign_teacher_to_course(db_session):
    """Test assigning a teacher to a course."""
    result = assign_teacher_to_course(db_session, 1, 1)  # Course ID 1, Teacher ID 1
    assert result.teacher_id == 1

def test_remove_teacher_from_course(db_session):
    """Test removing a teacher from a course."""
    result = remove_teacher_from_course(db_session, 1)  # Course ID 1
    assert result.teacher_id is None
```

This structured approach ensures that the implementation of the Teacher relationship with Courses is both thorough and compatible with the existing system architecture and functionalities.