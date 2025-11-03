# Implementation Plan: Create Teacher Entity

---

## INCREMENTAL DEVELOPMENT CONTEXT

### Previous Sprint Plan:
# Implementation Plan: Student Management Web Application

## I. Architecture Overview
The architecture for the Student Management Web Application will be extended to include the new Teacher entity while maintaining the existing structure. The fundamental components are as follows:

1. **FastAPI Server**: Continues to manage API requests and responses for Student and Course entities, with the addition of the Teacher entity.
2. **SQLite Database**: The database schema will be updated to include a new Teacher table while ensuring existing Student and Course records remain unaffected.
3. **Data Models**: Addition of a new Teacher model and modifications to ensure integration with existing entities.
4. **API Endpoints**: Two new endpoints for creating and retrieving teacher information will be added.
5. **Automatic Schema Creation**: Updates on application startup will handle the new Teacher table migrations.

## II. Technology Stack
- **Backend Framework**: FastAPI
- **Database**: SQLite
- **ORM**: SQLAlchemy (for database interaction)
- **ASGI Server**: Uvicorn (for serving the FastAPI app)
- **Dependency Management**: Poetry or Pip for package handling
- **Testing Framework**: pytest for unit and integration tests

## III. Module Boundaries and Responsibilities
- **Main Application Module**: The entry point for the FastAPI application, managing initial imports and route definitions.
- **Database Module**: Update to manage connections and schema changes for the new Teacher entity.
- **Models Module**: Create a new Teacher model in `src/models/teacher.py`.
- **API Module**: New routes for Teacher creation and retrieval.
- **Errors Module**: Centralized error responses for the Teacher entity operations.

## IV. Data Models and API Contracts

### Data Model Updates
```python
# In models/teacher.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, index=True)  # Auto-generated primary key
    name = Column(String, nullable=False)  # Required
    email = Column(String, nullable=False, unique=True)  # Required and unique
```

### API Contracts
- **Endpoint: POST `/teachers`**
  - **Request Body**:
    ```json
    {
      "name": "John Smith",
      "email": "john.smith@example.com"
    }
    ```
  - **Response** (Upon Successful Creation):
    ```json
    {
      "id": 1,
      "name": "John Smith",
      "email": "john.smith@example.com"
    }
    ```
  - **Error Response** (When required fields are missing):
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Name and email fields are required."
      }
    }
    ```

- **Endpoint: GET `/teachers/{id}`**
  - **Response** (On Successful Retrieval):
    ```json
    {
      "id": 1,
      "name": "John Smith",
      "email": "john.smith@example.com"
    }
    ```

## V. Implementation Steps

1. **Project Update**
   - Confirm the existing FastAPI project structure is maintained. Make sure directories for the new Teacher entity are created under `src/models` and `src/api`.

2. **Dependency Installation**
   - All required dependencies (FastAPI, SQLAlchemy, Alembic) are already present. No new installations are necessary.

3. **Model Creation**
   - Create the Teacher model in `src/models/teacher.py`, as specified above.

4. **Database Migration**
   - Use Alembic for managing database schema changes:
     1. Generate a migration using Alembic:
        ```bash
        alembic revision --autogenerate -m "Create Teacher table"
        ```
     2. Edit the generated migration script to create the `teachers` table:
        ```python
        def upgrade():
            op.create_table(
                'teachers',
                sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                sa.Column('name', sa.String(), nullable=False),
                sa.Column('email', sa.String(), nullable=False, unique=True)
            )
        
        def downgrade():
            op.drop_table('teachers')
        ```
     3. Apply the migration:
        ```bash
        alembic upgrade head
        ```

5. **API Endpoints Implementation**
   - Modify existing `src/api/api.py` to include new endpoints for creating and retrieving teachers:
     ```python
     @app.post("/teachers", response_model=Teacher)
     async def create_teacher(teacher: TeacherCreate):
         db_teacher = Teacher(name=teacher.name, email=teacher.email)
         db.add(db_teacher)
         db.commit()
         db.refresh(db_teacher)
         return db_teacher

     @app.get("/teachers/{id}", response_model=Teacher)
     async def read_teacher(id: int):
         teacher = db.query(Teacher).filter(Teacher.id == id).first()
         if teacher is None:
             raise HTTPException(status_code=404, detail="Teacher not found")
         return teacher
     ```

6. **Error Handling Module**
   - Extend existing centralized error handling in `src/errors/errors.py` to handle validation errors for teacher creation.

7. **Application Entry Point**
   - Ensure `src/app.py` is updated to include the new routes for handling teacher creation and retrieval.

8. **Testing**
   - Create a new test file `tests/test_teacher.py` and ensure it tests:
     - Successful creation of a teacher.
     - Response for missing name/email during teacher creation.
     - Retrieval of teacher details based on ID.
   - Existing tests must be updated to maintain all relevant test coverage.

9. **Documentation**
   - Update FastAPI’s auto-generated documentation to reflect new endpoints.
   - Modify the main `README.md` to include guidance on the new teacher-related endpoints.

## VI. Scalability, Security, and Maintainability Considerations
- **Scalability**: The Teacher entity design allows for future relationships with courses and students without major refactoring.
- **Security**: Input validation must check for existing teachers based on email to prevent duplication.
- **Maintainability**: Code will follow existing style guidelines for readability and future enhancements.

## VII. Trade-offs and Decisions
- **SQLite**: Remains a suitable choice for simplicity; an upgrade path to Postgres or MySQL can be planned for future scaling needs.
- **Separate Module for Teachers**: This design choice ensures that each model remains independent and fosters maintainability.

## VIII. Conclusion
This implementation plan provides a structured approach for integrating the Teacher entity into the Student Management Web Application while preserving the integrity of existing data and functionality. Following these steps will enhance the application's capabilities, preparing it for further growth in managing educational entities.

### Existing Code References
- **File: src/api/api.py**
```python
# Integrating new routes
from src.models import Teacher # Add this import

@app.post("/teachers", response_model=Teacher)
def create_teacher(teacher: TeacherCreate):
    # Logic to create a teacher
```

- **File: tests/test_teacher.py**
```python
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.app import app
from src.models import Base, Teacher  # Importing Teacher model for testing

@pytest.fixture(scope="module")
def test_db():
    # Setup for in-memory SQLite database and model fixtures...
```

This detailed plan outlines how to effectively add the Teacher entity to the existing application structure while preserving all essential functions and ensuring a clean integration.