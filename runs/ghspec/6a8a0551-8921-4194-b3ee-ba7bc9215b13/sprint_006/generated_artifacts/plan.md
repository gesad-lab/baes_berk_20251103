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

### 1.1 Architecture Type
- **Microservices**: Building upon the existing student management system, we will incorporate a new relationship between the Course and Teacher entities using RESTful API design principles for modular development and scalability.

### 1.2 Technology Stack
- **Backend Framework**: Flask (Python)
- **Database**: SQLite
- **Serialization**: Marshmallow for JSON serialization/deserialization
- **Testing Framework**: pytest
- **Environment Management**: Python `venv` for virtual environments
- **API Documentation**: OpenAPI/Swagger for endpoint documentation

## II. Module Boundaries and Responsibilities

### 2.1 Module Breakdown
1. **Course API Module**: Extend the existing Course API to include functionality related to the Teacher assignment.
2. **Service Module**: Implement business logic for linking Teachers to Courses.
3. **Persistence Module**: Handle database interactions related to the Course entity, particularly for updating the teacher relationship.
4. **Error Handling Module**: Validate incoming requests and handle errors for linking teachers and courses.

### 2.2 Module Responsibilities
- **Course API Module**: Define endpoints:
  - `POST /courses/{id}/assign-teacher` to assign a Teacher to a Course.
  - Update the existing endpoint `GET /courses/{id}` to include Teacher details in the response.

- **Service Module**: Manage the logic to assign and retrieve Teacher relationships for Courses, ensuring compliance with business rules.

- **Persistence Module**: Abstract data access for updating Course records with Teacher IDs in the SQLite database.

- **Error Handling Module**: Implement validation for Teacher ID during assignment and return relevant error responses when validation fails.

## III. Data Models and API Contracts

### 3.1 Data Models
1. **Course Model (updated)**:
```python
class Course:
    __tablename__ = 'courses'
    id: int  # Auto-incremented primary key
    name: str  # Required name field
    level: str  # Required level field
    teacher_id: int  # Foreign key referring to Teacher
```

### 3.2 API Contracts
1. **Assign Teacher to Course**
   - **Endpoint**: `POST /courses/{id}/assign-teacher`
   - **Request**:
     ```json
     {
       "teacher_id": 1
     }
     ```
   - **Response**:
     ```json
     {
       "id": 1,
       "name": "Course Name",
       "level": "Course Level",
       "teacher": {
         "id": 1,
         "name": "John Doe",
         "email": "john.doe@example.com"
       }
     }
     ```

2. **Retrieve Course Info with Teacher**:
   - **Endpoint**: `GET /courses/{id}`
   - **Response**:
     ```json
     {
       "id": 1,
       "name": "Course Name",
       "level": "Course Level",
       "teacher": {
         "id": 1,
         "name": "John Doe",
         "email": "john.doe@example.com"
       }
     }
     ```

### 3.3 Error Responses
- **Validation error when Course or Teacher ID is invalid**:
  ```json
  {
    "error": {
      "code": "E404",
      "message": "Course or Teacher not found."
    }
  }
  ```

- **Validation error when Teacher ID is missing**:
  ```json
  {
    "error": {
      "code": "E400",
      "message": "Teacher ID is required."
    }
  }
  ```

## IV. Implementation Approach

### 4.1 Development Steps
1. **Setup Development Environment**:
   - Ensure the existing Python virtual environment is active.

2. **Database Migration**:
   - Use `Flask-Migrate` to create a migration script that adds the `teacher_id` column to the `courses` table.

3. **Update Database Schema**:
   - Modify the Course model in `models.py` to reflect the new `teacher_id`.

4. **Implement RESTful Endpoints**:
   - Develop the `POST /courses/{id}/assign-teacher` and update the `GET /courses/{id}` endpoint to include teacher details according to the new API contracts.

5. **Data Validation**:
   - Validate incoming requests for the Teacher ID and ensure it corresponds to an existing Teacher. Return relevant error messages for invalid data.

6. **Error Handling**:
   - Implement specific error messages for validation scenarios.

7. **Testing**:
   - Write unit tests for the new API endpoint and existing Course retrieval, covering both successful and failed scenarios.

8. **Documentation**:
   - Update the API documentation using OpenAPI/Swagger to reflect new endpoints and functionality.

## V. Testing Strategy

### 5.1 Test Types
- **Unit Tests**: Test the new Teacher assignment logic and ensure Course retrieval includes Teacher information.
- **Integration Tests**: Validate the overall functionality of Teacher assignments across the system.

### 5.2 Coverage Goals
- Aim for at least 70% test coverage, ensuring that all new paths and critical operations exceed 90% coverage.

## VI. Security and Compliance

### 6.1 Data Protection
- Ensure compliance with PII regulations, ensuring that sensitive teacher and course information is stored securely and not logged.

### 6.2 Input Validation
- Robustly validate inputs for both Course and Teacher assignments, ensuring protections against SQL injection.

## VII. Deployment Considerations

### 7.1 Production Readiness
- Implement health checks to verify the availability of the new Teacher assignment features after deployment.

### 7.2 Environment Configuration
- Add any new necessary environment variables into `.env.example` for Teacher assignment purposes.

## VIII. Modification of Existing Files

### 8.1 Existing Code Modifications
1. **models.py**:
   - Update the `Course` model to add the `teacher_id` field to link the Course with the Teacher entity.

2. **api.py**:
   - Introduce the new route `POST /courses/{id}/assign-teacher` and enhance the existing `GET /courses/{id}` endpoint to include Teacher information.

3. **schema.py**:
   - Update Marshmallow schemas to include Teacher details in Course serialization.

4. **tests/test_api/test_course_api.py**:
   - Implement tests for the new API endpoint for assigning teachers to courses and updating existing test cases to ensure they validate teacher information retrieval correctly.

5. **tests/test_error_conditions.py**:
   - Enhance existing tests to cover error conditions related to teacher assignment validation, ensuring input handling is robust and complies with the expected error messages.

## IX. Database Migration Strategy
- Use Flask-Migrate to handle the addition of `teacher_id` in the `courses` table, ensuring strict referential integrity is maintained.
- The migration script should include validations to confirm the success of adding the new field without affecting existing Course data.

## X. Conclusion

This implementation plan defines a structured approach to add a Teacher relationship to the Course entity within the existing student management system. By adhering to established architecture principles, ensuring thorough validation and testing protocols, and guaranteeing backward compatibility, we are enhancing the system's capabilities while maintaining data integrity and security. This addition lays groundwork for a more organized approach to educational resource management in the future.

Existing Code Files:
File: tests/test_error_conditions.py
```python
import json
import pytest
from api import create_app, db
from api.models import Course, Teacher  # Assuming Teacher is defined

@pytest.fixture(scope='module')
def test_client():
    """Setup a test client for the Flask application."""
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        db.create_all()  # Create the in-memory database
        yield app.test_client()

# You can define additional tests for Course-Teacher assignments here
```

File: tests/test_api/test_course_api.py
```python
import json
import pytest
from api import create_app, db
from api.models import Course, Teacher  # Importing the Course and Teacher models

@pytest.fixture(scope='module')
def test_client():
    """Setup a test client for the Flask application."""
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        db.create_all()  # Create the in-memory database
        yield app.test_client()

def test_assign_teacher_to_course():
    """Test assigning a teacher to a course successfully."""
    teacher = Teacher(name="John Doe", email="john.doe@example.com")
    db.session.add(teacher)
    db.session.commit()
    
    course = Course(name="Course Name", level="Course Level")
    db.session.add(course)
    db.session.commit()
    
    response = test_client().post(f'/courses/{course.id}/assign-teacher', json={'teacher_id': teacher.id})
    assert response.status_code == 200
    assert response.json['teacher']['name'] == teacher.name
```

This implementation plan outlines how both new features and modifications to existing features will enhance the system while maintaining alignment with established architectural principles and practices.