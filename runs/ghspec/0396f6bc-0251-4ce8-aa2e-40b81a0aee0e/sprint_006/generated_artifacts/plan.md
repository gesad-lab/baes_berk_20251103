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
# Implementation Plan: Student Entity Management

**Version**: 1.0.0  
**Purpose**: To implement a RESTful API for associating the `Teacher` entity with the `Course` entity within the student management application, allowing better management of teaching assignments.  
**Scope**: This implementation focuses on updating the backend API services to handle the relationship between `Courses` and `Teachers`, enabling assignments and retrieval of course details along with assigned teacher information.

---

## I. Architecture Overview

### 1.1 Technical Stack
- **Programming Language**: Python 3.11+
- **Framework**: FastAPI (for building the RESTful API)
- **Database**: SQLite (for local data storage)
- **ORM**: SQLAlchemy (for database interactions)
- **Testing**: Pytest (for tests)
- **Environment Management**: Poetry (for dependency management)

### 1.2 System Components
- **API Layer**: FastAPI application handling request routing, validation, and response formatting for course and teacher assignments.
- **Database Layer**: SQLite database with SQLAlchemy for persistent management of the `Course` and `Teacher` entities.
- **Validation Layer**: Input validation to ensure data integrity during teacher assignment.

---

## II. Module Boundaries and Responsibilities

### 2.1 API Module
- **Endpoints**:
  - `PATCH /courses/{courseId}/assign-teacher`: Assign a teacher to a specific course.
  - `GET /courses/{courseId}`: Retrieve course details, including the assigned teacher.
- **Responsibilities**:
  - Manage incoming HTTP requests and responses for teacher assignment and course details retrieval.
  - Validate request parameters and bodies.
  - Invoke the service layer for database operations involving course assignments and retrieval.

### 2.2 Service Module
- **Functions**:
  - `assign_teacher_to_course(course_id: int, teacher_id: int)`: Assign the specified teacher to the specified course.
  - `get_course_details(course_id: int)`: Retrieve the details of a course, including the assigned teacher.
- **Responsibilities**:
  - Encapsulate business logic for assigning teachers to courses and retrieving course details.
  - Interact with the database to perform operations on the `Course` and `Teacher` entities.
  - Handle error cases and validation scenarios.

### 2.3 Database Module
- **Entities**:
  - `Course`
  - `Teacher`
- **Responsibilities**:
  - Define the database schema and relationships using SQLAlchemy.
  - Manage data persistence and retrieval for courses and teachers.

---

## III. Data Models and Schema Design

### 3.1 Course Entity Update
The existing `Course` entity must be updated to include a `teacher_id` field that acts as a foreign key referencing the `Teacher` entity.

```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))  # New relationship
    teacher = relationship("Teacher", back_populates="courses")  # Define relationship
```

### 3.2 Teacher Entity
No changes are needed in the `Teacher` entity as defined in the previous sprint.

### 3.3 Database Initialization
- Implement a function to create the updated `courses` table.
```python
def initialize_database(db_url: str):
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)  # This handles the creation of the updated `courses` and existing `teachers` tables
```

### 3.4 Database Migration Strategy
- Use Alembic to create a migration file that implements the addition of the `teacher_id` column to the existing `courses` table while preserving existing data.
- The migration should add the new column and establish a foreign key constraint to the `teachers` table.

---

## IV. API Contracts

### 4.1 Assign Teacher to Course
- **Request**: 
  - **Method**: PATCH
  - **Endpoint**: `/courses/{courseId}/assign-teacher`
  - **Body**: 
    ```json
    {
      "teacherId": 1  // required
    }
    ```
- **Response**: 
  ```json
  {
    "message": "Teacher assigned to course successfully."
  }
  ```

### 4.2 Retrieve Course Details
- **Request**: 
  - **Method**: GET
  - **Endpoint**: `/courses/{courseId}`
- **Response**: 
  ```json
  {
    "course": {
      "id": 1,
      "title": "Algebra 101",
      "description": "Introduction to Algebra",
      "teacher": {
        "id": 1,
        "name": "John Doe",
        "email": "john@example.com"
      }
    }
  }
  ```

### 4.3 Validation Errors
- If a PATCH request is made with an invalid `teacherId`, return:
```json
{
  "error": {
    "code": "E404",
    "message": "Teacher not found."
  }
}
```
- If a GET request is made for a non-existent course, return:
```json
{
  "error": {
    "code": "E404",
    "message": "Course not found."
  }
}
```
- If the course ID does not correspond to an existing course:
```json
{
  "error": {
    "code": "E400",
    "message": "Invalid course ID."
  }
}
```

---

## V. Implementation Strategy

### 5.1 Development Phases
1. **Setup Project Environment**:
   - Initialize a new Git repository or branch if necessary.
   - Use Poetry for dependencies, including FastAPI, SQLAlchemy, Alembic, and testing tools.

2. **Implement Database Updates**:
   - Update the `Course` model to include the `teacher_id` field and define the relationship with the `Teacher`.

3. **Modify API Layer**:
   - Define new PATCH and GET endpoints in the FastAPI application for assigning teachers and retrieving course details respectively.
   - Ensure proper validation for request bodies and parameters to validate `teacherId` and `courseId`.

4. **Service Layer Development**:
   - Implement service methods for assigning a teacher to a course and retrieving course details along with the assigned teacher.
   - Ensure thorough error handling for invalid inputs for both endpoints.

5. **Database Migration**:
   - Utilize Alembic to generate migration scripts for adding the `teacher_id` to the existing `courses` table.
   - Validate that migrations execute properly without data loss and ensure that foreign key constraints are enforced.

6. **Testing**:
   - Use Pytest to develop unit and integration tests to ensure functionality for assigning teachers and retrieving courses.
   - Aim for a minimum of 70% coverage on business logic involving course and teacher assignments.

7. **Documentation**:
   - Update `README.md` to reflect new API endpoints, request/response formats, and usage instructions.
   - Ensure all code is adequately documented with comments and docstrings.

---

## VI. Security and Performance Considerations

### 6.1 Security
- Validate input for assigning teachers to courses to guard against injection vulnerabilities.
- Use environment variables for sensitive configurations instead of hardcoding values.
- Ensure that only authorized users can access the teacher assignment endpoint.

### 6.2 Performance
- Monitor the SQLite performance and plan for PostgreSQL migration if the need for scalability arises.
- Optimize queries for retrieving course details with teachers by using appropriate lazy/eager loading strategies, depending on the use case.

---

## VII. Logging and Monitoring
- Implement structured logging for API requests and errors in the FastAPI application, ensuring that logs include contextual information such as request IDs.
- Monitor key performance metrics and establish alerts for error rates and latencies, especially for endpoint access.

---

## VIII. Version Control Practices
- Maintain good Git hygiene, with detailed commit messages elaborating what changes have been made and why.
- Utilize `.gitignore` to exclude sensitive files, temporary outputs, and local environment configurations.

---

## IX. Conclusion
This implementation plan outlines the steps to establish the relationship between the `Teacher` and `Course` entities in the student management application. By allowing teachers to be assigned to courses, we enhance the system’s ability to manage educational offerings effectively. The approach maintains a modular architecture, emphasizes testing, and adheres to established coding and security standards.

**Modifications Needed in Existing Code**:
1. **models.py**: Introduce the `teacher_id` column to the `Course` class and define the relationship with `Teacher`.
2. **api.py**: Add routes for `/courses/{courseId}/assign-teacher` and `/courses/{courseId}` with appropriate handlers.
3. **services.py**: Implement methods for assigning teachers to courses and retrieving course details.
4. **database.py**: Include new database initialization scripts and migration setup for the updated `courses` table.
5. **tests/test_courses.py**: Create tests for the new functionality to ensure expected responses are returned for handling course-teacher assignments.

With these adjustments, the overall functionality of the application will improve dramatically, allowing for better educational oversight and management.

Existing Code Files:
```python
# Mockup for tests/test_courses.py for testing new functionality

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from fastapi.testclient import TestClient
from models import Base, Course, Teacher  # Import Course and Teacher models
from your_app import app  # Import the FastAPI application

@pytest.fixture(scope='function')
def test_database():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)  # Create all tables

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    yield SessionLocal  # Provide session to the tests
    Base.metadata.drop_all(engine)  # Cleanup after tests

@pytest.fixture(scope='function')
def client(test_database):
    app.dependency_overrides[get_db] = test_database  # Override get_db with the test database session
    with TestClient(app) as c:
        yield c  # Provide the test client

# Add test cases for assigning teachers to courses and retrieving course details here
``` 

This sets clear pathways for the implementation of the new teacher-to-course relationship while ensuring consistency and maintainability in the existing code architecture.