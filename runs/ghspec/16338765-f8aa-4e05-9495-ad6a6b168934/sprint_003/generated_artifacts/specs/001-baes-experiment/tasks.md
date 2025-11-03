# Tasks: Create Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `src/db_setup.py`
- `tests/test_student_api.py`

---

## Task Breakdown

- [ ] **Task 1: Define Course Model**
  - **File**: `src/models/course.py`
  - **Description**: Create a new file to define the `Course` model class using SQLAlchemy. Include attributes `id`, `name`, and `level`.
  
```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    __tablename__ = "courses"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # Required field
    level = Column(String, nullable=False)  # Required field
```

- [ ] **Task 2: Update Database Setup**
  - **File**: `src/db_setup.py`
  - **Description**: Modify the existing database setup file to import the `Course` model and create the `courses` table in the database.
  
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student, Course  # Ensure to import the new Course model
...

def setup_database():
    ...
    Base.metadata.create_all(engine)  # This will now create both tables Students and Courses
```

- [ ] **Task 3: Implement Course API Logic**
  - **File**: `src/course_api.py`
  - **Description**: Create a new FastAPI router for course management. Implement the endpoints for creating, retrieving, and updating courses.
  
```python
from fastapi import APIRouter, HTTPException
from models import CourseCreate, CourseResponse, Course
from db_setup import SessionLocal
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/courses", response_model=CourseResponse, status_code=201)
def create_course(course: CourseCreate):
    session = SessionLocal()
    new_course = Course(name=course.name, level=course.level)
    session.add(new_course)
    session.commit()
    session.refresh(new_course)
    session.close()
    return new_course

@router.get("/courses/{id}", response_model=CourseResponse)
def get_course(id: int):
    session = SessionLocal()
    course = session.query(Course).filter(Course.id == id).first()
    session.close()
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@router.put("/courses/{id}", response_model=CourseResponse)
def update_course(id: int, course_data: CourseCreate):
    session = SessionLocal()
    course = session.query(Course).filter(Course.id == id).first()
    if course is None:
        session.close()
        raise HTTPException(status_code=404, detail="Course not found")
    
    course.name = course_data.name
    course.level = course_data.level
    session.commit()
    session.refresh(course)
    session.close()
    return course
```

- [ ] **Task 4: Create API Request and Response Models**
  - **File**: `src/models/course.py` (extend the existing Course model file)
  - **Description**: Extend the `course.py` file to include Pydantic models for request and response data validation.
  
```python
from pydantic import BaseModel

class CourseCreate(BaseModel):
    name: str  # Required
    level: str  # Required

class CourseResponse(BaseModel):
    id: int
    name: str
    level: str
```

- [ ] **Task 5: Implement Database Migration Script**
  - **File**: `migrations/add_course_table.py` (new file)
  - **Description**: Create a migration script to add the `courses` table to the SQLite database without impacting existing student data.
  
```python
# Your migration logic here to create the `courses` table
```

- [ ] **Task 6: Create Unit Tests for Course Functionality**
  - **File**: `tests/test_course_api.py` (new file)
  - **Description**: Implement unit tests for the new course functionality: creation, retrieval, and updates.
  - **Note**: These tests should mirror the success criteria defined in the specification.
  
```python
# Your tests for creating, retrieving, and updating courses
```

- [ ] **Task 7: Update README.md Documentation**
  - **File**: `README.md`
  - **Description**: Update the project documentation to include details about the new course API endpoints, including example requests and responses.
  
- [ ] **Task 8: Verify Environment and Deployment Considerations**
  - **File**: N/A
  - **Description**: Ensure that environment variables are set correctly and validate the application starts successfully with the new feature. Confirm migration executes without downtime.

--- 

Following this structured task breakdown will facilitate the effective implementation of the Course entity feature while ensuring adherence to existing code styles, integration with current systems, and thorough testing.