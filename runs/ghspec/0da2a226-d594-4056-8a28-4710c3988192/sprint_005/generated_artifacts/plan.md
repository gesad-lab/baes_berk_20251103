# Implementation Plan: Create Teacher Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Course Relationship to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Email Field to Student Entity

## Version
1.0.0

## Overview
This implementation plan outlines the steps required to introduce a new Teacher entity within the existing educational management system. The Teacher entity will enable effective management of teacher records, paving the way for future functionalities related to teacher assignments, scheduling, and performance tracking.

## Architecture Overview
- **Architecture Pattern**: RESTful microservice (consistent with prior implementations)
- **Components**:
  - API Layer: New endpoints for creating and retrieving Teacher records.
  - Service Layer: Business logic for handling Teacher-related operations.
  - Data Layer: Update the existing SQLite database schema to incorporate the new Teacher entity.
- **Deployment**: Remains on the existing lightweight server setup, no infrastructure changes required.

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
  - Define new routes for creating and retrieving Teacher records.
  - Validate incoming requests for Teacher creation.

### 2. Service Layer
- **Module Name**: `services`
- **Responsibilities**:
  - Implement business logic in a new `teacher_service.py` to handle Teacher creation and retrieval.

### 3. Data Layer
- **Module Name**: `models`
- **Responsibilities**:
  - Define the new Teacher entity schema and manage database migrations to ensure data integrity.

## Implementation Approach

### Project Structure
```
educational_management_app/
│
├── src/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── routes.py          # Update API endpoints to include teacher management
│   │   └── dependencies.py     # Dependency functions
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── student_service.py  # Existing student service logic
│   │   └── teacher_service.py   # New business logic for managing teachers
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── models.py           # Update to include Teacher entity
│   │
│   ├── main.py                 # Application entry point
│   └── config.py               # Configuration settings
│
├── tests/
│   ├── __init__.py
│   ├── test_routes.py          # Unit tests for API endpoints
│   ├── test_services.py        # Unit tests for business logic
│   └── test_teacher.py         # New tests for teacher creation and retrieval
│
├── .env.example                 # Sample environment variables
├── requirements.txt             # Project dependencies
└── README.md                    # Documentation
```

### Step-by-Step Implementation

1. **Update Data Models**
   - Modify `models.py` to define the new `Teacher` entity:
   ```python
   from sqlalchemy import Column, Integer, String
   from sqlalchemy.ext.declarative import declarative_base

   Base = declarative_base()

   class Teacher(Base):
       __tablename__ = 'teachers'

       id = Column(Integer, primary_key=True, autoincrement=True)
       name = Column(String, nullable=False)
       email = Column(String, nullable=False)

       __table_args__ = (
           UniqueConstraint('email', name='uq_teacher_email'),  # Ensure email uniqueness
       )
   ```

2. **Database Migration Strategy**
   - Utilize Alembic to create a migration that:
     - Adds the `teachers` table for storing teacher records.
     - Preserves data integrity for existing tables (Students and Courses) during the migration.
   ```bash
   alembic revision --autogenerate -m "Add Teacher entity to the database"
   ```

3. **Implement Services Logic**
   - In `teacher_service.py`, implement:
     - `create_teacher(name: str, email: str)`: to create a new Teacher record.
     - `get_teachers()`: to retrieve existing Teacher records.
   ```python
   def create_teacher(name: str, email: str):
       # Logic to create a new teacher record, ensure email uniqueness.
   ```

4. **Define API Endpoints**
   - In `routes.py`, create new endpoints:
   - **POST** `/teachers` to create a Teacher:
     ```json
     {
       "name": "John Doe",
       "email": "john.doe@example.com"
     }
     ```
   - **GET** `/teachers` to retrieve a list of Teachers:
     ```json
     {
       "teachers": [
         {
           "id": 1,
           "name": "John Doe",
           "email": "john.doe@example.com"
         }
       ]
     }
     ```

5. **Implement Input Validation**
   - Use Pydantic schemas to validate the request body for teacher creation ensuring that both the name and email are provided.

6. **Error Handling**
   - Implement checks to return meaningful error messages for scenarios such as missing fields or invalid email formats.

7. **Testing**
   - Create a new testing file `test_teacher.py` to validate all Teacher-related scenarios:
   ```python
   def test_create_teacher_with_valid_data():
       response = client.post("/teachers", json={"name": "Jane Doe", "email": "jane.doe@example.com"})
       assert response.status_code == 201  # Created
   ```

8. **Documentation**
   - Update `README.md` to include instructions for the new Teacher API endpoints, showcasing example requests and responses.

## Data Models

### New Teacher Entity
```json
{
  "id": "integer (primary key, automatically generated)",
  "name": "string (required)",
  "email": "string (required, must follow a valid email format, unique)"
}
```

## API Contracts

### Create Teacher
- **Endpoint**: POST `/teachers`
- **Request Body**:
  ```json
  {
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
  ```
- **Response** (201 Created):
  ```json
  {
    "message": "Teacher successfully created."
  }
  ```

### Retrieve Teachers
- **Endpoint**: GET `/teachers`
- **Response**:
  ```json
  {
    "teachers": [
      {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com"
      }
    ]
  }
  ```

### Error Responses
- **Missing Required Fields** (400):
```json
{
  "error": {
    "code": "E001",
    "message": "Both name and email are required."
  }
}
```
- **Invalid Email Format** (400):
```json
{
  "error": {
    "code": "E002",
    "message": "Email format is invalid."
  }
}
```
- **Email Already Exists** (409):
```json
{
  "error": {
    "code": "E003",
    "message": "A teacher with this email already exists."
  }
}
```

## Success Criteria
- All user scenarios pass without errors confirming the expected behavior of the Teacher entity.
- The application correctly creates and stores Teacher records with valid name and email entries.
- All API responses related to teachers are valid JSON and correctly format the required data.
- The database schema is updated accordingly to reflect the new Teacher entity while preserving existing records for Students and Courses.

## Final Considerations
### Scalability
- Plan for potential migration to a more robust database solution (e.g., PostgreSQL) as usage increases.

### Security
- Conduct thorough input validation and error handling to prevent vulnerabilities.

### Maintainability
- Follow clean code practices and maintain a clear project structure for future modifications.

### Logging and Monitoring
- Consider implementing structured logging within the API to track Teacher creation and retrieval actions and their outcomes.

--- 

This implementation plan serves as a comprehensive guide to adding the Teacher entity to the educational management system, ensuring integration with existing functionalities and maintaining high development standards.