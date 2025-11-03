# Implementation Plan: Create Teacher Entity

---

## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Course Relationship to Student Entity

---

## Version
**Version**: 1.0.0  

## Purpose
This implementation plan details the addition of a `Teacher` entity to the existing Student Management Web Application. This feature aims to enhance the system’s capability to manage teacher information effectively, thereby improving course management and resource allocation in future updates.

## Architecture Overview
The application architecture follows a microservices pattern using FastAPI and SQLAlchemy. The implementation of the `Teacher` entity is designed to integrate seamlessly with the existing API and database schema while ensuring that the integrity of current functionalities is preserved.

## Technology Stack
- **Programming Language**: Python 3.11+
- **Web Framework**: FastAPI
- **ORM**: SQLAlchemy
- **Database**: SQLite
- **API Testing Tool**: Postman / cURL

## Module Boundaries and Responsibilities
1. **API Layer**:
   - New Endpoints:
     - `POST /teachers`: Create a new Teacher.
     - `GET /teachers/{teacher_id}`: Retrieve Teacher information.

2. **Business Logic Layer**:
   - Implement validation checks for mandatory fields (name and email).
   - Ensure the email field is unique and handle the logic for teacher creation and retrieval.

3. **Data Access Layer**:
   - Introduce a new model for `Teacher` that interacts with the database.

## Data Models
### Teacher Model
Definition of the new `Teacher` model:
```python
from sqlalchemy import Column, Integer, String, UniqueConstraint
from sqlalchemy.orm import relationship
from models import Base

class Teacher(Base):
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, index=True)  # Primary key
    name = Column(String, nullable=False)  # Teacher's name
    email = Column(String, nullable=False, unique=True)  # Teacher's email (unique)
    
    # Optional relationships can be added here in future enhancements
```

## API Contracts
### 1. Create a Teacher
- **Endpoint**: `POST /teachers`
- **Request Body**:
  ```json
  {
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
  ```
- **Response**:
  - **Success (201)**:
    ```json
    {
      "message": "Teacher created successfully.",
      "teacher": {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com"
      }
    }
    ```
  - **Error (400)** (Missing required fields):
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Missing required field(s): name, email"
      }
    }
    ```
  - **Error (409)** (Duplicate email):
    ```json
    {
      "error": {
        "code": "E002",
        "message": "Email already exists."
      }
    }
    ```

### 2. Retrieve Teacher Information
- **Endpoint**: `GET /teachers/{teacher_id}`
- **Response**:
  - **Success (200)**:
    ```json
    {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```
  - **Error (404)**:
    ```json
    {
      "error": {
        "code": "E003",
        "message": "Teacher not found."
      }
    }
    ```

## Implementation Approach
1. **Environment Setup**:
   - Ensure Python 3.11+ is installed.
   - Create a virtual environment if not done already.
   - Install necessary dependencies:
     ```bash
     pip install fastapi[all] sqlalchemy
     ```

2. **Database Migration**:
   - Create a migration script to introduce the `teachers` table while preserving existing data:
   ```python
   from sqlalchemy import create_engine, Column, Integer, String, UniqueConstraint
   from sqlalchemy.orm import sessionmaker
   from models import Base

   # Define the new Teacher model here or in a separate file as part of future enhancements
   class Teacher(Base):
       __tablename__ = 'teachers'
       
       id = Column(Integer, primary_key=True)
       name = Column(String, nullable=False)
       email = Column(String, nullable=False, unique=True)

   engine = create_engine('sqlite:///./database.db')
   Base.metadata.create_all(engine)  # This will create the new teachers table.
   ```

3. **Endpoint Implementation**:
   - Modify the `api/teachers.py` file to implement the new `POST` and `GET` endpoints for managing Teachers:
   ```python
   from fastapi import APIRouter, Depends, HTTPException
   from sqlalchemy.orm import Session
   from models import Teacher  # Import the new Teacher model
   from database import get_db  # Dependency for the database session
   from pydantic import BaseModel

   class TeacherCreateModel(BaseModel):
       name: str
       email: str

   router = APIRouter()

   @router.post("/teachers", status_code=201)
   async def create_teacher(teacher: TeacherCreateModel, db: Session = Depends(get_db)):
       # Check for existing teacher with the same email
       if db.query(Teacher).filter(Teacher.email == teacher.email).first():
           raise HTTPException(status_code=409, detail="Email already exists.")
       
       # Create new teacher record
       new_teacher = Teacher(name=teacher.name, email=teacher.email)
       db.add(new_teacher)
       db.commit()
       db.refresh(new_teacher)

       return {
           "message": "Teacher created successfully.",
           "teacher": {
               "id": new_teacher.id,
               "name": new_teacher.name,
               "email": new_teacher.email
           }
       }

   @router.get("/teachers/{teacher_id}", response_model=TeacherCreateModel)
   async def get_teacher(teacher_id: int, db: Session = Depends(get_db)):
       teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
       if not teacher:
           raise HTTPException(status_code=404, detail="Teacher not found.")
       return {"id": teacher.id, "name": teacher.name, "email": teacher.email}
   ```

4. **Testing**:
   - Create tests in `tests/test_teachers.py`:
   - Verify API functionality for creating and retrieving teachers.
   - Check various scenarios, including successful teacher creation and handling of errors for duplicate emails and missing fields.
```python
def test_create_teacher(client):
    response = client.post("/teachers", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201
    assert response.json()["teacher"]["name"] == "John Doe"
```

## Scalability and Security Considerations
- **Scalability**:
  - The application remains scalable with a stateless design, facilitating future enhancements without disrupting existing functionality.
- **Security**:
  - All field inputs are validated for correctness and sanitized to prevent SQL injection attacks and data integrity issues.

## Implementation Timeline
- **Week 1**:
  - Environment setup and model creation for the `Teacher` entity.
- **Week 2**:
  - Implement API endpoints for creating and retrieving Teacher data.
- **Week 3**:
  - Write unit tests covering all new functionality, ensuring 90%+ coverage for critical paths.
- **Week 4**:
  - Conduct integration testing, update the documentation, and prepare for deployment.

## Documentation and References
- **Code Documentation**:
  - Ensure relevant docstrings are included in new and modified classes and functions.
- **README.md**:
  - Update the main README to detail the new endpoints and usage guidelines.

## Trade-offs and Decisions
- **New Teacher Model**:
  - The Teacher model was created using the existing structure of other entities while ensuring it is capable of scaling with future needs.
- **Backward Compatibility**:
  - The migration strategy was designed to ensure existing student and course records maintain integrity while new functionalities are added.

This implementation plan outlines the key steps necessary to effectively integrate the Teacher entity into the current Student Management Web Application, thus significantly enhancing its capabilities for managing educational resources.