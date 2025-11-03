# Implementation Plan: Create Teacher Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:  
# Implementation Plan: Add Email Field to Student Entity

---

## I. Architecture Overview

The application will maintain its microservices architecture principles and continue using the same core components:

1. **Web Server**: FastAPI will be utilized to manage HTTP requests and serve API endpoints for handling Teacher entities.
2. **Database**: SQLite will be used to efficiently persist teacher records, allowing for easy retrieval and management of data without impacting existing tables.

### Tech Stack
- **Web Framework**: FastAPI (Python 3.11+)
- **Database**: SQLite
- **Data Serialization**: Pydantic (for request and response validation)
- **Testing Framework**: pytest
- **ORM**: SQLAlchemy

## II. Module Boundaries

1. **API Module**:
   - Introduce new API routes for managing teacher records (`create`, `retrieve`, `update`).

2. **Database Module**:
   - Implement a new `Teacher` data model to represent the teacher entity and handle its schema management.

3. **Error Handling Module**:
   - Ensure thorough validation for teacher data inputs, returning appropriate error messages for invalid requests.

4. **Testing Module**:
   - Implement tests reflecting the scenarios associated with creating, retrieving, and updating teacher information.

## III. Data Models

### Teacher Model

```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Teacher(Base):
    __tablename__ = "Teacher"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
```

### API Request and Response Models
```python
from pydantic import BaseModel, EmailStr

class TeacherCreate(BaseModel):
    name: str  # Required field for teacher's name
    email: EmailStr  # Required field for teacher's email

class TeacherResponse(BaseModel):
    id: int
    name: str
    email: str
```

## IV. API Endpoints

### 1. Create a Teacher
- **Endpoint**: `/teachers`  
- **Method**: POST 
- **Request Body**: 
```json
{
    "name": "John Doe",
    "email": "john.doe@example.com"
}
```
- **Response (201 Created)**:
```json
{
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com"
}
```

### 2. Retrieve Teacher Information
- **Endpoint**: `/teachers/{teacher_id}`
- **Method**: GET
- **Response (200 OK)**:
```json
{
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com"
}
```

### 3. Update Teacher Information
- **Endpoint**: `/teachers/{teacher_id}` 
- **Method**: PUT 
- **Request Body**: 
```json
{
    "name": "John Smith",
    "email": "john.smith@example.com"
}
```
- **Response (200 OK)**:
```json
{
    "id": 1,
    "name": "John Smith",
    "email": "john.smith@example.com"
}
```

## V. Implementation Approach

1. **Set Up Environment**:
   - Ensure that the existing project environment and dependencies are compatible with the new Teacher module.

2. **Implement API Logic**:
   - Create new routes in a file `teacher_api.py` to handle `POST`, `GET`, and `PUT` requests for teacher management.

3. **Set Up Database**:
   - Modify `db_setup.py` to include the `Teacher` model in the SQLite schema and ensure correct table creation.

4. **Database Migration Strategy**:
   - Create migration scripts using a tool like Alembic (if not already in use) to introduce the `Teacher` table into the database without affecting existing records.

## VI. Error Handling

- Implement input validation to check the format of the teacher email before allowing creation or updates.
- Return clear messages for invalid requests to guide the admin on how to correct their submission.

## VII. Success Criteria Verification

1. Verify that creating a new teacher works with valid `name` and `email`, returning the correct confirmation.
2. Ensure that retrieving teacher details by their ID returns accurate information.
3. Update operations must reflect new data appropriately when the information is fetched again.

## VIII. Testing Strategy

1. **Unit Tests**: Test the functionality of creating, retrieving, and updating teachers.
2. **Integration Tests**: Validate the API endpoints for creating a teacher, retrieving their information, and updating their details:
   - Implement tests for POST, GET, and PUT endpoints.

## IX. Documentation

- Update the `README.md` to include the new API endpoints, their formats, and examples for how to interact with the Teacher API.
- Document the process for running database migrations to ensure deployment readiness.

## X. Version Control Practices

- Commit changes with clear messages reflecting the addition of the Teacher feature.
- Structure commits logically to ensure documentation remains aligned with the code.

## XI. Deployment Considerations 

- Ensure that migration for creating the `Teacher` table is fully tested in a staging environment before production deployment.
- Confirm that the application starts without issues, and that new and existing functionalities work seamlessly without disruptions.

### Existing Code Modifications:

**File**: `src/db_setup.py`
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student, Course, Teacher  # Ensure to import the new Teacher model
...

def setup_database():
    ...
    Base.metadata.create_all(engine)  # This will create all necessary tables including Teacher
```

**File**: `src/teacher_api.py` (new file for managing teachers)
```python
from fastapi import APIRouter, HTTPException
from models import Teacher, TeacherCreate, TeacherResponse
from db_setup import SessionLocal
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/teachers", response_model=TeacherResponse, status_code=201)
def create_teacher(teacher: TeacherCreate):
    session = SessionLocal()
    new_teacher = Teacher(name=teacher.name, email=teacher.email)
    session.add(new_teacher)
    session.commit()
    session.refresh(new_teacher)
    session.close()
    return TeacherResponse(id=new_teacher.id, name=new_teacher.name, email=new_teacher.email)

@router.get("/teachers/{teacher_id}", response_model=TeacherResponse)
def get_teacher(teacher_id: int):
    session = SessionLocal()
    teacher = session.query(Teacher).filter(Teacher.id == teacher_id).first()
    if not teacher:
        session.close()
        raise HTTPException(status_code=404, detail="Teacher not found")
    response = TeacherResponse(id=teacher.id, name=teacher.name, email=teacher.email)
    session.close()
    return response

@router.put("/teachers/{teacher_id}", response_model=TeacherResponse)
def update_teacher(teacher_id: int, teacher: TeacherCreate):
    session = SessionLocal()
    existing_teacher = session.query(Teacher).filter(Teacher.id == teacher_id).first()
    if not existing_teacher:
        session.close()
        raise HTTPException(status_code=404, detail="Teacher not found")
    
    existing_teacher.name = teacher.name
    existing_teacher.email = teacher.email
    session.commit()
    session.refresh(existing_teacher)
    session.close()
    return TeacherResponse(id=existing_teacher.id, name=existing_teacher.name, email=existing_teacher.email)
```

### Testing Files

**File**: `tests/test_teacher_api.py`
```python
import pytest
from fastapi.testclient import TestClient
from src.main import app  # Adjust based on your project structure
from src.models import Teacher  # Import the Teacher model

client = TestClient(app)

# Test creation of a teacher
def test_create_teacher():
    response = client.post("/teachers", json={"name": "Jane Doe", "email": "jane.doe@example.com"})
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Jane Doe"
    assert data["email"] == "jane.doe@example.com"

# Test retrieval of a teacher
def test_get_teacher():
    response = client.get("/teachers/1")  # Adjust ID as necessary
    assert response.status_code == 200
    data = response.json()
    assert "name" in data
    assert "email" in data

# Test updating a teacher
def test_update_teacher():
    response = client.put("/teachers/1", json={"name": "Jane Smith", "email": "jane.smith@example.com"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Jane Smith"
```

By following this implementation plan, we will successfully integrate the new Teacher entity into the existing application, enhancing its educational management capabilities while preserving existing functionalities and ensuring high code quality.