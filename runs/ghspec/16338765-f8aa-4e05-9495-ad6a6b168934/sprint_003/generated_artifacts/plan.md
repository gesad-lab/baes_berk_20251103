# Implementation Plan: Create Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:  
# Implementation Plan: Add Email Field to Student Entity

---

## I. Architecture Overview

The application will continue to utilize a microservices architecture with clear boundaries between modules. The core components remain the same:

1. **Web Server**: FastAPI will manage HTTP requests and serve API endpoints.
2. **Database**: SQLite will persist course records efficiently alongside student records.

### Tech Stack
- **Web Framework**: FastAPI (Python 3.11+)
- **Database**: SQLite
- **Data Serialization**: Pydantic (for request and response validation)
- **Testing Framework**: pytest

## II. Module Boundaries

1. **API Module**:
   - Implement new routes and HTTP request handling for managing courses in addition to the existing student management functionalities.

2. **Database Module**:
   - Introduce a `Course` data model and handle schema management for the new `Course` table.

3. **Error Handling Module**: (Basic level)
   - Enhance error handling to validate inputs for course creation and updates.

4. **Testing Module**:
   - Implement tests reflecting the new scenarios associated with course entity creation, retrieval, and updates.

## III. Data Models

### Course Model
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

### API Request and Response Models
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

## IV. API Endpoints

### 1. Create a Course
- **Endpoint**: `/courses`
- **Method**: POST
- **Request Body**: 
```json
{
    "name": "Introduction to Python",
    "level": "Beginner"
}
```
- **Response (201 Created)**:
```json
{
    "id": 1,
    "name": "Introduction to Python",
    "level": "Beginner"
}
```

### 2. Retrieve a Single Course by ID
- **Endpoint**: `/courses/{id}`
- **Method**: GET
- **Response (200 OK)**:
```json
{
    "id": 1,
    "name": "Introduction to Python",
    "level": "Beginner"
}
```

### 3. Update a Course's Details
- **Endpoint**: `/courses/{id}`
- **Method**: PUT
- **Request Body**: 
```json
{
    "name": "Advanced Python",
    "level": "Intermediate"
}
```
- **Response (200 OK)**:
```json
{
    "id": 1,
    "name": "Advanced Python",
    "level": "Intermediate"
}
```

## V. Implementation Approach

1. **Set Up Environment**:
   - Verify that Python 3.11+ and SQLite are available and that FastAPI is properly configured.
   - No changes to existing project structure required, but new files will be added.

2. **Implement API Logic**:
   - Extend FastAPI routes in `course_api.py` to include new `POST`, `GET`, and `PUT` endpoints for course management.

3. **Set Up Database**:
   - Update `db_setup.py` to modify the SQLite schema, creating the new `courses` table with appropriate constraints.

4. **Database Migration Strategy**:
   - Create a new migration script that sets up the `courses` table without disrupting existing student data.
   - Utilize SQLite's standard practices to ensure the addition of the new table maintains referential integrity.

## VI. Error Handling

- Enhance error handling in the API to check for valid inputs (both name and level are required) and return error messages when invalid data is provided during creation or updates.

## VII. Success Criteria Verification

1. Validate that creating a course works as expected with valid name and level, returning course details in response.
2. Ensure retrieving courses includes correct details by ID.
3. Confirm that updating a course's details reflects changes appropriately when retrieved thereafter.

## VIII. Testing Strategy

1. **Unit Tests**: Cover functionality for creating, retrieving, and updating courses.
2. **Integration Tests**: Validate endpoint functionality for creating and modifying course records:
   - Implement tests for creation, retrieval, and updating of course records.

## IX. Documentation

- Update the `README.md` to reflect new API endpoints, request/response formats, and example payloads for courses.
- Include migration instructions necessary for deployment.

## X. Version Control Practices

- Commit changes in small increments focusing on logical units.
- Update documentation alongside code changes.

## XI. Deployment Considerations

- Verify that the database migration to add the `courses` table is ready for deployment, ensuring no downtime is involved.
- Confirm the application starts successfully with the new feature included, relying on environment variables and existing configurations.

By following this implementation plan, the introduction of the Course entity ensures that capabilities for managing curriculum can effectively enhance user experience without disruption of existing functionalities. 

### Existing Code Files:
File: `src/db_setup.py`

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student, Course  # Ensure to import the new Course model
...

def setup_database():
    ...
    Base.metadata.create_all(engine)  # This will now create both tables Students and Courses
```

File: `src/course_api.py` (new file for course management).
```python
from fastapi import APIRouter
from models import CourseCreate, CourseResponse
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

By ensuring that each component of this plan integrates seamlessly with existing modules, the enhancement can be achieved while maintaining adherence to architecture and coding standards.