# Implementation Plan: Add Teacher Relationship to Course Entity

---

## I. Project Overview

### 1.1 Purpose
The purpose of this feature is to establish a relationship between the existing Course entity and the newly introduced Teacher entity. This enhancement will enable the system to associate specific teachers with courses, thereby providing better visibility into course management, facilitating teacher assignments, and streamlining course-related reporting.

### 1.2 Scope
This implementation will extend existing functionalities to:
- Introduce a `teacher_id` foreign key in the existing `Course` model.
- Provide API endpoints for assigning a teacher to a course and retrieving course details with associated teacher information.
- Ensure seamless database schema migration while maintaining existing records and integrity.

### 1.3 Key Technologies
- **Framework**: FastAPI (Python)
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Testing Framework**: pytest
- **Migration Tool**: Alembic

---

## II. Architectural Design

### 2.1 Layered Architecture
#### 2.1.1 Layers
- **Presentation Layer**: API endpoints for managing course-teacher relationships.
- **Service Layer**: Business logic for assigning teachers to courses and retrieving related data.
- **Database Layer**: SQLAlchemy models for Courses and Teachers, handling the relationship.

#### 2.1.2 Module Responsibilities
- **`app/main.py`**: Main application entry point, integrating new routes for course-teacher management.
- **`app/models.py`**: Update the existing Course SQLAlchemy model to include the `teacher_id` foreign key attribute.
- **`app/schemas.py`**: Define Pydantic models for request and response validation related to course-teacher interactions.
- **`app/routes/course.py`**: New API routes to handle teacher assignments and retrieval of course details.
- **`app/database.py`**: Migration script to adjust the Course table schema for the new teacher relationship.

### 2.2 Data Models
#### 2.2.1 Updated Course Model
```python
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)

    teacher = relationship("Teacher", back_populates="courses")

class Teacher(Base):
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

    courses = relationship("Course", back_populates="teacher")
```

---

## III. API Contracts

### 3.1 Endpoints
#### 3.1.1 Assign Teacher to Course
- **Endpoint**: `POST /courses/{course_id}/assign-teacher`
- **Request Body**: 
    ```json
    {
      "teacher_id": 1
    }
    ```
- **Response**: 
    - **Success**: 
      ```json
      {
        "message": "Teacher assigned to course successfully."
      }
      ```
    - **Error**: 
      ```json
      {
        "error": {
          "code": "E002",
          "message": "Teacher does not exist."
        }
      }
      ```

#### 3.1.2 Retrieve Course with Teacher
- **Endpoint**: `GET /courses/{course_id}`
- **Response**: 
  ```json
  {
    "id": 1,
    "name": "Course Name",
    "teacher": {
      "id": 1,
      "name": "John Doe"
    }
  }
  ```

### 3.2 Error Handling
- Ensure consistent error responses are provided for non-existent teachers in assignments and any validation failures.

---

## IV. Startup Process & Database Schema Creation

### 4.1 Automatic Schema Updates
On application startup, the new `teacher_id` column must be added to the existing Courses table using database migrations.

#### Migration Strategy
- Utilize Alembic to create a migration script addressing the new `teacher_id` column.
```bash
alembic revision --autogenerate -m "Add teacher_id to Courses table"
```

The generated script will include the following migration:
```python
def upgrade():
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))
    op.create_foreign_key('fk_teacher', 'courses', 'teachers', ['teacher_id'], ['id'])

def downgrade():
    op.drop_constraint('fk_teacher', 'courses', type_='foreignkey')
    op.drop_column('courses', 'teacher_id')
```

---

## V. Testing Plan

### 5.1 Test Coverage
Aim for a minimum of 70% coverage across the new functionalities, especially focusing on critical paths for teacher assignment and retrieval.

### 5.2 Test Cases
- **Assign Teacher to Course**: Check correct assignments and error scenarios.
- **Retrieve Course Details**: Validate retrieval of course data, verifying the presence of teacher information.
- **Migration Verification**: Confirm that the migration successfully modifies the Courses table without loss of existing data.

---

## VI. Security Considerations

### 6.1 Data Protection
Ensure that sensitive information, such as teacher emails, is handled properly and not logged.

### 6.2 Authentication
Consider implementing authentication mechanisms for API endpoints to restrict unauthorized access in future iterations.

---

## VII. Performance Considerations

### 7.1 Efficiency Improvements
- Implement indexing on the `teacher_id` foreign key in the Courses table to optimize lookup performance.

---

## VIII. Configuration Management

### 8.1 Environment Variables
Review and update any necessary environment variables related to the new functionality, if applicable.

---

## IX. Documentation

### 9.1 README.md
Update the README file to include new API endpoints related to course-teacher relationships, complete with usage examples.

### 9.2 Code Comments
Ensure inline documentation appropriately describes business logic, particularly for newly implemented features in service layers.

---

## X. Deployment Considerations

### 10.1 Production Readiness
Ensure comprehensive testing validates all new features and that the tests pass successfully before deployment.

### 10.2 Backward Compatibility
The addition of `teacher_id` must not disrupt any existing relationships within the Courses, Enrollments, or Students models.

---

## XI. Conclusion

This implementation plan outlines the strategy for integrating a Teacher relationship into the Course entity within the existing student management system, ensuring backward compatibility, maintainability, and compliance with best practices.

**Existing Code Modifications**:
- **models.py**: Update the Course model to include the `teacher_id` field and implement the relationship with the Teacher model.
- **routes/course.py**: Add new route definitions for assigning teachers and retrieving courses with teacher details.
- **schemas.py**: Define the necessary Pydantic models for request/response validation on newly defined endpoints.
- **tests/test_course.py**: Establish test cases for the new course-teacher functionalities.
- **database.py**: Adjust migration handling to integrate the new `teacher_id` field in Courses.

**New Additional Files**:
- **routes/course.py**: Implementation of the Course API routes with teacher assignments.
- **schemas/course.py**: Define Pydantic models for course request/response validation.
- **migrations/versions/add_teacher_id.py**: Migration script for modifying the Courses table.

This implementation plan is thorough and aligns with the existing architecture, ensuring a smooth integration of the new Teacher entity in a structured manner.