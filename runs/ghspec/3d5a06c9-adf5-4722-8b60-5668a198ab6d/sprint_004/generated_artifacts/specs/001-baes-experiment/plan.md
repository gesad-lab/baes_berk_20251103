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

## I. Overview

This implementation plan outlines the technical architecture, technology stack, and implementation approach for adding relationship functionality between the existing **Student** entity and the newly introduced **Course** entity within the Student Management Web Application. This capability allows for the linking of students to multiple courses, which enhances the application's ability to track student course participation effectively.

## II. Technology Stack

- **Backend Framework**: FastAPI (Python 3.11+)
- **Database**: SQLite (embedded database)
- **Data Access**: SQLAlchemy (for ORM interaction with SQLite)
- **API Documentation**: FastAPI's automatic OpenAPI support
- **Testing Framework**: pytest for unit and integration testing
- **Environment Management**: `venv` for virtual environment management
- **Dependency Management**: `requirements.txt` for Python dependencies

## III. Architecture

### A. Module Structure

The overall project structure will remain largely the same with the addition of a new `enrollment_routes.py` for handling course enrollments. The modified structure is as follows:

```
/student_management_app
│
├── src/                     # Source code for the application
│   ├── main.py              # Entry point for the FastAPI application
│   ├── models.py            # Database models (SQLAlchemy)
│   ├── schemas.py           # Pydantic schemas for request/response validation
│   ├── routes/              # API route handlers
│   │   ├── student_routes.py # Endpoint definitions related to students
│   │   ├── course_routes.py  # Endpoint definitions related to courses
│   │   └── enrollment_routes.py # New endpoint definitions for enrollments
│   └── database.py          # Database connection and setup
│
├── tests/                   # Testing files
│   ├── test_student_routes.py # Tests for student API routes
│   ├── test_course_routes.py  # Tests for course API routes
│   ├── test_enrollment_routes.py # New tests for enrollment API routes
│   └── test_database.py      # Tests for database interactions
│
├── .env.example              # Example environment variables
├── requirements.txt          # Python dependencies
└── README.md                 # Documentation for setup and usage
```

### B. Module Responsibilities

1. **models.py**: Create an SQLAlchemy model for the Enrollment entity with fields corresponding to `id`, `student_id`, and `course_id`.
2. **schemas.py**: Create new Pydantic schemas for request and response validation for enrollment operations.
3. **routes/enrollment_routes.py**: Implement API endpoints for enrolling students in courses, including endpoints to enroll a student and retrieve enrolled courses.
4. **database.py**: Modify the database initialization process to incorporate the new Enrollment table and relationships.

## IV. API Design

### A. API Endpoints

1. **Enroll Student in Course**
   - **Endpoint**: `POST /enrollments`
   - **Request Body**: 
     ```json
     {
       "student_id": "string",
       "course_id": "string"
     }
     ```
   - **Response**: 
     ```json
     {
       "id": "integer",
       "student_id": "string",
       "course_id": "string"
     }
     ```

2. **Retrieve Enrolled Courses for Student**
   - **Endpoint**: `GET /students/{student_id}/courses`
   - **Response**: 
     ```json
     [
       {
         "course_id": "integer",
         "course_name": "string"
       }
     ]
     ```

### B. Error Handling

- Consistent error responses will be utilized for handling invalid inputs:
  ```json
  {
    "error": {
      "code": "E002",
      "message": "Student ID or Course ID is invalid",
      "details": {}
    }
  }
  ```

## V. Database Design

### A. Schema Modification

- **Table**: Enrollments (new table)
  - **Columns**:
    - `id`: INTEGER PRIMARY KEY AUTOINCREMENT
    - `student_id`: INTEGER NOT NULL (foreign key referencing Student)
    - `course_id`: INTEGER NOT NULL (foreign key referencing Course)

### B. Database Migration Strategy

- A database migration will be created to add the `enrollments` table while ensuring existing Student and Course data remains intact. This will be implemented using Alembic.

```bash
# Migration command
alembic revision --autogenerate -m "Create Enrollments table and relationships"
```

## VI. Success Criteria

1. The API correctly handles enrollment creation and retrieval of enrolled courses.
2. All API endpoints return valid JSON responses according to specifications.
3. The SQLite database is correctly updated with an `enrollments` table.
4. Appropriate validation ensures that both Student ID and Course ID are required for enrollment, with correct error messaging for invalid inputs.

## VII. Testing Plan

### A. Test Coverage

- Targeting a minimum of 70% coverage across the application logic, particularly focusing on the new enrollment functionalities.
- Critical cases will involve successful enrollment and retrieval as well as testing for invalid payloads.

### B. Testing Structure

- **Unit Tests**: Units will be tested at the model and schema level.
- **Integration Tests**: Full route functionality will be tested in `tests/test_enrollment_routes.py`.

```python
# Example test in tests/test_enrollment_routes.py

def test_enroll_student(client):
    response = client.post('/enrollments', json={"student_id": "1", "course_id": "101"})
    assert response.status_code == 200
    assert response.json()["student_id"] == "1"

def test_retrieve_student_courses(client):
    response = client.get('/students/1/courses')
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Should return a list of courses
```

## VIII. Deployment Considerations

- Ensure the environment adheres to Python 3.11+ and SQLite versions as specified.
- Update the `.env.example` file to reflect any changes in required environment variables for the new functionality.

## IX. Documentation

- Update the README.md to include setup steps for enabling the enrollment feature, with usage examples and API endpoint documentation.

## X. Technical Trade-offs and Decisions

1. **Use of SQLAlchemy and FastAPI**: These choices facilitate rapid development and allow for ease of integration with existing models with minimal overhead.
2. **SQLite**: Opting for SQLite fits the current scale and simplicity needs, but future scalability may necessitate migration to a more robust database.
3. **Maintainability**: Following the existing coding standards and modular structure promotes long-term maintainability and ease of integration for subsequent features.

This implementation plan outlines a focused approach to integrating course enrollment functionality into the Student Management Web Application, ensuring seamless incorporation without disrupting existing capabilities and maintaining adherence to best coding practices.