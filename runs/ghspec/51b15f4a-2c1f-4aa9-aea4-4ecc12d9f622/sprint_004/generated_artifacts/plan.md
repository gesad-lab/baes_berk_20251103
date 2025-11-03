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
# Implementation Plan: Student Entity Management Web Application

## I. Architecture Overview

### 1.1 Technology Stack
- **Backend Framework**: Flask (Python)
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Data Format**: JSON
- **Testing Framework**: pytest

### 1.2 Architectural Pattern
- MVC (Model-View-Controller) pattern, where:
  - Model: Represents the `Student` and `Course` entities with their attributes, and the `Enrollment` relationship.
  - View: JSON responses sent to clients.
  - Controller: API routes handling requests and responses for course enrollment.

## II. Module Boundaries and Responsibilities

### 2.1 New Modules
- **models/**: Update the existing `Student` model and create an `Enrollment` model to represent the many-to-many relationship.
- **controllers/**: Expand the existing student controller to manage enrollment-related endpoints.
- **schemas/**: Define validation schemas for enrollment input.
- **database/**: Manage new migrations for establishing the enrollment relationship.

### 2.2 Responsibilities
- **models/enrollment.py**: Define the `Enrollment` class to map to the enrollment relationship in the database.
- **controllers/student_controller.py**: Implement API endpoint code to handle student enrollment in courses.
- **schemas/enrollment_schema.py**: Create request validation to enforce requirement for `student_id` and `course_ids`.
- **database/migrations/**: Create migration scripts necessary to add the enrollment table and establish relationships.

## III. Data Models

### 3.1 Enrollment Model
```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Enrollment(Base):
    __tablename__ = 'enrollments'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('students.id'), nullable=False)
    course_id = Column(Integer, ForeignKey('courses.id'), nullable=False)

    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="students")
```

### 3.2 API Contracts

#### 3.2.1 Enroll Student in Courses Endpoint
- **Endpoint**: `POST /api/v1/students/enroll`
- **Request Body**:
```json
{
    "student_id": 1,
    "course_ids": [1, 2, 3]
}
```
- **Response**:
  - Success (200 OK)
  ```json
  {
      "student_id": 1,
      "enrolled_courses": [
          {
              "id": 1,
              "name": "Mathematics",
              "level": "Advanced"
          },
          {
              "id": 2,
              "name": "Science",
              "level": "Beginner"
          }
      ]
  }
  ```
  - Error (400 Bad Request)
  ```json
  {
      "error": {
          "code": "E002",
          "message": "Invalid course IDs provided."
      }
  }
  ```

#### 3.2.2 Retrieve Student Courses Endpoint
- **Endpoint**: `GET /api/v1/students/{student_id}/courses`
- **Response**:
```json
[
    {
        "id": 1,
        "name": "Mathematics",
        "level": "Advanced"
    },
    {
        "id": 2,
        "name": "Science",
        "level": "Beginner"
    }
]
```
- Status Code: 200 OK

## IV. Implementation Approach

### 4.1 Development Steps
1. **Setup Project Structure**: Create `models/enrollment.py`, `schemas/enrollment_schema.py`, and update `controllers/student_controller.py` under the existing directory structure.

2. **Create Enrollment Model**: Define `Enrollment` class in `models/enrollment.py` to manage database interactions for the relationships.

3. **Update Database Migration**: Modify `database/migrations/` to add a new `enrollments` table.
   ```python
   def upgrade():
       op.create_table(
           'enrollments',
           sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
           sa.Column('student_id', sa.Integer(), sa.ForeignKey('students.id'), nullable=False),
           sa.Column('course_id', sa.Integer(), sa.ForeignKey('courses.id'), nullable=False)
       )

   def downgrade():
       op.drop_table('enrollments')
   ```

4. **Implement API Endpoints**: Update `controllers/student_controller.py` to handle `POST` for enrolling students and `GET` for retrieving course lists.

5. **Update Request Validation**: Create `schemas/enrollment_schema.py` with input validation ensuring that both `student_id` and `course_ids` are present and valid.

6. **Testing**: Create tests in `tests/test_student_enrollment.py` to validate course enrollment and retrieval functionality.

7. **Documentation**: Update the `README.md` file to reflect new API structure and usage for enrollment endpoints.

### 4.2 Error Handling
- Implement validation error handling to check if the `student_id` and each `course_id` exists in the database; return standardized JSON error messages if validation fails.
  ```json
  {
      "error": {
          "code": "E002",
          "message": "Invalid course IDs provided."
      }
  }
  ```

## V. Testing Approach

### 5.1 Test Coverage
- **Unit Tests**: Test the function for student enrollment and retrieval of courses to ensure validations work as expected.
- **Integration Tests**: Validate the API request/response cycle for enrolling students in courses and retrieving their courses.
- **Contract Tests**: Ensure the new `POST` and `GET` enrollment endpoints conform to the specified contracts.

### 5.2 Tooling
- Utilize `pytest` for tests, ensuring that coverage targets are met as per specifications.

## VI. Deployment Considerations

### 6.1 Production Readiness
- Verify the application starts successfully without manual intervention and runs migrations automatically on startup.
- Ensure appropriate health check endpoints are in place with documentation of environment variables.

### 6.2 Configuration
- Use environment variables for managing database configurations to avoid hardcoding sensitive information.

## VII. Documentation

### 7.1 README.md
- Provide an updated introduction to the enrollment feature.
- Include instructions for the database migration, how to use the new API endpoints for enrolling students and retrieving course lists.
- Document test setup instructions.

## VIII. Conclusion

This implementation plan outlines a strategy for establishing a course enrollment relationship in the student management system. The plan maintains integration with existing services, fulfilling the requirements to manage student-course relationships, while ensuring backward compatibility with existing models. Comprehensive specifications for API contracts, validation, and testing coverage are included to ensure the quality and usability of the new feature.

### Existing Code Files

File: tests/test_student_enrollment.py
```python
import pytest
from app import create_app, db
from models.enrollment import Enrollment

@pytest.fixture(scope='module')
def test_client():
    app = create_app('testing')  # Initialize app with testing configuration
    testing_client = app.test_client()

    with app.app_context():
        db.create_all()  # Setup test database environment

        yield testing_client  # This is where the testing happens!

        db.drop_all()  # Teardown after tests

def test_enroll_student_success(test_client):
    response = test_client.post('/api/v1/students/enroll', json={
        "student_id": 1,
        "course_ids": [1, 2]
    })
    assert response.status_code == 200  # Validate the enrollment was successful
    assert response.json['enrolled_courses'] == [ ... ]  # Expected data structure
```

File: models/student.py
```python
# models/student.py (already existing)

from sqlalchemy.orm import relationship

class Student(Base):
    ...
    courses = relationship("Enrollment", back_populates="student")  # New relationship added
```

File: tests/test_student_enrollment.py
```python
import pytest
from app import create_app, db
from models.enrollment import Enrollment

@pytest.fixture(scope='module')
def test_client():
    app = create_app('testing')
    testing_client = app.test_client()

    with app.app_context():
        db.create_all()

        yield testing_client

        db.drop_all()

def test_enroll_student_success(test_client):
    response = test_client.post('/api/v1/students/enroll', json={
        "student_id": 1,
        "course_ids": [1, 2]
    })
    assert response.status_code == 200
    # Validate full structure
```

This plan ensures that the implementation of the new Course relationship is systematic and well-structured, following best practices established in previous sprints.