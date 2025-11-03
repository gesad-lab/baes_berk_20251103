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
This implementation plan outlines the architecture, technology stack, and implementation approach for adding a `Course` entity to the application. This feature enables the management of educational courses that students can enroll in, improving the overall educational experience.

## Architecture
The application will continue to follow a modular architecture approach, allowing us to introduce the `Course` entity while keeping existing components intact.

- **API Layer**: Handles incoming requests and responses related to courses.
- **Service Layer**: Contains the business logic for creating and retrieving courses.
- **Data Access Layer (DAL)**: Manages database interactions for the `Course` entity.
- **Database Layer**: A new `Course` table will be created to store course information.

## Technology Stack
- **Language**: Python 3.11
- **Web Framework**: Flask
- **Database**: SQLite
- **Data Modeling**: SQLAlchemy ORM
- **API Documentation**: OpenAPI (Swagger)
- **Testing Framework**: pytest

## Module Boundaries and Responsibilities
1. **API Module** (`api.py`)
   - Implement the API endpoints for creating and retrieving courses.

2. **Service Module** (`services/course_service.py`)
   - Encapsulate business logic related to courses, including validation and retrieval.

3. **Data Access Module** (`models/course.py`)
   - Define the `Course` entity with the required attributes.

4. **Configuration Module** (`config.py`)
   - No changes required.

5. **Testing Module** (`tests/test_course.py`)
   - Implement tests for course creation and retrieval scenarios, including error handling.

## Data Model and API Contracts

### Data Model
**Course Entity**
- `id`: Integer (auto-incrementing primary key)
- `name`: String (required)
- `level`: String (required)

### API Endpoints
**1. Create a Course**
- **Endpoint**: `POST /courses`
- **Request Body**: 
    ```json
    {
      "name": "string",
      "level": "string"
    }
    ```
- **Responses**:
    - **200 OK**: Successful creation
      ```json
      {
        "message": "Course created successfully.",
        "course": {
          "id": 1,
          "name": "Algebra 101",
          "level": "Beginner"
        }
      }
      ```
    - **400 Bad Request**: Validation error for missing name
      ```json
      {
        "error": {
          "code": "E001",
          "message": "The course name is required."
        }
      }
      ```
    - **400 Bad Request**: Validation error for missing level
      ```json
      {
        "error": {
          "code": "E002",
          "message": "The course level is required."
        }
      }
      ```

**2. Retrieve Courses**
- **Endpoint**: `GET /courses`
- **Responses**: 
    - **200 OK**: Successful retrieval
      ```json
      [
        {
          "id": 1,
          "name": "Algebra 101",
          "level": "Beginner"
        },
        {
          "id": 2,
          "name": "Biology 101",
          "level": "Intermediate"
        }
      ]
      ```

## Implementation Approach

### Step-by-Step Implementation

1. **Setup Project Structure**
    - Maintain the existing project structure while adding files for the new `Course` entity.

2. **Modify Database Schema**
    - In `models/course.py`, define the `Course` class:
      ```python
      from sqlalchemy import Column, Integer, String
      from sqlalchemy.ext.declarative import declarative_base
      
      Base = declarative_base()

      class Course(Base):
          __tablename__ = 'courses'
          
          id = Column(Integer, primary_key=True, autoincrement=True)
          name = Column(String, nullable=False)
          level = Column(String, nullable=False)

          def __init__(self, name: str, level: str):
              self.name = name
              self.level = level
              
          def __repr__(self):
              return f"<Course(name='{self.name}', level='{self.level}')>"
      ```

3. **Database Migration**
    - Implement migration to create the `courses` table:
      ```python
      from alembic import op
      from sqlalchemy import Column, String, Integer
      
      def upgrade():
          op.create_table(
              'courses',
              Column('id', Integer, primary_key=True, autoincrement=True),
              Column('name', String, nullable=False),
              Column('level', String, nullable=False)
          )

      def downgrade():
          op.drop_table('courses')
      ```

4. **Develop API Module**
    - Update `api.py` to add handlers for the `POST /courses` and `GET /courses` endpoints. Example for creating a course:
      ```python
      from flask import Blueprint, request, jsonify
      from services.course_service import create_course, get_all_courses
      
      course_bp = Blueprint('course', __name__)

      @course_bp.route('/courses', methods=['POST'])
      def create_course_endpoint():
          data = request.json
          try:
              course = create_course(data['name'], data['level'])
              return jsonify({"message": "Course created successfully.", "course": course}), 200
          except ValueError as ve:
              return jsonify({"error": {"code": "E001", "message": str(ve)}}), 400
          except KeyError as ke:
              return jsonify({"error": {"code": "E002", "message": f"The course {str(ke)} is required."}}), 400

      @course_bp.route('/courses', methods=['GET'])
      def get_courses_endpoint():
          courses = get_all_courses()
          return jsonify(courses), 200
      ```

5. **Develop Service Layer**
    - In `services/course_service.py`, implement the business logic for creating and retrieving courses, including validation:
      ```python
      from models.course import Course
      from sqlalchemy.orm import Session

      def create_course(name: str, level: str) -> Course:
          if not name:
              raise ValueError("name")
          if not level:
              raise ValueError("level")

          course = Course(name=name, level=level)
          # Assume session is created and managed elsewhere as part of the application context
          db_session.add(course)
          db_session.commit()
          return course
      
      def get_all_courses() -> list:
          all_courses = db_session.query(Course).all()
          return [{"id": course.id, "name": course.name, "level": course.level} for course in all_courses]
      ```

6. **Testing**
    - Enhance `tests/test_course.py` with tests for creating and retrieving courses, including error handling:
      ```python
      import pytest
      from flask import Flask
      from src.api import create_app
      from models.course import Course, init_db

      @pytest.fixture
      def app():
          app = create_app()
          app.config['TESTING'] = True

          with app.app_context():
              init_db()
          yield app

      def test_create_course(client):
          response = client.post('/courses', json={"name": "Algebra 101", "level": "Beginner"})
          assert response.status_code == 200
          data = response.get_json()
          assert 'course' in data

      def test_create_course_missing_name(client):
          response = client.post('/courses', json={"level": "Beginner"})
          assert response.status_code == 400
          assert response.get_json()['error']['code'] == 'E001'

      def test_get_courses(client):
          client.post('/courses', json={"name": "Algebra 101", "level": "Beginner"})
          response = client.get('/courses')
          assert response.status_code == 200
          assert len(response.get_json()) == 1
      ```

7. **Documentation**
    - Update API documentation to capture new endpoints for courses.
    - Adjust the `README.md` file to include instructions for course API usage.

### Scalability, Security, and Maintainability Considerations
- **Scalability**: New course functionalities can be expanded upon as needed without affecting existing features.
- **Security**: Inputs are validated to prevent SQL injection; ensure that the database layer sanitizes inputs.
- **Maintainability**: Follow existing coding standards to enable easy future enhancements.

## Technical Trade-offs and Decisions
- Utilizing SQLite continues to simplify setup and development, making it less complex than transitioning to a more comprehensive database system at this stage.
- Directly integrating the `Course` functionalities into existing modular design ensures the application maintains a clean architecture.

## Configuration Management
- No additional configuration management changes required for the new course implementation.

## Logging & Monitoring
- Continue to implement structured logging to capture details on course creation requests, including any validation failures.

## Deployment Considerations
- Ensure that migrations are applied as part of the deployment process to create the `courses` table without disrupting existing data and functionality.

## Future Enhancements
- Future developments might include adding features for editing or deleting course records and implementing relationships with students for enrollment and management purposes.

## Conclusion
This implementation plan provides a structured and comprehensive approach to enhancing the educational management application by introducing course management capabilities while adhering to maintainable coding standards.

### Existing Code Files: Modifications Needed
1. **`models/course.py`**: New file to define the `Course` entity.
2. **`api.py`**: Add new API endpoints for course creation and retrieval.
3. **`services/course_service.py`**: New file for course-related business logic.
4. **`tests/test_course.py`**: New file for testing course functionalities.

### Existing Code Files:
- File: `models/course.py`
```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)

    def __init__(self, name: str, level: str):
        self.name = name
        self.level = level

    def __repr__(self):
        return f"<Course(name='{self.name}', level='{self.level}')>"
```

- File: `tests/test_course.py`
```python
import pytest
from flask import Flask
from src.api import create_app
from models.course import Course, init_db

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    
    with app.app_context():
        init_db()
    yield app

def test_create_course(client):
    response = client.post('/courses', json={"name": "Algebra 101", "level": "Beginner"})
    assert response.status_code == 200
    data = response.get_json()
    assert 'course' in data

def test_create_course_missing_name(client):
    response = client.post('/courses', json={"level": "Beginner"})
    assert response.status_code == 400
    assert response.get_json()['error']['code'] == 'E001'

def test_get_courses(client):
    client.post('/courses', json={"name": "Algebra 101", "level": "Beginner"})
    response = client.get('/courses')
    assert response.status_code == 200
    assert len(response.get_json()) == 1
```