# Implementation Plan: Add Teacher Relationship to Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

### Previous Sprint Plan: Create Teacher Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

### Previous Sprint Plan: Create Course Entity

## Version: 1.0.0  
**Purpose**: To detail the technical implementation plan for adding a relationship between the Course entity and the Teacher entity within the existing educational system, enhancing course management functionality and supporting application growth in educational management capabilities.

## I. Architecture Overview

### 1.1 Application Structure
The application maintains an MVC architecture. With the introduction of the teacher relationship, we will:

- **Model**: Extend the existing Course model to include a foreign key relationship with the Teacher model.
- **Controller**: Implement new API endpoints to handle assigning a teacher to a course and retrieving course details along with the teacher information.
- **Database**: Use SQLite, migrating to update the existing schema to include the teacher relationship within the Course table.

### 1.2 Technology Stack
- **Programming Language**: Python 3.11+
- **Web Framework**: FastAPI
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Migration Tool**: Alembic
- **Testing Framework**: Pytest

## II. Module Boundaries & Responsibilities

### 2.1 Modules
1. **Models**:
   - Extend the Course model to include `teacher_id` as a foreign key referencing the Teacher model.

```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # Required Field
    level = Column(String, nullable=False)  # Required Field
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # Nullable to allow courses without assigned teachers

    teacher = relationship("Teacher", back_populates="courses")  # Relationship to Teacher
```

2. **Controllers**:
   - Create API routes for assigning a teacher to a course and retrieving course details with teacher information.

3. **Database**:
   - Develop migration scripts to add the `teacher_id` column to the existing Course table, ensuring the new relationship is established without data loss.

## III. Data Models

### 3.1 Course Model Update
The updated Course model now includes the teacher_id field.

### 3.2 Database Migration
Utilizing Alembic to propagate schema changes:
1. Generate a migration to add `teacher_id` to the Course table.

```bash
alembic revision --autogenerate -m "add teacher relationship to courses"
```

```python
def upgrade():
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))
    op.create_foreign_key('fk_teacher_course', 'courses', 'teachers', ['teacher_id'], ['id'])

def downgrade():
    op.drop_constraint('fk_teacher_course', 'courses', type_='foreignkey')
    op.drop_column('courses', 'teacher_id')
```

## IV. API Contracts

### 4.1 Assign Teacher to Course
- **Endpoint**: `PUT /courses/{course_id}/assign-teacher`
- **Request Body**:
```json
{
    "teacher_id": "<teacher_id>"
}
```
- **Response**:
```json
{
    "id": "<course_id>",
    "name": "<course_name>",
    "level": "<course_level>",
    "teacher": {
        "id": "<teacher_id>",
        "name": "<teacher_name>",
        "email": "<teacher_email>"
    }
}
```
- **Error Response (404)**:
```json
{
    "error": {
        "code": "E002",
        "message": "Course not found."
    }
}
```
- **Error Response (400)**:
```json
{
    "error": {
        "code": "E001",
        "message": "Required field 'teacher_id' is missing."
    }
}
```

### 4.2 Get Course Details with Teacher Information
- **Endpoint**: `GET /courses/{course_id}`
- **Response**:
```json
{
    "id": "<course_id>",
    "name": "<course_name>",
    "level": "<course_level>",
    "teacher": {
        "id": "<teacher_id>",
        "name": "<teacher_name>",
        "email": "<teacher_email>"
    }
}
```
- **Error Response (404)**:
```json
{
    "error": {
        "code": "E002",
        "message": "Course not found."
    }
}
```

## V. Implementation Approach

### 5.1 Development
- Update the Course model to include the `teacher_id` foreign key relationship.
- Develop the `assign_teacher_to_course` and `get_course_details` functions to handle respective requests.

### 5.2 Error Handling
- Validate teacher assignments by checking if the course ID exists.
- Validate the presence of `teacher_id` in the request body when assigning a teacher.

```python
from fastapi import HTTPException

def assign_teacher(course_id: int, teacher_data: dict):
    if "teacher_id" not in teacher_data:
        raise HTTPException(status_code=400, detail={
            "error": {
                "code": "E001",
                "message": "Required field 'teacher_id' is missing."
            }
        })
    
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail={
            "error": {
                "code": "E002",
                "message": "Course not found."
            }
        })
    
    course.teacher_id = teacher_data["teacher_id"]
    db.commit()
    return course
```

### 5.3 Testing Strategy
- **Unit Tests**:
  - Validate functionality for assigning a teacher and retrieving course details.
- **Integration Tests**:
  - Ensure API endpoints work correctly with the database.
- **API Response Tests**:
  - Confirm the correctness of all API responses based on defined contracts.

## VI. Error Handling & Validation

- Implement comprehensive validation in API endpoints for both assigning teachers and retrieving course details to ensure data integrity and appropriate error messaging.

## VII. Deployment Considerations

### 7.1 Production Readiness
- Execute necessary migrations during application startup, ensuring the new teacher assignments are integrated into the existing Course structure.

### 7.2 Health Check Endpoint
- Implement a `/health` endpoint to verify system status with a `200 OK` response.

## VIII. Documentation

- Update the API documentation to incorporate changes related to assigning teachers and retrieving course information.
- Ensure `README.md` reflects the updated API usage and configuration specifics regarding the new course-teacher relationship functionality.

## IX. Success Criteria

- Successful assignment of teachers to courses and retrieval of complete course details, including assigned teacher information.
- Correct handling of errors with appropriate HTTP status codes and concise JSON error messages.
- Existing data related to Students and Courses remains intact during migrations.
- Streamlined database schema updates without manual intervention failures.

## X. Technical Trade-offs

- **Model Complexity**: The introduction of foreign key relationships may complicate model management but enhances data linkages for more robust querying.
- **Migration Necessity**: Alembic's usage for database schema modifications can introduce overhead in migration management, but it safeguards data integrity.

## XI. Next Steps

1. **Setup and Configure Migration**: Ensure Alembic for the Course table migration is properly set up.
2. **Implement Course Model Updates**: Extend the model to include the new `teacher_id` field.
3. **Create Associated API Endpoints**: Develop the new endpoints to assign teachers and retrieve courses with teacher information.
4. **Write Comprehensive Tests**: Create test scenarios that check all new functionalities.
5. **Update All Relevant Documentation**: Keep the API docs and `README.md` updated with new functionalities and usage instructions.
6. **Prepare for Deployment**: Plan the deployment to the production environment following validation and successful local testing.

---
This document provides a detailed plan for implementing the teacher relationship within the Course entity, integrating new modules seamlessly with existing functionality, and maintaining backward compatibility with the existing data models.