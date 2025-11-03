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

### 1.1 Architecture Type
- **Microservices**: Enhancing the existing service for managing the Student entity under RESTful API design principles, maintaining modularity.

### 1.2 Technology Stack
- **Backend Framework**: Flask (Python)
- **Database**: SQLite
- **Serialization**: Marshmallow for JSON serialization/deserialization
- **Testing Framework**: pytest
- **Environment Management**: Python `venv` for virtual environments
- **API Documentation**: OpenAPI/Swagger for endpoint documentation

## II. Module Boundaries and Responsibilities

### 2.1 Module Breakdown
1. **API Module**: Extend the current API to manage Student-Course relationships with new endpoints.
2. **Service Module**: Extend the existing service logic to handle the relationship between Students and Courses.
3. **Persistence Module**: Implement data access methods for the Student-Course relationship.
4. **Error Handling Module**: Handle error responses for invalid course assignment inputs.

### 2.2 Module Responsibilities
- **API Module**: Implement endpoints:
  - `POST /students/{id}/courses` to assign courses to a student.
  - `GET /students/{id}` to view student details with associated courses.

- **Service Module**: Manage the business logic for assigning and retrieving courses related to a student.

- **Persistence Module**: Define interaction with the database for managing course enrollments.

- **Error Handling Module**: Validate course data and return appropriate error messages for invalid input (e.g., non-existent course IDs).

## III. Data Models and API Contracts

### 3.1 Data Models
1. **Updated Student Model**:
```python
class Student:
    __tablename__ = 'students'
    id: int  # Auto-incremented primary key
    name: str  # Required name field
    courses: List[Course]  # Many-to-many relationship with Course
```

2. **New Course Model**:
```python
class Course:
    __tablename__ = 'courses'
    id: int  # Auto-incremented primary key
    name: str  # Required course name
    level: str  # Required course level
```

3. **Intermediate Enrollment Model**:
This model defines the many-to-many relationship between students and courses.
```python
class Enrollment:
    __tablename__ = 'enrollments'
    student_id: int  # Foreign key to Student
    course_id: int  # Foreign key to Course
```

### 3.2 API Contracts
1. **Assign Courses to Student**
   - **Endpoint**: `POST /students/{id}/courses`
   - **Request**:
     ```json
     {
       "course_ids": [1, 2, 3]
     }
     ```
   - **Response**:
     ```json
     {
       "student_id": 1,
       "courses": [
         {
           "id": 1,
           "name": "Introduction to Programming",
           "level": "Beginner"
         },
         ...
       ]
     }
     ```

2. **Retrieve Student Info with Courses**
   - **Endpoint**: `GET /students/{id}`
   - **Response**:
     ```json
     {
       "id": 1,
       "name": "John Doe",
       "courses": [
         {
           "id": 1,
           "name": "Introduction to Programming",
           "level": "Beginner"
         },
         ...
       ]
     }
     ```

### 3.3 Error Responses
- **Validation error when course IDs are invalid**:
  ```json
  {
    "error": {
      "code": "E400",
      "message": "One or more course IDs do not exist."
    }
  }
  ```

## IV. Implementation Approach

### 4.1 Development Steps
1. **Setup Development Environment**:
   - Ensure the existing Python virtual environment is active.

2. **Database Migration**:
   - Use `Flask-Migrate` to create a migration script to add the `enrollments` table to the SQLite database.

3. **Update Database Schema**:
   - Define the necessary models (`Student`, `Course`, and `Enrollment`) as described in section III.

4. **Implement RESTful Endpoints**:
   - Develop the `POST /students/{id}/courses` and `GET /students/{id}` endpoints according to the new API contracts.

5. **Data Validation**:
   - Validate incoming `course_ids` to ensure they exist and meet requirements. Return relevant error messages for invalid data.

6. **Error Handling**:
   - Expand existing error handling to provide specific messages for issues related to course assignments.

7. **Testing**:
   - Write unit tests for the new API endpoints and service layer for associating courses with a student.

8. **Documentation**:
   - Update the `README.md` and API documentation to reflect new endpoints and functionality.

## V. Testing Strategy

### 5.1 Test Types
- **Unit Tests**: Target functions related to course assignments and validations.
- **Integration Tests**: Validate the integration between new endpoints and the service/persistence layers.

### 5.2 Coverage Goals
- Achieve at least 70% test coverage overall, with 90% coverage on critical paths such as course assignment.

## VI. Security and Compliance

### 6.1 Data Protection
- Follow PII guidelines and ensure course data is secure.

### 6.2 Input Validation
- Implement strong validation mechanisms to protect against SQL injection and other common threats.

## VII. Deployment Considerations

### 7.1 Production Readiness
- Include a health check endpoint for monitoring the functionality of course-related operations after deployment.

### 7.2 Environment Configuration
- Document any new environment variables that will be added.

## VIII. Modification of Existing Files

### 8.1 Existing Code Modifications
1. **models.py**:
   - Add the `Course` and `Enrollment` model definitions to establish the new relationships.
   
2. **api.py**:
   - Introduce new routes and handlers for `POST /students/{id}/courses` and the update to `GET /students/{id}`.

3. **schema.py**:
   - Create Marshmallow schemas for validation of incoming data for course assignments.

4. **tests/test_api/test_course_api.py**:
   - Implement tests to validate the new API endpoints for assignments and retrieval of student-course relationships.

5. **tests/test_error_conditions.py**:
   - Enhance existing tests to cover validation scenarios for invalid course IDs when assigning courses to students.

## IX. Database Migration Strategy
- Use Flask-Migrate to handle the creation of the `enrollments` table for associating students with courses.
- Ensure the migration is reversible and that existing Student and Course data remains intact.

## X. Conclusion

This implementation plan outlines a structured approach to integrate courses with the existing Student entity. By adhering to the specified architecture and guidelines, we ensure system integrity, maintainability, and security while enhancing system functionality. This addition will provide a richer context for managing student enrollments and academic journeys.

Existing Code Files:
File: tests/test_error_conditions.py
```python
import json
import pytest
from api import create_app, db
from api.models import Course

@pytest.fixture(scope='module')
def test_client():
    """Setup a test client for the Flask application."""
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        db.create_all()  # Create the in-memory database
        yield app.test_client()  # Create the test client
        db.drop_all()  # Clean up

```

File: tests/test_api/test_course_api.py
```python
import json
import pytest
from api import create_app, db
from api.models import Course  # Assuming the Course model is defined in models.py


@pytest.fixture(scope='module')
def test_client():
    """Setup a test client for the Flask application."""
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        db.create_all()  # Create the in-memory database
        yield app.test_client()  # Create the test client
        db.drop_all()  # Clean up

```