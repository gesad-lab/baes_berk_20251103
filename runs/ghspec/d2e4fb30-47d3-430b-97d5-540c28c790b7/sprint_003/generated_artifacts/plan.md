# Implementation Plan: Create Course Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
```markdown
# Implementation Plan: Add Email Field to Student Entity

## Version
1.0.0

## Purpose
To implement a web application that allows users to manage Student records, including creating and retrieving student information.

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
The application will follow a clean architecture approach ensuring separation of concerns:
- **API Layer**: Manages HTTP requests and responses.
- **Service Layer**: Contains business logic for student management.
- **Data Access Layer**: Manages interactions with the database.
- **Database Layer**: Configuration of database models and relationships.

## Module Responsibilities

### 1. API Layer
- Handles incoming HTTP requests for student management.
- Maps requests to appropriate service methods.
- Responsible for input validation and returning appropriate responses.

### 2. Service Layer
- Implements business logic for creating and retrieving student records.
- Validates data before passing it to the data access layer.

### 3. Data Access Layer
- Interacts with the database using SQLAlchemy to perform CRUD operations.
- Ensures the proper schema is created on application startup.

## Data Models

### Student Model
```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
```

## API Contracts

### Create Student
- **Endpoint**: `POST /students`
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
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    ```
- **Response** (Error - 400 Bad Request):
    ```json
    {
        "error": {
            "code": "E001",
            "message": "Email field is required."
        }
    }
    ```

### Retrieve All Students
- **Endpoint**: `GET /students`
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
   - Continue using the existing FastAPI project setup.
   - Ensure Docker is configured for PostgreSQL as per previous implementation.

2. **Model Creation**
   - Create a new `Course` model in the `src/models/course.py` file.
   ```python
   from sqlalchemy import Column, Integer, String
   from sqlalchemy.ext.declarative import declarative_base

   Base = declarative_base()

   class Course(Base):
       __tablename__ = 'courses'
       
       id = Column(Integer, primary_key=True, autoincrement=True)
       name = Column(String(255), nullable=False)
       level = Column(String(255), nullable=False)
   ```

3. **Database Schema Management**
   - Implement a migration script using Alembic to create the `courses` table without affecting existing `students` data.
   ```bash
   alembic revision --autogenerate -m "Add Course Table"
   ```
   - Ensure the migration script includes:
     ```python
     def upgrade():
         op.create_table(
             'courses',
             sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
             sa.Column('name', sa.String(length=255), nullable=False),
             sa.Column('level', sa.String(length=255), nullable=False)
         )

     def downgrade():
         op.drop_table('courses')
     ```

4. **API Development**
   - Create a new API router for courses in `src/routes/course.py`.
   - Define the `/courses` endpoint for both creation and retrieval.
   ```python
   from fastapi import APIRouter, HTTPException
   from pydantic import BaseModel
   from sqlalchemy.orm import Session
   from ..models.course import Course
   from ..database import get_db

   router = APIRouter()

   class CourseCreate(BaseModel):
       name: str
       level: str

   @router.post("/courses", response_model=CourseCreate)
   async def create_course(course: CourseCreate, db: Session = Depends(get_db)):
       if not course.name or not course.level:
           raise HTTPException(status_code=400, detail="Name and level are required")
       new_course = Course(name=course.name, level=course.level)
       db.add(new_course)
       db.commit()
       db.refresh(new_course)
       return new_course

   @router.get("/courses", response_model=List[CourseCreate])
   async def get_courses(db: Session = Depends(get_db)):
       return db.query(Course).all()
   ```

5. **Update Main Application**
   - Integrate the course router into the main FastAPI application in `src/main.py`:
   ```python
   from fastapi import FastAPI
   from .routes.course import router as course_router

   app = FastAPI()

   app.include_router(course_router)
   ```

6. **Testing**
   - Create a test file `tests/test_courses.py` for course API tests:
   ```python
   from fastapi.testclient import TestClient
   from your_project.main import app  # Adjust import as necessary

   client = TestClient(app)

   def test_create_course():
       response = client.post("/courses", json={"name": "Math 101", "level": "Beginner"})
       assert response.status_code == 201
       assert response.json() == {"id": 1, "name": "Math 101", "level": "Beginner"}

   def test_create_course_missing_fields():
       response = client.post("/courses", json={"name": "Math 101"})
       assert response.status_code == 400
       assert response.json() == {"error": {"code": "E001", "message": "Name and level are required"}} 

   def test_get_courses():
       response = client.get("/courses")
       assert response.status_code == 200
       assert isinstance(response.json(), list)
   ```

7. **Documentation**
   - Ensure that API documentation provided by FastAPI reflects the new `/courses` endpoint and its expected input/output formats.

8. **Deployment**
   - Update Docker configurations if necessary to include new migrations.
   - Validate that the migration works on both local and production environments.

## Success Criteria
- **Create Course**: Successfully creating a course returns a status code of 201 and the course details.
- **Validation**: Invalid requests (e.g., missing name or level) return a status code of 400 with an appropriate error message.
- **Retrieve Courses**: The endpoint returns a list of all courses with a status code of 200.
- **Database Migration**: The migration succeeds without affecting existing student data and allows for application startup with no errors.

## Trade-offs and Considerations
- **Migration Dependency**: The use of Alembic for migrations ensures that schema changes are trackable, but it requires an understanding of migration scripts to ensure compatibility.
- **Error Handling**: Initial error messaging is basic but can be enhanced with more informative details in future iterations.
- **Testing Requirements**: Comprehensive tests are necessary for new functionality to ensure system integrity after the integration of the Course entity. 

## Conclusion
This implementation plan delineates the steps required to add the Course entity to the existing educational application, ensuring that modular design principles, testing strategies, and documentation standards are maintained to enhance scalability and maintainability of the codebase.
```