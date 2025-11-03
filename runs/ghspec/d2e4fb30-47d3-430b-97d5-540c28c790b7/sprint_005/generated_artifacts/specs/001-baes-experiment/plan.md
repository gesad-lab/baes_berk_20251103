# Implementation Plan: Create Teacher Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Course Entity

## Version
1.0.0

## Purpose
To implement a feature that allows administrators to create a new Teacher entity within the existing educational application. This implementation will enhance teacher management and support future functionalities, including course assignments and performance tracking.

## Technology Stack
- **Backend Framework**: FastAPI (Python)
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Data Validation**: Pydantic
- **API Documentation**: Swagger (automatically provided by FastAPI)
- **Testing Framework**: pytest
- **Deployment**: Docker for containerization
- **Environment Management**: .env files for configuration 

## Architectural Overview
The application will maintain a clean architecture, ensuring proper separation of concerns between different modules:
- **API Layer**: Manages HTTP requests and responses related to teacher management.
- **Service Layer**: Contains business logic for creating and retrieving teachers.
- **Data Access Layer**: Interacts with the database to manage teacher data.
- **Database Layer**: Configuration of the new `Teachers` table and related schema management.

## Module Responsibilities

### 1. API Layer
- Handles incoming HTTP requests for creating teachers and retrieving teacher data.
- Maps requests to appropriate service methods.
- Responsible for input validation and returning appropriate responses, including error messages.

### 2. Service Layer
- Implements business logic for teacher creation and retrieval.
- Validates input data, ensuring uniqueness and correctness before interacting with the data access layer.

### 3. Data Access Layer
- Manages interactions with the database using SQLAlchemy to perform create and query operations related to the Teacher entity.

## Data Models

### Teacher Model
```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Teacher(Base):
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
```

## API Contracts

### Create Teacher
- **Endpoint**: `POST /teachers`
- **Request Body**:
    ```json
    {
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    ```
- **Response** (Success - 201 Created):
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
- **Response** (Error - 400 Bad Request):
    ```json
    {
        "error": {
            "code": "E001",
            "message": "Email already exists."
        }
    }
    ```

### Retrieve All Teachers
- **Endpoint**: `GET /teachers`
- **Response** (Success - 200 OK):
    ```json
    [
        {
            "id": 1,
            "name": "John Doe",
            "email": "john.doe@example.com"
        },
        {
            "id": 2,
            "name": "Jane Smith",
            "email": "jane.smith@example.com"
        }
    ]
    ```

## Implementation Steps

1. **Project Setup**
   - Maintain the existing FastAPI project structure set up in previous implementations.
   - Ensure Docker is configured for PostgreSQL as per the existing setup.

2. **Model Creation**
   - Create the `Teacher` model in `src/models/teacher.py`:
   ```python
   from sqlalchemy import Column, Integer, String
   from sqlalchemy.ext.declarative import declarative_base
   
   Base = declarative_base()

   class Teacher(Base):
       __tablename__ = 'teachers'
       
       id = Column(Integer, primary_key=True, autoincrement=True)
       name = Column(String(255), nullable=False)
       email = Column(String(255), nullable=False, unique=True)
   ```

3. **Database Schema Management**
   - Create an Alembic migration script to add the `Teachers` table:
   ```bash
   alembic revision --autogenerate -m "Create Teachers Table"
   ```
   - The migration script should include:
   ```python
   def upgrade():
       op.create_table(
           'teachers',
           sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
           sa.Column('name', sa.String(length=255), nullable=False),
           sa.Column('email', sa.String(length=255), nullable=False, unique=True)
       )

   def downgrade():
       op.drop_table('teachers')
   ```

4. **API Development**
   - Create a new API router for teachers in `src/routes/teachers.py`:
   ```python
   from fastapi import APIRouter, HTTPException, Depends
   from sqlalchemy.orm import Session
   from ..models.teacher import Teacher
   from ..database import get_db
   from pydantic import BaseModel

   router = APIRouter()

   class TeacherCreate(BaseModel):
       name: str
       email: str

   @router.post("/teachers", status_code=201)
   async def create_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
       existing_teacher = db.query(Teacher).filter(Teacher.email == teacher.email).first()
       if existing_teacher:
           raise HTTPException(status_code=400, detail="Email already exists.")
       
       new_teacher = Teacher(name=teacher.name, email=teacher.email)
       db.add(new_teacher)
       db.commit()
       db.refresh(new_teacher)
       return {"message": "Teacher created successfully.", "teacher": {"id": new_teacher.id, "name": new_teacher.name, "email": new_teacher.email}}

   @router.get("/teachers")
   async def get_teachers(db: Session = Depends(get_db)):
       teachers = db.query(Teacher).all()
       return [{'id': t.id, 'name': t.name, 'email': t.email} for t in teachers]
   ```

5. **Update Main Application**
   - Integrate the updated teacher router into the main FastAPI application in `src/main.py`:
   ```python
   from fastapi import FastAPI
   from .routes.teachers import router as teacher_router

   app = FastAPI()

   app.include_router(teacher_router)
   ```

6. **Testing**
   - Create a test file `tests/test_teachers.py` for the teacher creation and retrieval functionalities:
   ```python
   from fastapi.testclient import TestClient
   from main import app

   client = TestClient(app)

   def test_create_teacher():
       response = client.post("/teachers", json={"name": "John Doe", "email": "john.doe@example.com"})
       assert response.status_code == 201
       assert response.json() == {
           "message": "Teacher created successfully.",
           "teacher": {
               "id": 1,
               "name": "John Doe",
               "email": "john.doe@example.com"
           }
       }

   def test_create_teacher_duplicate_email():
       client.post("/teachers", json={"name": "Jane Smith", "email": "jane.smith@example.com"})
       response = client.post("/teachers", json={"name": "Duplicate", "email": "jane.smith@example.com"})
       assert response.status_code == 400
       assert response.json() == {
           "error": {
               "code": "E001",
               "message": "Email already exists."
           }
       }

   def test_retrieve_teachers():
       response = client.get("/teachers")
       assert response.status_code == 200
       assert isinstance(response.json(), list)
   ```

7. **Documentation**
   - Ensure that the FastAPI automatically generates documentation for the new endpoints in Swagger and validate that the `/teachers` endpoints are described accurately.

8. **Deployment**
   - Update Docker configurations if necessary for the migrations.
   - Validate the success of the migration in local and production environments.

## Success Criteria
- **Teacher Creation**: Successfully creating a teacher returns a status code of 201 with confirmation details.
- **Duplicate Email Handling**: Attempting to create a teacher with an existing email returns a status code of 400 with an appropriate error message.
- **Retrieve Teachers**: The endpoint returns a list of teachers with a status code of 200 containing teacher details.
- **Database Migration**: The migration for the `Teachers` table executes without affecting existing student or course records.

## Trade-offs and Considerations
- **Migration Overheads**: Introducing a migration step is necessary for maintaining database integrity.
- **Error Messaging**: Basic error messages are implemented; more detailed messages can be incorporated in future iterations.
- **Testing Depth**: Adequate tests cover the new functionality and ensure existing features remain reliable after integration.

## Conclusion
This implementation plan outlines the structured steps needed to create a Teacher entity in the educational application, ensuring adherence to established architecture principles and maintaining code maintainability for future enhancements.

Existing Code Files:
File: `tests/test_teachers.py`
```python
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app, Base, get_db
from sqlalchemy.exc import IntegrityError
from src.models.teacher import Teacher

# Setup for testing
DATABASE_URL = "postgresql://user:password@localhost/test_db"

# Create a new database engine for testing
engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Use a test client to simulate requests
client = TestClient(app)

# Ensure your test setup populates the necessary tables for testing
```
