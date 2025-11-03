# Implementation Plan: Create Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Student Management Web Application

## Version
**Version**: 1.1.0

## 1. Architecture Overview
This implementation introduces a new `Course` entity to manage and categorize courses associated with students. The addition will follow the existing microservice architecture utilizing Python with the FastAPI framework, SQLite for data persistence, and SQLAlchemy for ORM.

### Architecture Components
- **FastAPI**: Continue using for creating RESTful API endpoints.
- **SQLite**: Utilizing the same lightweight database.
- **SQLAlchemy**: ORM for managing database interactions, now including the new `Course` entity.

## 2. Technology Stack
- **Programming Language**: Python 3.11+
- **Framework**: FastAPI
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Testing Framework**: pytest
- **API Testing Tool**: Postman (for manual testing)

## 3. Module Boundaries & Responsibilities
### 3.1 Services
- **CourseService**: New service to handle business logic related to creating and retrieving course records.

### 3.2 Data Models
- **Course**: New data model representing the course entity with `id`, `name`, and `level` attributes.

### 3.3 API Endpoints
- **POST** `/courses`: New endpoint to create a course.
- **GET** `/courses/{id}`: New endpoint to retrieve course information.

## 4. Data Models
```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
```

## 5. API Contracts
### 5.1 Endpoints Specification
#### 5.1.1 Create a Course
- **Endpoint**: `POST /courses`
- **Request Body**:
    ```json
    {
        "name": "Mathematics",
        "level": "Beginner"
    }
    ```
- **Response** (201 Created):
    ```json
    {
        "id": 1,
        "name": "Mathematics",
        "level": "Beginner"
    }
    ```
- **Error Response** (400 Bad Request):
    ```json
    {
        "error": {
            "code": "E001",
            "message": "Name and level fields are required."
        }
    }
    ```

#### 5.1.2 Get Course Information
- **Endpoint**: `GET /courses/{id}`
- **Response**:
    ```json
    {
        "id": 1,
        "name": "Mathematics",
        "level": "Beginner"
    }
    ```
- **Error Response** (404 Not Found):
    ```json
    {
        "error": {
            "code": "E002",
            "message": "Course not found."
        }
    }
    ```

## 6. Database Migration Strategy
### 6.1 Migration Strategy
- Create a migration script that adds the new `courses` table, ensuring no loss of data within the existing database structure.
- Utilize Alembic for managing database migrations.

```bash
# Create migration file using Alembic 
alembic revision --autogenerate -m "Create courses table"
```

### 6.2 Migration Script Example
```python
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'xxxxxxx'
down_revision = 'yyyyyyy'  # Adjust this to match the last migration
branch_labels = None
depends_on = None

def upgrade():
    # Create courses table
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False)
    )

def downgrade():
    # Drop courses table
    op.drop_table('courses')
```

## 7. Testing Approach
### 7.1 Test Cases
1. **Create a Course**: Validate a valid request with both name and level creates a course and returns the correct response.
2. **Get Course Information**: Validate retrieval of a course's data using a valid ID.
3. **Handle Invalid Input**: Ensure appropriate errors are returned when creating a course without name or level.
4. **Database Schema Creation on Startup**: Verify the courses table is created successfully when the application starts.

### 7.2 Testing Framework
- Use `pytest` for unit and integration tests.
- Organize tests alongside the corresponding application module structure.

## 8. Security Considerations
- Ensure input validation for course name and level to prevent SQL injection and other security vulnerabilities.
- Implement structured error responses to avoid exposing sensitive error information.

## 9. Error Handling
- Provide structured error responses throughout the API for course-related validations.
- Implement validation checks for both `name` and `level` during the course creation process.

## 10. Documentation
- Update existing documentation to describe the new `/courses` endpoint and its usage.
- Document the database schema changes in the `README.md` to aid in migration understanding.

## 11. Deployment Considerations
- Thoroughly test the new functionality in a staging environment to ensure no disruptions occur in production.
- Verify that all API responses are consistently formatted in JSON according to the updated API contracts.

## 12. Version Control Practices
- Ensure each code change is committed with clear messages that detail the "why" behind changes, especially those related to the new Course entity.
- Maintain a clean `.gitignore` to exclude unnecessary files.

## 13. Implementation Timeline
- **Week 1**: Define the `Course` model and implement API endpoints.
- **Week 2**: Design, implement, and test migrations for the new course table.
- **Week 3**: Complete thorough testing, finalize documentation updates, and prepare for deployment.

---

**Trade-offs and Decisions**:
- Continued use of SQLite keeps the project lightweight while preparing it for potential scaling in the future.
- FastAPI will facilitate rapid API development and provide interactive documentation through Swagger.
- The design prioritizes backward compatibility to ensure that existing data remains untouched while adding new capabilities.

This implementation plan brings forth the `Course` entity in the Student Management Web Application while adhering to all defined architectural and design principles. 

Existing Code Files:
File: tests/test_course.py
```python
import pytest
from fastapi.testclient import TestClient
from main import app  # Assuming the FastAPI app is defined in main.py

client = TestClient(app)

@pytest.fixture(scope="module")
def setup_db():
    # Code for creating the test database schema can be added here.
    yield
    # Code for tearing down the database can be added here.

def test_create_course_success(setup_db):
    """Test successful creation of a course."""
    response = client.post("/courses", json={"name": "Mathematics", "level": "Beginner"})
    assert response.status_code == 201
    assert response.json()["name"] == "Mathematics"
    assert response.json()["level"] == "Beginner"
```

File: tests/integration/test_course_api.py
```python
import pytest
from fastapi.testclient import TestClient
from main import app  # Assuming the FastAPI app is defined in main.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Course  # Assuming the new Course model is in models.py

client = TestClient(app)

# Database setup for testing
DATABASE_URL = "sqlite:///./test.db"  # Use a separate test database
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="module")
def setup_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def test_get_course_success(setup_db):
    """Test retrieval of a course by ID."""
    # Assuming a course was created earlier using client.post
    response = client.get("/courses/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1
``` 

This plan facilitates the integration of a new `Course` entity into the existing application architecture, ensuring quality, security, and maintainability throughout the implementation process.