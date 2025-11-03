# Implementation Plan: Add Course Relationship to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Course Entity

---

## Version: 1.1.0

## Overview
This implementation plan outlines the steps to enhance the existing Student Management Web Application by establishing a many-to-many relationship between the `Student` and `Course` entities. This feature will allow for the assignment of multiple Courses to individual Students and facilitate better tracking of educational progress. 

## 1. Architecture

### 1.1 Technical Architecture
The application will maintain the Model-View-Controller (MVC) architecture. A new junction table (i.e., `student_courses`) will be created to manage the many-to-many relationship, which will be integrated into the Model and managed through the API Controller.

### 1.2 Technology Stack
- **Programming Language**: Python 3.11+
- **Web Framework**: FastAPI for API development
- **Database**: SQLite for data persistence
- **ORM**: SQLAlchemy for database interaction
- **Testing Framework**: pytest for unit and integration testing

### 1.3 Deployment
The deployment strategy remains unchanged; the application will continue to be containerized using Docker.

## 2. Module Boundaries

### 2.1 Modules
1. **Database Module**: Manages database connections, schema management, and migrations.
2. **Model Module**: Contains data models for entities, including `Student`, `Course`, and the new junction table `student_courses`.
3. **API Module**: Implements the FastAPI application and routes for managing Course assignments to Students.
4. **Validation Module**: Validates incoming requests and parameters for Course assignments.

### 2.2 Responsibilities
- **Database Module**: Create a new `student_courses` table schema and manage migrations with Alembic.
- **Model Module**: Implement a junction model for the many-to-many relationship, ensuring foreign keys reference valid Students and Courses.
- **API Module**: Provide endpoints to assign, retrieve, and remove Courses from Students.
- **Validation Module**: Validate Course and Student IDs when creating or disassociating relationships and handle error responses appropriately.

## 3. Data Models

### 3.1 Entity Definition
**Student-Course Junction Model**:
```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class StudentCourse(Base):
    __tablename__ = 'student_courses'

    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    @staticmethod
    def validate_ids(student_id: int, course_id: int) -> bool:
        """Validates that the provided Student and Course IDs exist."""
        return all([student_id > 0, course_id > 0])
```

## 4. API Contracts

### 4.1 Endpoints
1. **Assign Courses to a Student**
   - **Route**: `POST /api/v1/students/{student_id}/courses`
   - **Request Body**:
     ```json
     {
       "course_ids": [1, 2, 3]
     }
     ```
   - **Response**:
     - **201 Created**
     ```json
     {
       "student_id": 1,
       "courses": [{"course_id": 1}, {"course_id": 2}, {"course_id": 3}]
     }
     ```
     - **400 Bad Request** for validation errors.
     ```json
     {
       "error": {
         "code": "E002",
         "message": "All provided Course IDs must be valid."
       }
     }
     ```

2. **Retrieve Courses for a Student**
   - **Route**: `GET /api/v1/students/{student_id}/courses`
   - **Response**:
     - **200 OK**
     ```json
     {
       "student_id": 1,
       "courses": [
         {"course_id": 1, "name": "Math 101"},
         {"course_id": 2, "name": "Science 101"}
       ]
     }
     ```
     - **404 Not Found** if Student does not exist.

3. **Remove a Course from a Student**
   - **Route**: `DELETE /api/v1/students/{student_id}/courses/{course_id}`
   - **Response**:
     - **204 No Content**
     - **404 Not Found** if Course or Student does not exist.

## 5. Database Setup

### 5.1 Schema Creation
Modify the existing SQLite database to include a new junction table `student_courses` using Alembic for migrations.

#### Migration Script (Alembic)
```python
"""Create student_courses table

Revision ID: xyz987
Revises: previous_revision_id
Create Date: 2023-10-10 14:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'xyz987'
down_revision = 'previous_revision_id'
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'student_courses',
        sa.Column('student_id', sa.Integer(), nullable=False),
        sa.Column('course_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['student_id'], ['students.id']),
        sa.ForeignKeyConstraint(['course_id'], ['courses.id']),
        sa.PrimaryKeyConstraint('student_id', 'course_id')
    )

def downgrade():
    op.drop_table('student_courses')
```

## 6. Security Considerations
- Validate all inputs to prevent SQL injection or data corruption.
- Error messages should not expose sensitive system details.

## 7. Testing Strategy

### 7.1 Test Coverage
- Implement unit tests for Course assignment, retrieval, and disassociation functions.
- Integration tests to confirm API endpoints return expected JSON responses.
- Ensure a minimum of 70% test coverage on new functionalities.

### 7.2 Example Test Cases
- Test assigning multiple Courses to a Student.
- Test retrieving all Courses assigned to a specific Student.
- Test removing a Course from a Student.
- Test validation error messages for invalid inputs.

## 8. Documentation
- Update API documentation to include details on Course assignments to Students.
- Provide instructions for running database migrations in the README.

## Success Criteria
- The application should allow for assigning, retrieving, and removing Courses from Students with required validations.
- Successful migration of the `student_courses` table without affecting existing data.
- Comprehensive testing efforts resulting in at least 70% coverage on all added functionalities.

## Conclusion
This implementation plan provides a clear approach to establishing a relationship between Students and Courses in the Student Management Web Application. Following this plan will enhance the application's functionality while ensuring backward compatibility and adherence to high-quality code standards.

## Modifications to Existing Files
1. **Model Module**:
   - Add `StudentCourse` model in the `models.py` file to define the junction table.

2. **API Endpoints**:
   - Add new routes to the FastAPI application for handling Course assignments to Students.
   ```python
   @app.post("/api/v1/students/{student_id}/courses")
   async def assign_courses_to_student(student_id: int, course_ids: List[int]):
       # Implementation for assigning courses
       pass

   @app.get("/api/v1/students/{student_id}/courses")
   async def get_student_courses(student_id: int):
       # Implementation for retrieving student's courses
       pass

   @app.delete("/api/v1/students/{student_id}/courses/{course_id}")
   async def remove_course_from_student(student_id: int, course_id: int):
       # Implementation for removing a course assignment
       pass
   ```

3. **Database Migration**:
   - Create the Alembic migration script to incorporate the `student_courses` junction table into the existing schema.

By implementing this plan, the application will provide robust handling of Course assignments, ensuring integrity in existing functionalities and maintaining high-quality code standards.