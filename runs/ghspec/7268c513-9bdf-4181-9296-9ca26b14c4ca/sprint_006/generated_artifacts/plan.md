# Implementation Plan: Add Teacher Relationship to Course Entity

---

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
# Implementation Plan: Add Course Entity

---

## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan: 
# Implementation Plan: Add Email Field to Student Entity

---

## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan: 
# Implementation Plan: Student Entity Management

## I. Project Overview
The goal of this implementation plan is to establish a relationship between the Course and Teacher entities within the existing student management system. This feature will facilitate efficient management of educational resources by allowing for the assignment of teachers to courses, ultimately enhancing scheduling, reporting, and tracking capabilities within the system.

## II. Technical Architecture

### 1. Architecture Overview
- **Type**: RESTful API
- **Framework**: Flask for Python
- **Database**: SQLite for lightweight and scalable local storage

### 2. Modular Design
- **Module 1: API Layer**
  - Responsible for handling incoming HTTP requests related to course-teacher assignment and routing them to appropriate service methods.

- **Module 2: Service Layer**
  - Handles the business logic for assigning teachers to courses, including validation and error responses.

- **Module 3: Data Access Layer**
  - Updates the existing Course model to include the teacher relationship and interacts with the SQLite database for performing operations.

## III. Technology Stack
- **Programming Language**: Python
- **Web Framework**: Flask
- **ORM**: SQLAlchemy for database abstraction
- **Database**: SQLite
- **Testing Framework**: pytest
- **Documentation**: Swagger for API documentation

## IV. API Contracts

### 1. Assign Teacher to Course
- **Endpoint**: `POST /courses/{course_id}/assign-teacher`
- **Request Body**: 
```json
{
    "teacher_id": 1
}
```
- **Response**:
  - Success: `200 OK`
    ```json
    {
        "id": 1,
        "name": "Mathematics",
        "level": "Beginner",
        "teacher_id": 1
    }
    ```
  - Error (invalid teacher ID): `400 Bad Request`
    ```json
    {
        "error": {
            "code": "E002",
            "message": "Teacher ID does not exist."
        }
    }
    ```
  
## V. Data Models

### 1. Updated Course Model
- Updating the existing Course model to include the `teacher_id` attribute:
```python
class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))  # Establishing the relationship
```

## VI. Implementation Steps

### Step 1: Environment Setup
- Ensure the Python virtual environment is activated.
- Install necessary packages: Flask, SQLAlchemy, and pytest.

### Step 2: Database Migration
- Create a migration script to add the `teacher_id` foreign key column to the existing `courses` table.
```python
def upgrade():
    op.add_column('courses', sa.Column('teacher_id', sa.Integer, sa.ForeignKey('teachers.id')))
```
- Ensure the migration maintains existing data integrity for students and courses.

### Step 3: Implement API Endpoints
- Create the `POST /courses/{course_id}/assign-teacher` endpoint in the API layer.
- Implement necessary routing logic to direct requests to the Teacher assignment service.

### Step 4: Validation Logic
- Validate the request body to ensure `teacher_id` is provided and exists in the teachers table.

### Step 5: Error Handling
- Implement structured error responses for cases where `teacher_id` is invalid or non-existent.

### Step 6: Write Tests
- Create unit tests to cover:
  - Successful assignment of a teacher to a course with valid data.
  - Error handling for invalid `teacher_id`.

### Step 7: Documentation
- Update API documentation to reflect the new endpoint `POST /courses/{course_id}/assign-teacher`.

## VII. Testing Strategy

### 1. Unit Tests
- Tests should cover:
  - Successful assignment of a teacher to a course with valid inputs.
  - Error handling when attempting to assign a teacher with an invalid ID.

### 2. Integration Tests
- Validate interactions between the API, service layer, and database to ensure correct functionality and persistence after assignment.

## VIII. Deployment Considerations

### 1. Production Readiness
- Ensure that the application starts successfully and runs the necessary migrations on startup, specifically for adding the `teacher_id` column.

### 2. Configuration Management
- Use environment variables for sensitive data and configuration options to maintain flexibility.

## IX. Security Considerations
- Validate all incoming requests to prevent SQL injections and ensure robust error handling practices.

## X. Monitoring & Logging
- Implement logging of API requests and responses without exposing sensitive data for error tracking.

## XI. Documentation
- Update the `README.md` file with instructions on how to set up, run, and use the API for assigning teachers to courses.

## XII. Reflection on Trade-offs
- The choice of SQLite allows for efficient handling of course and teacher records while maintaining backward compatibility with existing student data, supporting future features more effectively.

---

## Modifications to Existing Files

1. **Database Migration**:
   - Create a new migration file `migrations/xxxx_add_teacher_id_to_courses.py`:
   ```python
   from alembic import op
   import sqlalchemy as sa

   def upgrade():
       op.add_column('courses', sa.Column('teacher_id', sa.Integer, sa.ForeignKey('teachers.id')))

   def downgrade():
       op.drop_column('courses', 'teacher_id')
   ```

2. **API Layer**:
   - Update the routes in `routes.py` to include the teacher assignment endpoint:
   ```python
   from flask import Blueprint, request, jsonify
   from models.course import Course
   from models.teacher import Teacher
   from app import db

   courses_bp = Blueprint('courses', __name__)

   @courses_bp.route('/courses/<int:course_id>/assign-teacher', methods=['POST'])
   def assign_teacher_to_course(course_id):
       data = request.get_json()
       teacher_id = data.get('teacher_id')
       
       teacher = Teacher.query.get(teacher_id)
       course = Course.query.get(course_id)
       
       if not teacher:
           return jsonify({"error": {"code": "E002", "message": "Teacher ID does not exist."}}), 400
       
       if not course:
           return jsonify({"error": {"code": "E003", "message": "Course ID does not exist."}}), 404

       course.teacher_id = teacher_id
       db.session.commit()

       return jsonify({"id": course.id, "name": course.name, "level": course.level, "teacher_id": course.teacher_id}), 200
   ```

3. **Tests**:
   - Create or update tests in the `tests/test_course.py` file:
   ```python
   def test_assign_teacher_to_course(client):
       # Scenario: Successful assignment
       response = client.post('/courses/1/assign-teacher', json={"teacher_id": 1})
       assert response.status_code == 200
       assert response.json['teacher_id'] == 1

   def test_assign_teacher_with_invalid_teacher_id(client):
       # Scenario: Invalid teacher ID
       response = client.post('/courses/1/assign-teacher', json={"teacher_id": 999})  # Assumes teacher with ID 999 does not exist
       assert response.status_code == 400
       assert response.json['error']['code'] == "E002"
   ```

This comprehensive plan outlines the steps necessary to implement the Teacher relationship feature for the Course entity while ensuring compatibility and maintaining high-quality standards throughout the ongoing development process.