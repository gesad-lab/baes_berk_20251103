# Implementation Plan: Add Teacher Relationship to Course Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

**Previous Sprint Plan:**  
# Implementation Plan: Create Teacher Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

**Previous Sprint Plan:**  
# Implementation Plan: Add Course Relationship to Student Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

**Previous Sprint Plan:**  
# Implementation Plan: Create Course Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

**Previous Sprint Plan:**  
# Implementation Plan: Add Email Field to Student Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

**Previous Sprint Plan:**  
# Implementation Plan: Student Management Web Application

## I. Architecture Overview

The existing architecture of the Student Management Web Application will be expanded to establish a relationship between the `Course` and `Teacher` entities. This includes enhancements in the API layer for new endpoints, updates to the database schema for maintaining relationships, and ensuring that existing functionality remains uninterrupted.

## II. Technology Stack

- **Programming Language:** Python 3.11+
- **Web Framework:** FastAPI
- **Data Persistence:** SQLite
- **Data Access Library:** SQLAlchemy
- **Testing Framework:** Pytest
- **Dependency Management:** Poetry
- **Configuration Management:** Environment variables and a `.env` file

## III. Module Boundaries and Responsibilities

### 1. API Layer
- **Routes**:
  - `PUT /courses/{course_id}/assign-teacher`: Assign a teacher to a course.
  - `DELETE /courses/{course_id}/unassign-teacher`: Remove the association of a teacher from a course.

### 2. Service Layer
- **CourseService**: 
  - `assign_teacher(course_id: int, teacher_id: int)`: Assign a teacher to a course.
  - `unassign_teacher(course_id: int)`: Unassign a teacher from a course.

### 3. Data Layer
- **Database Configuration and Models**:
  - **Course Model** (existing):
    ```python
    from sqlalchemy import Column, Integer, String, ForeignKey
    from sqlalchemy.ext.declarative import declarative_base

    Base = declarative_base()

    class Course(Base):
        __tablename__ = 'courses'
        id = Column(Integer, primary_key=True, autoincrement=True)
        name = Column(String, nullable=False)
        teacher_id = Column(Integer, ForeignKey('teachers.id'))

        # Add relationship to Teacher
        teacher = relationship("Teacher", back_populates="courses")
    ```

  - **Teacher Model** (existing, no changes):
    ```python
    from sqlalchemy import Column, Integer, String
    from sqlalchemy.ext.declarative import declarative_base

    Base = declarative_base()

    class Teacher(Base):
        __tablename__ = 'teachers'
        
        id = Column(Integer, primary_key=True, autoincrement=True)
        name = Column(String, nullable=False)
        email = Column(String, nullable=False, unique=True)
    ```

## IV. API Contracts

### 1. Assign Teacher to Course Endpoint
- **Endpoint:** `PUT /courses/{course_id}/assign-teacher`
- **Request**:
  ```json
  {
    "teacher_id": 1
  }
  ```
- **Response**:
  - **Success** (200 OK):
    ```json
    {
      "id": 1,
      "name": "Mathematics",
      "teacher_id": 1
    }
    ```
  - **Error** (404 Not Found):
    - If the specified course or teacher does not exist:
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Course not found."
      }
    }
    ```

### 2. Remove Teacher from Course Endpoint
- **Endpoint:** `DELETE /courses/{course_id}/unassign-teacher`
- **Response**:
  - **Success** (200 OK):
    ```json
    {
      "id": 1,
      "message": "Teacher unassigned successfully."
    }
    ```

## V. Database Schema

### Migration Strategy
We will create a migration to add the `teacher_id` foreign key to the `courses` table, ensuring that existing data is not lost.

1. Create a migration file to succeed the changes to the `courses` table:
   ```python
   from alembic import op
   import sqlalchemy as sa

   def upgrade():
       op.add_column('courses', sa.Column('teacher_id', sa.Integer, sa.ForeignKey('teachers.id'), nullable=True))

   def downgrade():
       op.drop_column('courses', 'teacher_id')
   ```

## VI. Implementation Approach

1. **Setup Development Environment**:
   - Ensure the development environment is set up with dependencies installed via Poetry.
   - Update the `.env` file as necessary.

2. **Modify API Endpoints**:
   - Add the `PUT /courses/{course_id}/assign-teacher` and `DELETE /courses/{course_id}/unassign-teacher` routes to FastAPI.
   - Implement the endpoints to handle requests, including necessary business logic and error responses.

3. **Implement Service Logic**:
   - Create a `CourseService` class with the following methods to manage relationships:
   ```python
   class CourseService:
       def assign_teacher(self, course_id: int, teacher_id: int):
           # Logic to check if course and teacher exist
           # Update the course record with the new teacher_id
       
       def unassign_teacher(self, course_id: int):
           # Logic to set teacher_id to None for the specified course
   ```

4. **Database Layer with SQLAlchemy**:
   - Update the `Course` model to include the `teacher_id` foreign key.
   - Implement methods in `CourseService` to interact with courses.

5. **Create Tests**:
   - Add tests in `tests/api/test_routes.py` for the new API endpoints:
     - Validate successful assignment of a teacher to a course.
     - Validate error handling for assigning to non-existent courses/teachers.
     - Validate successful unassignment of a teacher from a course.
   - Add tests in `tests/services/test_course_service.py` to cover business logic for assigning and unassigning teachers.

6. **Documentation**:
   - Update the API documentation with new request and response structures for `assign` and `unassign` operations.
   - Ensure all modifications are documented in the codebase.

7. **Run Migrations**:
   - Run the migration to update the `courses` table.

## VII. Security & Error Handling

- **Input Validation**: Ensure that the `teacher_id` provided corresponds to an existing teacher.
- **Structured Error Responses**: Clearly defined error formats for invalid requests as per the outlined API contracts.

## VIII. Testing Strategies

- Implement unit tests for the `CourseService` to cover:
  - Successful assignment and unassignment of teachers.
  - Error handling for missing courses or teachers.
- Implement integration tests to validate the API responses meet the defined specifications.

## IX. Monitoring & Logging

- Utilize structured logging to capture request and error details related to course-teacher assignments.
- Implement health check endpoints to monitor the availability of the API.

## X. Success Criteria

1. Teachers must be successfully assigned to courses via the API.
2. JSON responses containing the course's updated details are returned as expected.
3. Appropriate error messages are generated when trying to assign non-existent teachers or courses.
4. Existing data in the Student and Course tables remains unaffected after schema changes.

## Existing Code Files Modifications

- **`src/main.py`:** 
  - Add routes for `PUT /courses/{course_id}/assign-teacher` and `DELETE /courses/{course_id}/unassign-teacher`.
- **`src/models.py`:** 
  - Update the `Course` model with `teacher_id` foreign key.
- **`src/services/course_service.py`:**
  - Implement the assignment and unassignment logic in the `CourseService`.
- **`tests/api/test_routes.py`:** 
  - Add tests for the assignment and unassignment endpoints.
- **`tests/services/test_course_service.py`:** 
  - Create new tests to validate the business logic in the `CourseService`.

By adhering to this implementation plan, we will effectively integrate the teacher-student relationship into the existing architecture while ensuring all modifications are in accordance with the coding standards and architectural practices established in previous sprints.