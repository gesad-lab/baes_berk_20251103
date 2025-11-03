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

## Version
**Version**: 1.1.0

## Purpose
This implementation plan outlines the technical design for enhancing the Student Management Web Application by establishing a relationship between the Student and Course entities, allowing students to enroll in multiple courses. This feature enhances the tracking of student course participation, improving the application's educational management capabilities.

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
   - Extend existing endpoints and create new ones for enrolling students in courses and retrieving course enrollments.

2. **Data Access Layer**:
   - Update the SQLAlchemy models to incorporate the new many-to-many relationship between Student and Course through a junction table.

3. **Testing Module**:
   - Create tests to validate the new enrollment functionality and course retrieval, ensuring compliance with specifications.

## API Endpoints Design
### 1. Enroll Student in Course
- **Endpoint**: `POST /api/v1/enroll`
- **Request Body**:
  ```json
  {
    "student_id": 1,
    "course_id": 1
  }
  ```
- **Response**:
  - **Success (200 OK)**:
    ```json
    {
      "message": "Student enrolled in course successfully"
    }
    ```
  - **Error (400 Bad Request)**:
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Invalid student ID or course ID"
      }
    }
    ```

### 2. Retrieve Student Courses
- **Endpoint**: `GET /api/v1/students/{student_id}/courses`
- **Response**:
  - **Success (200 OK)**:
    ```json
    {
      "student_id": 1,
      "courses": [
        {
          "id": 1,
          "name": "Mathematics",
          "level": "Intermediate"
        },
        {
          "id": 2,
          "name": "History",
          "level": "Beginner"
        }
      ]
    }
    ```

## Data Model
### StudentCourses (Junction Table)
- **Table Name**: student_courses
  - `student_id`: Integer, foreign key referencing the Student entity.
  - `course_id`: Integer, foreign key referencing the Course entity.

### SQLAlchemy Model Updates
```python
# models.py (modifications)
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class StudentCourses(db.Model):
    __tablename__ = 'student_courses'
    
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), primary_key=True)

    student = db.relationship('Student', backref='enrollments')
    course = db.relationship('Course', backref='enrolled_students')
```

## Implementation Steps
1. **Database Migration**:
   - Create a migration script to add the `student_courses` junction table.
   - Using Alembic, create the migration script:
     ```bash
     alembic revision --autogenerate -m "Create student_courses table"
     ```
   - Migration script will look like:
     ```python
     def upgrade():
         op.create_table(
             'student_courses',
             sa.Column('student_id', sa.Integer(), nullable=False),
             sa.Column('course_id', sa.Integer(), nullable=False),
             sa.ForeignKeyConstraint(['student_id'], ['students.id']),
             sa.ForeignKeyConstraint(['course_id'], ['courses.id']),
             sa.PrimaryKeyConstraint('student_id', 'course_id')
         )

     def downgrade():
         op.drop_table('student_courses')
     ```

2. **Update Application Structure**:
   Ensure application structure accommodates new functionality:
   ```
   /student_management
   ├── src/
   │   ├── app.py
   │   ├── models.py  # Update for StudentCourses model
   │   ├── routes.py  # Add new routes for enrollment
   │   ├── tests/
   │   │   ├── test_routes.py  # Add tests for new endpoints
   ├── config.py
   ├── requirements.txt
   ├── README.md
   ```

3. **Modify `routes.py`**:
   Implement logic for the enrollment endpoint (`POST /api/v1/enroll`) and modify retrieval for courses associated with a student (`GET /api/v1/students/{student_id}/courses`).

4. **Update Tests**:
   Add tests in `tests/test_routes.py` for the new functionality:
   - **New Test Cases**:
     - `test_enroll_student_in_course_succeeds()`
     - `test_get_student_courses_returns_correct_data()`

```python
def test_enroll_student_in_course_succeeds(client):
    """ Test enrolling a student in a course """
    response = client.post('/api/v1/enroll', json={'student_id': 1, 'course_id': 1})
    assert response.status_code == 200
    assert response.get_json() == {'message': 'Student enrolled in course successfully'}

def test_get_student_courses_returns_correct_data(client):
    """ Test retrieving all courses for a student """
    response = client.get('/api/v1/students/1/courses')
    assert response.status_code == 200
    assert 'courses' in response.get_json()
```

5. **Run Database Migration**:
   Apply the migration to the development database:
   ```bash
   alembic upgrade head
   ```

6. **Verify All Functionalities**:
   Confirm that all functionalities work as expected, particularly the automated tests for enrollment and retrieval scenarios.

## Error Handling & Validation
- Validate input when enrolling a student, ensuring both `student_id` and `course_id` are provided and valid:
  - Return a 400 error with a message if the IDs are invalid.

## Security Considerations
- Sanitize and validate all inputs on the API endpoints to prevent SQL injection or other types of attacks.

## Testing Strategy
- **Unit Tests**: Validate individual logic for the `StudentCourses` model.
- **Integration Tests**: Use the pytest framework to validate the new API endpoints.

## Scalability Considerations
- The use of a junction table for many-to-many relationships is designed to scale with the application as the number of courses and students grows.

## Logging & Monitoring
- Implement structured logging for events related to course enrollments and errors.

## Deployment Considerations
- Ensure the application maintains existing health check endpoints and responds correctly after the implementation.

## Trade-offs & Decisions
- Enhancements are focused primarily on the backend with minimal overhead, ensuring quick deployment without compromising system integrity or performance.
- Advanced validation or other relationship complexities will be deferred for future iterations, following agile principles.

This implementation plan provides detailed steps to enhance the Student Management Web Application by linking students with courses, ensuring adherence to the specification and maintaining backward compatibility.