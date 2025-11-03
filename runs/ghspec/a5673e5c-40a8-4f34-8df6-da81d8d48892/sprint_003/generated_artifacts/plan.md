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
This document outlines the technical implementation plan for introducing a new Course entity within the existing Student Management Web Application. This new feature will enable better organization and categorization of courses, allowing users to associate students with specific courses.

## II. Architecture
- **Type**: Microservices architecture
- **Components**:
  - **API Service**: Handles CRUD operations and business logic for courses.
  - **Database**: SQLite for both the Course and Student data.

### Component Interaction
1. The API service will interact with the SQLite database to store and retrieve course records.
2. The API will expose new RESTful endpoints for client interaction, dedicated to course management functions.

## III. Tech Stack
- **Backend Framework**: FastAPI (Python 3.11+)
- **Database**: SQLite (via SQLAlchemy ORM)
- **Serialization**: Pydantic for data validation and serialization
- **Testing Framework**: Pytest for unit and integration testing
- **Environment Management**: Poetry (to manage dependencies)

## IV. Module Boundaries and Responsibilities
### API Service (`api` module)
- Responsible for the following operations:
  - Create a new course record.
  - Retrieve course details.
  - Update a course's level.
  - Validate inputs for course creation and updates.

### Database Model (`models` module)
- Contains SQLAlchemy models and relationships.
- Define a new `Course` entity in the Course model.

### Validation (`schemas` module)
- Pydantic schemas for request validation and response serialization for courses.

## V. Data Models
### Course Model
```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)  # Course name (required)
    level = Column(String, nullable=False)  # Course level (required)
```

### Pydantic Schemas
#### Create and Update Course
```python
from pydantic import BaseModel

class CourseCreate(BaseModel):
    name: str  # Required
    level: str  # Required

class CourseUpdate(BaseModel):
    level: str  # This will be used for updates only
```

#### Course Response Schema
```python
class CourseResponse(BaseModel):
    id: int
    name: str
    level: str
```

## VI. API Contracts
### Endpoints Specification
- **POST /courses**: Create a new course record
  - **Request Body**: `{"name": "Mathematics", "level": "100"}`
  - **Response**: `201 Created` with course details including name and level.
  
- **GET /courses/{name}**: Retrieve a course record by name
  - **Response**: `200 OK` with course details including name and level or `404 Not Found` if not found.
  
- **PUT /courses/{name}**: Update an existing course's level
  - **Request Body**: `{"level": "200"}`
  - **Response**: `200 OK` with updated course details or `404 Not Found`.

## VII. Implementation Approach
1. **Set up environment**: Confirm Python 3.11+ and Poetry for dependency management are configured.
2. **Update FastAPI app**:
   - Create `models.py` to define the new `Course` model.
   - Create `schemas.py` for Pydantic models to validate and serialize course-related data.
   - Modify `api.py` to include endpoints for creating, retrieving, and updating courses.
3. **Database Migration**:
   - Utilize Alembic to create migration scripts to add the `courses` table without affecting existing `students` table.
4. **CRUD Logic Implementation**:
   - Implement necessary logic in `api.py` to handle course CRUD operations.
5. **Input Validation Logic**:
   - Integrate Pydantic validation to ensure the correct format of course `name` and `level`.
6. **Testing**:
   - Write tests in `tests/test_api.py` to assess course functionalities and ensure validations work properly.

## VIII. Testing Strategy
### Coverage Goals
- Minimum of 80% test coverage across all business logic related to Course operations.
- Testing scenarios based on user scenarios outlined in the specification:
  - Successful creation, retrieval, and updating of course records.
  - Validation error handling when provided with invalid inputs.

### Test Organization
- Directory Structure:
```
.
├── src/
│   ├── api.py        # New endpoints for courses
│   ├── models.py     # New Course model
│   ├── schemas.py    # New schemas for courses
│   └── main.py
├── tests/
│   ├── test_api.py   # Tests for course functionalities
└── README.md
```

## IX. Security Considerations
- Utilize Pydantic for input validation to avoid SQL injection and malformed data.
- Ensure no sensitive user data is exposed through the API responses.

## X. Deployment Considerations
- Use environment variables for database connection strings and any sensitive configurations.
- Implement CI/CD pipelines for automated testing and deployment (if applicable).
- Validate that the application includes a health check endpoint.

## XI. Documentation
- Comprehensive README.md file should include:
  - Setup instructions for the new course feature.
  - Updated API usage instructions.
  - Testing procedures for the course-related functionalities.

## XII. Future Enhancements
- Additional features like course scheduling and prerequisites could be considered for expansion.
- User role management for accessing course-related functionalities may be implemented in future iterations.

## XIII. Trade-offs and Decisions
- **Migration Strategy**: Designing migration scripts carefully ensures that no data is lost and that existing functionalities continue to work.
- **FastAPI**: Selected for its performance and robustness, particularly suited for constructing APIs with high validation needs.
- **Testing Strategy**: Focused on achieving essential test coverage now; deeper testing scenarios (e.g., end-to-end tests) can follow as needed in later phases.

This plan establishes a systematic approach to integrate a new Course entity into the Student Management Web Application while adhering to industry best practices and ensuring backward compatibility with existing functionality.

Existing Code Files Modifications:
1. **models.py**: Create the `Course` class to define the new `courses` table in addition to the existing `students` table.
2. **schemas.py**: Add new Pydantic schemas for the Course entity.
3. **api.py**: Introduce new endpoints for course management, ensuring they fit within the current system's routing and structure.

Database Migration Strategy:
- An Alembic migration script to create the `courses` table:
```python
"""Create courses table

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
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False),
    )


def downgrade():
    op.drop_table('courses')
```

Existing Code Files:
File: `tests/test_api.py`
```python
import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.schemas import CourseCreate
from src.models import Course

client = TestClient(app)

@pytest.fixture(scope="module", autouse=True)
def setup_database():
    """Sets up the database for testing."""
    # Setup logic for creating the database schema goes here
    ...
    
def test_create_course():
    response = client.post("/courses", json={"name": "Biology", "level": "100"})
    assert response.status_code == 201
    assert response.json() == {"id": 1, "name": "Biology", "level": "100"}

def test_get_course():
    response = client.get("/courses/Biology")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Biology", "level": "100"}

def test_update_course_level():
    response = client.put("/courses/Biology", json={"level": "200"})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Biology", "level": "200"}

def test_create_course_invalid():
    response = client.post("/courses", json={"name": "", "level": ""})
    assert response.status_code == 422  # Unprocessable Entity
```

This technical implementation plan is designed to enhance the Student Management Web Application by introducing a Course entity and aligns with the project’s coding standards and architectural needs.