# Implementation Plan: Add Teacher Relationship to Course Entity

---

INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:  
# Implementation Plan: Create Teacher Entity

---

INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:  
# Implementation Plan: Add Course Relationship to Student Entity

## I. Overview

This document outlines the technical implementation plan for establishing a relationship between the Course and Teacher entities within the educational management system. This feature will allow courses to reference assigned teachers, thereby streamlining course management and enhancing the overall functionality of the educational management system.

## II. Architecture

### 1. System Architecture
- **Client-Server Architecture**: Same as existing architecture; the frontend communicates with the backend API.
- **API Layer**: The application exposes RESTful endpoints to manage course and teacher assignments.
- **Database**: SQLite remains in use, which will accommodate changes to both Course and Teacher entities via migrations.

### 2. Component Diagram
```plaintext
+---------------+                 +-----------------------+
|     Client    | <--- HTTP --->  |       API Layer       |
|  (Admin User) |                 |  (Flask/FastAPI)     |
+---------------+                 +-----------------------+
                                        |
                                        |
                                   +--------------+
                                   |   SQLite DB  |
                                   +--------------+
```

## III. Technology Stack

- **Backend Framework**: Flask
- **ORM**: SQLAlchemy
- **Database**: SQLite
- **Data Serialization**: Marshmallow (for validation and serialization)
- **Containerization**: Docker (optional for deployment)
- **Testing Framework**: pytest

## IV. Module Design

### 1. Module Boundaries
- **Course Management Module**: Responsible for operations related to the Course entity.
- **Teacher Management Module**: Functions remain unchanged from previous implementation.

### 2. API Endpoints
- **POST /courses/{courseId}/assign-teacher**
  - **Request**: 
    ```json
    {
      "teacher_id": 1
    }
    ```
  - **Response** (200 OK):
    ```json
    {
      "message": "Teacher assigned successfully.",
      "course": {
        "id": 1,
        "assigned_teacher_id": 1,
        "other_course_details": "..."
      }
    }
    ```
  - **Error Response** (400 Bad Request):
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Invalid Course ID or Teacher ID."
      }
    }
    ```

- **GET /courses/{courseId}**
  - **Response** (200 OK):
    ```json
    {
      "id": 1,
      "assigned_teacher": {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com"
      },
      "other_course_details": "..."
    }
    ```

### 3. Data Model
- **Course Entity**: 
  - `id`: Integer (Primary Key, auto-increment).
  - `teacher_id`: Integer (Foreign Key referencing `Teacher`).

## V. Implementation Approach

### 1. Development Steps
1. **Set Up Environment**: Ensure the virtual environment is active and install any necessary dependencies (Flask, SQLAlchemy, Marshmallow, pytest).

2. **Database Schema Migration**:
   - Use Alembic to create a migration script that adds a `teacher_id` foreign key to the `courses` table.
   - Maintain backward compatibility by ensuring existing relationships in the database are preserved.

   ```python
   from alembic import op
   import sqlalchemy as sa

   def upgrade():
       op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))
       op.create_foreign_key('fk_course_teacher', 'courses', 'teachers', 'teacher_id', 'id')

   def downgrade():
       op.drop_constraint('fk_course_teacher', 'courses', type_='foreignkey')
       op.drop_column('courses', 'teacher_id')
   ```

3. **API Development**:
   - Implement the `/courses/{courseId}/assign-teacher` endpoint to assign a teacher to a course, validating both IDs and handling error scenarios gracefully.
   - Use Marshmallow for schema validation and serialization when assigning teachers.

4. **Testing**:
   - Ensure the implementation is covered by unit and integration tests, maintaining a minimum of 70% coverage for business logic and 90% for validation.
   - Test scenarios including valid assignments, retrievals, and error handling for invalid IDs.

5. **Documentation**:
   - Update API documentation to reflect new endpoints and modify README to include setup instructions and usage examples.

### 2. Testing Strategies
- **Unit Tests**: Validate individual components such as input validation for course assignments.
- **Integration Tests**: Ensure that API endpoints function correctly within the application.
- **Contract Tests**: Verify that the API specification aligns with expected responses for all scenarios.

### 3. Error Handling and Validation
- Implement validation checks to verify both course and teacher IDs are provided correctly and refer to valid records. Log meaningful error messages when these validations fail.

## VI. Security Considerations

- Sanitize user inputs to avoid SQL injection vulnerabilities.
- Validate access control to ensure only authorized administrators can assign teachers to courses.

## VII. Deployment Considerations

### 1. Environment Configuration
- Document necessary environment variables in a `.env.example` file for any new configurations associated with teacher assignments.
- Ensure all configurations are correctly set before deployment.

### 2. Health Checks
- Extend the existing health check endpoint to verify the operational status of the course management functionality.

## VIII. Fail-Fast Philosophy

- Validate configurations during application startup, and ensure that all required fields for API endpoints are well-defined.
- Log actionable error messages if validation failures occur, preventing misleading application states.

## IX. Technical Trade-offs
- **Continued Use of SQLite**: While SQLite is sufficient for current operations, consider transitioning to a more robust solution if scalability or performance issues are encountered with concurrent operations in the future.

- **Synchronous API Calls**: Maintaining Flask for synchronous operations, but consider migrating to an asynchronous framework if future requirements dictate enhanced performance for concurrent requests.

## X. Documenting this Plan
This implementation plan will be shared under `implementation_plan_add_teacher_relationship_to_course_entity.md` in the project repository.

### Existing Code Modifications:
- **File: api/routes/courses.py** (Modify to include new API methods)
   ```python
   @courses_bp.route('/courses/<int:course_id>/assign-teacher', methods=['POST'])
   def assign_teacher(course_id):
       """Assign a teacher to a specific course."""
       data = request.json
       teacher_id = data.get('teacher_id')
       
       # Validate course and teacher IDs
       course = Course.query.get(course_id)
       teacher = Teacher.query.get(teacher_id)
       
       if not course or not teacher:
           return jsonify({"error": {"code": "E001", "message": "Invalid Course ID or Teacher ID."}}), 400

       course.teacher_id = teacher.id
       db.session.commit()

       return jsonify({"message": "Teacher assigned successfully.", "course": {
           "id": course.id,
           "assigned_teacher_id": course.teacher_id,
           "other_course_details": "..."
       }}), 200
   ```

- **File: models/course.py** (Modify to include teacher_id relationship)
   ```python
   from sqlalchemy import Integer, ForeignKey
   from sqlalchemy.orm import relationship
   
   class Course(db.Model):
       """Course model representing courses in the educational management system."""
       
       __tablename__ = 'courses'

       id = Column(Integer, primary_key=True, autoincrement=True)
       teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # New foreign key to Teacher

       teacher = relationship("Teacher", back_populates="courses")  # Establish a relationship to Teacher
       ...
   ```

- **File: models/teacher.py** (Add relationship to Course)
   ```python
   class Teacher(db.Model):
       """Teacher model to represent a teacher entity in the system."""
       
       __tablename__ = 'teachers'
       ...

       courses = relationship("Course", back_populates="teacher")  # Back-reference to courses this teacher instructs
   ```

- **File: tests/test_courses.py** (New test cases for course teacher assignment)
   ```python
   def test_assign_teacher_to_course_success(client):
       """Test assigning a teacher to a course successfully."""
       response = client.post('/courses/1/assign-teacher', json={
           'teacher_id': 1
       })
       assert response.status_code == 200
       assert response.get_json()['course']['assigned_teacher_id'] == 1

   def test_assign_teacher_to_invalid_course(client):
       """Test assignment to a non-existent course."""
       response = client.post('/courses/999/assign-teacher', json={
           'teacher_id': 1
       })
       assert response.status_code == 400
       assert 'Invalid Course ID or Teacher ID.' in response.get_json()['error']['message']

   def test_assign_teacher_to_invalid_teacher(client):
       """Test assignment with a non-existent teacher."""
       response = client.post('/courses/1/assign-teacher', json={
           'teacher_id': 999
       })
       assert response.status_code == 400
       assert 'Invalid Course ID or Teacher ID.' in response.get_json()['error']['message']
   ```

This structured implementation plan outlines the steps required to successfully integrate a teacher relationship into the existing course entity, adhering to the specified requirements while ensuring continuity in existing functionalities.