# Implementation Plan: Create Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Student Entity Management

## Version
1.0.0

## Purpose
To introduce a new Course entity in the system that allows the definition of educational courses with specific attributes. This feature will enhance course management capabilities, enabling associations with existing entities, such as Students, and improving the organization of courses within the application.

## Architecture Overview
The application continues to maintain a microservices architecture centered on RESTful APIs. The backend is developed using Python with FastAPI, and SQLite serves as the database. This new feature will be integrated seamlessly with the existing structure, ensuring the application remains extensible.

## Technology Stack
- **Backend Framework**: FastAPI
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Testing**: pytest

## Module Boundaries and Responsibilities
1. **API Layer**:
   - Introduce endpoints for CRUD operations related to the Course entity.

2. **Service Layer**:
   - Manage the business logic for creating, retrieving, and validating Course entities.

3. **Persistence Layer**:
   - Define the schema for the Course entity and handle database interactions through SQLAlchemy.

## Data Models and API Contracts

### Data Model: Course
```python
from sqlalchemy import Column, Integer, String

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)  # New field added
```

### API Endpoints
1. **Create Course**
   - **Endpoint**: `POST /courses`
   - **Request Body**: 
     ```json
     {
       "name": "string",
       "level": "string"
     }
     ```
   - **Response**: 
     - 201 Created: `{ "id": integer, "name": "string", "level": "string" }`
     - 400 Bad Request if `name` or `level` is missing or invalid.

2. **Retrieve Course**
   - **Endpoint**: `GET /courses/{course_id}`
   - **Response**: 
     - 200 OK: `{ "id": integer, "name": "string", "level": "string" }`
     - 404 Not Found if `course_id` does not exist.

## Implementation Approach

### 1. Project Structure Update
- Update the existing FastAPI project structure to include the new Course entity as follows:
  ```
  src/
  ├── main.py
  ├── models.py       # New Course model added here
  ├── services.py     # New service functions for Course operations
  ├── api.py          # New API endpoints for Course management
  ├── database.py     # Database schema changes handled here
  tests/
  ├── test_api.py     # New tests for Course API endpoints
  ├── test_services.py # New tests for Course-related business logic
  ```

### 2. Database Migration
- **Alembic**: Implement database migrations using Alembic to create the new `courses` table while preserving existing data:
  ```python
  from alembic import op
  import sqlalchemy as sa

  def upgrade():
      op.create_table('courses',
          sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
          sa.Column('name', sa.String(), nullable=False),
          sa.Column('level', sa.String(), nullable=False)
      )

  def downgrade():
      op.drop_table('courses')
  ```

### 3. API Implementation
- Create new API endpoints in `api.py` for Course operations:
  - `POST /courses`: To create a new course with validation for `name` and `level`.
  - `GET /courses/{course_id}`: To retrieve course details by `course_id`.
  
### 4. Business Logic Update
- Implement service functions in `services.py` for:
  - Creating a new Course: Validate input and handle persistence.
  - Retrieving Course details: Fetch from the database and manage responses based on existence.

### 5. Input Validation
- Use Pydantic models for input validation in FastAPI:
```python
from pydantic import BaseModel

class CourseCreate(BaseModel):
    name: str
    level: str

class CourseResponse(BaseModel):
    id: int
    name: str
    level: str
```

### 6. Testing
- Write unit tests in `test_services.py` to validate Course creation and retrieval logic.
- Create integration tests in `test_api.py` to ensure that API endpoints respond as expected.

### 7. Docker Setup
- Ensure that the Dockerfile and Docker Compose configurations support new database migrations upon startup. Maintain integration with the existing deployment pipeline.

## Scalability, Security, and Maintainability Considerations
- Ensure that all configuration values are managed via environment variables.
- Implement robust input validation and error handling for Course creation.
- Maintain clear responsibilities in functions to support future enhancements.

## Trade-Offs and Decisions
- **Course Level Validation**: The `level` attribute will require predefined values (e.g., "Beginner," "Intermediate," "Advanced"). This decision enforces consistency but adds complexity in input validation.
- **No GUI Changes**: As per the specification, the initial rollout does not include any frontend integration. API functionality is prioritized for this phase.

### Success Criteria
- Ensure that all Course-related API endpoints return expected response times within the 500 ms threshold.
- Coverage for business logic involving Courses reaches at least 70% through unit and integration tests.

## Deployment Considerations
- Review and ensure Docker configurations are set to manage and perform database migrations smoothly during deployment.
- Maintain backward compatibility with existing entities, particularly ensuring that there are no disruptions to other functionalities.

## Conclusion
This implementation plan outlines the procedures necessary for integrating a new Course entity into the system, ensuring compliance with best practices for maintainability and scalability while addressing all specified functional requirements.

Existing Code Files:
### File: tests/test_api.py
```python
import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

@pytest.fixture(scope="module")
def setup_database():
    # Set up any necessary database state before tests
    yield
    # Clean up database state after tests

# Pydantic models for Course creation
class CourseCreate(BaseModel):
    name: str
    level: str  # Required field for course creation

def test_create_course_success(setup_database):
    """Test that creating a course successfully returns the expected course object."""
    response = client.post("/courses", json={"name": "Mathematics", "level": "Beginner"})
    assert response.status_code == 201
    assert response.json()["name"] == "Mathematics"
    assert response.json()["level"] == "Beginner"

def test_create_course_missing_fields(setup_database):
    """Test that creating a course without required fields returns a 400 error."""
    response = client.post("/courses", json={"name": ""})
    assert response.status_code == 400
    assert "error" in response.json()
```

### File: tests/test_services.py
```python
import pytest
from src.services import create_course, get_course_by_id
from sqlalchemy.orm import Session

@pytest.fixture(scope="module")
def db_session():
    """Set up a test database session."""
    # Setup code for the test database would go here
    yield db_session  # Replace with the actual session
    # Tear down code would go here

def test_create_course(db_session):
    """Test creating a course in the database."""
    course = create_course(db_session, "Science", "Intermediate")
    assert course is not None
    assert course.name == "Science"
    assert course.level == "Intermediate"

def test_get_course_by_id(db_session):
    """Test retrieving a course by its ID."""
    course = create_course(db_session, "History", "Advanced")
    retrieved_course = get_course_by_id(db_session, course.id)
    assert retrieved_course is not None
    assert retrieved_course.name == course.name
    assert retrieved_course.level == course.level
```
This implementation plan allows for developing the Course entity while maintaining modular design and adhering to coding standards established in the project's constitution.