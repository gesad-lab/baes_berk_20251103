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
# Implementation Plan: Student Entity Web Application

## I. Overview

The purpose of this implementation plan is to establish a relationship between the `Course` and `Teacher` entities within the existing educational management system. By associating each `Course` with a `Teacher`, we will enhance the application’s capabilities for managing course assignments and improve reporting functionality regarding instructional resources.

## II. Architecture

### 2.1 Architectural Overview
This feature will follow a RESTful API architecture, building upon the existing structure while seamlessly integrating new functionalities for managing course-teacher relationships through defined API endpoints.

### 2.2 Components
1. **API Layer**: New endpoints to manage the association between Courses and Teachers.
2. **Service Layer**: Logic to handle business rules surrounding the course-teacher relationship.
3. **Data Access Layer (DAL)**: Responsible for CRUD operations concerning course-teacher associations.
4. **Database**: Updating the existing database schema to introduce the `teacher_id` foreign key in the `course` table.

## III. Technology Stack

- **Programming Language**: Python 3.11+
- **Web Framework**: FastAPI
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Testing Framework**: Pytest
- **Environment Management**: `pip`
- **Logging**: Python's built-in logging module

## IV. Module Boundaries and Responsibilities

### 4.1 API Module
- Endpoint Definitions:
  - `POST /courses/{courseId}/assignTeacher`: Associate a teacher with a course (requires `teacherId`).
  - `GET /courses/{courseId}`: Retrieve details for a course, including associated teacher information.
  - `PUT /courses/{courseId}/assignTeacher`: Update the teacher assigned to a course (requires updated `teacherId`).

### 4.2 Service Layer
- Business logic will include:
  - Validation of `courseId` and `teacherId` when associating or updating teachers.
  - Logic to ensure teacher association is valid.

### 4.3 Data Access Layer
- Responsible for database interactions related to course-teacher relationships:
  - Modify course model to include `teacher_id`.
  - Implement methods for assigning, updating, and retrieving teacher associations.

## V. Data Models

### 5.1 Updated Course Model
```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, autoincrement=True)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)

    teacher = relationship("Teacher", back_populates="courses")

class Teacher(Base):
    __tablename__ = "teachers"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

    courses = relationship("Course", back_populates="teacher")
```

### 5.2 Migration Script
The migration script will be created to update the `courses` table:
```sql
ALTER TABLE courses
ADD COLUMN teacher_id INTEGER,
ADD FOREIGN KEY (teacher_id) REFERENCES teachers(id);
```

## VI. API Contracts

### 6.1 Request/Response Format

1. **Assign a Teacher to a Course** (`POST /courses/{courseId}/assignTeacher`)
   - **Request**:
   ```json
   {
       "teacherId": 1
   }
   ```
   - **Response** (200 OK):
   ```json
   {
       "id": 1,
       "teacher_id": 1,
       "teacher": {
           "name": "John Doe",
           "email": "john.doe@example.com"
       }
   }
   ```

2. **Retrieve Course Details** (`GET /courses/{courseId}`)
   - **Response** (200 OK):
   ```json
   {
       "id": 1,
       "teacher": {
           "name": "John Doe",
           "email": "john.doe@example.com"
       }
   }
   ```

3. **Update Teacher Assignment for a Course** (`PUT /courses/{courseId}/assignTeacher`)
   - **Request**:
   ```json
   {
       "teacherId": 2
   }
   ```
   - **Response** (200 OK):
   ```json
   {
       "id": 1,
       "teacher_id": 2,
       "teacher": {
           "name": "Jane Smith",
           "email": "jane.smith@example.com"
       }
   }
   ```

### 6.2 Error Responses
- **Validation Error when Assigning Teacher**:
```json
{
    "error": {
        "code": "E001",
        "message": "Invalid teacher ID provided."
    }
}
```

- **Course Not Found Error**:
```json
{
    "error": {
        "code": "E002",
        "message": "Course not found."
    }
}
```

## VII. Error Handling

- Validate inputs for `courseId` and `teacherId` upon assignments or updates.
- Implement appropriate error handling to return specific messages on validation failures.

## VIII. Implementation Steps

1. **Database Migration**:
   - Create the migration script to update the `courses` table by adding a `teacher_id` column and defining the appropriate foreign key relationship.

2. **Update Data Access Layer**:
   - Modify the existing `Course` model to include the new `teacher_id` relationship.
   - Implement necessary methods in the DAL for associating, retrieving, and updating teacher associations.

3. **Implement API Endpoints**:
   - Implement `POST /courses/{courseId}/assignTeacher` for assigning a teacher.
   - Implement `GET /courses/{courseId}` to retrieve course details including teacher information.
   - Implement `PUT /courses/{courseId}/assignTeacher` for updating the teacher assignment.

4. **Enhance Service Layer**:
   - Create services that handle the business logic for each API call concerning course-teacher relationships.
   - Ensure logging and error handling is integrated into all service functions.

5. **Write Tests**:
   - Create unit tests for new functionalities related to course-teacher associations, ensuring compliance with testing standards and coverage.

6. **Documentation**:
   - Update API documentation to include new endpoints and their usage information, ensuring consistent documentation standards.

7. **End-to-End Testing**:
   - Execute integration testing to validate that the new course-teacher endpoints function correctly within the existing system.

8. **Deployment**:
   - Validate changes in a staging or testing environment before moving to production to ensure system stability.

## IX. Testing Strategy

- Implement automated tests focusing on:
  - Unit tests for service and data access layers related to course-teacher relationships.
  - Integration tests for the newly introduced API endpoints.

## X. Deployment Considerations

- Ensure environment variables are properly set up to accommodate database changes.
- Document the migration process to support rollbacks if necessary, ensuring that the migration does not disrupt existing data integrity.

## XI. Conclusion

This implementation plan provides a comprehensive approach for establishing the teacher relationship with the course entity in the educational management system. By following strict guidelines and integration principles, we will maintain data integrity, enhance the capabilities of the system, and ensure a seamless user experience.

### Existing Code Modifications:
- **Course Model**: Update the existing model to include `teacher_id` as a nullable foreign key.
- **New API Endpoints**: For assigning teachers, retrieving course details, and updating assignments.
- **Migration Script**: To apply the necessary schema changes to the database.
- **Testing Files**: Create new testing files to validate the course-teacher relationship functionalities.

**Example migration script**:
```python
# migration.py
"""Add teacher_id to courses table

Revision ID: <unique_id>
"""
from sqlalchemy import Column, Integer, ForeignKey
from alembic import op


def upgrade():
    op.add_column('courses', Column('teacher_id', Integer, ForeignKey('teachers.id'), nullable=True))


def downgrade():
    op.drop_column('courses', 'teacher_id')
```

### Testing File Example:
File: `tests/test_teacher_to_course_api.py`
```python
import pytest
from fastapi.testclient import TestClient
from src.main import app  # Assume your FastAPI app is instantiated in src/main.py

@pytest.fixture(scope="module")
def client():
    """Setup the test client for the FastAPI application."""
    with TestClient(app) as client:
        yield client

@pytest.mark.parametrize("courseId, teacherId", [(1, 1), (2, 2)])  # Replace with valid IDs
def test_assign_teacher_to_course(client, courseId, teacherId):
    """Test assigning a teacher to a course successfully."""
    response = client.post(f"/courses/{courseId}/assignTeacher", json={"teacherId": teacherId})
    assert response.status_code == 200
    assert response.json()["teacher_id"] == teacherId

def test_retrieve_course_with_teacher(client):
    """Test retrieving course details including teacher."""
    response = client.get("/courses/1")  # Replace with a valid course ID
    assert response.status_code == 200
    assert "teacher" in response.json()

def test_update_teacher_for_course(client):
    """Test updating a teacher assigned to a course."""
    response = client.put("/courses/1/assignTeacher", json={"teacherId": 2})  # Replace with valid IDs
    assert response.status_code == 200
    assert response.json()["teacher_id"] == 2

def test_handle_invalid_teacher_id(client):
    """Test validation error when assigning an invalid teacher."""
    response = client.post("/courses/1/assignTeacher", json={"teacherId": -1})  # Invalid ID
    assert response.status_code == 400
```

With this structured plan, the implementation of the teacher relationship within the course entity will enhance the educational management system’s ability to manage instructional resources effectively.