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
# Implementation Plan: Student Management Web Application

## 1. Overview
The objective of this implementation plan is to establish a relationship between the `Course` entity and the `Teacher` entity within the existing Student Management Web Application. This feature enables a Course to be associated with a specific Teacher, enhancing data integrity and resource management within the educational system.

## 2. Architecture
The existing microservice architecture will be updated to create a foreign key relationship that links the Course to the Teacher entity.

### 2.1 Module Breakdown
- **Course Service**: Modify the existing service that manages Course operations to support assignment of Teachers.
- **Database Layer**: The database schema will be enhanced to include a foreign key field `teacher_id` in the `courses` table.
- **API Layer**: New API endpoints will be added to assign a Teacher to a Course and retrieve Course details along with Teacher information.

## 3. Tech Stack
- **Programming Language**: Python
- **Web Framework**: Flask
- **Database**: SQLite
- **ORM**: SQLAlchemy for database interactions
- **Request Handling**: Marshmallow for request validation and serialization
- **Testing Framework**: pytest for unit and integration testing

## 4. Implementation Approach

### 4.1 Database Schema
An update to the `courses` table will be performed to add the foreign key `teacher_id`.

#### Updated Database Schema
- **Table**: courses
  - **Columns**:
    - Existing attributes (retained)
    - `teacher_id`: INTEGER (nullable, foreign key referencing the teachers table)

#### Migration Strategy
- Use Flask-Migrate to manage the schema migration, ensuring minimal disruption to existing data.
- The migration script will add a `teacher_id` column to the `courses` table without affecting existing student and course data.

Example migration code:
```python
from flask_migrate import migrate, op
import sqlalchemy as sa

def upgrade():
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))
    op.create_foreign_key('fk_teacher', 'courses', 'teachers', ['teacher_id'], ['id'])

def downgrade():
    op.drop_constraint('fk_teacher', 'courses', type_='foreignkey')
    op.drop_column('courses', 'teacher_id')
```

### 4.2 API Endpoints
The following API endpoints will be defined for assigning a Teacher and retrieving Course information:

1. **POST /courses/{course_id}/assign-teacher/{teacher_id}**
   - **Purpose**: Assign a Teacher to an existing Course.
   - **Response**:
     - **Success (200 OK)**:
       ```json
       {
         "message": "Teacher assigned successfully."
       }
       ```
     - **Error (400 Bad Request)**:
       ```json
       {
         "error": {
           "code": "E001",
           "message": "Invalid course or teacher ID."
         }
       }
       ```

2. **GET /courses/{course_id}**
   - **Purpose**: Retrieve detailed information about a Course, including Teacher details.
   - **Response**:
     - **Success (200 OK)**:
       ```json
       {
         "course": {
           "id": 1,
           "name": "Math 101",
           "teacher": {
             "name": "John Doe",
             "email": "johndoe@example.com"
           }
         }
       }
       ```

### 4.3 Functionality Implementation
- **Model Updates**: Update the existing SQLAlchemy model for `Course` to include `teacher_id`.
  ```python
  class Course(db.Model):
      __tablename__ = 'courses'
      id = db.Column(db.Integer, primary_key=True)
      name = db.Column(db.String, nullable=False)
      teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'), nullable=True)
  
      teacher = db.relationship('Teacher', backref='courses')
  ```

- **Routes and Controllers**: Implement Flask routes to handle the logic for assigning a Teacher and retrieving Course details.
  
- **Example Route Implementation**:
  ```python
  @app.route('/courses/<int:course_id>/assign-teacher/<int:teacher_id>', methods=['POST'])
  def assign_teacher(course_id, teacher_id):
      course = Course.query.get(course_id)
      teacher = Teacher.query.get(teacher_id)

      if not course or not teacher:
          return jsonify(error={'code': 'E001', 'message': 'Invalid course or teacher ID.'}), 400

      course.teacher_id = teacher.id
      db.session.commit()

      return jsonify(message='Teacher assigned successfully.'), 200

  @app.route('/courses/<int:course_id>', methods=['GET'])
  def get_course_details(course_id):
      course = Course.query.filter_by(id=course_id).first()
      if not course:
          return jsonify(error={'code': 'E002', 'message': 'Course not found.'}), 404

      return jsonify(course={
          "id": course.id,
          "name": course.name,
          "teacher": {
              "name": course.teacher.name,
              "email": course.teacher.email
          } if course.teacher else None
      }), 200
  ```

### 4.4 Testing Strategy
- **Unit Tests**: Create unit tests for the Course entity, especially for assigning Teachers and retrieving Course information.
- **Integration Tests**: Validate that API endpoints function correctly by using test data.
- Test coverage targets:
  - Minimum 70% coverage for business logic related to Course and Teacher assignments.
  - 90%+ coverage for critical API paths, such as course assignment and retrieval.

## 5. Security Considerations
- Validate all input IDs to prevent unauthorized access to resources.
- Return clear error messages without exposing sensitive information.

## 6. Error Handling & Validation
- Return error messages for invalid operations:
  - Invalid course or teacher IDs.
  - Appropriate status codes for each error condition.

Example error handling structure:
```python
if not course or not teacher:
    return jsonify(error={'code': 'E001', 'message': 'Invalid course or teacher ID.'}), 400
```

## 7. Deployment Considerations
- Ensure local testing passes successfully before migration to the production environment.
- Monitor API performance after deployment to catch any issues related to the new functionality.

## 8. Documentation
- Update the API documentation to include descriptions of the `/assign-teacher` and detailed Course retrieval endpoints.
- Update `README.md` to reflect setup instructions for the new features.

## 9. Technical Trade-offs
- Stick with SQLite as the current database choice for consistency, noting that it may impose limitations as user load increases. Consider a transition to a more robust relational database such as PostgreSQL in the future.
- Use Flask due to its simplicity and existing ecosystem to minimize learning curve and implementation time.

## 10. Success Metrics
- Successful execution of Teacher assignments and Course retrieval operations.
- Ensure that the data integrity remains intact and that existing functionalities for Courses are still operational post-implementation.
- Validate that the migration executes correctly without data loss.

### Existing Code Files Modifications
File: `app/models.py` (Update Course model to add `teacher_id`):
```python
class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'), nullable=True)

    teacher = db.relationship('Teacher', backref='courses')
```

File: `app/routes.py` (Add new routes for course assignments):
```python
@app.route('/courses/<int:course_id>/assign-teacher/<int:teacher_id>', methods=['POST'])
def assign_teacher(...):
    # Implementation for assigning a teacher to a course

@app.route('/courses/<int:course_id>', methods=['GET'])
def get_course_details(...):
    # Implementation for getting course details including assigned teacher
```

File: `tests/test_api/test_course.py` (New Test Cases for Course API):
```python
import pytest
from app import create_app, db
from app.models import Teacher, Course  # Ensure Course and Teacher models are imported
from http import HTTPStatus

@pytest.fixture
def client():
    app = create_app({'TESTING': True})
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create schema for testing
            yield client
            db.drop_all()  # Clean up after testing

def test_assign_teacher_to_course(client):
    # Create a sample course and teacher, then test assignment

def test_view_course_with_teacher(client):
    # Assign a teacher to a course and test retrieval

def test_assign_teacher_invalid_course(client):
    # Attempt to assign a teacher to a non-existent course
```

This implementation plan outlines the necessary steps to create a robust mechanism for assigning Teachers to Courses while maintaining existing features and data integrity in the Student Management Web Application.