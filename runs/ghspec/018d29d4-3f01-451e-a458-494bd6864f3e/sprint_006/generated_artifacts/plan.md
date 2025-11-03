# Implementation Plan: Add Teacher Relationship to Course Entity

---
**INCREMENTAL DEVELOPMENT CONTEXT**

**Previous Sprint Plan:**
# Implementation Plan: Create Teacher Entity

---
**INCREMENTAL DEVELOPMENT CONTEXT**

**Previous Sprint Plan:**
# Implementation Plan: Add Course Relationship to Student Entity

---

**INCREMENTAL DEVELOPMENT CONTEXT**

**Previous Sprint Plan:**
# Implementation Plan: Add Email Field to Student Entity

---

**INCREMENTAL DEVELOPMENT CONTEXT**

**Previous Sprint Plan:**
# Implementation Plan: Student Management Web Application

## Version: 1.0.0  
## Date: [Insert Date]

---

## I. Overview
The purpose of this document is to outline the technical implementation plan for adding a relationship between the Course and Teacher entities within the existing Educational Management System. This feature aims to optimize course management, enabling efficient tracking of which teachers instruct which courses. It sets the groundwork for improved administrative functions, including scheduling and teacher performance evaluations.

## II. Technology Stack
- **Programming Language**: Python 3.11+
- **Web Framework**: FastAPI
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Testing Framework**: pytest
- **Migration Tool**: Alembic

## III. Architecture Overview
The architecture extends the existing FastAPI framework to manage HTTP requests while utilizing SQLAlchemy for database interactions. This implementation will involve adding a `teacher_id` foreign key to the `Course` table, linking it to the `Teacher` entity.

### 1. Module Boundaries
- **API Module**: New API endpoints for assigning and retrieving teacher information linked to courses.
- **Models Module**: Modification of the existing `Course` model to include `teacher_id`.
- **Database Module**: Migration management to add the new relationship without affecting existing data.
- **Validation Module**: Input validations for course and teacher IDs during the assignment process.

## IV. Data Model
### 1. Course Entity Update
- **Table Name**: courses
- **Updated Fields**:
  - **id** (INTEGER, Primary Key, Auto Increment)
  - **name** (STRING, REQUIRED)
  - **description** (STRING, OPTIONAL)
  - **teacher_id** (INTEGER, FOREIGN KEY, nullable=True, references `teachers.id`)

### 2. Migration Strategy
- A migration script will be created using Alembic to add the `teacher_id` field to the `courses` table while preserving existing data.

## V. API Contracts
### 1. Endpoints
- **POST /courses/{course_id}/assign_teacher**
  - **Description**: Assign a teacher to a specific course.
  - **Request Body**:
    ```json
    {
      "teacher_id": "integer" (required)
    }
    ```
  - **Responses**:
    - **200 OK**: Successfully assigned the teacher to the course.
    - **404 Not Found**: Course or teacher ID does not exist.

- **GET /courses/{course_id}**
  - **Description**: Retrieve course details including assigned teacher information.
  - **Responses**:
    - **200 OK**: Returns course details along with the teacher's name.
    ```json
    {
      "id": "integer",
      "name": "string",
      "description": "string",
      "teacher": {
        "name": "string"
      }
    }
    ```
    - **404 Not Found**: Course not found with the specified ID.

### 2. Error Responses
- Consistent error response structure:
```json
{
  "error": {
    "code": "E001",
    "message": "Validation error message here",
    "details": {}
  }
}
```

## VI. Implementation Phases
### 1. Setup Development Environment
- Ensure Python 3.11+ is installed.
- Verify existing stack is ready:
  ```bash
  pip install fastapi sqlalchemy alembic pytest
  ```

### 2. Develop the Application
#### 2.1 API Module Development
- Implement the `POST /courses/{course_id}/assign_teacher` endpoint to accept the `teacher_id`.
- Create the handler function to:
  - Validate existence of both course and teacher.
  - Update the `teacher_id` field in the `courses` table.

#### 2.2 Models Module Development
- Update the existing `Course` model with the new `teacher_id` field:
```python
from sqlalchemy import Column, ForeignKey

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # New relationship
```

#### 2.3 Database Module Development
- Create a migration script using Alembic to add the `teacher_id` column:
```python
from alembic import op
import sqlalchemy as sa

def upgrade():
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))
    op.create_foreign_key('fk_teacher', 'courses', 'teachers', ['teacher_id'], ['id'])

def downgrade():
    op.drop_constraint('fk_teacher', 'courses', type_='foreignkey')
    op.drop_column('courses', 'teacher_id')
```

### 3. Error Handling and Validation
- Implement checks to ensure valid course and teacher IDs are provided.
- Return appropriate HTTP error messages for invalid requests.

### 4. Testing
- Write automated tests focusing on:
  - Assigning a teacher to a course with valid IDs.
  - Retrieving course details, including the teacher's name when assigned.
  - Testing error responses for invalid course and teacher IDs.
- Example test structure:
```python
def test_assign_teacher_to_course_valid():
    response = client.post("/courses/1/assign_teacher", json={"teacher_id": 1})
    assert response.status_code == 200

def test_get_course_details_with_teacher():
    response = client.get("/courses/1")
    assert response.status_code == 200
    assert "teacher" in response.json()  # Ensure teacher info is included

def test_assign_teacher_to_invalid_course():
    response = client.post("/courses/999/assign_teacher", json={"teacher_id": 1})
    assert response.status_code == 404
```

## VII. Deployment Considerations
- Update the SQLite connection strings and ensure environment variables in `.env` are configured appropriately.
- Provide documentation in README.md for setup, API usage, and testing instructions.

## VIII. Logging and Monitoring
- Integrate structured logging practices for capturing API requests and error events for better visibility.

## IX. Scaling Considerations
- Future scalability strategies may involve moving to a more robust database system (e.g., PostgreSQL) to handle increased load.
- Consider implementing caching mechanisms for teacher and course data to enhance performance over time.

## X. Success Criteria
- Successful assignment of teachers to courses confirmed via automated tests.
- Ensure API responses adhere to defined JSON formats.
- Maintain the application’s stability during stress testing.

---

## Trade-offs and Decisions
1. **Tech Stack Consistency**: Kept the current technology stack to ensure compatibility and minimize the learning curve.
2. **Database Migration**: Chose Alembic for its ease of use with SQLAlchemy and ability to handle migrations safely.
3. **Foreign Key Constraint**: Incorporated to ensure referential integrity while allowing `NULL` values for courses without assigned teachers.

---

This implementation plan outlines the steps necessary to establish a relationship between the Teacher and Course entities in the Educational Management System. It documents all aspects of development, testing, and deployment while ensuring compatibility with the current setup.

Existing Code Files:
File: `tests/test_courses_api.py`
```python
import pytest
from fastapi.testclient import TestClient
from main import app  # Assume FastAPI app is instantiated in a file named main.py
from models import Course  # Import the Course model

client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_database():
    """Setup the database before each test case."""
    # Prepare a clean state for the tests, create tables, etc.
    pass  # Implement your actual test DB setup logic here
```