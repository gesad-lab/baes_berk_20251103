# Implementation Plan: Add Course Relationship to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Course Entity

---

## Version: 1.0.0  
## Purpose: Technical implementation plan for establishing a relationship between Students and Courses within the Student Management Application.  
## Scope: Implement a RESTful API for managing the student-course relationships.

---

## I. Architecture Overview

- **Architecture Type**: Monolithic API
- **Deployment**: Cloud (e.g., AWS, Heroku)
- **Communication Protocol**: HTTP/HTTPS
- **Data Format**: JSON for requests and responses
- **Technology Stack**:
  - **Backend Framework**: FastAPI (Python) for rapid development of APIs
  - **Database**: PostgreSQL for relational data storage
  - **ORM**: SQLAlchemy for database interaction
  - **Testing Framework**: Pytest for unit and integration testing
  - **Dependency Management**: Poetry for managing Python dependencies
  - **Environment Management**: Docker for containerization

---

## II. Module Breakdown

### 1. API Module
- **Responsibilities**:
  - Handle incoming HTTP requests for managing student-course relationships.
  - Parse and validate requests for assigning courses to students and retrieving course data.
  - Interact with the database through the ORM for course and student mappings.
  - Return JSON responses.

### 2. Database Module
- **Responsibilities**:
  - Define and manage the `student_courses` join table schema.
  - Interface with the PostgreSQL database to perform CRUD operations related to the student-course relationships.

### 3. Test Module
- **Responsibilities**:
  - Contain all tests for the API endpoints that validate the functionality related to student-course relationships.
  - Validate scenarios as defined in the User Scenarios section regarding adding courses to students and retrieving lists.

---

## III. Data Models

### Updated Student and Course Models
We will introduce a `student_courses` join table to establish a many-to-many relationship between `students` and `courses`.

### StudentCourse Model
```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class StudentCourse(Base):
    __tablename__ = 'student_courses'
    
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)
```

### Database Migration Strategy
- Use Alembic for database migrations.
- Create a migration script that:
  - Creates a new `student_courses` join table.
  - Defines foreign key relationships to ensure referential integrity between `students` and `courses`.
- Ensure the migration is created with the command:
  ```bash
  alembic revision --autogenerate -m "create student_courses table"
  ```
- Test migrations to confirm that the structure is created correctly and does not interfere with the existing data in `students` or `courses`.

---

## IV. API Contract

### 1. Assign Course to Student Endpoint
- **Endpoint**: `POST /students/{student_id}/courses`
- **Request Body**:
    ```json
    {
      "course_id": 1
    }
    ```
- **Response**:
    ```json
    {
      "message": "Course assigned successfully",
      "student_id": 1,
      "course_id": 1
    }
    ```
- **HTTP Status Codes**:
  - 201 Created: If the course is successfully assigned.
  - 400 Bad Request: If the student or course does not exist.

### 2. Retrieve Student Courses Endpoint
- **Endpoint**: `GET /students/{student_id}/courses`
- **Response (Success)**:
    ```json
    [
      {
        "id": 1,
        "name": "Introduction to Programming",
        "level": "Beginner"
      },
      ...
    ]
    ```
- **Response (Error)**:
    ```json
    {
      "error": {
        "code": "E404",
        "message": "Student not found."
      }
    }
    ```
- **HTTP Status Codes**:
  - 200 OK: When successful in retrieving the student's courses.
  - 404 Not Found: If the student does not exist.

### 3. List All Students in a Course Endpoint
- **Endpoint**: `GET /courses/{course_id}/students`
- **Response**:
    ```json
    [
      {
        "id": 1,
        "name": "Alice Smith"
      },
      ...
    ]
    ```
- **HTTP Status Codes**:
  - 200 OK: List of students enrolled in the specified course.

---

## V. Implementation Strategy

1. **Setup Project Environment**:
   - Ensure Docker setup is updated for the new database migration strategy.
   - Existing PostgreSQL instance provides compatibility for the join table structure.

2. **Develop API Endpoints**:
   - Implement new endpoints using FastAPI in `src/api/student_course_api.py` to handle the functionality of course assignments and retrieval of students in courses.
   - Validate inputs to ensure integrity (check if the student and course exist before operations).

3. **Database Integration**:
   - Extend existing SQLAlchemy models in `src/models.py` to include the `StudentCourse` join table.
   - Implement methods for creating and retrieving student-course relationships.

4. **Testing**:
   - Create unit tests for `student_course_api.py` using Pytest, ensuring coverage of all scenarios per the functional requirements.
   - Test responses for valid and invalid inputs.

5. **Deployment**:
   - Use Docker to containerize the application ensuring that the schema migration succeeds without issues.
   - Monitor and validate deployment in the cloud environment.

---

## VI. Performance, Scalability, and Security Considerations

1. **Performance**:
   - Ensure optimized queries to reduce response times, particularly in fetching lists of students or courses.

2. **Scalability**:
   - Use stateless requests for added resilience when involving many students/courses.

3. **Security**:
   - Validate and sanitize all user input to prevent SQL injection.
   - Securely manage database connections through environment variables.

---

## VII. Logging & Monitoring

- Implement structured logging for the new endpoints to track assignments and retrieval processes.
- Set up monitoring tools to measure the API's response time and error rates, focusing on the new relationships functionality.

---

## VIII. Documentation

- Update API documentation for the new endpoints concerning student-course relationships using FastAPI's built-in documentation features.
- Provide detailed setup instructions and usage guidelines in `README.md`.

---

## IX. Conclusion

This implementation plan outlines the steps necessary to establish the relationship between students and courses in the Student Management Application. By adhering to existing coding standards and incorporating new functionality, we will enhance the application's capability to manage student enrollments effectively.

---

### Existing Code File Modifications:

- **New Modules**:
  - Create `src/api/student_course_api.py` for student-course API logic.
  
### File Modifications:
- **Database Migration**: Utilize Alembic to implement the migrations required for creating the `student_courses` join table.
- **New API Endpoint Methods**: Create new methods in `src/api/student_course_api.py` to facilitate the student-course relationship logic.

### Example test modifications:
File: tests/api/test_student_course_api.py
```python
import pytest
from fastapi.testclient import TestClient
from src.api.student_course_api import app  # Assuming the FastAPI instance for student-course is in this module

client = TestClient(app)

def test_assign_course_to_student(db):
    response = client.post("/students/1/courses", json={"course_id": 1})
    assert response.status_code == 201
    assert response.json() == {
        "message": "Course assigned successfully",
        "student_id": 1,
        "course_id": 1
    }

def test_retrieve_student_courses(db):
    response = client.get("/students/1/courses")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Ensure it returns a list of courses

def test_list_students_in_course(db):
    response = client.get("/courses/1/students")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Ensure it returns a list of students
```

This plan provides clear guidance to implement the course relationships within the Student Management Application, ensuring compatibility with past coding practices and overall system architecture.