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

## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Student Management Web Application

## Version
1.1.0

## Overview
This implementation plan outlines the architecture, technology stack, and implementation approach for adding a relationship between the `Student` and `Course` entities within the application. This feature enables students to enroll in courses, thereby improving the educational management capabilities of the system.

## Architecture
The application will follow a modular architecture approach, ensuring that existing functionality remains intact while introducing the new student-course relationship feature.

- **API Layer**: Handles incoming requests and responses for enrolling students in courses and fetching course details.
- **Service Layer**: Contains business logic for student-course relationship management including validations.
- **Data Access Layer (DAL)**: Manages database interactions related to student-course enrollments.
- **Database Layer**: Introduces a new join table `StudentCourses` to facilitate the many-to-many relationship.

## Technology Stack
- **Language**: Python 3.11
- **Web Framework**: Flask
- **Database**: SQLite
- **Data Modeling**: SQLAlchemy ORM
- **API Documentation**: OpenAPI (Swagger)
- **Testing Framework**: pytest

## Module Boundaries and Responsibilities
1. **API Module** (`api.py`)
   - Implement new API endpoints for enrolling students and viewing courses.

2. **Service Module** (`services/student_course_service.py`)
   - Encapsulate business logic related to student enrollment in courses.

3. **Data Access Module** (`models/student_course.py`)
   - Define the `StudentCourses` join table that captures enrollments.

4. **Configuration Module** (`config.py`)
   - No changes required.

5. **Testing Module** (`tests/test_student_course.py`)
   - Implement tests for the new student enrollment and retrieval of enrolled courses.

## Data Model and API Contracts

### Data Model
**StudentCourses Join Table**
- `id`: Integer (auto-incrementing primary key)
- `student_id`: Integer (foreign key referencing `Student`)
- `course_id`: Integer (foreign key referencing `Course`)

### API Endpoints
**1. Enroll a Student in a Course**
- **Endpoint**: `POST /students/{student_id}/enroll`
- **Request Body**: 
    ```json
    {
      "course_id": "integer"
    }
    ```
- **Responses**:
    - **200 OK**: Successful enrollment
      ```json
      {
        "message": "Student enrolled successfully."
      }
      ```
    - **400 Bad Request**: Course does not exist
      ```json
      {
        "error": {
          "code": "E001",
          "message": "The course does not exist."
        }
      }
      ```
    - **400 Bad Request**: Student already enrolled
      ```json
      {
        "error": {
          "code": "E002",
          "message": "The student is already enrolled in this course."
        }
      }
      ```

**2. View Student's Enrolled Courses**
- **Endpoint**: `GET /students/{student_id}/courses`
- **Responses**: 
    - **200 OK**: Successful retrieval
      ```json
      [
        {
          "course_id": "integer",
          "course_name": "string",
          "course_level": "string"
        }
      ]
      ```

## Implementation Approach

### Step-by-Step Implementation

1. **Setup Project Structure**
    - Maintain the existing project structure while adding files for the new `StudentCourses` relationship.

2. **Modify Database Schema**
    - In `models/student_course.py`, define the `StudentCourses` join table:
      ```python
      from sqlalchemy import Column, Integer, ForeignKey
      from sqlalchemy.ext.declarative import declarative_base
      
      Base = declarative_base()

      class StudentCourses(Base):
          __tablename__ = 'student_courses'
          
          id = Column(Integer, primary_key=True, autoincrement=True)
          student_id = Column(Integer, ForeignKey('students.id'), nullable=False)
          course_id = Column(Integer, ForeignKey('courses.id'), nullable=False)

          def __init__(self, student_id: int, course_id: int):
              self.student_id = student_id
              self.course_id = course_id
      ```

3. **Database Migration**
    - Implement migration to create the `student_courses` join table:
      ```python
      from alembic import op
      from sqlalchemy import Column, Integer, ForeignKey
      
      def upgrade():
          op.create_table(
              'student_courses',
              Column('id', Integer, primary_key=True, autoincrement=True),
              Column('student_id', Integer, ForeignKey('students.id'), nullable=False),
              Column('course_id', Integer, ForeignKey('courses.id'), nullable=False)
          )

      def downgrade():
          op.drop_table('student_courses')
      ```

4. **Develop API Module**
    - Update `api.py` to add handlers for the `POST /students/{student_id}/enroll` and `GET /students/{student_id}/courses` endpoints. Example for enrolling a student:
      ```python
      from flask import Blueprint, request, jsonify
      from services.student_course_service import enroll_student_in_course, get_student_courses
      
      student_course_bp = Blueprint('student_course', __name__)

      @student_course_bp.route('/students/<int:student_id>/enroll', methods=['POST'])
      def enroll_student_endpoint(student_id):
          data = request.json

          try:
              enroll_student_in_course(student_id, data['course_id'])
              return jsonify({"message": "Student enrolled successfully."}), 200
          except ValueError as ve:
              return jsonify({"error": {"code": "E001", "message": str(ve)}}), 400
          except Exception as e:
              return jsonify({"error": {"code": "E002", "message": str(e)}}), 400

      @student_course_bp.route('/students/<int:student_id>/courses', methods=['GET'])
      def get_courses_endpoint(student_id):
          courses = get_student_courses(student_id)
          return jsonify(courses), 200
      ```

5. **Develop Service Layer**
    - In `services/student_course_service.py`, implement the business logic for enrolling students and retrieving courses:
      ```python
      from models.student_course import StudentCourses
      from sqlalchemy.orm import Session

      def enroll_student_in_course(student_id: int, course_id: int) -> None:
          if not course_exists(course_id):
              raise ValueError("The course does not exist.")
          
          if student_already_enrolled(student_id, course_id):
              raise Exception("The student is already enrolled in this course.")

          enrollment = StudentCourses(student_id=student_id, course_id=course_id)
          db_session.add(enrollment)
          db_session.commit()

      def get_student_courses(student_id: int) -> list:
          enrollments = db_session.query(StudentCourses).filter(StudentCourses.student_id == student_id).all()
          courses = [{"course_id": enrollment.course_id} for enrollment in enrollments]
          return courses
          
      def course_exists(course_id: int) -> bool:
          # Function to verify if a course exists.
          pass

      def student_already_enrolled(student_id: int, course_id: int) -> bool:
          # Function to check if a student is already enrolled.
          pass
      ```

6. **Testing**
    - Enhance `tests/test_student_course.py` to include tests for student enrollment and retrieval of enrolled courses:
      ```python
      import pytest
      from flask import Flask
      from src.api import create_app
      from models.student_course import StudentCourses, init_db

      @pytest.fixture
      def app():
          app = create_app()
          app.config['TESTING'] = True
          with app.app_context():
              init_db()
          yield app

      def test_enroll_student_in_course(client):
          response = client.post('/students/1/enroll', json={"course_id": 1})
          assert response.status_code == 200
          data = response.get_json()
          assert data['message'] == "Student enrolled successfully."

      def test_enroll_student_non_existent_course(client):
          response = client.post('/students/1/enroll', json={"course_id": 999})
          assert response.status_code == 400
          assert response.get_json()['error']['code'] == 'E001'

      def test_get_student_courses(client):
          response = client.get('/students/1/courses')
          assert response.status_code == 200
          assert isinstance(response.get_json(), list)
      ```

7. **Documentation**
    - Update API documentation to include new endpoints for enrolling students and fetching their courses.
    - Adjust the `README.md` file to reflect usage instructions for the new features.

### Scalability, Security, and Maintainability Considerations
- **Scalability**: The many-to-many relationship structure provides flexibility for enrollment in numerous courses.
- **Security**: Ensure proper input validation to prevent SQL injection attacks and handle potential exceptions effectively.
- **Maintainability**: All components maintain a modular design adhering to established coding standards for easier future updates.

## Technical Trade-offs and Decisions
- Keeping SQLite as the chosen database facilitates easy management of development and testing environments without the overhead of setting up a more complex relational database.
- The introduction of a join table maintains a clean design for the student-course relationship without impacting existing data models.

## Configuration Management
- No additional configuration management changes required for the new enrollment implementation.

## Logging & Monitoring
- Integrate structured logging to capture details on student enrollment requests and results for debugging purposes.

## Deployment Considerations
- Ensure migration scripts are executed during deployment to automatically update the database schema to include the new join table for student-course relationships.

## Future Enhancements
- Future considerations may include implementing the ability for students to drop courses, or modifying how enrollments are displayed or managed at the administrative level.

## Conclusion
This implementation plan provides a comprehensive framework for adding a student-course relationship to the educational management application, ensuring a maintainable and scalable design that adheres to existing coding principles.

### Existing Code Files: Modifications Needed
1. **`models/student_course.py`**: New file to define the `StudentCourses` entity.
2. **`api.py`**: Add new API endpoints for student enrollment and course retrieval.
3. **`services/student_course_service.py`**: New file implementing service logic for enrollment.
4. **`tests/test_student_course.py`**: New file for testing student enrollment and course query.

### Existing Code Files:
- File: `models/student_course.py`
```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class StudentCourses(Base):
    """Model representing the relationship between students and courses."""
    
    __tablename__ = 'student_courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('students.id'), nullable=False)
    course_id = Column(Integer, ForeignKey('courses.id'), nullable=False)

    def __init__(self, student_id: int, course_id: int):
      self.student_id = student_id
      self.course_id = course_id
```

- File: `tests/test_student_course.py`
```python
import pytest
from flask import Flask
from src.api import create_app
from models.student_course import StudentCourses, init_db

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True

    with app.app_context():
        init_db()
    yield app

def test_enroll_student_in_course(client):
    response = client.post('/students/1/enroll', json={"course_id": 1})
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == "Student enrolled successfully."

def test_enroll_student_non_existent_course(client):
    response = client.post('/students/1/enroll', json={"course_id": 999})
    assert response.status_code == 400
    assert response.get_json()['error']['code'] == 'E001'

def test_get_student_courses(client):
    response = client.get('/students/1/courses')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)
```

This implementation plan ensures a systematic approach to enhancing the student management capabilities of the application while maintaining best practices in coding standards and architectural integrity.