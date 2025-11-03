# Implementation Plan: Create Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Student Management Web Application

## I. Overview

This implementation plan outlines the technical architecture, technology stack, and implementation approach for adding a new **Course** entity to the Student Management Web Application. This enhancement will enable the application to manage courses more effectively, linking them to students and their enrollments. The plan delineates modifications needed for the existing codebase to ensure smooth integration of the Course entity while maintaining backward compatibility.

## II. Technology Stack

- **Backend Framework**: FastAPI (Python 3.11+)
- **Database**: SQLite (embedded database for simplicity)
- **Data Access**: SQLAlchemy (for ORM interaction with SQLite)
- **API Documentation**: Automatically generated with FastAPI's built-in OpenAPI support
- **Testing Framework**: pytest for unit and integration testing
- **Environment Management**: `venv` for virtual environment management
- **Dependency Management**: `requirements.txt` for Python dependencies

## III. Architecture

### A. Module Structure

The project will continue to be organized into the existing directory structure, with the following modifications for the Course feature:

```
/student_management_app
│
├── src/                     # Source code for the application
│   ├── main.py              # Entry point for the FastAPI application
│   ├── models.py            # Database models (SQLAlchemy)
│   ├── schemas.py           # Pydantic schemas for request/response validation
│   ├── routes/              # API route handlers
│   │   ├── student_routes.py # Endpoint definitions related to students
│   │   └── course_routes.py   # Endpoint definitions related to courses
│   └── database.py          # Database connection and setup
│
├── tests/                   # Testing files
│   ├── test_student_routes.py # Tests for student API routes
│   ├── test_course_routes.py   # Tests for course API routes
│   └── test_database.py      # Tests for database interactions
│
├── .env.example              # Example environment variables
├── requirements.txt          # Python dependencies
└── README.md                 # Documentation for setup and usage
```

### B. Module Responsibilities

1. **models.py**: Create a SQLAlchemy model for the Course entity with attributes `id`, `name`, and `level`.
2. **schemas.py**: Create new Pydantic schemas for request and response validation for course creation and retrieval.
3. **routes/course_routes.py**: Implement the API endpoints for managing the Course entity (creation and retrieval).
4. **database.py**: Enhance the database initialization process to accommodate the new Course model.

## IV. API Design

### A. API Endpoints

1. **Create a Course**
   - **Endpoint**: `POST /courses`
   - **Request Body**: 
     ```json
     {
       "name": "string",
       "level": "string"
     }
     ```
   - **Response**: 
     ```json
     {
       "id": "integer",
       "name": "string",
       "level": "string"
     }
     ```

2. **List Courses**
   - **Endpoint**: `GET /courses`
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

### B. Error Handling

- Use consistent error responses to handle validation errors:
  ```json
  {
    "error": {
      "code": "E001",
      "message": "Course name is required",
      "details": {}
    }
  }
  ```

## V. Database Design

### A. Schema Modification

- **Table**: Courses (new table)
  - **Columns**:
    - `id`: INTEGER PRIMARY KEY AUTOINCREMENT
    - `name`: TEXT NOT NULL
    - `level`: TEXT NOT NULL

### B. Database Migration Strategy

- A database migration will be created to add the `courses` table while ensuring that the integrity of existing student records is preserved. This can be accomplished using Alembic for schema migration.

```bash
# Migration command
alembic revision --autogenerate -m "Create Course table"
```

## VI. Success Criteria

1. The API correctly handles all CRUD operations for the Course entity.
2. All API endpoints return valid JSON responses as per updated specifications.
3. The SQLite database is correctly initialized with the `courses` table.
4. Validation rules ensure that both name and level are required upon course creation and provide appropriate error messages for invalid inputs.

## VII. Testing Plan

### A. Test Coverage

- Aiming for at least 70% coverage across the application logic, focusing on the new Course functioning.
- Critical paths include scenarios for creation and retrieval of course records.

### B. Testing Structure

- **Unit Tests**: Testing individual components (models, schemas).
- **Integration Tests**: Testing overall API route functionality, especially with the Course functionality.

```python
# Example test in tests/test_course_routes.py

def test_create_course(client):
    response = client.post('/courses', json={"name": "Math 101", "level": "Beginner"})
    assert response.status_code == 200
    assert response.json()["name"] == "Math 101"
    assert response.json()["level"] == "Beginner"

def test_create_course_without_name(client):
    response = client.post('/courses', json={"level": "Beginner"})
    assert response.status_code == 400
    assert response.json()['error']['code'] == "E001"
```

## VIII. Deployment Considerations

- Ensure that the environment supports Python 3.11+ and SQLite.
- Provide a `.env.example` for environment configurations to avoid hardcoding sensitive data.

## IX. Documentation

- An updated README.md file will include setup instructions for the new Course functionality, usage examples, and updated API endpoint documentation.

## X. Technical Trade-offs and Decisions

1. **Choice of Migration Tool (Alembic)**: Using Alembic enables us to manage changes to our database schema effectively while ensuring data integrity during modifications.
2. **Maintaining SQLite**: Continuing with SQLite simplifies deployment and development; however, for future scaling needs, consideration should be given to transitioning to a more robust database solution.

By adhering to this implementation plan, the Student Management Web Application will successfully integrate the Course entity while maintaining adherence to coding best practices and ensuring backward compatibility.

Existing Code Files:
File: tests/test_course_routes.py
```python
import pytest

# Assuming the existence of a client fixture for the FastAPI application
@pytest.fixture
def client():
    from main import app  # Importing the FastAPI application
    from fastapi.testclient import TestClient
    return TestClient(app)

def test_list_courses(client):
    # Step 1: Create a couple of courses
    client.post('/courses', json={"name": "Physics 101", "level": "Intermediate"})
    client.post('/courses', json={"name": "Chemistry 101", "level": "Beginner"})
    
    # Step 2: Retrieve the courses
    response = client.get('/courses')
    assert response.status_code == 200
    assert len(response.json()) == 2
```

This implementation plan provides a structured approach for introducing the Course entity, ensuring seamless integration with existing functionalities while adhering to coding standards and maintaining backward compatibility.