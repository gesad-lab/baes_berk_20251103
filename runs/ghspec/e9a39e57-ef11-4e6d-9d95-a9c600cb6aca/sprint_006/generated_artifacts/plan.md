# Implementation Plan: Add Teacher Relationship to Course Entity

---

INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Teacher Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Student Entity Extensions

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Student Management Web Application

## I. Project Overview

- **Feature Name**: Add Teacher Relationship to Course Entity
- **Version**: 1.0.0
- **Purpose**: To establish a relationship between the Course and Teacher entities within the Student Management system, enabling administrators to assign teachers to courses, thereby improving resource management and curriculum alignment.

## II. Architecture

### 1. System Architecture
- The existing microservices architecture will be enhanced by adding a relationship between the Course service and the Teacher service, allowing seamless interaction and data retrieval involving both entities.

### 2. Technology Stack
- **Backend Framework**: Flask (Python)
- **Database**: SQLite (for local development, with migration to a relational DB for production)
- **API Format**: RESTful API with JSON responses
- **Testing Framework**: pytest for unit and integration tests
- **Development Environment**: Python 3.x

### 3. Key Components
- **Course Service**: Will be modified to handle interactions with the Teacher entity.
- **Teacher Service**: Will be extended to include new functionalities related to course assignments.
- **Database Layer**: `Course` table schema will be updated to include a foreign key reference to the `Teacher` entity.

## III. Module Design

### 1. Course Module
- **Responsibilities**:
  - Assigning a teacher to a course.
  - Retrieving course information, including teacher details.
  - Updating teacher assignments for courses.

### 2. Database Schema
- Modify the existing `Course` table schema to include:
    - `teacher_id`: INTEGER (nullable, foreign key referencing Teacher).
```sql
ALTER TABLE courses ADD COLUMN teacher_id INTEGER REFERENCES teachers(id);
```

### 3. Data Models
- **Course Model**:
```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)

    teacher = relationship("Teacher", back_populates="courses")
```

### 4. API Contracts
- **Assign Teacher to Course API**:
  - **Request**:
    - Method: POST
    - Endpoint: `/courses/{course_id}/assign_teacher`
    - Body: `{"teacher_id": 1}`
  - **Response**:
    - Status: 200 OK (if successful)
    - Body: `{"message": "Teacher assigned successfully.", "course": {...}}` or
    - Status: 400 Bad Request
    - Body: `{"error": {"code": "E002", "message": "Invalid teacher assignment."}}`

- **Retrieve Course Information API**:
  - **Request**:
    - Method: GET
    - Endpoint: `/courses/{course_id}`
  - **Response**:
    - Status: 200 OK
    - Body: `{"id": 1, "name": "Math 101", "level": "Beginner", "teacher_id": 1, "teacher": {"name": "John Doe", "email": "john.doe@example.com"}}` or
    - Status: 404 Not Found
    - Body: `{"error": {"code": "E001", "message": "Course not found"}}`

## IV. Implementation Approach

### 1. Setup & Configuration
- Existing project structure remains unchanged. All modifications and new modules will be integrated within the existing directory structure:
```
/src/
    /models/
        teacher.py  # Existing Teacher model
        course.py    # Modified Course model
    /routes/
        course_routes.py  # Update to include teacher assignment functionality
    /services/
    /config/
    /tests/
    /docs/
README.md
.env.example
```

### 2. Database Initialization & Migration
- Utilize Alembic to manage database migrations. A migration script will be created to update the `Course` table schema by adding the `teacher_id` column:
```python
from alembic import op
import sqlalchemy as sa

def upgrade():
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))
    op.create_foreign_key('fk_teacher', 'courses', 'teachers', ['teacher_id'], ['id'])

def downgrade():
    op.drop_constraint('fk_teacher', 'courses', type_='foreignkey')
    op.drop_column('courses', 'teacher_id')
```

### 3. API Development
- Modify `course_routes.py` to implement new endpoints for assigning and retrieving course-teacher relationships:
```python
@app.route('/courses/<int:course_id>/assign_teacher', methods=['POST'])
def assign_teacher(course_id):
    data = request.json
    teacher_id = data.get('teacher_id')
    # Logic to assign a teacher to a course
    return jsonify({"message": "Teacher assigned successfully.", "course": course_details}), 200

@app.route('/courses/<int:course_id>', methods=['GET'])
def get_course_info(course_id):
    # Logic to retrieve the course including teacher details
    return jsonify(course_details), 200
```

### 4. Input Validation
- Apply thorough validation to ensure the `teacher_id` exists in the `Teacher` table, and respond with meaningful error messages if not.

### 5. Unit & Integration Testing
- Create test cases ensuring functionalities related to the new teacher assignments. Tests should cover:
  - Successful teacher assignment.
  - Retrieval of course details including associated teacher data.
  - Appropriate response for assignment with invalid teacher IDs.
  
## V. Error Handling & Security

### 1. Error Handling
- All endpoints must handle errors gracefully and return structured responses for both valid and invalid requests.
- Implement logging for all error scenarios to assist in debugging.

### 2. Basic Security
- Ensure that any API endpoints provide sanitized responses to prevent exposure of sensitive information.
- Use environment variables for any sensitive settings such as database URIs and secret keys.

## VI. Deployment Considerations

### 1. Local Deployment
- Ensure that the application can run locally with the new endpoint for assigning teachers to courses included.
- Update `README.md` to provide information on new API endpoints and required migrations.

## VII. Documentation

### 1. API Documentation
- Update the API documentation to include details about new endpoints for assigning teachers to courses, including request/response formats.

### 2. Code Documentation
- Ensure all new and modified functions have appropriate docstrings explaining their purpose and functionality.

## VIII. Success Criteria
- Successful assignment and retrieval of teachers and courses through the defined API endpoints without errors.
- Proper handling of invalid data submissions with clear user feedback.
- The `courses` table updates correctly with the new `teacher_id` relationship without compromising existing integrity.
- Maintain test coverage of at least 70% for all functionalities introduced for teacher assignments.

---

This implementation plan outlines a comprehensive strategy for integrating the teacher relationship into the existing Course entity within the Student Management Web Application while ensuring secure, maintainable, and backward-compatible systems.