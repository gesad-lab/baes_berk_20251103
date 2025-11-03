# Implementation Plan: Add Teacher Relationship to Course Entity

## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Teacher Entity

---

## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Course Relationship to Student Entity

---

## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Course Entity

---

## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Email Field to Student Entity

---

## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Student Management Web Application

## Version
**Version**: 1.0.0  
**Purpose**: Implementation plan for adding a relationship between the Course and Teacher entities within the educational management system.

## I. Architecture Overview

### 1.1 High-Level Architecture
This implementation introduces a relationship between `Course` and `Teacher` entities by adding an optional `teacher_id` attribute to the `Course` model. The corresponding API endpoints will facilitate the assignment and retrieval of teachers related to specific courses. 

### 1.2 Technology Stack
- **Programming Language**: Python
- **Web Framework**: FastAPI
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Testing Framework**: pytest

## II. Module Design

### 2.1 API Module
**Responsibilities**:
- Implement new API endpoints for assigning and retrieving teachers to/from courses.

**Endpoints**:
1. `POST /courses/{course_id}/assign-teacher` - Assign a teacher to an existing course.
2. `GET /courses/{course_id}` - Retrieve course details, including assigned teacher information.

### 2.2 Service Layer
**Responsibilities**:
- Handle business logic related to teacher assignment and retrieval for courses.
- Validate inputs and enforce collection of required fields.

### 2.3 Data Access Layer
**Responsibilities**:
- Update SQLAlchemy models for the `Course` entity by modifying the existing schema to include `teacher_id`.

### 2.4 Database Models
#### Entities:

**Course (with new attribute)**:
```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)

    # Relationship with Teacher
    teacher = relationship("Teacher", back_populates="courses")
```

**Teacher**:
```python
class Teacher(Base):
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    
    courses = relationship("Course", back_populates="teacher")
```

### Updates to Relationships
- Ensure the `Course` model is compatible with the `Teacher` model's structure and vice versa.

## III. API Contracts

### 3.1 Request and Response Formats

#### 3.1.1 Assign Teacher to Course
- **Request**:
  - Method: `POST`
  - URL: `/courses/{course_id}/assign-teacher`
  - Body: `{"teacher_id": 1}`
- **Response**:
  - Status: `200 OK`
  - Body: `{"message": "Teacher assigned successfully"}` or `404 Not Found` if the Teacher does not exist, `409 Conflict` if the Course already has a teacher assigned.

#### 3.1.2 Retrieve Course with Assigned Teacher
- **Request**:
  - Method: `GET`
  - URL: `/courses/{course_id}`
- **Response**:
  - Status: `200 OK`
  - Body: `{"id": 1, "title": "Course Title", "teacher": {"id": 1, "name": "John Doe", "email": "johndoe@example.com"}}` or `404 Not Found`.

### 3.2 Error Responses
- **404 Not Found** for invalid Course ID or Teacher ID:
  ```json
  {"error": {"code": "E001", "message": "Course or Teacher not found."}}
  ```
- **409 Conflict** if a teacher assignment cannot be made because a teacher is already assigned:
  ```json
  {"error": {"code": "E002", "message": "Course already has a teacher assigned."}}
  ```

## IV. Database Management

### 4.1 Schema Migration
- Use Alembic to create a migration script to add the `teacher_id` column in the `courses` table.

#### Migration Script Example
```python
from alembic import op
import sqlalchemy as sa

def upgrade():
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))
    
def downgrade():
    op.drop_column('courses', 'teacher_id')
```

### 4.2 Schema Initialization
- Update the application startup logic to ensure the new `teacher_id` field exists and relationships can be established.

## V. Security Considerations
- Validate all incoming request data rigorously, ensuring that IDs provided correspond to existing entities.
- Employ proper input sanitization to mitigate risks such as SQL injection attacks.

## VI. Testing Strategy

### 6.1 Test Coverage
- Aim for a minimum of 70% test coverage for the new Course-Teacher functionality.

### 6.2 Testing Structure
- Add tests to verify the functionality of the new API endpoints for both assigning teachers to courses and retrieving course information.

### 6.3 Example Test Cases
- `test_assign_teacher_to_course_success()`
- `test_assign_teacher_with_nonexistent_course_fails()`
- `test_assign_teacher_when_course_already_assigned_fails()`
- `test_retrieve_course_with_teacher_info_success()`

## VII. Deployment Considerations

### 7.1 Deployment Strategy
- Package the application with Docker, ensuring that the migration script is executed during the deployment process to modify the `courses` table.

### 7.2 Health Check Endpoint
- Update existing health check mechanisms to assess that the new functionality is live and operational.

## VIII. Documentation

### 8.1 Required Documentation
- Amend the README.md to include details about the new Course-Teacher assignment API endpoints.

### 8.2 API Documentation
- Utilize OpenAPI/Swagger for generating richer API documentation that includes the new endpoints for teacher assignments.

## IX. Project Management and Version Control

### 9.1 Version Control Practices
- Maintain existing version control practices in Git and update `CHANGELOG.md` to reflect the addition of the teacher assignment functionality.

## X. Conclusion
This implementation plan methodically outlines the steps required to integrate the Teacher relationship into the Course entity while adhering to defined coding standards. The approach assures backward compatibility and solidifies the foundation for enhanced administrative capabilities within the educational management system.

### Existing Code Modifications 
File: `app/api/course.py`  
This file will require the addition of methods for assigning and retrieving teachers to courses:

```python
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models import Course, Teacher
from database import get_db

router = APIRouter()

@router.post("/courses/{course_id}/assign-teacher")
async def assign_teacher_to_course(course_id: int, teacher_id: int, db: Session = Depends(get_db)):
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail={"error": {"code": "E001", "message": "Course not found."}})
    
    if course.teacher_id is not None:
        raise HTTPException(status_code=409, detail={"error": {"code": "E002", "message": "Course already has a teacher assigned."}})

    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if not teacher:
        raise HTTPException(status_code=404, detail={"error": {"code": "E001", "message": "Teacher not found."}})
    
    course.teacher_id = teacher_id
    db.commit()
    return {"message": "Teacher assigned successfully"}

@router.get("/courses/{course_id}", response_model=dict)
async def get_course(course_id: int, db: Session = Depends(get_db)):
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail={"error": {"code": "E001", "message": "Course not found."}})
    
    return {
        "id": course.id,
        "title": course.title,
        "teacher": {
            "id": course.teacher.id,
            "name": course.teacher.name,
            "email": course.teacher.email,
        } if course.teacher else None
    }
```

File: `tests/api/test_course.py`  
Add test cases for the new endpoints:

```python
def test_assign_teacher_to_course_success(client):
    response = client.post("/courses/1/assign-teacher", json={"teacher_id": 1})
    assert response.status_code == 200
    assert response.json() == {"message": "Teacher assigned successfully"}

def test_assign_teacher_with_nonexistent_course_fails(client):
    response = client.post("/courses/999/assign-teacher", json={"teacher_id": 1})
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E001", "message": "Course not found."}}

def test_assign_teacher_when_course_already_assigned_fails(client):
    response = client.post("/courses/1/assign-teacher", json={"teacher_id": 1})
    assert response.status_code == 409
    assert response.json() == {"error": {"code": "E002", "message": "Course already has a teacher assigned."}}

def test_retrieve_course_with_teacher_info_success(client):
    response = client.get("/courses/1")
    assert response.status_code == 200
    assert "teacher" in response.json()
```

This structured implementation plan ensures that the assignment of teachers to courses is effectively executed within the existing educational management system architecture.