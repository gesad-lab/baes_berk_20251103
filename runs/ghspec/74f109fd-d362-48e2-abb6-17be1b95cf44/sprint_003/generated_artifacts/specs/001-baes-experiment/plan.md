# Implementation Plan: Create Course Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Email Field to Student Entity

## Version: 1.1.0

## Overview
This implementation plan outlines the introduction of a new Course entity into the educational management system. It details the necessary updates to the data model, the API endpoints for creating and retrieving courses, and the overall integration approach while maintaining backward compatibility. This modification is crucial for effectively managing educational offerings and provides structured data about available courses.

## Technology Stack
- **Backend Framework**: Flask (Python)
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **API Format**: JSON
- **Testing Framework**: pytest
- **Request Validation**: marshmallow

## Architecture Overview
The application will be updated to include the new Course entity while maintaining the modular architecture outlined in the previous implementation plan.

### Module Structure
- **src/**
  - **models/**: Contains the database models (e.g., Student, Course).
    - Implement a new `Course` model that includes `name` and `level`.
  - **repositories/**: Handles database interactions (e.g., CRUD operations).
    - Implement a `CourseRepository` for managing database operations related to the Course entity.
  - **services/**: Contains business logic for courses.
    - Implement a service to handle course creation and retrieval with validation logic.
  - **api/**: Manages API routes and requests.
    - Add routes for course creation and retrieval.
  - **db/**: Manages database initialization and migrations.
    - Implement migrations to add the new Course table to the database.
  - **config/**: Holds configuration settings.
  - **app.py**: Main application entry point.

- **tests/**: Contains unit and integration tests organized by feature.
  - Add new tests to validate course functionalities.

## Data Model
### Course Model
```python
from sqlalchemy import Column, Integer, String
from database import Base

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)

    def __repr__(self):
        return f"<Course(id={self.id}, name={self.name}, level={self.level})>"
```

## API Contract
### Endpoints
1. **Create Course**
   - **Method**: POST
   - **Endpoint**: `/api/v1/courses`
   - **Request Payload**:
   ```json
   {
     "name": "Introduction to Programming",
     "level": "Beginner"
   }
   ```

   - **Response (201 Created)**:
   ```json
   {
     "id": 1,
     "name": "Introduction to Programming",
     "level": "Beginner"
   }
   ```

   - **Response (400 Bad Request)**:
   ```json
   {
     "error": {
       "code": "E003",
       "message": "Course name and level are required."
     }
   }
   ```

2. **Retrieve Course by ID**
   - **Method**: GET
   - **Endpoint**: `/api/v1/courses/{id}`
   - **Response (200 OK)**:
   ```json
   {
     "id": 1,
     "name": "Introduction to Programming",
     "level": "Beginner"
   }
   ```

   - **Response (404 Not Found)**:
   ```json
   {
     "error": {
       "code": "E004",
       "message": "Course not found."
     }
   }
   ```

## Implementation Approach
1. **Set Up Project Structure**:
   - Utilize existing directory layout and integrate new files as described.

2. **Create Course Model**:
   - Implement the `Course` model to reflect the defined schema with `name` and `level` attributes.

3. **Database Schema Update**:
   - Write a database migration script to create the new `courses` table while ensuring existing data is preserved. 
   - Migration example (using SQLAlchemy Migrate or Alembic):
   ```sql
   CREATE TABLE courses (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       name TEXT NOT NULL,
       level TEXT NOT NULL
   );
   ```

4. **Implement API Endpoints**:
   - Add the Flask routes in `api` to handle course creation and retrieval requests.
   - Implement error handling for missing or invalid course data.

5. **Create Course Repository**:
   - Implement the `CourseRepository` to manage the insertion and retrieval of Course entities from the database.

6. **Create Course Service**:
   - Implement a service that encapsulates the business logic for creating and retrieving courses, including validation checks.

7. **Testing**:
   - Write unit tests to validate the course creation and retrieval functionalities.
   - Ensure the tests cover scenarios including validation errors and successful operations.

8. **Documentation**:
   - Update README.md to reflect changes in the API structure for course management, including examples of requests and responses.

## Key Considerations
- **Scalability**: Structure the Course model for future extensibility, accommodating additional attributes if necessary without major refactoring.
- **Security**: Ensure proper validation is in place to prevent invalid or harmful inputs from being processed.
- **Maintainability**: Adhere to coding standards outlined in the Default Project Constitution to keep the codebase organized as it grows.

## Success Criteria
- 100% success rate for valid course creation requests, confirming both name and level are processed correctly.
- 100% success rate for retrieving courses by ID, ensuring all relevant details are returned if the course exists.
- Successful application startup without errors, verifying the new schema and ensuring existing Student data remains unaffected.
- All API responses delivered in valid JSON format with appropriate HTTP status codes.

## Conclusion
This implementation plan specifies the necessary modifications for adding a Course entity to the educational management system, providing a clear and structured approach that integrates with existing functionality. It accounts for future scalability while ensuring the codebase remains straightforward and maintainable.

Existing Code Modifications:
```python
# New File: src/models/course.py
from sqlalchemy import Column, Integer, String
from database import Base

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)

    def __repr__(self):
        return f"<Course(id={self.id}, name={self.name}, level={self.level})>"

# New File: src/repositories/course_repository.py
from models.course import Course
from database import session

class CourseRepository:
    """Handles database interactions for the Course entity."""
    
    def create_course(self, name, level):
        course = Course(name=name, level=level)
        session.add(course)
        session.commit()
        return course

    def get_course_by_id(self, course_id):
        return session.query(Course).filter_by(id=course_id).first()

# New File: src/services/course_service.py
from repositories.course_repository import CourseRepository

class CourseService:
    """Contains business logic for managing courses."""
    
    def __init__(self):
        self.course_repo = CourseRepository()

    def create_course(self, name, level):
        if not name or not level:
            raise ValueError("Course name and level are required.")
        return self.course_repo.create_course(name, level)

    def get_course(self, course_id):
        course = self.course_repo.get_course_by_id(course_id)
        if not course:
            raise ValueError("Course not found.")
        return course

# New File: src/api/course_api.py
from flask import Blueprint, request, jsonify
from services.course_service import CourseService

course_api = Blueprint('course_api', __name__)
course_service = CourseService()

@course_api.route('/api/v1/courses', methods=['POST'])
def create_course():
    data = request.json
    try:
        course = course_service.create_course(data['name'], data['level'])
        return jsonify({"id": course.id, "name": course.name, "level": course.level}), 201
    except ValueError as e:
        return jsonify({"error": {"code": "E003", "message": str(e)}}), 400

@course_api.route('/api/v1/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    try:
        course = course_service.get_course(course_id)
        return jsonify({"id": course.id, "name": course.name, "level": course.level}), 200
    except ValueError as e:
        return jsonify({"error": {"code": "E004", "message": str(e)}}), 404

# New tests in tests/test_course.py
def test_create_course(course_repository):
    """Test creating a new course."""
    course_data = {
        'name': 'Introduction to Programming',
        'level': 'Beginner'
    }
    course = course_repository.create_course(course_data['name'], course_data['level'])
    assert course.name == 'Introduction to Programming'
    assert course.level == 'Beginner'
``` 

This implementation plan ensures a structured approach to creating a course entity and integrates seamlessly with the existing student management system while maintaining the best coding practices.