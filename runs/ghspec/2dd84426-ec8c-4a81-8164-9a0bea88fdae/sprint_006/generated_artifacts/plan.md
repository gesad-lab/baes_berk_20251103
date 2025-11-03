# Implementation Plan: Add Teacher Relationship to Course Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Teacher Entity

---
## Version
**Version**: 1.1.0

## Technology Stack
- **Backend Framework**: Flask (Python)
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **API Documentation**: Swagger/OpenAPI
- **Testing Framework**: pytest
- **Environment Management**: venv (Python virtual environments)
- **Serialization**: Marshmallow

## Architecture Overview
This implementation extends the existing educational framework to establish a relationship between the `Course` and `Teacher` entities. The key focus is to integrate the `teacher_id` foreign key into the `Course` entity while maintaining the performance, integrity, and backward compatibility of existing functionalities related to `Student` and `Course`.

### Module Boundaries
1. **API Module**:
   - Add new routes for assigning a teacher to a course and retrieving course information with teacher details.
  
2. **Service Module**:
   - Implement logic for assigning a teacher to a course.

3. **Data Module**:
   - Update the `Course` entity model to include a `teacher_id` attribute.
  
4. **Validation Module**:
   - Implement input validation for assigning teachers to courses.
  
5. **Database Migration Module**:
   - Implement migration logic for updating the `Course` table schema.

## Data Models
Define the updated `Course` entity in `src/models/course.py`.

```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)

    def __repr__(self):
        return f"<Course(name={self.name}, teacher_id={self.teacher_id})>"
```

### Updated Database Schema
The modified `courses` table will now have the following schema:
- **id**: Integer (Primary Key)
- **name**: String (Required)
- **teacher_id**: Integer (Foreign Key to `Teacher`, Nullable)

## API Contracts

### 1. Assign a Teacher to a Course
- **Endpoint**: `POST /courses/{course_id}/assign-teacher/{teacher_id}`
- **Responses**:
  - **200 OK**:
    ```json
    {
      "message": "Teacher successfully assigned to course."
    }
    ```
  - **404 Not Found**:
    ```json
    {
      "error": {
        "code": "E004",
        "message": "Course not found."
      }
    }
    ```

### 2. Retrieve Course Information
- **Endpoint**: `GET /courses/{course_id}`
- **Responses**:
  - **200 OK**:
    ```json
    {
      "id": "integer",
      "name": "string",
      "teacher": {
          "id": "integer",
          "name": "string",
          "email": "string"
      } // Teacher object if assigned, else null
    }
    ```

## Implementation Approach

### Step 1: Setup Project Structure
No specific changes needed to the existing project structure; new files will be added as necessary.

### Step 2: Install Dependencies
No new dependencies are required; the existing setup will remain in use.

### Step 3: Update the Data Module
- Modify `src/models/course.py` to include the new `teacher_id` attribute.

### Step 4: Database Migration
- Create a migration script using Flask-Migrate to alter the `courses` table:
```bash
flask db migrate -m "Add teacher_id to courses table"
flask db upgrade
```
- Ensure that the migration script preserves existing data within the `Course` and `Teacher` entities.

### Step 5: Extend the Service Module
- In `src/services/course_service.py`, implement the logic for assigning a teacher to a course.

```python
from models.course import Course
from models.teacher import Teacher
from sqlalchemy.orm.exc import NoResultFound

def assign_teacher_to_course(db_session, course_id, teacher_id):
    course = db_session.query(Course).filter(Course.id == course_id).one_or_none()
    
    if course is None:
        raise NoResultFound("Course not found.")

    course.teacher_id = teacher_id
    db_session.commit()
    return course
```

### Step 6: Implement the API Module
- Create or update `src/api/course_api.py` to define endpoints for assigning a teacher and retrieving course information.

```python
from flask import Blueprint, request, jsonify
from services.course_service import assign_teacher_to_course
from db import get_db_session
from sqlalchemy.orm.exc import NoResultFound

course_bp = Blueprint('course', __name__)

@course_bp.route('/courses/<int:course_id>/assign-teacher/<int:teacher_id>', methods=['POST'])
def assign_teacher(course_id, teacher_id):
    try:
        assign_teacher_to_course(get_db_session(), course_id, teacher_id)
        return jsonify({"message": "Teacher successfully assigned to course."}), 200
    except NoResultFound:
        return jsonify({"error": {"code": "E004", "message": "Course not found."}}), 404

@course_bp.route('/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    course = get_db_session().query(Course).filter(Course.id == course_id).one_or_none()
    if course:
        return jsonify({
            "id": course.id,
            "name": course.name,
            "teacher": {
                "id": course.teacher.id if course.teacher else None,
                "name": course.teacher.name if course.teacher else None,
                "email": course.teacher.email if course.teacher else None
            }
        }), 200
    else:
        return jsonify({"error": {"code": "E004", "message": "Course not found."}}), 404
```

### Step 7: Input Validation
Input validation can be integrated into the service layer where assignments are processed. However, for simplicity, checks can be directly included in the service methods (as demonstrated above).

### Step 8: Write Unit Tests
- Create or update `tests/api/test_course_api.py` to include tests for the new features.

```python
def test_assign_teacher_to_course(client):
    # Pre-requisite: Create a course and teacher
    course_id = 1  # Assume this exists
    teacher_id = 1 # Assume this exists

    response = client.post(f'/courses/{course_id}/assign-teacher/{teacher_id}')
    assert response.status_code == 200
    assert response.json["message"] == "Teacher successfully assigned to course."
    
def test_assign_teacher_to_nonexistent_course(client):
    response = client.post('/courses/9999/assign-teacher/1')
    assert response.status_code == 404
    assert response.json["error"]["code"] == "E004"
```

### Step 9: Documentation
- Update API documentation to reflect the new endpoint for assigning a teacher to a course and retrieving course information.

### Step 10: Continuous Integration
- Ensure all new and existing tests run successfully in the CI/CD pipeline.

## Summary of Technical Decisions
- Flask and SQLAlchemy continue to be utilized to maintain consistency with the existing code base.
- SQLite remains the database of choice, and migration strategies ensure seamless alterations to the `Course` table.
- This implementation ensures backward compatibility with existing data models and maintains functionality concerning `Student` entities.

## Next Steps
1. Review this plan with stakeholders for approval.
2. Proceed with implementing the outlined approach.
3. Conduct tests focusing on the use cases defined in the specification.

## Modifications Needed to Existing Files
1. **src/models/course.py**:
   - Modify the `Course` model to include the `teacher_id` attribute.

2. **src/services/course_service.py**:
   - Implement the `assign_teacher_to_course` function for assigning teachers to courses.

3. **src/api/course_api.py**:
   - Implement the new endpoints for assigning teachers and retrieving course information.

4. **tests/api/test_course_api.py**:
   - Write new tests for the assignment functionality and retrieval of course details.

5. **db/__init__.py**:
   - Ensure the database session management correctly accommodates querying `Course` and `Teacher` with the new relationships.

## Documentation
- Update API documentation to accurately represent the new routes for managing teacher assignments to courses, ensuring clarity for future development and usage.

--- 

This implementation plan details the steps needed to successfully integrate the teacher-course relationship while adhering to existing development standards and maintaining data integrity.