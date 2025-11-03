# Implementation Plan: Create Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Student Management Web Application

## I. Architecture Overview
The architecture for the Student Management Web Application remains predominantly unchanged. The addition of the Course entity involves integrating a new data model and corresponding API endpoints. The architecture consists of the following components:

1. **FastAPI Server**: Continues to manage API requests and responses for both Student and Course entities.
2. **SQLite Database**: The schema will be updated to accommodate the new Course table without affecting existing Student records.
3. **Data Models**: New model implementation for Course data.
4. **API Endpoints**: Addition of new endpoints for Course management.
5. **Automatic Schema Creation**: Updates on application startup will handle the new Course schema migrations.

## II. Technology Stack
- **Backend Framework**: FastAPI
- **Database**: SQLite
- **ORM**: SQLAlchemy (for database interaction)
- **ASGI Server**: Uvicorn (for serving the FastAPI app)
- **Dependency Management**: Poetry or Pip for package handling
- **Testing Framework**: pytest for unit and integration tests

## III. Module Boundaries and Responsibilities
- **Main Application Module**: Entry point for the FastAPI application.
- **Database Module**: Additions to manage connections, schema changes, and migrations for both Student and Course entities.
- **Models Module**: Introduction of the new Course model, alongside existing Student model.
- **API Module**: New routes for Course endpoints and validations.
- **Errors Module**: Centralized error handling to include responses for Course-related errors.

## IV. Data Models and API Contracts

### Data Model
```python
class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)  # Required
    level = Column(String, nullable=False)  # Required
```

### API Contracts
- **Endpoint: POST `/courses`**
  - **Request Body**:
    ```json
    {
      "name": "Introduction to Python",
      "level": "Beginner"
    }
    ```
  - **Response** (Upon Successful Creation):
    ```json
    {
      "id": 1,
      "name": "Introduction to Python",
      "level": "Beginner"
    }
    ```
  - **Error Response** (When name or level is missing):
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Both name and level are required."
      }
    }
    ```

- **Endpoint: GET `/courses/{id}`**
  - **Response** (On Successful Retrieval):
    ```json
    {
      "id": 1,
      "name": "Introduction to Python",
      "level": "Beginner"
    }
    ```
  - **Error Response** (When ID does not exist):
    ```json
    {
      "error": {
        "code": "E002",
        "message": "Course not found."
      }
    }
    ```

## V. Implementation Steps

1. **Project Update**
   - Confirm the existing FastAPI project structure is intact. No extra directories are necessary for the new Course feature.

2. **Dependency Installation**
   - All required dependencies are already present in the project. No new installations required.

3. **Model Creation**
   - Create a new file named `models/course.py` and implement the following Course model:
    ```python
    from sqlalchemy import Column, Integer, String
    from src.database import Base

    class Course(Base):
        __tablename__ = 'courses'
        
        id = Column(Integer, primary_key=True, index=True)
        name = Column(String, nullable=False)  # Required
        level = Column(String, nullable=False)  # Required
    ```

4. **Database Migration**
   - Use Alembic for managing database schema changes to add the Course table. Implement a migration file through the following steps:
     1. Generate a migration using Alembic:
        ```bash
        alembic revision --autogenerate -m "Add Course table"
        ```
     2. Edit the generated migration script to:
        ```python
        def upgrade():
            op.create_table(
                'courses',
                sa.Column('id', sa.Integer(), nullable=False),
                sa.Column('name', sa.String(), nullable=False),
                sa.Column('level', sa.String(), nullable=False),
                sa.PrimaryKeyConstraint('id')
            )
        
        def downgrade():
            op.drop_table('courses')
        ```
     3. Apply the migration on application startup using:
        ```bash
        alembic upgrade head
        ```

5. **API Endpoints Implementation**
   - Create or modify the `api.py` file to include new endpoints for creating and retrieving courses. Validation must be implemented to check for the presence of `name` and `level`.

6. **Error Handling Module**
   - Extend the existing centralized error handling in `errors.py` to respond appropriately for Course validations where fields are missing.

7. **Application Entry Point**
   - Ensure `app.py` is configured to include the new Course routes. Confirm no changes are necessary unless there are adjustments for managing migrations on startup.

8. **Testing**
   - Extend `tests/test_api.py` and create a new `tests/test_course.py` to include tests for:
     - Creating a course with both a name and a level.
     - Handling errors when either name or level is missing.
     - Ensuring all existing functionalities with the Student entity remain intact.
   - Validate the creation and retrieval of courses using `pytest`.

9. **Documentation**
   - Update FastAPI’s auto-generated OpenAPI documentation to reflect new endpoints.
   - Modify `README.md` to provide guidance on the new Course entity’s API endpoints, ensuring there's clarity on input and output specifications.

## VI. Scalability, Security, and Maintainability Considerations
- **Scalability**: The design will support future resilience; additional performance enhancements may be implemented as the user load increases.
- **Security**: Follow the principle of least privilege when considering future user access. Validate user input to mitigate injection attacks.
- **Maintainability**: All new code follows established coding standards to promote accessibility and understanding.

## VII. Trade-offs and Decisions
- **SQLite**: Remains the chosen database due to existing integrations and ease of use, although considerations are made for possible migration to PostgreSQL.
- **Single Responsibility**: The structure has been maintained for clarity and understanding by continually following project patterns.

## VIII. Conclusion
This implementation plan outlines a systematic approach to adding a Course entity to the Student Management Web Application. It ensures that the existing functionality is preserved while integrating new features, enabling better course management within the application.

Existing Code Files:

File: tests/test_api.py
```
```python
import pytest
from fastapi.testclient import TestClient
from src.app import app
from src.db import get_db
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from src.models import Base, Student
from src.models.course import Course

# Setting up the test database in memory
@pytest.fixture(scope="module")
def test_db():
    # Create a new SQLite database in memory
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(bind=engine)

    # Create a new session for testing
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()

    yield db

    db.close()
```

File: tests/test_models.py
```
```python
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models import Base, Student
from src.models.course import Course

# Create a new SQLite database in memory for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a fixture to set up the database for each test
@pytest.fixture(scope="function")
def db():
    # Create the database tables for testing
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)
```