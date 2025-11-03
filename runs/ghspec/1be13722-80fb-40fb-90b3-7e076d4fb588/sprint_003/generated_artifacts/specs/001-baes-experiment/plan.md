# Implementation Plan: Create Course Entity

---

## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Email Field to Student Entity

---

## I. Overview
This implementation plan outlines the steps needed to introduce a new Course entity into the existing application. By implementing this feature, we will enable better management of educational courses by allowing users to create and retrieve course information, thus enhancing the overall educational data structure. The plan includes necessary architectural updates, technology decisions, module interactions, API contracts, and testing strategies.

## II. Technology Stack
- **Web Framework**: FastAPI (for building the API)
- **Database**: SQLite (lightweight and serverless)
- **ORM**: SQLAlchemy (for object-relational mapping)
- **Testing Framework**: pytest (for unit and integration testing)
- **Environment Management**: Poetry (for dependency management)
- **Documentation**: OpenAPI (auto-generated documentation through FastAPI)

## III. Architecture
### 1. Module Boundaries
- **API Module**: Introduction of routes for creating courses and retrieving course information.
- **Service Layer**: New business logic for managing Course entities will be implemented.
- **Data Access Layer**: New access methods for interacting with the Course table in the database.
- **Model Layer**: Definition of the Course data schema, including all required attributes.

### 2. Directory Structure
```
/course_entity_management
│
├── /src
│   ├── /api
│   │   └── course.py                # New API routes for courses
│   ├── /models
│   │   └── course.py                # SQLAlchemy models for Course entity
│   ├── /services
│   │   └── course_service.py        # Business logic for course management
│   ├── /database
│   │   └── db.py                    # Existing database connection and initialization
│   └── main.py                      # Entry point of the application
│
├── /tests
│   ├── /api
│   │   └── test_course.py           # Test cases for course API
│   └── /services
│       └── test_course_service.py    # Test cases for course service
│
├── .env.example                      # Environment variable definitions
├── pyproject.toml                    # Poetry dependency management
└── README.md                         # Project documentation
```

## IV. Data Models
### 1. Course Entity
```python
# /src/models/course.py

from sqlalchemy import Column, Integer, String
from database import Base

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # Required Course name
    level = Column(String, nullable=False)  # Required Course level
```

## V. API Contracts
### 1. Create Course Endpoint
- **Method**: `POST`
- **Endpoint**: `/courses`
- **Request Body**:
  ```json
  {
    "name": "Introduction to Computer Science",
    "level": "100"
  }
  ```
- **Success Response**:
  - **Status**: 201 Created
  - **Body**:
    ```json
    {
      "id": 1,
      "name": "Introduction to Computer Science",
      "level": "100"
    }
    ```
- **Error Responses**:
  - **Status**: 400 Bad Request
  - **Body**:
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Name is required."
      }
    }
    ```
  - **Status**: 400 Bad Request
  - **Body**:
    ```json
    {
      "error": {
        "code": "E002",
        "message": "Level is required."
      }
    }
    ```

### 2. Retrieve Courses Endpoint
- **Method**: `GET`
- **Endpoint**: `/courses`
- **Success Response**:
  - **Status**: 200 OK
  - **Body**:
    ```json
    [
      {
        "id": 1,
        "name": "Introduction to Computer Science",
        "level": "100"
      }
    ]
    ```

## VI. Implementation Approach
1. **Setup Environment**:
   - Ensure the development environment is prepared using Poetry.
   - Verify that existing dependencies are installed.

2. **Database Migration**:
   - **Strategy**: Create a new migration script to add a `courses` table, ensuring that the migration does not disrupt or affect existing Student data. Use Alembic for database migrations.

```python
# Migration Script (using Alembic)
def upgrade():
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False),
    )

def downgrade():
    op.drop_table('courses')
```

3. **Implement API Endpoints**:
   - Create a new `course.py` file in the API module for defining `POST /courses` and `GET /courses` endpoints. Implement the necessary business logic to handle course creation, including validations for required fields.

```python
# src/api/course.py

from fastapi import APIRouter, HTTPException
from models.course import Course
from services.course_service import create_course, get_all_courses
from pydantic import BaseModel

router = APIRouter()

class CourseCreate(BaseModel):
    name: str
    level: str

@router.post("/courses", response_model=Course, status_code=201)
async def create_course_endpoint(course: CourseCreate):
    return await create_course(course)

@router.get("/courses", response_model=List[Course])
async def retrieve_courses_endpoint():
    return await get_all_courses()
```

4. **Business Logic Layer**:
   - Create a new `course_service.py` in the service layer that includes logic for course creation and retrieval. Validate the presence of fields before performing database operations.

```python
# /src/services/course_service.py

from models.course import Course
from database import SessionLocal

async def create_course(course_data: CourseCreate):
    if not course_data.name or not course_data.level:
        raise HTTPException(status_code=400, detail="Name and level are required.")
    
    course = Course(name=course_data.name, level=course_data.level)
    db: Session = SessionLocal()
    db.add(course)
    db.commit()
    db.refresh(course)
    return course

async def get_all_courses():
    db: Session = SessionLocal()
    return db.query(Course).all()
```

5. **Testing**:
   - Develop tests in `test_course.py` and `test_course_service.py` to validate the new course functionalities. Ensure the tests cover success cases and errors (e.g., missing fields).

```python
# tests/api/test_course.py

def test_create_course_success(client):
    response = client.post("/courses", json={"name": "Math 101", "level": "1"})
    assert response.status_code == 201
    assert "id" in response.json()

def test_create_course_missing_name(client):
    response = client.post("/courses", json={"level": "1"})
    assert response.status_code == 400
    assert response.json()["error"]["message"] == "Name is required."
```

6. **Documentation**:
   - Update the API documentation to include the new course-related endpoints in the autogenerated OpenAPI documentation.

## VII. Success Criteria
- Successful creation of a course should return a 201 status code, including the course ID and details.
- Course retrieval should work accurately, returning a list of courses in JSON format.
- Proper validation errors should be raised for missing required fields.

## VIII. Security Considerations
- Inputs must be validated to prevent injection attacks. Ensure no user-input values are logged unnecessarily and implement strict input validation on course creation.

## IX. Performance Considerations
- Ensure that the SQLite database performs adequately for CRUD operations related to course management; however, anticipate the need for a more robust database as growth occurs.

## X. Deployment Considerations
- Review the Dockerfile and configuration files to ensure they reflect the new database schema. Document necessary environment variables in `.env.example`, especially those concerning DB connections.

## XI. Conclusion
Implementing this plan will successfully introduce the Course entity into the application. Following these steps ensures a robust, thoroughly tested integration that enhances course management. The next course of action involves initializing the database migration and implementing the outlined API functionalities.