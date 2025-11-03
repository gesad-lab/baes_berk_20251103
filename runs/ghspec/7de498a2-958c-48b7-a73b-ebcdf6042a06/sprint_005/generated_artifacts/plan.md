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

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Student Entity Management

## Version
1.0.0

## Purpose
To create a new Teacher entity that will enable the tracking of teachers, their names, and email addresses within the system, thereby allowing for better educational management and future integrations with other entities.

## Architecture Overview
The application retains its microservices architecture, employing RESTful APIs, developed with Python and FastAPI, and using SQLite as the database. This new Teacher feature will seamlessly integrate into the existing structure, adhering to principles of modularity and separation of concerns while enhancing the educational management capabilities of the system.

## Technology Stack
- **Backend Framework**: FastAPI
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Testing**: pytest

## Module Boundaries and Responsibilities
1. **API Layer**:
   - Implement new endpoints for Teacher functionalities, focusing on creation, retrieval, updating, and deletion of Teacher entities.

2. **Service Layer**:
   - Encapsulate business logic for managing Teachers, including validations and interactions with the persistence layer.

3. **Persistence Layer**:
   - Create a new Teacher entity and adapt the existing data model to accommodate the changes while maintaining relationships with Students and Courses.

## Data Models and API Contracts

### Data Model: Teacher
```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
```

### API Endpoints
1. **Create Teacher**
   - **Endpoint**: `POST /teachers`
   - **Request Body**:
     ```json
     {
       "name": "string",
       "email": "string"
     }
     ```
   - **Response**:
     - 201 Created with JSON representation of the created Teacher object, or 400 Bad Request if validation fails.

2. **Retrieve Teacher Information**
   - **Endpoint**: `GET /teachers/{teacher_id}`
   - **Response**:
     - 200 OK with JSON representation of the Teacher, or 404 Not Found if the Teacher ID does not exist.

3. **Update Teacher Information**
   - **Endpoint**: `PUT /teachers/{teacher_id}`
   - **Request Body**:
     ```json
     {
       "name": "string (optional)",
       "email": "string (optional)"
     }
     ```
   - **Response**:
     - 200 OK with the updated Teacher object, or 404 Not Found if the Teacher ID does not exist.

4. **Delete Teacher**
   - **Endpoint**: `DELETE /teachers/{teacher_id}`
   - **Response**:
     - 204 No Content on successful deletion, or 404 Not Found if the Teacher ID does not exist.

## Implementation Approach

### 1. Project Structure Update
- Update the existing FastAPI project structure to include the Teacher entity:
  ```
  src/
  ├── main.py            # Integrate new Teacher routes
  ├── models.py          # Add the new Teacher class definition
  ├── services.py        # Add logic for Teacher-related business functions
  ├── api.py             # Define Teacher API endpoints
  ├── database.py        # Include Teacher migrations
  tests/
  ├── test_api.py        # Test Teacher API endpoints
  ├── test_services.py    # Test Teacher business logic
  ```

### 2. Database Migration Strategy
- Utilize **Alembic** to create a migration for adding the new Teacher table:
```python
from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table('teachers',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), unique=True, nullable=False)
    )

def downgrade():
    op.drop_table('teachers')
```

### 3. API Implementation
- In `api.py`, implement the following new routes:
  ```python
  @app.post("/teachers")
  async def create_teacher(teacher: TeacherCreate):
      # Logic to create Teacher via service layer
  ```

### 4. Business Logic Implementation
- Write service functions in `services.py` to handle the business logic for Teacher management:
```python
from src.models import Teacher
from sqlalchemy.orm import Session

def create_teacher(db: Session, name: str, email: str):
    new_teacher = Teacher(name=name, email=email)
    db.add(new_teacher)
    db.commit()
    db.refresh(new_teacher)
    return new_teacher

def get_teacher(db: Session, teacher_id: int):
    return db.query(Teacher).filter(Teacher.id == teacher_id).first()

def update_teacher(db: Session, teacher_id: int, name: str = None, email: str = None):
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if teacher:
        if name:
            teacher.name = name
        if email:
            teacher.email = email
        db.commit()
        return teacher
    return None

def delete_teacher(db: Session, teacher_id: int):
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if teacher:
        db.delete(teacher)
        db.commit()
        return True
    return False
```

### 5. Input Validation
- Create Pydantic models to validate input for creating and updating Teachers:
```python
from pydantic import BaseModel, EmailStr

class TeacherCreate(BaseModel):
    name: str
    email: EmailStr

class TeacherUpdate(BaseModel):
    name: str = None
    email: EmailStr = None
```

### 6. Testing
- Implement tests in `test_api.py` and `test_services.py` for covering all functionalities:
```python
def test_create_teacher():
    response = client.post("/teachers", json={"name": "John Doe", "email": "john@example.com"})
    assert response.status_code == 201
    assert response.json()["name"] == "John Doe"

def test_get_teacher():
    response = client.get("/teachers/1")
    assert response.status_code == 200
    assert "name" in response.json()
```

### 7. Docker Setup
- Ensure Docker configurations allow for database migrations and service availability following updates.

## Scalability, Security, and Maintainability Considerations
- Use environment variables for all sensitive data and configuration.
- Implement robust validation and error handling for inputs to safeguard against incorrect data entry.
- Organize the service methods to allow for scalability and future feature introductions.

## Trade-Offs and Decisions
- **Uniqueness Constraint on Email**: This guarantees that no two teachers can register with the same email address, potentially preventing data collisions.
- **Error Handling**: Detailed validation mechanisms will be implemented using Pydantic to ensure user-friendly error messages.

### Success Criteria
- Ensure API endpoints return the correct HTTP statuses and payloads as specified in the functional requirements.
- Achieve at least 70% coverage for the new Teacher features through unit tests.

## Deployment Considerations
- Validate that the Docker image's startup routines include the necessary migrations.
- Ensure continuity of existing functionalities while incorporating the new Teacher entity.

## Conclusion
This implementation plan details the introduction of a Teacher entity into the system's architecture, ensuring adherence to best practices in software design, maintainability, and security while enabling enhanced educational management capabilities. The plan accounts for integration with existing functionalities, database migration strategies, endpoint specifications, and testing strategies to guarantee robust deployment and operation.

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

def test_create_teacher_success(setup_database):
    """Test that creating a teacher successfully returns the created object."""
    response = client.post("/teachers", json={"name": "Alice Smith", "email": "alice@school.com"})
    assert response.status_code == 201
    assert response.json()["name"] == "Alice Smith"
    assert response.json()["email"] == "alice@school.com"

def test_get_teacher_success(setup_database):
    """Test that retrieving a teacher by ID returns the correct details."""
    response = client.get("/teachers/1")  # Assuming teacher with ID 1 exists
    assert response.status_code == 200
    assert "name" in response.json()
    assert "email" in response.json()
```

### File: tests/test_services.py
```python
import pytest
from sqlalchemy.orm import Session
from src.services import create_teacher, get_teacher, update_teacher, delete_teacher
from src.models import Teacher

@pytest.fixture(scope="module")
def db_session():
    """Set up a test database session."""
    # Setup code for the test database here
    yield db_session  # Replace with the session

def test_create_teacher(db_session):
    """Test creating a teacher."""
    result = create_teacher(db_session, "Bob Brown", "bob@school.com")
    assert result.name == "Bob Brown"
    assert result.email == "bob@school.com"

def test_get_teacher(db_session):
    """Test retrieving an existing teacher."""
    teacher = get_teacher(db_session, 1)  # Assuming teacher with ID 1 exists
    assert teacher is not None
    assert teacher.name == "Bob Brown"

def test_update_teacher(db_session):
    """Test updating a teacher's information."""
    updated_teacher = update_teacher(db_session, 1, email="bob.brown@school.com")
    assert updated_teacher.email == "bob.brown@school.com"

def test_delete_teacher(db_session):
    """Test deleting a teacher."""
    assert delete_teacher(db_session, 1) is True
``` 

The structured implementation plan above details how to accommodate the creation of a Teacher entity within the existing software architecture, maintaining backward compatibility and ensuring robust performance across interactions.