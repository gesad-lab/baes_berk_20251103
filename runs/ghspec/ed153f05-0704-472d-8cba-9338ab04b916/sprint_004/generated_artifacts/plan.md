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

## I. Architecture Overview

### 1.1 Technology Stack
- **Backend Framework**: Flask (Python)
- **Database**: SQLite 
- **Serialization**: Marshmallow for JSON validation and serialization
- **Environment Management**: pipenv for virtual environment and dependency management
- **Testing Framework**: pytest 
- **API Documentation**: OpenAPI (Swagger) for documenting endpoints 

### 1.2 Module Structure
```
student_management/
│
├── src/
│   ├── app.py               # Application entry point
│   ├── models.py            # Database models (add StudentCourse join model here)
│   ├── schemas.py           # Marshmallow schemas (add StudentCourse schema here)
│   ├── routes.py            # API endpoint definitions (add StudentCourse routes here)
│   ├── database.py          # Database configuration and initialization
│   └── config.py            # Configuration settings
│
├── tests/
│   ├── test_routes.py       # Unit and integration tests for API endpoints (add StudentCourse tests here)
│   └── test_models.py       # Unit tests for database models (add StudentCourse tests here)
│
├── .env                     # Environment variables for configuration
├── .env.example             # Example environment variables file
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

## II. Database Design

### 2.1 Schema Definition
- **Student Course Join Table** (`student_courses`):
  - `student_id`: Integer (Foreign Key referencing Student)
  - `course_id`: Integer (Foreign Key referencing Course)

### 2.2 Initialization
- Implement a migration strategy using Flask-Migrate to create the `student_courses` join table and ensure compatibility with existing Student and Course tables.

## III. API Design

### 3.1 Endpoints
- **POST /students/{id}/courses**
  - Request Body: 
    ```json
    {
      "course_id": "number"
    }
    ```
  - Success Response: 
    ```json
    {
      "message": "Enrollment successful."
    }
    ```
  - Status Code: `201 Created`
  - Error Response (student not found): 
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Student does not exist."
      }
    }
    ```
  - Status Code: `404 Not Found`

- **GET /students/{id}/courses**
  - Success Response: 
    ```json
    [
      {
        "id": "number",
        "name": "string",
        "level": "string"
      },
      ...
    ]
    ```
  - Status Code: `200 OK`
  - Error Response (student not found): 
    ```json
    {
      "error": {
        "code": "E002",
        "message": "Student does not exist."
      }
    }
    ```
  - Status Code: `404 Not Found`

## IV. Implementation Plan

### 4.1 Step-by-step Implementation
1. **Setup Environment**
   - Ensure the `.env` file is updated with any necessary configuration settings.

2. **Update the Model**
   - Create a new `StudentCourse` model in `models.py` to handle the relationship between students and courses.
   ```python
   class StudentCourse(db.Model):
       __tablename__ = 'student_courses'
       student_id = db.Column(db.Integer, db.ForeignKey('students.id'), primary_key=True)
       course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), primary_key=True)
   ```

3. **Database Migration**
   - Use Flask-Migrate to create a migration script for adding the `student_courses` join table and apply the migration without affecting existing Student and Course records.
   ```bash
   flask db migrate -m "Add student_courses join table"
   flask db upgrade
   ```

4. **Update Marshmallow schemas**
   - Create a new schema in `schemas.py` for the `StudentCourse` relationship validation.
   ```python
   class StudentCourseSchema(ma.SQLAlchemyAutoSchema):
       class Meta:
           model = StudentCourse
           fields = ("student_id", "course_id")
   ```

5. **Add API Endpoints**
   - Implement the `POST /students/{id}/courses` endpoint in `routes.py` to enroll a student in a course.
   - Implement `GET /students/{id}/courses` endpoint to retrieve all courses for a student.
   ```python
   @app.route('/students/<int:id>/courses', methods=['POST'])
   def enroll_student_in_course(id):
       ...

   @app.route('/students/<int:id>/courses', methods=['GET'])
   def get_student_courses(id):
       ...
   ```

6. **Implement Error Handling and Validation**
   - Add checks for the existence of the student before processing course enrollments. Return structured error responses if the student does not exist.

7. **Testing**
   - Write new integration tests for course enrollment and retrieval in the `tests` folder.
   - Aim for a minimum of 70% coverage on the new business logic related to course-enrollment and data retrieval.

8. **Documentation**
   - Update the README.md file to include details regarding the new course enrollment functionality.
   - Ensure the API documentation reflects changes for the new endpoints.

## V. Testing Strategy

### 5.1 Types of Tests
- **Unit Tests**: Validate the `StudentCourse` model and schema functionality.
- **Integration Tests**: Verify API endpoints for student course enrollment and retrieval.
- **Contract Tests**: Ensure that the API responses meet defined specifications.

### 5.2 Coverage Requirements
- Minimum coverage target: 70% for all new business logic, with critical paths targeting 90%.

## VI. Deployment Considerations

### 6.1 Environment Management
- Confirm any environment configurations required for the new feature are documented.

### 6.2 Deployment Steps
- Run migrations to ensure the `student_courses` join table is properly created along with existing data.
- Verify the application starts without errors after the deployment.

### 6.3 Monitoring & Logging
- Implement monitoring mechanisms for API performance and error rates post-deployment.

## VII. Conclusion

This implementation plan outlines the steps required to add a course relationship to the Student entity within our application. By adhering to the prescribed development workflow, we ensure a maintainable codebase and deliver a seamless user experience through our API.

### Modifications to Existing Files:
- **models.py**: Added a new `StudentCourse` class to manage the course relationships.
- **schemas.py**: Included a schema for `StudentCourse` to validate the relationship data.
- **routes.py**: Implemented new API endpoints for enrolling students in courses and retrieving their course list.
- **tests/test_routes.py**: Created tests for the new course enrollment endpoint.
- **tests/test_models.py**: Created tests for the `StudentCourse` model and its functionalities.

### Database Migration Strategy:
- Use Flask-Migrate to automatically generate a migration script that will introduce the `student_courses` table without risking current data integrity.

Existing Code Files Example:
File: tests/test_routes.py
```python
import pytest
from src.database import get_db, init_db
from src.models import Student, Course, StudentCourse
from flask import json

@pytest.fixture()
def db():
    """Set up a test database environment."""
    init_db()
    yield get_db()  

def test_enroll_student_in_course(db):
    """Test enrolling a student in a course."""
    student = Student(name="John Doe")
    course = Course(name="Mathematics", level="Intermediate")
    db.session.add(student)
    db.session.add(course)
    db.session.commit()

    response = app.test_client().post(f'/students/{student.id}/courses', json={"course_id": course.id})
    assert response.status_code == 201
    assert response.json['message'] == "Enrollment successful."
```

File: tests/test_models.py
```python
import pytest
from src.database import get_db, init_db
from src.models import Student, Course, StudentCourse

@pytest.fixture()
def db():
    """Set up a test database environment."""
    init_db()
    yield get_db()  

def test_student_course_relationship(db):
    """Test the creation of a StudentCourse relationship."""
    student = Student(name="Jane Doe")
    course = Course(name="Biology", level="Introductory")
    db.session.add(student)
    db.session.add(course)
    db.session.commit()

    relationship = StudentCourse(student_id=student.id, course_id=course.id)
    db.session.add(relationship)
    db.session.commit()

    assert StudentCourse.query.count() == 1
    assert relationship.student_id == student.id
    assert relationship.course_id == course.id
```