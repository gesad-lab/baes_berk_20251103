# Tasks: Create Course Entity

---

INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `tests/test_routes.py` (2863 bytes)
- `tests/test_student.py` (2501 bytes)

---

## Task Breakdown

### 1. **Create Course Model**

- **File:** `src/models/course.py`
  - [ ] Define the Course data model using SQLAlchemy.
  
```python
from sqlalchemy import Column, Integer, String
from db.database import Base

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
```
  
### 2. **Create Course Schemas**

- **File:** `src/schemas/course_schemas.py`
  - [ ] Define Pydantic models for request and response validation of Course.
  
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

### 3. **Create Course Service**

- **File:** `src/services/course_service.py`
  - [ ] Implement business logic for creating, retrieving, updating, and deleting courses.
  
```python
class CourseService:
    # Define methods for create, retrieve, update, delete for course
    ...
```

### 4. **Create Course Routes**

- **File:** `src/routes/course_routes.py`
  - [ ] Implement API endpoints for CRUD operations on courses.
  
```python
from fastapi import APIRouter
from src.schemas.course_schemas import CourseCreate, CourseResponse
from src.services.course_service import CourseService

router = APIRouter()

@router.post("/courses/", response_model=CourseResponse)
async def create_course(course: CourseCreate):
    # Call course service to create a course
    ...

@router.get("/courses/{id}", response_model=CourseResponse)
async def retrieve_course(id: int):
    # Call course service to retrieve course by id
    ...

@router.put("/courses/{id}", response_model=CourseResponse)
async def update_course(id: int, course: CourseCreate):
    # Call course service to update course
    ...

@router.delete("/courses/{id}")
async def delete_course(id: int):
    # Call course service to delete course
    ...
```

### 5. **Write Tests for Course Functionality**

- **File:** `tests/test_course.py`
  - [ ] Create new test cases for CRUD operations for Course using pytest.
  
```python
import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_create_course():
    # Test creating course POST request
    ...

def test_retrieve_course():
    # Test retrieving course GET request
    ...

def test_update_course():
    # Test updating course PUT request
    ...

def test_delete_course():
    # Test deleting course DELETE request
    ...
```

### 6. **Database Migration for Course Table**

- **File:** `src/db/migrations/create_course_table.py` (New Migration Script)
  - [ ] Create migration to add `courses` table to existing database schema.
  
```python
from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('level', sa.String, nullable=False),
    )

def downgrade():
    op.drop_table('courses')
```

### 7. **Integrate Course Routes into Main Application**

- **File:** `src/main.py`
  - [ ] Update the main application entry point to include the course routes.
  
```python
from fastapi import FastAPI
from src.routes.course_routes import router as course_router

app = FastAPI()

app.include_router(course_router)
```

### 8. **Update Documentation**

- **File:** `README.md`
  - [ ] Document new Course entity, including API endpoints and examples for usage.

---
This structured breakdown allows for focused implementation on the new Course entity while ensuring each task can be tested independently and all code adheres to existing patterns and specifications.