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
# Implementation Plan: Student Management Web Application

## I. Project Overview

- **Feature Name**: Add Course Relationship to Student Entity
- **Version**: 1.0.0
- **Purpose**: To enhance the existing Student Management system by establishing a relationship between Students and Courses, allowing for efficient management of student enrollments in multiple courses.

## II. Architecture

### 1. System Architecture
- The existing microservices architecture remains unchanged, integrating the new functionality for course registrations within the Student Management service. This enhancement will facilitate user management of students' course enrollments without impacting current system operations.

### 2. Technology Stack
- **Backend Framework**: Flask (Python)
- **Database**: SQLite (embedded database for easier local development)
- **API Format**: RESTful API with JSON responses
- **Testing Framework**: pytest for unit and integration tests
- **Development Environment**: Python 3.x

### 3. Key Components
- **Student Service**: Existing service responsible for managing student data.
- **Course Service**: Existing service that manages course-related operations (as implemented in previous sprint).
- **StudentCourses Service**: New module introducing functionalities related to the junction between students and courses.
- **Database Layer**: Introduce a new `student_courses` junction table schema to manage the many-to-many relationship.

## III. Module Design

### 1. StudentCourses Module
- **Responsibilities**:
  - Enrolling a student in a course.
  - Retrieving courses for a student.
  - Removing a student from a course.

### 2. Database Schema
- New `student_courses` junction table schema to be defined:
    - `student_id`: INTEGER NOT NULL (Foreign key referencing the Student entity).
    - `course_id`: INTEGER NOT NULL (Foreign key referencing the Course entity).

### 3. Data Models
- **StudentCourses Model**:
  ```python
  from sqlalchemy import Column, Integer, ForeignKey
  from sqlalchemy.orm import relationship
  from src.database import Base

  class StudentCourses(Base):
      __tablename__ = 'student_courses'
      student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
      course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

      student = relationship("Student", back_populates="courses")
      course = relationship("Course", back_populates="students")
  ```

### 4. API Contracts
- **Enroll Student in Course API**:
  - **Request**:
    - Method: POST
    - Endpoint: `/students/{student_id}/courses`
    - Body: `{"course_id": 1}`
  - **Response**:
    - Status: 200 OK
    - Body: `{"student_id": 1, "course_id": 1}`

- **Retrieve Student Courses API**:
  - **Request**:
    - Method: GET
    - Endpoint: `/students/{student_id}/courses`
  - **Response**:
    - Status: 200 OK
    - Body: `[{"course_id": 1, "name": "Introduction to Python", "level": "beginner"}]` or
    - Status: 404 Not Found
    - Body: `{"error": {"code": "E001", "message": "Student not found"}}`

- **Remove Student from Course API**:
  - **Request**:
    - Method: DELETE
    - Endpoint: `/students/{student_id}/courses/{course_id}`
  - **Response**:
    - Status: 200 OK
    - Body: `{"message": "Student removed from course."}` or
    - Status: 404 Not Found
    - Body: `{"error": {"code": "E002", "message": "Course not found"}}`

## IV. Implementation Approach

### 1. Setup & Configuration
- Update the existing Flask application structure as follows:
  ```
  /src/
      /models/
          student.py  # existing student model
          course.py    # existing course model
          student_courses.py  # new StudentCourses model
      /routes/
          student_routes.py  # existing routes for students
          course_routes.py    # existing routes for courses
          student_courses_routes.py  # new routes for student-course relationships
      /services/
      /config/
  /tests/
  /docs/
  README.md
  .env.example
  ```

### 2. Database Initialization & Migration
- Utilize Alembic to manage database migrations. A migration script will be created to add the new `student_courses` junction table to the existing database:
  - Migration script will include:
    ```python
    from alembic import op
    import sqlalchemy as sa

    def upgrade():
        op.create_table('student_courses',
            sa.Column('student_id', sa.Integer(), nullable=False),
            sa.Column('course_id', sa.Integer(), nullable=False),
            sa.ForeignKeyConstraint(['student_id'], ['students.id']),
            sa.ForeignKeyConstraint(['course_id'], ['courses.id']),
            sa.PrimaryKeyConstraint('student_id', 'course_id')
        )
    
    def downgrade():
        op.drop_table('student_courses')
    ```

### 3. API Development
- Implement new API routes in `student_courses_routes.py`:
  - Define `/students/{student_id}/courses` for enrolling students in courses and retrieving student courses.
    - Example API methods:
    ```python
    @app.route('/students/<int:student_id>/courses', methods=['POST'])
    def enroll_student():
        data = request.json
        course_id = data.get('course_id')
        # Validate student ID and course ID existence
        # Logic to associate student with the course
        return jsonify({"student_id": student_id, "course_id": course_id}), 200
        
    @app.route('/students/<int:student_id>/courses', methods=['GET'])
    def get_student_courses():
        # Logic to retrieve courses for the specified student
        return jsonify(courses), 200
    ```

### 4. Input Validation
- Implement validation for the `student_id` and `course_id` fields at the API layer to ensure user-friendly and actionable error messages.
  - Check for valid IDs against existing Student and Course records.

### 5. Unit & Integration Testing
- Create test cases to ensure functionalities:
  - Test for successful enrollment, retrieval of courses, and removal from courses.
  - Include tests for invalid scenarios and maintain at least 70% code coverage on the integration of student-course relationships.

## V. Error Handling & Security

### 1. Error Handling
- Implement structured error responses for invalid enrollment scenarios (e.g., missing fields or invalid IDs).
- Log errors accurately while providing user-friendly error messages.

### 2. Basic Security
- Maintain proper logging methods to avoid exposure of sensitive data.
- Ensure the use of environment variables for sensitive configuration settings.

## VI. Deployment Considerations

### 1. Local Deployment
- Ensure the application can run locally after the integration of course enrollment functionality.
- Update the `README.md` file to reflect new API endpoints and information about migrations.

## VII. Documentation

### 1. API Documentation
- Update and document new API routes in the documentation (including input/output examples for the student-course relationship APIs).
- Ensure all changes are well-documented in the `README.md`.

### 2. Code Documentation
- Add relevant docstrings to all new public functions and classes, detailing the purpose and functionality of the `StudentCourses` entity and routes.

## VIII. Success Criteria
- Successful enrollment and retrieval of course entries for students according to validation rules.
- Correct management and logging of errors for specified scenarios.
- The `student_courses` junction table is established and migrated without affecting existing data.
- Maintain at least 70% test coverage for all new functionalities introduced with the student-course relationship features.

--- 

This implementation plan outlines a strategy for integrating course relationships into the Student Management Web Application, ensuring secure, maintainable, and backward-compatible systems during the development process.