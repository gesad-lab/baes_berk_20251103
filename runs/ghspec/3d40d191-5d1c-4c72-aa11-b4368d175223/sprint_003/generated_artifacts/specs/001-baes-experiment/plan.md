# Implementation Plan: Create Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

## Previous Sprint Plan:
# Implementation Plan: Add Email Field to Student Entity

---

## Overview
This implementation plan outlines the creation of a new Course entity within the existing application. The goal is to allow users to manage and categorize courses independently while ensuring that existing data structures remain intact. This feature will involve adding new API endpoints for creating and retrieving courses, updating the database schema, and ensuring robust error handling for invalid requests.

## Architecture
The architecture follows the existing Model-View-Controller (MVC) pattern, with the following components being impacted by this implementation:

- **API Layer**: New endpoints for creating and retrieving Course entities.
- **Service Layer**: Logic for handling Course entity creation and retrieval.
- **Data Access Layer (DAL)**: Updates to the data model for the Course entity.
- **Database**: The SQLite database schema will be updated to include a new Course table.

### Module Boundaries
- **api.py**: Introduce new endpoints for managing Course entities.
- **models.py**: Create the Course model that defines the properties for courses.
- **services.py**: Add business logic for course management, including creation and retrieval.
- **database.py**: Implement migration functionality to add the Course table.

## Technology Stack
- **Programming Language**: Python 3.11+
- **Framework**: FastAPI
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Serialization/Validation**: Pydantic
- **Testing Framework**: pytest

## Implementation Steps

### 1. Environment Setup
- Utilize the existing environment setup from the previous sprint with FastAPI and SQLAlchemy already installed; no new installations are necessary.

### 2. Define Data Models
- Create a new `Course` model in `models.py` to include attributes for `id`, `name`, and `level`:

```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
```

- Define a Pydantic schema for course creation in a new file, `schemas.py`:

```python
from pydantic import BaseModel

class CourseCreate(BaseModel):
    name: str
    level: str
```

### 3. Database Management
- Create a migration script using Alembic to add the Course table to the existing database schema without affecting Student records. Example migration script:

```python
from alembic import op
import sqlalchemy as sa

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

### 4. Implement API Endpoints
- Add a new `POST /courses` endpoint in `api.py` for creating courses:

```python
@app.post("/courses", response_model=CourseCreate, status_code=201)
def create_course(course: CourseCreate):
    return create_course_service(course.name, course.level)
```

- Implement the `GET /courses` endpoint in `api.py` to retrieve all courses:

```python
@app.get("/courses", response_model=List[CourseCreate])
def get_courses():
    return get_all_courses_service()
```

### 5. Implement Business Logic
- Define service functions in `services.py` to handle logic for creating and retrieving courses:

```python
def create_course_service(name: str, level: str):
    course = Course(name=name, level=level)
    session.add(course)
    session.commit()
    session.refresh(course)
    return course

def get_all_courses_service():
    return session.query(Course).all()
```

### 6. Error Handling
- Ensure appropriate error handling in `api.py` for missing `name` or `level` fields:

```python
@app.post("/courses", response_model=CourseCreate, status_code=201)
def create_course(course: CourseCreate):
    if not course.name:
        raise HTTPException(status_code=400, detail="Name field is required.")
    if not course.level:
        raise HTTPException(status_code=400, detail="Level field is required.")
    return create_course_service(course.name, course.level)
```

### 7. Testing
- Create a new test file `tests/test_courses.py` to cover the new functionality, ensuring to include tests for successful course creation and error handling:

```python
def test_create_course(client):
    response = client.post("/courses", json={"name": "Mathematics", "level": "Beginner"})
    assert response.status_code == 201
    assert response.json()["name"] == "Mathematics"
    assert response.json()["level"] == "Beginner"

def test_create_course_missing_name(client):
    response = client.post("/courses", json={"level": "Beginner"})
    assert response.status_code == 400
    assert response.json()["detail"] == "Name field is required."

def test_create_course_missing_level(client):
    response = client.post("/courses", json={"name": "Mathematics"})
    assert response.status_code == 400
    assert response.json()["detail"] == "Level field is required."
```

### 8. Documentation
- Update the existing `README.md` file to include new API requirements for course creation and retrieval, along with usage examples.

## Scalability and Security Considerations
- **Scalability**: The new Course entity ensures scalability by maintaining a stateless design, allowing horizontal scaling.
- **Security**: Validate all inputs to prevent SQL injection attacks and ensure that error messages do not expose sensitive information.

## Deployment Considerations
- Migrate the database schema to include the new Course table during the deployment process. Execute the migration commands as follows:

```bash
alembic upgrade head
```

## Conclusion
This implementation plan details the structured approach for creating a Course entity, allowing for future functionalities while preserving existing data structures. The defined steps ensure that the API is robust, error handling is comprehensive, and testing is thorough, facilitating a smooth integration into the existing application framework.

Existing Code Files:
- **api.py** will require the addition of new endpoints.
- **models.py** will need a new `Course` model.
- **services.py** will have new business logic for course management.
- A new file `schemas.py` will house Pydantic models relevant to the Course entity.
- **tests/test_courses.py** will be newly created for course-related tests.