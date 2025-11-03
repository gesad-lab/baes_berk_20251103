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
# Implementation Plan: Student Management Web Application

## I. Architecture Overview

### 1.1 Components
- **API Layer**: A RESTful API for associating courses with students and retrieving student details, responding with JSON data.
- **Database Layer**: SQLite to manage existing Student records with an enhanced relationship to the Course entity.
- **Business Logic Layer**: Handles validation and processing of requests concerning Student-Course relationships.

### 1.2 Technology Stack
- **Programming Language**: Python (version 3.11 or higher)
- **Web Framework**: FastAPI (provides built-in JSON support and rapid development)
- **Database**: SQLite (for lightweight database management)
- **ORM**: SQLAlchemy (to facilitate database interactions)
- **Testing Framework**: pytest (for unit and integration tests)
- **Environment Management**: Poetry (for dependency management)
- **Migration Tool**: Alembic (to manage database schema updates)

---

## II. Module Boundaries and Responsibilities

### 2.1 API Layer
- **Module**: `app/api/student.py`
  - **Responsibilities**:
    - Handle HTTP requests for Student operations (`POST /students/{id}/courses`, `GET /students/{id}`).
    - Validate incoming requests and format JSON responses.

### 2.2 Database Layer
- **Module**: `app/models/student.py`
  - **Responsibilities**:
    - Update the `Student` entity to include a Many-to-Many relationship with the `Course` entity.
  
### 2.3 Business Logic Layer
- **Module**: `app/services/student_service.py`
  - **Responsibilities**:
    - Validate the course assignment logic and process assignment requests.
    - Retrieve student information along with associated courses.

---

## III. Data Models and API Contracts

### 3.1 Data Model
#### Student
```python
from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

# Association table for Student-Course relationship
student_courses = Table(
    'student_courses',
    Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    
    courses = relationship('Course', secondary=student_courses, back_populates='students')
```

### 3.2 Data Model for Course
```python
class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)

    students = relationship('Student', secondary=student_courses, back_populates='courses')
```

### 3.3 API Contract
#### Associate Student with Course
- **Endpoint**: `POST /students/{id}/courses`
- **Request Body**:
  ```json
  {
      "course_id": 1
  }
  ```
- **Responses**:
  - **200 OK**:
    ```json
    {
        "message": "Course assigned successfully."
    }
    ```
  - **404 Not Found**:
    ```json
    {
        "error": {
            "code": "E001",
            "message": "Invalid course ID."
        }
    }
    ```

#### Retrieve Student with Courses
- **Endpoint**: `GET /students/{id}`
- **Responses**:
  - **200 OK**:
    ```json
    {
        "id": 1,
        "name": "John Doe",
        "email": "john@example.com",
        "courses": [
            {"id": 1, "name": "Mathematics", "level": "Beginner"}
        ]
    }
    ```
  - **404 Not Found**:
    ```json
    {
        "error": {
            "code": "E002",
            "message": "Student not found."
        }
    }
    ```

---

## IV. Implementation Approach

### 4.1 Initial Setup
- **Modify the Student Module**:
  - Update `app/models/student.py` to define the Many-to-Many relationship with `Course`.
  - Create `app/api/student.py` for handling the new API endpoints for associating courses with students.
  
### 4.2 Database Migration
1. **Using Alembic for migrations**:
   - Install Alembic via Poetry:
     ```bash
     poetry add alembic
     ```
   - Create a migration script for updating the `students` table:
     ```bash
     alembic revision --autogenerate -m "Add many-to-many relationship between students and courses"
     ```
   - The migration script should include:
     ```python
     def upgrade():
         op.create_table(
             'student_courses',
             sa.Column('student_id', sa.Integer(), sa.ForeignKey('students.id'), primary_key=True),
             sa.Column('course_id', sa.Integer(), sa.ForeignKey('courses.id'), primary_key=True)
         )

     def downgrade():
         op.drop_table('student_courses')
     ```

### 4.3 Implementing API Endpoints
- **POST /students/{id}/courses**:
  - Implement logic in `app/api/student.py` to handle course assignment with validation for the course ID.
  
- **GET /students/{id}**:
  - Update retrieval logic to format the response with the student’s details and enrolled courses.

### 4.4 Input Validation and Response Generation
- Validations will be added in `app/services/student_service.py` to check if the ID provided corresponds to an existing course and appropriately send back error messages.

### 4.5 Testing
- Write tests in a new file `tests/test_student.py`:
  - Example tests:
    - Test associating a course with a student.
    - Test retrieving a student with their associated courses.
    
Example test file structure:
```python
import pytest

def test_associate_student_with_course(client):
    response = client.post("/students/1/courses", json={"course_id": 1})
    assert response.status_code == 200
    assert response.json() == {"message": "Course assigned successfully."}

def test_invalid_course_assignment(client):
    response = client.post("/students/1/courses", json={"course_id": 999})
    assert response.status_code == 404
    assert response.json() == {
        "error": {
            "code": "E001",
            "message": "Invalid course ID."
        }
    }

def test_retrieve_student_with_courses(client):
    response = client.get("/students/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "John Doe",
        "email": "john@example.com",
        "courses": []  # adjust based on available courses for the student
    }
```

---

## V. Security Considerations
- Validate all user inputs to prevent injections (e.g., SQL Injection).
- Ensure sensitive information is not included in error messages or logs.

---

## VI. Deployment Considerations
- Prepare a `.env` file that configures the SQLite database path.
- Ensure application capabilities for rolling out database migrations on startup without affecting existing data.

---

## VII. Development Workflow
1. Implement the required updates to the Student model and API as specified.
2. Execute the database migration and verify existing Student and Course data's integrity.
3. Conduct tests to ensure each functional requirement is achieved.
4. Update README.md with instructions on the new endpoints and overall system adjustments.

---

## VIII. Monitoring and Logging
- Implement logging of significant events and errors using a structured format, ensuring sensitive data is never exposed in logs.

---

## IX. Future Considerations
- Future iterations could include interfaces for course management where educators can create or delete courses linked to students.
- Integration of user authorization measures to manage who can assign courses to students.

This implementation plan outlines the complete steps to establish a Course relationship within the Student entity, ensuring simplicity, stability, and the retention of existing functionality.