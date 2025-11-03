# Implementation Plan: Create Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Email Field to Student Entity

## Version
1.0.1

## Overview
This implementation plan outlines the steps to enhance the existing Student Entity Web Application by adding a new Course entity. The new feature will allow users to manage courses alongside existing student records, enabling a structured overview of educational offerings.

## Architecture Overview
- **Architecture Pattern**: RESTful microservice (consistent with prior implementations)
- **Components**:
  - API Layer: New endpoints for Course management.
  - Service Layer: Business logic to handle course entity operations.
  - Data Layer: SQLite database schema to be updated to include the Course table alongside existing Student records.
- **Deployment**: No changes required; remains on the existing lightweight server setup.

## Technology Stack
- **Backend Framework**: FastAPI (Python)
- **Database**: SQLite
- **ORM**: SQLAlchemy (for database interactions)
- **Data Format**: JSON
- **Testing Framework**: pytest
- **Containerization**: Docker (optional for deployment)
- **Version Control**: Git

## Module Boundaries and Responsibilities

### 1. API Layer
- **Module Name**: `api`
- **Responsibilities**:
  - Define new routes for creating and retrieving courses.
  - Validate incoming requests for course creation.

### 2. Service Layer
- **Module Name**: `services`
- **Responsibilities**:
  - Implement business logic in a new `course_service.py` to handle creation and retrieval of courses.

### 3. Data Layer
- **Module Name**: `models`
- **Responsibilities**:
  - Define the new Course entity schema in `models.py`.
  - Manage database migrations for the new Course table, preserving existing Student data.

## Implementation Approach

### Project Structure
```
student_entity_app/
│
├── src/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── routes.py          # Update API endpoints for courses
│   │   └── dependencies.py     # Dependency functions
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── student_service.py  # Existing student service logic 
│   │   └── course_service.py    # New business logic for courses
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── models.py           # Update to include Course entity
│   │
│   ├── main.py                 # Application entry point
│   └── config.py               # Configuration settings
│
├── tests/
│   ├── __init__.py
│   ├── test_routes.py          # Unit tests for API endpoints
│   ├── test_services.py        # Unit tests for business logic
│   └── test_course.py          # New tests for Course entity
│
├── .env.example                 # Sample environment variables
├── requirements.txt             # Project dependencies
└── README.md                    # Documentation
```

### Step-by-Step Implementation

1. **Update Data Models**
   - Modify `models.py` to define the new `Course` entity:
   ```python
   from sqlalchemy import Column, Integer, String
   from sqlalchemy.ext.declarative import declarative_base

   Base = declarative_base()

   class Course(Base):
       __tablename__ = 'courses'

       id = Column(Integer, primary_key=True, autoincrement=True)
       name = Column(String, nullable=False)
       level = Column(String, nullable=False)  # New field
   ```

2. **Database Migration Strategy**
   - Use Alembic for handling database migrations. Create a migration script that:
     - Represents the Course table schema creation without impacting existing Student records.
   ```bash
   alembic revision --autogenerate -m "Add Course table"
   ```

3. **Implement Services Logic**
   - In a new `course_service.py`, implement:
     - `create_course(name: str, level: str)`: to create a course.
     - `get_course(course_id: int)`: to retrieve course information.
   ```python
   def create_course(name: str, level: str):
       # Logic to create a new course
       new_course = Course(name=name, level=level)
       # Add to session and commit...
   ```

4. **Define API Endpoints**
   - In `routes.py`, create new endpoints:
   - **POST** `/courses`:
     - Request body should include both `name` and `level`.
     ```json
     {
       "name": "Mathematics",
       "level": "Advanced"
     }
     ```
   - **GET** `/courses/{id}`: return course details including name and level.
     ```json
     {
       "id": 1,
       "name": "Mathematics",
       "level": "Advanced"
     }
     ```

5. **Implement Input Validation**
   - Utilize Pydantic schemas to validate the `name` and `level` fields ensuring they are required and formatted correctly.
   
6. **Error Handling**
   - Ensure appropriate error responses are implemented for missing fields or invalid inputs with clear messaging.

7. **Testing**
   - Create a new testing file `test_course.py` to validate the Course entity scenarios:
   - Implement tests for creating and retrieving courses, checking for error messages on invalid input.
   ```python
   def test_create_course_without_level():
       response = client.post("/courses", json={"name": "Mathematics"})
       assert response.status_code == 422  # Unprocessable Entity
       assert "level" in response.json()["detail"][0]["loc"]
   ```

8. **Documentation**
   - Update `README.md` to include usage instructions for the new course APIs and examples of requests and responses.

## Data Models

### New Course Entity
```json
{
  "id": "integer (primary key, automatically generated)",
  "name": "string (required)",
  "level": "string (required)"
}
```

## API Contracts

### Create Course
- **Endpoint**: POST `/courses`
- **Request Body**:
  ```json
  {
    "name": "Mathematics",
    "level": "Advanced"
  }
  ```
- **Response**:
  ```json
  {
    "id": 1,
    "name": "Mathematics",
    "level": "Advanced"
  }
  ```

### Retrieve Course
- **Endpoint**: GET `/courses/{id}`
- **Response**:
  ```json
  {
    "id": 1,
    "name": "Mathematics",
    "level": "Advanced"
  }
  ```

### Error Response for Missing Level
- **Response (400)**:
  ```json
  {
    "error": {
      "code": "E002",
      "message": "Level is required.",
      "details": {}
    }
  }
  ```

## Success Criteria
- All API endpoints return valid JSON including the name and level fields for courses.
- Successful execution of all specified user scenarios without errors.
- Appropriate handling of error cases related to missing or invalid fields.
- Successful creation and verification of the Course table in the SQLite database, ensuring existing Student records remain intact.

## Final Considerations
### Scalability
- Evaluate the need to transition to a more robust database such as PostgreSQL in the future for managing a growing user base.

### Security
- Ensure all inputs are validated and sanitized to prevent injection vulnerabilities.

### Maintainability
- Follow clean coding practices and retain a coherent project structure to facilitate future changes.

### Logging and Monitoring
- Implement structured logging to trace significant events throughout the course entity management process.

---

This plan establishes a clear framework for implementing the Course entity in the existing application, ensuring compatibility with current features and maintaining high standards of quality and maintainability.