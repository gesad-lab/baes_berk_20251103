# Implementation Plan: Add Teacher Relationship to Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Teacher Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Course Relationship to Student Entity

---

## I. Overview

This implementation plan details the steps necessary to create a relationship between the Course entity and the Teacher entity within the educational management system. This feature will allow the assignment of teachers to courses, thereby enhancing the system's functionality and enabling better course management and organization.

## II. Architecture

### 1. Architecture Components
- **Web Framework**: FastAPI
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Data Serialization**: Pydantic

### 2. Module Boundaries
- **API Module**: Manages HTTP requests and responses related to course and teacher assignments.
- **Database Module**: Modifies the existing Course table to establish a foreign key relationship with the Teacher table.
- **Service Layer**: Contains the business logic for handling course assignments to teachers, including validation and error handling.

## III. Technology Stack

1. **Programming Language**: Python 3.11+
2. **Web Framework**: FastAPI
3. **Database**: SQLite
4. **ORM**: SQLAlchemy
5. **Data Validation**: Pydantic
6. **Dependency Management**: Poetry (or pip requirements)

## IV. Data Models and API Contracts

### 1. Data Model

```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)

    teacher = relationship("Teacher", back_populates="courses")

class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

    courses = relationship("Course", back_populates="teacher")
```

### 2. API Contracts

- **PATCH /courses/{course_id}/assign-teacher**
  - **Request Body**: 
    ```json
    {
      "teacher_id": "integer"
    }
    ```
  - **Response**: 
    ```json
    {
      "message": "Teacher assigned successfully."
    }
    ```
  - **Status Codes**: `200 OK` on success.

- **GET /courses/{course_id}**
  - **Response**: 
    ```json
    {
      "id": "integer",
      "title": "string",
      "teacher": {
        "id": "integer",
        "name": "string",
        "email": "string"
      }
    }
    ```
  - **Status Codes**: `200 OK`

## V. Implementation Approach

### 1. Project Structure

```
course_management_app/
├── src/
│   ├── main.py          # Entry point of the application
│   ├── models.py        # Database models including Course and Teacher
│   ├── schemas.py       # Pydantic validation schemas for course and teacher assignments
│   ├── api.py           # API endpoint definitions for course and teacher assignment
│   └── database.py      # Database connection and initialization
├── tests/
│   ├── test_api.py      # API test cases for course operations
├── requirements.txt      # Dependency requirements
└── README.md             # Project documentation
```

### 2. Development Steps
1. **Update `models.py`**:
   - Modify the existing `Course` model to add the `teacher_id` foreign key.
   
2. **Create or Update `schemas.py`**:
   - Define Pydantic models for validation of course assignment requests.
   
3. **Adjust API Endpoint Definitions**:
   - Implement the `PATCH /courses/{course_id}/assign-teacher` endpoint in `api.py`.
   - Implement the `GET /courses/{course_id}` endpoint to return course details including teacher information.

4. **Implement Course Assignment Logic**:
   - Validate the `teacher_id` against the `Teacher` table.
   - Handle errors gracefully, returning meaningful messages for invalid `teacher_id`.

5. **Create a Migration Script**:
   - Use Alembic to create a migration that adds the `teacher_id` column to the existing `courses` table without affecting existing data.

6. **Write Unit Tests**:
   - Validate the course assignment logic, ensuring that the correct success and error responses are returned.

7. **Implement Integration Tests**:
   - Test the overall process of assigning a teacher to a course and fetching course details.

8. **Update Documentation**:
   - Ensure `README.md` includes details on the new endpoints and usage examples for course and teacher relationships.

### 3. Database Migration Strategy
- Use Alembic to create a migration that updates the `courses` table:
  - SQL command:
    ```sql
    ALTER TABLE courses ADD COLUMN teacher_id INTEGER REFERENCES teachers(id);
    ```
- Ensure that this migration correctly alters the table while preserving existing data and relationships.

## VI. Testing Approach

### 1. Testing Strategies
- **Unit Tests**: Focus on validation logic for course assignments and interactions with the Teacher entity.
- **Integration Tests**: Ensure that both API endpoints function correctly for assigning teachers and retrieving course details.

### 2. Minimum Test Coverage
- Aim for at least 70% coverage on new business logic and a minimum of 90% coverage on the course assignment process.

## VII. Security & Performance Considerations

### 1. Security Measures
- Validate and sanitize user inputs for `teacher_id` to prevent invalid assignments.
- Ensure error messages are clear and informative for any validation failures.

### 2. Performance Optimization
- Consider adding an index on the `teacher_id` field for better performance in queries related to course-teacher assignments.

## VIII. Conclusion

This implementation plan provides a comprehensive approach to add a Teacher relationship to the Course entity within the educational management system. By adhering to architectural guidelines and ensuring proper validation and error handling, we will enhance the system's capabilities while maintaining data integrity.

**Existing Code Files Modifications**:
- **models.py**: Update the `Course` model to include `teacher_id`.
- **schemas.py**: Add validation for requests relating to course assignments.
- **api.py**: Implement the new endpoints for course teacher assignments (i.e., `PATCH /courses/{course_id}/assign-teacher`, `GET /courses/{course_id}`).

### Instructions for Technical Plan:
1. Document every modification clearly, ensuring backward compatibility.
2. Follow the defined migration strategy without disrupting any existing relationships.
3. Implement thorough error handling for cases of invalid teacher assignments.
4. Ensure that unit and integration tests are written to cover all new functionalities.

Existing Code Files:
File: tests/test_api.py
```python
import requests

BASE_URL = "http://localhost:8000/courses"  # Base URL for Course API

def test_assign_teacher_to_course():
    """Test assigning a teacher to a specific course."""
    response = requests.patch(f"{BASE_URL}/1/assign-teacher", json={"teacher_id": 1})
    
    assert response.status_code == 200  # Confirm assignment success
    assert response.json()["message"] == "Teacher assigned successfully."

def test_get_course_with_teacher():
    """Test retrieving course details with assigned teacher information."""
    response = requests.get(f"{BASE_URL}/1")
    
    assert response.status_code == 200  # Confirm retrieval success
    course = response.json()
    assert course["teacher"]["id"] == 1  # Check assigned teacher ID
```

### Instructions for Technical Plan:
1. MUST adhere to the existing tech stack and project structure.
2. Ensure new modules are seamlessly integrated with existing functionalities.
3. Document specific modifications needed to existing code files, maintaining backward compatibility.