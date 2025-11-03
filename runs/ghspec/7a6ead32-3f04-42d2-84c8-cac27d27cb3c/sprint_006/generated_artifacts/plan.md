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

## Version: 1.1.0

## Overview
This implementation plan focuses on updating the existing educational system to establish a relationship between the Course entity and the Teacher entity. The enhancement will allow a Course to be associated with a specific Teacher, facilitating better educational management through enhanced data organization and reporting capabilities.

## 1. Architecture

### 1.1 Technical Architecture
The system will continue to leverage the Model-View-Controller (MVC) architecture. New functionalities for handling the Course-Teacher relationship will be integrated into the existing API Controller, ensuring logical separation in functionality while maintaining smooth interactions with other modules.

### 1.2 Technology Stack
- **Programming Language**: Python 3.11+
- **Web Framework**: FastAPI for API development
- **Database**: SQLite for data persistence
- **ORM**: SQLAlchemy for database interaction
- **Testing Framework**: pytest for unit and integration testing

### 1.3 Deployment
The deployment strategy will remain unchanged, and the application will continue to be containerized using Docker.

## 2. Module Boundaries

### 2.1 Modules
1. **Database Module**: Manages database connections, schema management, and migrations, focusing on the Course and Teacher entities.
2. **Model Module**: Houses the Course and Teacher data models.
3. **API Module**: Implements the FastAPI application and routes for managing Course-Teacher relationships.
4. **Validation Module**: Validates incoming requests related to Course assignments to Teachers.

### 2.2 Responsibilities
- **Database Module**: Update the Course table schema to include a foreign key reference to the Teacher table and implement necessary migrations with Alembic.
- **Model Module**: Modify the Course model to accommodate the new `teacher_id` field.
- **API Module**: Provide endpoints for assigning a Teacher to a Course, viewing Course details along with Teacher information, and handling validation accordingly.
- **Validation Module**: Ensure that Teacher IDs are correct before assignment, and handle error cases.

## 3. Data Models

### 3.1 Entity Definition
**Course Model Update**:
```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)

    teacher = relationship("Teacher", back_populates="courses")
```

**Teacher Model** (to show relationship):
```python
class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    
    courses = relationship("Course", back_populates="teacher")
```

## 4. API Contracts

### 4.1 Endpoints
1. **Assign a Teacher to a Course**
   - **Route**: `PUT /api/v1/courses/{course_id}/assign_teacher`
   - **Request Body**:
     ```json
     {
       "teacher_id": 1
     }
     ```
   - **Response**:
     - **200 OK**
     ```json
     {
       "message": "Teacher assigned successfully."
     }
     ```
     - **404 Not Found** if Course does not exist.
     - **400 Bad Request** for validation errors (e.g., course already has a teacher assigned or invalid teacher ID).

2. **View Course with Teacher Information**
   - **Route**: `GET /api/v1/courses/{course_id}`
   - **Response**:
     - **200 OK**
     ```json
     {
       "id": 1,
       "teacher": {
         "id": 1,
         "name": "Jane Doe",
         "email": "jane.doe@example.com"
       }
     }
     ```
     - **404 Not Found** if Course does not exist.

## 5. Database Setup

### 5.1 Schema Creation
Implement a migration script for updating the Course table to include the `teacher_id` foreign key. Using Alembic to create the migration will ensure existing data remains intact.

#### Migration Script (Alembic)
```python
"""Add teacher_id to courses table

Revision ID: def456
Revises: abc123
Create Date: 2023-10-10 14:30:00

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'def456'
down_revision = 'abc123'
branch_labels = None
depends_on = None

def upgrade():
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), sa.ForeignKey('teachers.id'), nullable=True))

def downgrade():
    op.drop_column('courses', 'teacher_id')
```

## 6. Security Considerations
- Validate all inputs to prevent SQL injection or data corruption.
- Ensure error messages do not expose sensitive system details.
- Use environment variables for configuration secrets.

## 7. Testing Strategy

### 7.1 Test Coverage
- Create unit tests for the Course-Teacher assignment functionalities.
- Implement integration tests for ensuring API endpoints return expected responses and handle edge cases.
- Aim for a minimum of 70% test coverage on new functionalities.

### 7.2 Example Test Cases
- Test successful assignment of a Teacher to a Course.
- Test validation when assigning a Teacher ID that does not exist.
- Test error handling when trying to assign a second Teacher to a Course that already has one assigned.
- Test retrieval of a Course including Teacher information.

## 8. Documentation
- Update API documentation to include details on the Course-Teacher relationship endpoints.
- Provide instructions for running database migrations in the README.

## Conclusion
This implementation plan outlines a structured approach to integrating a Teacher relationship into the existing Course entity. By following the proposed steps and maintaining backward compatibility throughout the process, the educational management system will effectively enhance its resource allocation capabilities.

## Modifications to Existing Files
1. **Model Module**:
   - Update `Course` model to include the `teacher_id` foreign key and `relationship` with the `Teacher` model.
   
2. **API Endpoints**:
   - Introduce new routes to the FastAPI application for assigning teachers and viewing Course details.
   ```python
   @app.put("/api/v1/courses/{course_id}/assign_teacher")
   async def assign_teacher(course_id: int, teacher_id: int):
       # Implementation for assigning a teacher to a course
       pass

   @app.get("/api/v1/courses/{course_id}")
   async def get_course(course_id: int):
       # Implementation for retrieving a course and its associated teacher
       pass
   ```

3. **Database Migration**:
   - Implement the Alembic migration script to modify the existing schema by adding the `teacher_id` field to the `courses` table.

By executing this detailed plan, the application can successfully integrate the Teacher relationship while adhering to existing architecture principles and maintaining data integrity.