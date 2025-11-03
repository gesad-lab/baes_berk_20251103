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
# Implementation Plan: Student Web Application

**Version**: 1.0.0  
**Purpose**: Technical implementation plan to add a relationship between the Course and Teacher entities in the existing student management system using FastAPI and SQLite.

---

## I. Architecture Overview

### 1.1 Overview
This implementation introduces a relationship between courses and teachers, enabling tracking of which teacher is responsible for each course. This will add two main functionalities: assigning a teacher to a course via a PATCH endpoint and retrieving course details along with the assigned teacher.

### 1.2 Modules
- **API Module**: Enhance the existing API module to include functionality for assigning teachers to courses and retrieving course details with teacher information.
- **Data Access Module**: Update models to reflect the new teacher relationship in the Course entity.
- **Validation Module**: Implement input validation to ensure integrity when assigning teachers to courses.

### 1.3 Technology Stack
- **Framework**: FastAPI (for API development)
- **Database**: SQLite (for data persistence)
- **ORM**: SQLAlchemy (to manage database interactions)
- **Testing**: pytest (for automated testing)

---

## II. Database Design

### 2.1 Schema Definition

- **Course Table** (updated)
  - `id`: Integer (Primary Key, automatically generated)
  - `name`: String (Required)
  - `level`: String (Required)
  - `teacher_id`: Integer (Foreign Key referencing Teacher entity)

### 2.2 Database Migration Strategy
1. Create a migration script to update the Course table structure:
   - Use Alembic for migration.
   - Add the `teacher_id` column to the existing Course table.
   - Ensure existing data remains intact.

   Migration Script Example (Current Migration Folder):
   ```python
   """Add teacher_id to courses table

   Revision ID: xxxxxxxx
   Revises: previous_revision_id
   Create Date: 2023-xx-xx xx:xx:xx.xxxxxx
   """
   
   from alembic import op
   import sqlalchemy as sa

   def upgrade():
       op.add_column('courses', sa.Column('teacher_id', sa.Integer, sa.ForeignKey('teachers.id'), nullable=True))

   def downgrade():
       op.drop_column('courses', 'teacher_id')
   ```

---

## III. API Design

### 3.1 Endpoints & Contracts

1. **Assign Teacher to Course**
   - **Endpoint**: `PATCH /courses/{course_id}`
   - **Request Body**: 
     ```json
     {
       "teacher_id": 1
     }
     ```
   - **Responses**:
     - **200 OK** (Success):
       ```json
       {
         "id": "integer",
         "name": "string",
         "level": "string",
         "teacher_id": "integer"
       }
       ```
     - **400 Bad Request** (Validation Error):
       ```json
       {
         "error": {
           "code": "E001",
           "message": "Invalid teacher_id provided."
         }
       }
       ```

2. **Retrieve Course Details**
   - **Endpoint**: `GET /courses/{course_id}`
   - **Responses**:
     - **200 OK** (Success):
       ```json
       {
         "id": "integer",
         "name": "string",
         "level": "string",
         "teacher": {
           "id": "integer",
           "name": "string"
         }
       }
       ```

### 3.2 Error Handling
- Return clear error messages if the `teacher_id` is invalid, or if the course does not exist, structured as follows:
  ```json
  {
    "error": {
      "code": "E002",
      "message": "Course not found."
    }
  }
  ```

---

## IV. Implementation Approach

### 4.1 Project Structure

```
/student_management_app
│
├── src/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── student.py       # Existing API logic for student endpoints
│   │   ├── course.py        # Existing API logic for course endpoints (modify here for new functionality)
│   │   ├── teacher.py       # Existing API logic for teacher endpoints
│   ├── db/
│   │   ├── __init__.py
│   │   ├── models.py        # Update existing models with Course model changes
│   │   ├── database.py      # Database initialization logic
│   ├── validations/
│   │   ├── __init__.py
│   │   ├── student_validators.py  # Existing validation logic for student
│   │   ├── course_validators.py   # Update existing validation logic for course
│   │   ├── teacher_validators.py   # Existing validation logic for teacher
│   ├── main.py              # FastAPI application entry point
│
├── tests/
│   ├── __init__.py
│   ├── test_student.py      # Existing tests for student management
│   ├── test_course.py       # Update existing tests for course management
│   ├── test_teacher.py      # Existing tests for teacher management
│
├── migrations/               # Directory for Alembic migration scripts
│
├── .env.example              # Environment configuration example
├── README.md                 # Project documentation
└── requirements.txt          # Project dependencies
```

### 4.2 Development Workflow
1. **Database Schema Updates**:
   - Modify `models.py` to include the `teacher_id` in the Course model.
   - Apply migrations using Alembic to adjust the schema for existing Course records.

2. **API Development**:
   - Update `course.py` to include implementations of the PATCH endpoint for assigning a teacher and modify the GET endpoint to return teacher details.
   - Update `course_validators.py` with necessary validations for the new `teacher_id`.

3. **Testing**:
   - Update `test_course.py` to cover the new features related to teacher assignments and ensure different scenarios are tested.
   - Implement new tests for validation errors specific to teacher IDs.

4. **Documentation**:
   - Update `README.md` to reflect new API endpoints and their usage, including examples.

---

## V. Testing Strategy

### 5.1 Test Coverage
- Ensure a minimum of 70% test coverage for the new functionality, especially for error handling and success pathways.

### 5.2 Test Types
- **Unit Tests**: For testing validation functions and CRUD operations.
- **Integration Tests**: Validate endpoint behavior with the database.
- **Contract Tests**: Verify that responses for PATCH and GET requests match expected API contracts.

### 5.3 Testing Framework
Utilize pytest to execute tests and check for coverage.

---

## VI. Security Considerations

### 6.1 Data Protection
- Validate that IDs (both course and teacher) are checked for existence before modification.
- Sanitize inputs to avoid vulnerabilities associated with invalid data.

### 6.2 HTTP Error Handling
- Specify appropriate error outputs for invalid requests, ensuring clarity for users and maintainers.

---

## VII. Deployment Considerations

### 7.1 Production Readiness
- Ensure the application has implemented health check endpoints to monitor services.
- Validate environment variables and check the migration paths for production readiness.

### 7.2 Configuration Management
- Maintain clear documentation in `.env.example` for required configuration settings.

---

## VIII. Documentation

### 8.1 Code Documentation
- Provide comprehensive docstrings in all new and modified functions and classes.

### 8.2 README.md
- Revise the documentation to clearly outline the new features, API endpoints, and usage examples.

---

## IX. Relevant Trade-offs & Decisions

1. **Backward Compatibility**: Careful attention has been paid to ensure that existing Course data remains valid and operational throughout the migration and implementation process.
2. **Modularity**: Changes are deliberately modular to promote scalability and maintainability, allowing for future features to be added with minimal friction.
3. **Error Handling Strategy**: Ensured that error messages are actionable to facilitate a better user experience.

---

This implementation plan provides a structured approach to integrate the Teacher relationship into the Course entity, thereby enriching the functionality of the student management system while adhering to existing architectural standards and practices.