# Implementation Plan: Add Course Relationship to Student Entity

---

## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Course Relationship to Student Entity

---

## I. Overview

This implementation plan outlines detailed steps for adding a relationship between the Student and Course entities to allow students to enroll in multiple courses. This enhancement will enable the tracking of students' academic progress and facilitate better management of their educational journey.

## II. Architecture

### 1. Architecture Components
- **Web Framework**: FastAPI (remains unchanged)
- **Database**: SQLite (remains unchanged)
- **ORM**: SQLAlchemy (remains unchanged)
- **Data Serialization**: Pydantic (remains unchanged)

### 2. Module Boundaries
- **API Module**: Responsible for handling HTTP requests and responses related to Student-Course enrollment.
- **Database Module**: Introduce a new junction table, `StudentCourse`, to establish many-to-many relationships between Students and Courses.
- **Service Layer**: Business logic for enrolling and unenrolling students from courses will be implemented, including validation.

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
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class StudentCourse(Base):
    __tablename__ = 'student_courses'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('students.id'), nullable=False)
    course_id = Column(Integer, ForeignKey('courses.id'), nullable=False)
```

### 2. API Contracts

- **POST /students/{id}/courses**
  - **Request Body**: 
    ```json
    {
      "course_ids": [1, 2, 3]
    }
    ```
  - **Response**: 
    ```json
    {
      "message": "Enrollment successful"
    }
    ```
  - **Status Codes**: `200 OK`
  
- **DELETE /students/{id}/courses/{course_id}**
  - **Response**: `204 No Content` (successful unenrollment)
  
- **GET /students/{id}/courses**
  - **Response**: 
    ```json
    [
      {
        "id": "integer",
        "name": "string",
        "level": "string"
      }
    ]
    ```
  - **Status Codes**: `200 OK`
  
- **GET /students/{id}**
  - **Response**: 
    ```json
    {
      "id": "integer",
      "name": "string",
      "courses": [
        {
          "id": "integer",
          "name": "string",
          "level": "string"
        }
      ]
    }
    ```
  - **Status Codes**: `200 OK`

## V. Implementation Approach

### 1. Project Structure

```
student_course_app/
├── src/
│   ├── main.py          # Entry point of the application
│   ├── models.py        # Database models including the StudentCourse model
│   ├── schemas.py       # Pydantic validation schemas for course enrollment
│   ├── api.py           # API endpoint definitions for student enrollment
│   └── database.py      # Database connection and initialization
├── tests/
│   ├── test_api.py      # API test cases for student-course relationships
├── requirements.txt      # Dependency requirements
└── README.md             # Project documentation
```

### 2. Development Steps
1. **Update `models.py`**: Add the `StudentCourse` model.
2. **Create `schemas.py`**: Define Pydantic models for enrollment requests.
3. **Adjust API Endpoint Definitions**: Implement the student enrollment and unenrollment operations in `api.py`.
4. **Implement Enrollment Logic**: Validate course IDs during student enrollment requests.
5. **Create a Migration Script**: Utilize Alembic to create the `student_courses` junction table without affecting existing data.
6. **Write Unit Tests**: Validate the functionality of student enrollment and unenrollment, including input validations.
7. **Implement Integration Tests**: Test the complete flow of enrolling/unenrolling students through the API.
8. **Update Documentation**: Ensure `README.md` includes updated API details for student-course operations.

### 3. Database Migration Strategy
- Use Alembic for creating the migration file that defines the new junction table:
  - SQL command:
    ```sql
    CREATE TABLE student_courses (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      student_id INTEGER NOT NULL,
      course_id INTEGER NOT NULL,
      FOREIGN KEY (student_id) REFERENCES students(id),
      FOREIGN KEY (course_id) REFERENCES courses(id)
    );
    ```
- Ensure this migration does not disrupt any existing relationships or entities in the database.

## VI. Testing Approach

### 1. Testing Strategies
- **Unit Tests**: Focus on enrollment/unenrollment functionality, including validation errors for invalid course IDs.
- **Integration Tests**: Ensure that all API endpoints function correctly in retrieving, enrolling, and unenrolling students.

### 2. Minimum Test Coverage
- Aim for at least 70% coverage on business logic with critical paths (enrollment and unenrollment) exceeding 90%.

## VII. Security & Performance Considerations

### 1. Security Measures
- Input sanitization and validation are crucial to prevent injection attacks or invalid operations.
- Respond with appropriate error messages when validation checks fail.

### 2. Performance Optimization
- Consider adding indexes on commonly queried fields in the junction table in future enhancements to improve performance.

## VIII. Conclusion

This implementation plan provides a structured approach to establish a relationship between Students and Courses within the existing application. Adhering to the defined architecture and technology stack, along with robust testing and migration strategies, will enhance functionality without compromising the integrity of the existing system.

**Existing Code Files Modifications**:
- **models.py**: Add the `StudentCourse` model.
- **schemas.py**: Create Pydantic class for enrollment validation.
- **api.py**: Implement the endpoints for course enrollment and retrieval.

### Instructions for Technical Plan:
1. Ensure modifications are documented clearly and maintain backward compatibility with any existing data models.
2. Follow the defined migration strategy to create the `student_courses` table.
3. Validate error handling is appropriate for invalid requests during enrollment operations, especially regarding course ID validation.

Existing Code Files:
File: tests/test_api.py
```python
import requests

BASE_URL = "http://localhost:8000/students"  # Base URL for Student API

def test_enroll_student_in_courses():
    """Test enrolling a student in multiple courses."""
    student_id = 1  # Example student ID
    course_ids = [1, 2]  # Example course IDs
    response = requests.post(f"{BASE_URL}/{student_id}/courses", json={"course_ids": course_ids})
    assert response.status_code == 200  # Ensure enrollment is successful
    assert response.json()["message"] == "Enrollment successful"  # Confirm successful message

def test_unenroll_student_from_course():
    """Test unenrolling a student from a course."""
    student_id = 1  # Example student ID
    course_id = 1  # Example course ID
    response = requests.delete(f"{BASE_URL}/{student_id}/courses/{course_id}")
    assert response.status_code == 204  # Ensure unenrollment is successful
```

This plan should provide a clear path to effectively implement the student-course relationship functionality, ensuring a strong focus on maintainability, security, and performance throughout the development process.