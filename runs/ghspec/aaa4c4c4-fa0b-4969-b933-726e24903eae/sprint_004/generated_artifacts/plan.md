# Implementation Plan: Add Course Relationship to Student Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

### Previous Sprint Plan: Create Course Entity

## Version: 1.0.0  
**Purpose**: To detail the technical implementation plan for establishing a relationship between the Student entity and the Course entity, enabling efficient management of course enrollments for students while maintaining the integrity of existing systems.

## I. Architecture Overview

### 1.1 Application Structure
The application employs a Model-View-Controller (MVC) architecture, enhancing the existing API with new functionality:

- **Model**: Update the Student model to include a foreign key relationship with the Course model, allowing for the enrollment of multiple courses per student.
- **Controller**: Implement API endpoints to manage course enrollments through requests to the Student-resource URIs.
- **Database**: Retain the use of SQLite, with updates to the existing Student table structure via migrations to accommodate the new relationships.

### 1.2 Technology Stack
- **Programming Language**: Python 3.11+
- **Web Framework**: FastAPI
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Testing Framework**: Pytest

## II. Module Boundaries & Responsibilities

### 2.1 Modules
1. **Model**:
   - Extend the existing Student model to establish a many-to-many relationship with the Course model using an association table.

2. **Controller**:
   - Implement API routes for enrolling students in courses and retrieving student details, including their enrolled courses.

3. **Database**:
   - Develop migration scripts to alter the Student table structure and to create an association table to manage Student-Course relationships.

## III. Data Models

### 3.1 Updated Student Model
```python
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base

# Association table for many-to-many relationship
student_course_association = Table(
    'student_courses',
    Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # Required Field
    courses = relationship("Course", secondary=student_course_association, back_populates="students")

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # Required Field
    level = Column(String, nullable=False)  # Required Field
    students = relationship("Student", secondary=student_course_association, back_populates="courses")
```

### 3.2 Database Migration
Utilizing Alembic to create the association table and modify the existing Student table:
1. Generate a migration script for altering the Student schema.
2. Ensure the existing Student data is preserved.

```bash
alembic revision --autogenerate -m "add student-course relationship"
```

```python
def upgrade():
    # Create the association table
    op.create_table('student_courses',
        sa.Column('student_id', sa.Integer(), sa.ForeignKey('students.id')),
        sa.Column('course_id', sa.Integer(), sa.ForeignKey('courses.id'))
    )

def downgrade():
    op.drop_table('student_courses')
```

## IV. API Contracts

### 4.1 Enroll Student in Courses
- **Endpoint**: `POST /students/{student_id}/courses`
- **Request Body**:
```json
{
    "course_ids": [1, 2, 3]
}
```
- **Response**:
```json
{
    "student_id": 1,
    "name": "John Doe",
    "courses": [
        {"id": 1, "name": "Mathematics", "level": "Beginner"},
        {"id": 2, "name": "Science", "level": "Intermediate"}
    ]
}
```
- **Error Response (404)**:
```json
{
    "error": {
        "code": "E002",
        "message": "The specified course(s) do not exist."
    }
}
```

### 4.2 Get Student Details with Courses
- **Endpoint**: `GET /students/{student_id}`
- **Response**:
```json
{
    "id": 1,
    "name": "John Doe",
    "courses": [
        {"id": 1, "name": "Mathematics", "level": "Beginner"},
        {"id": 2, "name": "Science", "level": "Intermediate"}
    ]
}
```

## V. Implementation Approach

### 5.1 Development
- Update the Student model to include the association table.
- Implement the `enroll_student_courses` and `get_student_details` functions to handle incoming requests.

### 5.2 Error Handling
- Implement validation checks in the `enroll_student_courses` function to ensure the provided `course_ids` correspond to valid Course records:
```python
from fastapi import HTTPException

def enroll_student_courses(student_id: int, course_ids: List[int]):
    invalid_courses = []
    for course_id in course_ids:
        if not course_exists(course_id):  # Function to check course validity
            invalid_courses.append(course_id)
    if invalid_courses:
        raise HTTPException(status_code=404, detail={"error": {"code": "E002", "message": "The specified course(s) do not exist."}})
```

### 5.3 Testing Strategy
- **Unit Tests**:
  - Implement tests for course enrollment and retrieval of student data including courses.
- **Integration Tests**:
  - Validate the functional interdependencies of the enrollment and retrieval processes.
- **API Response Tests**:
  - Confirm the correctness of API response structures for students and their enrolled courses.

## VI. Error Handling & Validation

- Implement validations in the API routes ensuring that all course IDs in the enrollment request exist, enhancing overall reliability.

## VII. Deployment Considerations

### 7.1 Production Readiness
- Ensure that the migration scripts are executed upon application startup, and confirm the application runs smoothly without manual intervention.

### 7.2 Health Check Endpoint
- Implement a simple `/health` endpoint returning a `200 OK` response for server health checks.

## VIII. Documentation

- Update the API documentation to outline the new enrollment functionality and retrieval processes for students.
- Modify the `README.md` to provide setup instructions and configurations related to the new Student-Course relationship.

## IX. Success Criteria

- Successful enrollment of students in multiple courses, with the ability to retrieve the updated student data reflecting their courses.
- Proper error handling for invalid course enrollments with specific HTTP status codes.
- Existing student and course records remain intact and functional post-deployment.
- The database schema is updated successfully to facilitate the new relationships.

## X. Technical Trade-offs

- **Many-to-Many Relationship Management**: While establishing a many-to-many relationship facilitates flexibility in course enrollment, it introduces complexity in data retrieval which needs to be managed through careful API design.
- **Migration Complexity**: Using Alembic simplifies database management but necessitates careful planning to ensure data integrity during schema updates.

## XI. Next Steps

1. **Setup Migration Infrastructure**: Configure Alembic for schema management and run migrations.
2. **Implement Student Model Updates**: Extend the model to include the new relationship.
3. **Develop API Endpoints**: Introduce new endpoints for enrolling students and retrieving their details.
4. **Create Tests**: Develop comprehensive test cases covering the new functionalities.
5. **Update Documentation**: Ensure that all relevant documentation is current and complete.
6. **Deploy Changes**: Schedule deployment to the production environment following thorough testing.

---

This document serves as a comprehensive implementation plan for integrating course relationships into the existing Student entity, ensuring that architectural considerations, API designs, data integrity, and testing strategies are all addressed for a successful rollout.