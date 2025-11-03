# Implementation Plan: Add Teacher Relationship to Course Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Teacher Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

### Previous Sprint Plan:
# Implementation Plan: Add Course Relationship to Student Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

### Previous Sprint Plan:
# Implementation Plan: Create Course Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

### Previous Sprint Plan:
# Implementation Plan: Add Email Field to Student Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

### Previous Sprint Plan:
# Implementation Plan: Student Management Web Application

## I. Architecture Overview

The architecture of the Student Management Web Application will retain the microservices model with a RESTful API design facilitating CRUD operations. This feature will enrich the Course entity by establishing a relationship with the Teacher entity, allowing efficient management of course assignments and enhancing reporting functionalities.

## II. Technology Stack

- **Programming Language**: Python 3.11
- **Web Framework**: Flask
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Testing Framework**: pytest
- **Environment Management**: pip

## III. Module Boundaries and Responsibilities

### 1. API Layer
- Introduce endpoints in the `src/api/course_api.py` for handling teacher assignment related to courses.

### 2. Service Layer
- Update `course_service.py` to include business logic for assigning and updating the teacher assignment for courses.

### 3. Data Access Layer
- Modify the `Course` model in `src/models/course.py` to incorporate the new `teacher_id` field linking it to the `Teacher` model.

### 4. Validation Layer
- Implement validation in `src/validators/course_validator.py` to ensure correct inputs for assigning teachers to courses.

## IV. Data Models

### 1. Course Model Update
The `Course` model will be updated to include a new field:
```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    # existing fields...
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # New field for teacher assignment

    teacher = relationship("Teacher", back_populates="courses")  # Establishing relationship
```

### 2. Teacher Model
Ensure that the `Teacher` model supports the relationship:
```python
class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    courses = relationship("Course", back_populates="teacher")  # Reverse relationship
```

### 3. Database Initialization
- Modify `src/__init__.py` to ensure that the `Teacher` model is included in the database schema.
- Implement migration scripts to add the `teacher_id` column to the `courses` table while preserving existing data.

## V. API Contracts

### 1. Assign Teacher to Course
- **Endpoint**: `POST /courses/{courseId}/assign-teacher`
- **Request Body**:
    ```json
    {
      "teacher_id": 1
    }
    ```
- **Response**:
    - **Status**: 200 OK
    - **Body**:
    ```json
    {
      "id": 1,
      "name": "Course Name",
      "teacher_id": 1,
      "teacher": {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com"
      }
    }
    ```

### 2. Retrieve Course with Teacher
- **Endpoint**: `GET /courses/{id}`
- **Response**:
    - **Status**: 200 OK
    - **Body**:
    ```json
    {
      "id": 1,
      "name": "Course Name",
      "teacher": {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com"
      }
    }
    ```

### 3. Update Teacher Assignment for Course
- **Endpoint**: `PUT /courses/{courseId}/update-teacher`
- **Request Body**:
    ```json
    {
      "teacher_id": 2
    }
    ```
- **Response**:
    - **Status**: 200 OK
    - **Body**:
    ```json
    {
      "id": 1,
      "name": "Course Name",
      "teacher_id": 2,
      "teacher": {
        "id": 2,
        "name": "Jane Smith",
        "email": "jane.smith@example.com"
      }
    }
    ```

## VI. Implementation Approach

### 1. Development Steps
1. **Modify Project Structure**:
   - Update the `Course` model to include the `teacher_id` foreign key in `src/models/course.py`.
   - Create new methods in `src/services/course_service.py` for assigning and updating teachers for courses.
   - Implement new endpoints in `src/api/course_api.py` for assigning teachers and retrieving course data.

2. **API Layer Update**:
   - Implement the `POST /courses/{courseId}/assign-teacher` and `PUT /courses/{courseId}/update-teacher` endpoints in `src/api/course_api.py`.

3. **Validation Layer Implementation**:
   - Implement input validation in `src/validators/course_validator.py` to check for valid `courseId` and `teacher_id`.

4. **Database Migration**:
   - Use Alembic to create a migration script that will update the `courses` table to include the new `teacher_id` column:
     ```python
     from alembic import op
     from sqlalchemy import Column, Integer, ForeignKey

     def upgrade():
         op.add_column('courses', Column('teacher_id', Integer, ForeignKey('teachers.id'), nullable=True))

     def downgrade():
         op.drop_column('courses', 'teacher_id')
     ```

### 2. Testing Strategy
- **Unit Tests**: Create unit tests for the new API endpoints in `tests/test_course_api.py` and service methods in `tests/test_course_service.py`.
- **Integration Tests**: Verify end-to-end functionality for assigning teachers to courses through the API.

## VII. Error Handling & Validation

- Implement validation logic to enforce correct associations, rejecting requests for non-existent `teacher_id` or malformed requests.
- Return standardized error responses for invalid operations, including useful error messages for client-side debugging.

## VIII. Security Considerations

- Validate and sanitize all user inputs to prevent SQL injection and other malicious inputs.
- Ensure sensitive data, such as teacher emails or course information, is protected by proper access control.

## IX. Deployment Considerations

- Ensure the migration scripts are included in the deployment pipeline.
- Test the migration in a staging environment before deploying to production to confirm data integrity is maintained.

## X. Documentation

- Update `README.md` to document the new API endpoints related to teacher assignments.
- Ensure all new functions and classes have clear docstrings explaining their purpose and usage.

This implementation plan provides a comprehensive and structured approach to adding the teacher relationship within the course entity of the Student Management Web Application while ensuring compliance with existing architecture and practices. It maintains backward compatibility with existing data models and outlines the necessary modifications to integrate new functionality effectively.