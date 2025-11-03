# Implementation Plan: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Student Management Web Application

## I. Overview
This document outlines the technical implementation plan for adding an email field to the Student entity in the Student Management Web Application. This enhancement will allow for better communication and management of student records.

## II. Architecture
- **Type**: Microservices architecture
- **Components**:
  - **API Service**: Handles CRUD operations and business logic for student records.
  - **Database**: SQLite for simplicity and ease of use during development.
  
### Component Interaction
1. The API service will interact with the SQLite database to store and retrieve student records, including the new email field.
2. The service will expose updated RESTful endpoints for client interaction, incorporating the email field.

## III. Tech Stack
- **Backend Framework**: FastAPI (Python 3.11+)
- **Database**: SQLite (via SQLAlchemy ORM)
- **Serialization**: Pydantic for data validation and serialization
- **Testing Framework**: Pytest for unit and integration testing
- **Environment Management**: Poetry (to manage dependencies)

## IV. Module Boundaries and Responsibilities
### API Service (`api` module)
- Responsible for the following operations:
  - Create a new student record (including email).
  - Retrieve student details by name (including email).
  - Update an existing student's email.
  - Validate email format upon student record creation or update.

### Database Model (`models` module)
- Contains SQLAlchemy models and relationships.
- Updates to Student entity definition to include email.

### Validation (`schemas` module)
- Pydantic schemas for request validation and response serialization, updated to include email handling.

## V. Data Models
### Updated Student Model
```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)  # New email field
```

### Updated Pydantic Schemas
#### Create and Update Student
```python
from pydantic import BaseModel, EmailStr

class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Email is now a required field with email validation

class StudentUpdate(BaseModel):
    email: EmailStr  # Only email update
```

#### Student Response Schema
```python
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str  # Include email in response
```

## VI. API Contracts
### Updated Endpoints Specification
- **POST /students**: Create a new student record
  - **Request Body**: `{"name": "John Doe", "email": "john.doe@example.com"}`
  - **Response**: `201 Created` with student details including email.
  
- **GET /students/{name}**: Retrieve a student record by name
  - **Response**: `200 OK` with student details including email or `404 Not Found` if not found.
  
- **PUT /students/{name}**: Update an existing student’s email
  - **Request Body**: `{"email": "jane.doe@example.com"}`
  - **Response**: `200 OK` with updated student details or `404 Not Found`.
  
## VII. Implementation Approach
1. **Set up environment**: Ensure Python 3.11+, Poetry for dependency management is already configured.
2. **Update FastAPI app**:
   - Modify `models.py` to include a new email field in the Student model.
   - Update `schemas.py` to include email in the request and response schemas.
   - Modify `api.py` to extend CRUD operations to include email handling.
3. **Database Migration**:
   - Create a database migration script to add the new email column to the existing Student table, ensuring that existing data remains intact.
   - Use Alembic or a similar migration tool to handle this.
4. **CRUD Logic Implementation**:
   - Implement create logic to handle email input in `api.py`.
   - Implement retrieve logic to return student details with email.
   - Implement update logic for updating the email in `api.py`.
5. **Email Validation Logic**:
   - Integrate Pydantic email validation to ensure emails conform to standard formats before creating or updating student records.
6. **Testing**:
   - Write unit tests in `tests/test_api.py` to validate the new email functionality.
   - Scenarios include valid email handling, invalid email submissions, and CRUD operations with emails.

## VIII. Testing Strategy
### Coverage Goals
- Minimum of 80% test coverage across all business logic considering both student name and email functionalities.
- Testing scenarios matching the user scenarios outlined in the specification:
  - Successful creation, retrieval, and update of student email.
  - Handling of erroneous requests (e.g., invalid email format).

### Test Organization
- Directory Structure:
```
.
├── src/
│   ├── api.py        # Updated for email handling
│   ├── models.py     # Updated for email field
│   ├── schemas.py    # Updated with email validation
│   └── main.py
├── tests/
│   ├── test_api.py   # Updated for testing email functionalities
└── README.md
```

## IX. Security Considerations
- Input validation through Pydantic schemas to mitigate injection attacks and enforce email format validation.
- Ensure no sensitive data (e.g., passwords) is logged.

## X. Deployment Considerations
- Use environment variables for configuration (e.g., database URI).
- Implement a CI/CD pipeline for testing and deployment (if applicable).
- Ensure a health check endpoint is available for monitoring.

## XI. Documentation
- Comprehensive README.md file to include:
  - Setup instructions.
  - Updated API usage with email.
  - Testing instructions.

## XII. Future Enhancements
- Additional fields for the Student entity as needed.
- Enhancement of data relationships between students and other entities.
- Email notifications could be considered in future iterations.

## XIII. Trade-offs and Decisions
- **Migration Strategy**: Ensuring no data loss during migration may extend time but ensures data integrity.
- **FastAPI**: Above offers performance and data validation features, making it suitable for building robust APIs.
- **Testing Strategy**: The focus is on achieving minimum coverage; further in-depth testing (like end-to-end) can be considered in future phases depending on project trajectory.

This plan provides a structured approach to enhance the Student Management Web Application by adding an email field, ensuring no disruption to existing functionalities while adhering to best practices and standards. 

Existing Code Files Modifications:
1. **models.py**: Add the line for the `email` column in the `Student` class.
2. **schemas.py**: Add `EmailStr` for email validation in the `StudentCreate` and `StudentUpdate` classes.
3. **api.py**: Modify endpoints to handle email in the create and update operations.

Database Migration Strategy:
- Use Alembic to create a migration file that adds the `email` column to the Student table:
```python
"""Add email to student model

Revision ID: xxxxxxxx
Revises: xxxxxxxx
Create Date: YYYY-MM-DD HH:MM:SS.XXXXXX

"""
from alembic import op
import sqlalchemy as sa


revision = 'xxxxxxxx'
down_revision = 'xxxxxxxx'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('students', sa.Column('email', sa.String(), nullable=False))


def downgrade():
    op.drop_column('students', 'email')
```