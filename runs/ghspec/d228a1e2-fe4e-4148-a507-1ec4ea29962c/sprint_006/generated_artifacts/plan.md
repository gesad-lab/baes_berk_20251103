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
# Implementation Plan: Add Email Field to Student Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Student Entity Management in Web Application

## Version: 1.0.0

## 1. Overview
This implementation plan outlines the steps required to establish a relationship between the existing `Course` entity and the newly created `Teacher` entity. This feature enhances the application by clarifying which teacher is responsible for each course, thereby supporting better management of educational resources.

## 2. Architectural Design
### 2.1 High-Level Architecture
- **Client**: Any HTTP client (Postman, Curl, etc.) to interact with the new API for managing teacher-course relationships.
- **API Layer**: RESTful API endpoints to assign teachers to courses, retrieve course details, and list courses by teacher.
- **Service Layer**: Business logic for managing teacher assignments, retrieving course details, and listing courses.
- **Data Access Layer**: Interfaces with the `Course` model to perform CRUD operations related to assigning teachers.
- **Database**: Includes updated schema for the Course entity with a foreign key linking to the Teacher entity.

### 2.2 Technology Stack
The technology stack remains consistent with previous sprints:
- **Programming Language**: Python
- **Web Framework**: Flask
- **Database**: SQLite (with PostgreSQL as an option for production)
- **ORM**: SQLAlchemy
- **Testing Framework**: pytest
- **API Documentation**: Swagger (Flasgger)
- **Dependency Management**: pip with a `requirements.txt` file

## 3. Module Boundaries and Responsibilities
- **API Layer**: Implement endpoints for the following functionalities:
  - `POST /courses/{course_id}/assign-teacher` for assigning a teacher to a course.
  - `GET /courses/{course_id}` for retrieving course details including assigned teacher information.
  - `GET /teachers/{teacher_id}/courses` for listing courses assigned to a specific teacher.
  
- **Service Layer**: Implement service methods to handle:
  - Teacher assignment to courses.
  - Retrieving course details along with assigned teacher information.
  - Listing courses by teacher.

- **Data Access Layer**: Manage interactions with the `Course` model to accommodate the teacher assignments.

## 4. Data Models
### 4.1 Updated Course Model
```python
from sqlalchemy import Column, Integer, String, ForeignKey
from app import db

class Course(db.Model):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # Foreign key to Teacher
```

## 5. Database Migration
- A migration script will be created to add the `teacher_id` field to the existing `courses` table while preserving existing data.
- We will utilize Flask-Migrate to manage the migration process.

### Migration Script Example
```python
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app import app, db

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

# Define migration for updating the courses table
def upgrade():
    with op.batch_alter_table('courses') as batch_op:
        batch_op.add_column(sa.Column('teacher_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_teacher', 'teachers', ['teacher_id'], ['id'])

def downgrade():
    with op.batch_alter_table('courses') as batch_op:
        batch_op.drop_constraint('fk_teacher', 'courses')
        batch_op.drop_column('teacher_id')
```

## 6. API Contracts
### 6.1 Assign Teacher to Course API Endpoint
- **Method**: POST
- **URL**: `/courses/{course_id}/assign-teacher`
- **Request Body**:
  ```json
  {
    "teacher_id": 1
  }
  ```
- **Response**:
  - Success (200 OK):
  ```json
  {
    "message": "Teacher assigned to course successfully"
  }
  ```
  - Error (400 Bad Request):
  ```json
  {
    "error": {
      "code": "E001",
      "message": "Invalid input: Teacher ID is required"
    }
  }
  ```

### 6.2 Get Course Details API Endpoint
- **Method**: GET
- **URL**: `/courses/{course_id}`
- **Response** (200 OK):
```json
{
  "id": 1,
  "title": "Course Title",
  "teacher": {
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
}
```

### 6.3 List Courses by Teacher API Endpoint
- **Method**: GET
- **URL**: `/teachers/{teacher_id}/courses`
- **Response** (200 OK):
```json
[
  {
    "id": 1,
    "title": "Course Title 1"
  },
  {
    "id": 2,
    "title": "Course Title 2"
  }
]
```

## 7. Implementation Approach
### 7.1 Environment Setup
1. Ensure `requirements.txt` includes any dependencies required for the teacher assignment features.
2. Install dependencies in a virtual environment:
   ```bash
   pip install -r requirements.txt
   ```

### 7.2 Development Phases
1. **Database Migration**: Generate and apply the migration for the `courses` table to include `teacher_id`.
2. **API Endpoint Implementation**: 
   - Create the endpoint for assigning teachers, fetching course details, and listing courses per teacher in `app/routes.py`.
3. **Service Logic Implementation**:
   - Implement service methods for assigning teachers, retrieving course details, and listing courses.
4. **Error Handling Implementation**: 
   - Ensure compliance with specified error handling protocols in all API responses.
5. **Testing**: 
   - Write unit tests for the new API features, ensuring at least 70% coverage.

## 8. Success Criteria
- The application allows for assigning teachers to courses, retrieving course details with teacher information, and listing courses per teacher through the specified endpoints, along with appropriate error handling and HTTP status codes.
- Each endpoint achieves the 70% test coverage target for business logic.

## 9. Deployment Considerations
- Ensure deployment configurations account for the new database schema changes.
- Update API documentation using Swagger to reflect the new features and endpoints regarding teacher-course relationships.

## 10. Configuration Management
- Include necessary configurations for any environment variables related to the new functionalities and ensure existing configurations are unaffected for backward compatibility.

## 11. Logging & Monitoring
- Implement structured logging to trace actions related to teacher assignments and course details retrieval, capturing success, failure, and error scenarios.

## 12. Future Considerations
Future improvements may include:
- Implementing user roles to manage and authorize teacher-course assignments.
- Enhancing features for tracking multiple teachers assigned to a single course or advanced functionalities such as course ratings or evaluations.

---

### Existing Code Files Modifications
- **File**: `app/models.py` (Modify Course model to add `teacher_id` field).
- **File**: `app/routes.py` (Add API endpoints for assigning teachers to courses and retrieval).
- **File**: `tests/api/test_course_teacher_api.py` (Create unit tests for course-teacher relationships).

**Existing Code File Example:**
File: `tests/api/test_course_teacher_api.py`
```python
import pytest
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Import the Course model from app/models.py
from app.models import Course, Teacher  # Assume Teacher model exists

# Create the test client
@pytest.fixture
def client():
    db.create_all()  # Initialize the in-memory database
    # Create test data
    teacher = Teacher(name="John Doe", email="john.doe@example.com")
    course = Course(title="Math 101", teacher_id=None)
    db.session.add(teacher)
    db.session.add(course)
    db.session.commit()
    app_context = app.app_context()
    app_context.push()
    yield app.test_client()
    app_context.pop()

def test_assign_teacher_to_course(client):
    response = client.post('/courses/1/assign-teacher', json={"teacher_id": 1})
    assert response.status_code == 200
    assert response.json["message"] == "Teacher assigned to course successfully"

def test_get_course_details(client):
    response = client.get('/courses/1')
    assert response.status_code == 200
    assert response.json["title"] == "Math 101"
    assert "teacher" in response.json
```

This implementation plan provides a structured approach to integrating the Teacher-course relationship into the existing system while maintaining adherence to existing architecture and dependencies, thereby ensuring robust testing, clear API contracts, and streamlined deployment procedures.