# Implementation Plan: Add Teacher Relationship to Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Teacher Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Email Field to Student Entity

---

## Version
**Version**: 1.1.0

## Purpose
This implementation plan outlines the technical design for enhancing the Student Management Web Application by establishing a relationship between the Course and Teacher entities. This feature allows each course to be associated with a specific teacher, improving course management and reporting capabilities.

## Architecture Overview
- **Architecture Pattern**: RESTful API
- **Technology Stack**:
  - **Programming Language**: Python
  - **Web Framework**: Flask
  - **Database**: SQLite
  - **ORM**: SQLAlchemy
  - **Testing Framework**: pytest

## Module Boundaries and Responsibilities
1. **API Module**:
   - Introduce new API endpoints for assigning a teacher to a course and retrieving course details with teacher information.

2. **Data Access Layer**:
   - Update the existing SQLAlchemy Course model to include a new `teacher_id` foreign key relationship. This involves modifying the course schema and ensuring referential integrity.

3. **Testing Module**:
   - Develop tests for the new functionality including teacher assignment to courses and retrieval of course details with assigned teacher information.

## API Endpoints Design
### 1. Assign Teacher to Course
- **Endpoint**: `POST /api/v1/courses/{course_id}/assign_teacher`
- **Request Body**:
  ```json
  {
    "teacher_id": 1
  }
  ```
- **Response**:
  - **Success (200 OK)**:
    ```json
    {
      "message": "Teacher assigned successfully to course."
    }
    ```
  - **Error (400 Bad Request)**:
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Valid teacher ID must be provided."
      }
    }
    ```

### 2. Retrieve Course Details with Teacher Information
- **Endpoint**: `GET /api/v1/courses/{course_id}`
- **Response**:
  - **Success (200 OK)**:
    ```json
    {
      "id": 1,
      "title": "Mathematics",
      "description": "An introduction to mathematics.",
      "teacher": {
        "name": "John Doe",
        "email": "john.doe@example.com"
      }
    }
    ```
  - **Error (404 Not Found)**:
    ```json
    {
      "error": {
        "code": "E002",
        "message": "Course not found."
      }
    }
    ```

## Data Model
### Course Model Update
- **Table Name**: courses
  - Add to existing attributes:
    - `teacher_id`: Integer, foreign key referencing Teacher ID.

### SQLAlchemy Model Definition (Modifications)
```python
# models.py (modifications)
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Course(db.Model):
    __tablename__ = 'courses'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(512), nullable=True)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'), nullable=True)  # New column

    def __repr__(self):
        return f'<Course {self.title}>'
```

### Database Migration
- Create a migration script to add the `teacher_id` column to the `courses` table and enforce foreign key constraints:
  ```bash
  alembic revision --autogenerate -m "Add teacher_id to courses"
  ```

- The migration script will look like:
```python
def upgrade():
    with op.batch_alter_table('courses') as batch_op:
        batch_op.add_column(sa.Column('teacher_id', sa.Integer(), sa.ForeignKey('teachers.id'), nullable=True))

def downgrade():
    with op.batch_alter_table('courses') as batch_op:
        batch_op.drop_column('teacher_id')
```

## Implementation Steps
1. **Database Migration**:
   - Generate and apply a new migration script using Alembic to update the existing course schema.
   - Command to apply migration:
     ```bash
     alembic upgrade head
     ```

2. **Update Application Structure**:
   Ensure application structure accommodates new functionality:
   ```
   /student_management
   ├── src/
   │   ├── app.py
   │   ├── models.py  # Modify Course model to add teacher_id
   │   ├── routes.py  # Add new routes for course management
   │   ├── tests/
   │   │   ├── test_routes.py  # Add tests for new course functionality
   ├── config.py
   ├── requirements.txt
   ├── README.md
   ```

3. **Modify `routes.py`**:
   Implement logic for assigning a teacher to a course and retrieving course details.
```python
# routes.py (modifications)
from flask import request, jsonify
from .models import db, Course, Teacher

@app.route('/api/v1/courses/<int:course_id>/assign_teacher', methods=['POST'])
def assign_teacher_to_course(course_id):
    data = request.json
    teacher_id = data.get('teacher_id')
    
    if not teacher_id or not Teacher.query.get(teacher_id):
        return jsonify({'error': {'code': 'E001', 'message': 'Valid teacher ID must be provided.'}}), 400
    
    course = Course.query.get(course_id)
    if not course:
        return jsonify({'error': {'code': 'E002', 'message': 'Course not found.'}}), 404

    course.teacher_id = teacher_id
    db.session.commit()

    return jsonify({'message': 'Teacher assigned successfully to course.'}), 200

@app.route('/api/v1/courses/<int:course_id>', methods=['GET'])
def get_course_details(course_id):
    course = Course.query.get(course_id)
    if not course:
        return jsonify({'error': {'code': 'E002', 'message': 'Course not found.'}}), 404
    
    teacher = Teacher.query.get(course.teacher_id)
    teacher_info = {"name": teacher.name, "email": teacher.email} if teacher else None

    return jsonify({
        'id': course.id,
        'title': course.title,
        'description': course.description,
        'teacher': teacher_info
    }), 200
```

4. **Update Tests**:
   Create new tests in `tests/test_routes.py` for teacher assignment and course retrieval functionalities.
```python
def test_assign_teacher_to_course_succeeds(client):
    """Test assigning a teacher to a course."""
    payload = {"teacher_id": 1}  # Assuming Teacher ID 1 exists
    response = client.post('/api/v1/courses/1/assign_teacher', json=payload)
    assert response.status_code == 200
    assert response.get_json() == {'message': 'Teacher assigned successfully to course.'}

def test_get_course_details_includes_teacher(client):
    """Test retrieving course details including assigned teacher."""
    response = client.get('/api/v1/courses/1')  # Assuming Course ID 1 exists
    assert response.status_code == 200
    course_data = response.get_json()
    assert 'teacher' in course_data and course_data['teacher'] is not None
```

5. **Verify All Functionalities**:
   Confirm that all functionalities work as expected, particularly the automated tests for assigning a teacher to a course and retrieving course details with associated teacher information.

## Error Handling & Validation
- Validate inputs during teacher assignment to ensure the provided `teacher_id` exists.
- Return appropriate error codes and messages for invalid assignments.

## Security Considerations
- Sanitize all inputs on the API endpoints to guard against SQL injection vulnerabilities.
- Implement authentication and authorization checks for administrator-only operations.

## Testing Strategy
- **Unit Tests**: Validate the logic for assigning teachers and retrieving course details.
- **Integration Tests**: Use the pytest framework to validate the new API endpoints.

## Scalability Considerations
- The model for assigning teachers to courses is designed to support future enhancements such as dynamic reassignments or reporting.

## Logging & Monitoring
- Implement structured logging to capture key events during teacher assignments and data retrievals.

## Deployment Considerations
- Ensure health check endpoints remain functional and monitor responses after the implementation.

## Trade-offs & Decisions
- The focus on core functionality ensures rapid deployment while deferring complex relationship handling, adhering to good agile principles without over-complicating the initial implementation phases.

This implementation plan serves to methodically introduce the relationship between Teacher and Course entities, thereby enhancing the capabilities of the Student Management Web Application in accordance with the outlined specification.