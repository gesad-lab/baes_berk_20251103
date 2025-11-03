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
# Implementation Plan: Create Course Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Email Field to Student Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Student Entity Management Web Application

## I. Architecture Overview

### 1.1 Technology Stack
- **Backend Framework**: Flask (Python)
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Data Format**: JSON
- **Testing Framework**: pytest

### 1.2 Architectural Pattern
- MVC (Model-View-Controller) pattern: 
  - **Model**: Represents the `Teacher`, `Course` entities and their attributes.
  - **View**: JSON responses sent to clients.
  - **Controller**: API routes handling requests and responses for course-teacher relationship management.

## II. Module Boundaries and Responsibilities

### 2.1 New Modules
- **models/**: Update the existing `Course` model to include the `teacher_id` foreign key relationship.
- **controllers/**: Implement methods in `course_controller.py` to manage API endpoints for assigning teachers to courses and retrieving course information.
- **schemas/**: Update or create validation schemas for course assignment and retrieval.
- **database/**: Manage migrations for the updated `Course` entity.

### 2.2 Responsibilities
- **models/course.py**: Update the `Course` class to include the `teacher_id` column.
- **controllers/course_controller.py**: Implement API endpoint code to handle assigning teachers to courses and retrieving course information.
- **schemas/course_schema.py**: Modify request validation to enforce requirement for `course_id` and `teacher_id`.
- **database/migrations/**: Create migration scripts necessary to add the `teacher_id` column to the existing Course table.

## III. Data Models

### 3.1 Updated Course Model
```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)

    teacher = relationship("Teacher", back_populates="courses")
```

### 3.2 Teacher Model (for reference)
```python
class Teacher(Base):
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

    courses = relationship("Course", back_populates="teacher")
```

### 3.3 API Contracts

#### 3.3.1 Assign Teacher to Course
- **Endpoint**: `POST /api/v1/courses/{course_id}/assign_teacher`
- **Request Body**:
```json
{
    "teacher_id": 1
}
```
- **Response**:
  - Success (200 OK)
  ```json
  {
      "id": 1,
      "name": "Mathematics",
      "level": "Grade 10",
      "teacher_id": 1,
      "teacher": {
          "id": 1,
          "name": "John Doe",
          "email": "john.doe@example.com"
      }
  }
  ```
  - Error (404 Not Found)
  ```json
  {
      "error": {
          "code": "E002",
          "message": "Teacher not found."
      }
  }
  ```

#### 3.3.2 Retrieve Course Information with Teacher
- **Endpoint**: `GET /api/v1/courses/{course_id}`
- **Response**:
```json
{
    "id": 1,
    "name": "Mathematics",
    "level": "Grade 10",
    "teacher_id": 1,
    "teacher": {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
}
```
- Status Code: 200 OK

## IV. Implementation Approach

### 4.1 Development Steps
1. **Setup Project Structure**: Modify `models/course.py` to incorporate the `teacher_id` foreign key and relationship mapping.

2. **Update Course Model**: Add `teacher_id` column to the `Course` model in `models/course.py`.

3. **Implement API Endpoints**: Extend `controllers/course_controller.py` to handle the new `POST` for assigning a teacher and `GET` for retrieving course information.

4. **Update Request Validation**: In `schemas/course_schema.py`, add validation to ensure valid course and teacher IDs when assigning.

5. **Database Migration**: Create `database/migrations/` scripts to add the `teacher_id` column to the existing `courses` table.

   ```python
   def upgrade():
       op.add_column('courses', sa.Column('teacher_id', sa.Integer(), sa.ForeignKey('teachers.id'), nullable=True))

   def downgrade():
       op.drop_column('courses', 'teacher_id')
   ```

6. **Testing**: Create tests in `tests/test_course.py` to validate teacher assignments and retrieval of course details with teachers.

7. **Documentation**: Update the `README.md` file to outline the newly implemented API methods for course-teacher relationships.

### 4.2 Error Handling
- Implement error checking to validate if the provided `course_id` and `teacher_id` exist. Return standardized JSON error messages if validation fails.
```json
{
    "error": {
        "code": "E002",
        "message": "Teacher not found."
    }
}
```

## V. Testing Approach

### 5.1 Test Coverage
- **Unit Tests**: Ensure unit tests for the methods handling teacher assignments and course retrieval.
- **Integration Tests**: Validate the API request/response cycle for the course-teacher assignment and retrieval.
- **Contract Tests**: Ensure the endpoints conform to the specified contracts.

### 5.2 Tooling
- Utilize `pytest` for tests, ensuring that coverage targets are met according to the established standards (70% for business logic, 90% for critical paths).

## VI. Deployment Considerations

### 6.1 Production Readiness
- Verify that the application starts successfully without manual intervention and perform migrations during startup.
- Include appropriate health check endpoints to monitor the application.

### 6.2 Configuration Management
- Use environment variables for managing database configuration to avoid hardcoding sensitive details or credentials.

## VII. Documentation

### 7.1 README.md
- Update the introduction section to include information about the new course-teacher relationship feature.
- Include instructions for executing the database migration and using the new API endpoints for course management.

## VIII. Conclusion

This implementation plan provides a clear roadmap for the addition of a teacher relationship to the existing Course entity in the educational management system. By following the steps outlined, the plan ensures the integration is seamless, maintains backward compatibility, and adheres to the previously established coding and architectural standards. Comprehensive API contracts, validation logic, and testing coverage are included to guarantee the quality and usability of the new feature.

### Existing Code Files

File: models/course.py
```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)

    teacher = relationship("Teacher", back_populates="courses")
```

File: controllers/course_controller.py
```python
from flask import Blueprint, request, jsonify
from models.course import Course
from models.teacher import Teacher
from database import db
from schemas.course_schema import CourseSchema

course_bp = Blueprint('courses', __name__)

@course_bp.route('/api/v1/courses/<int:course_id>/assign_teacher', methods=['POST'])
def assign_teacher(course_id):
    course = Course.query.get_or_404(course_id)
    data = request.get_json()
    teacher_id = data.get('teacher_id')

    teacher = Teacher.query.get(teacher_id)
    if not teacher:
        return jsonify({"error": {"code": "E002", "message": "Teacher not found."}}), 404
    
    course.teacher_id = teacher_id
    db.session.commit()
    
    return jsonify({
        "id": course.id,
        "name": course.name,
        "level": course.level,
        "teacher_id": course.teacher_id,
        "teacher": {"id": teacher.id, "name": teacher.name, "email": teacher.email}
    }), 200

@course_bp.route('/api/v1/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    course = Course.query.get_or_404(course_id)
    teacher_details = {"id": course.teacher.id, "name": course.teacher.name, "email": course.teacher.email} if course.teacher else None

    return jsonify({
        "id": course.id,
        "name": course.name,
        "level": course.level,
        "teacher_id": course.teacher_id,
        "teacher": teacher_details
    }), 200
```

File: schemas/course_schema.py
```python
from marshmallow import Schema, fields, validate

class CourseSchema(Schema):
    course_id = fields.Integer(required=True)
    teacher_id = fields.Integer(required=True)
```

File: tests/test_course.py
```python
import pytest
from app import create_app, db
from models.course import Course
from models.teacher import Teacher

@pytest.fixture(scope='module')
def test_client():
    app = create_app('testing')  
    testing_client = app.test_client()

    with app.app_context():
        db.create_all() 

        yield testing_client  

        db.drop_all() 

def test_assign_teacher_success(test_client):
    # First, create a teacher
    teacher = Teacher(name="John Doe", email="john.doe@example.com")
    db.session.add(teacher)
    db.session.commit()

    course = Course(name="Mathematics", level="Grade 10")
    db.session.add(course)
    db.session.commit()

    response = test_client.post(f'/api/v1/courses/{course.id}/assign_teacher', json={
        "teacher_id": teacher.id
    })
    
    assert response.status_code == 200
    assert response.json['teacher']['name'] == "John Doe"

def test_assign_teacher_not_found(test_client):
    course = Course(name="Science", level="Grade 11")
    db.session.add(course)
    db.session.commit()

    response = test_client.post(f'/api/v1/courses/{course.id}/assign_teacher', json={
        "teacher_id": 9999  # Non-existent teacher ID
    })
    
    assert response.status_code == 404
    assert response.json['error']['code'] == "E002"
```

This implementation provides a comprehensive strategy for enhancing the educational management system with the new course-teacher relationship, adhering to the required standards and practices.