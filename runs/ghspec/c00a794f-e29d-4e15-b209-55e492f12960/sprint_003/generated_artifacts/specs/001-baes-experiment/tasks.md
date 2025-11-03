# Tasks: Create Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `tests/test_student.py` (2018 bytes)

---

## Task Breakdown

### Task 1: Create Database Model for Course

- **File Path**: `src/models.py`
- **Description**: Add the new `Course` model to the `models.py` file with attributes for `id`, `name`, and `level`.
- **Code Change**: Implement the SQLAlchemy class definition for the Course model.

```python
from sqlalchemy import Column, Integer, String
from database import Base

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # Name of the course
    level = Column(String, nullable=False)  # Level of the course
```
- [ ] Add `Course` model implementation to `models.py`.

### Task 2: Create API Routes for Course

- **File Path**: `src/routes/course_routes.py`
- **Description**: Implement API endpoints for creating and retrieving courses in the newly created `course_routes.py` file.
- **Code Change**: Define the `POST /courses` and `GET /courses` endpoints.

```python
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from models import Course
from database import SessionLocal

router = APIRouter()

class CourseCreate(BaseModel):
    name: str
    level: str

@router.post("/courses")
def create_course(course: CourseCreate):
    # Logic to add course to DB
    pass

@router.get("/courses")
def get_courses():
    # Logic to retrieve courses from DB
    pass
```
- [ ] Implement course creation and retrieval routes in `course_routes.py`.

### Task 3: Update Main Application to Include Course Routes

- **File Path**: `src/main.py`
- **Description**: Modify the main application entry point to include the new course routes.
- **Code Change**: Import `course_routes` and add it to the FastAPI app.

```python
from fastapi import FastAPI
from routes import student_routes, course_routes

app = FastAPI()

app.include_router(student_routes.router)
app.include_router(course_routes.router)
```
- [ ] Integrate course routes into the FastAPI application in `main.py`.

### Task 4: Create Unit Tests for Course API

- **File Path**: `tests/test_course.py`
- **Description**: Develop unit tests to validate the functionality of the course creation and retrieval endpoints.
- **Code Change**: Implement scenarios for valid and invalid requests to the course API.

```python
import pytest

def test_add_course_with_valid_data(client):
    response = client.post("/courses", json={"name": "Math 101", "level": "beginner"})
    assert response.status_code == 200
    assert response.json() == {"message": "Course added successfully"}

def test_add_course_without_level(client):
    response = client.post("/courses", json={"name": "Math 101"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Level is required."}}
```
- [ ] Write tests for course creation and retrieval scenarios in `test_course.py`.

### Task 5: Create Database Migration for Courses Table

- **File Path**: `migrations/versions/xxxx_create_courses_table.py`
- **Description**: Create a migration script for adding the `courses` table to the SQLite database.
- **Code Change**: Define `upgrade` and `downgrade` functions for the new table.

```python
from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False)
    )

def downgrade():
    op.drop_table('courses')
```
- [ ] Develop the migration script for the `courses` table in the appropriate migrations folder.

### Task 6: Update Documentation

- **File Path**: `README.md`
- **Description**: Revise the `README.md` to include documentation for the new Course entity, including details about endpoints and example requests.
- **Code Change**: Add sections for Course entity, API usage, and any new configurations.

```markdown
## Course Entity

### Create Course
- `POST /courses`: Create a new course with a JSON body containing `name` and `level`.

### Retrieve Courses
- `GET /courses`: Get a list of all courses with their names and levels.
```
- [ ] Update `README.md` to document the Course API and related functionalities.

### Task 7: Validate the Functionality

- **File Path**: `tests/test_course.py`
- **Description**: Execute all tests to ensure course functionality works and all checks meet success criteria.
- **Code Change**: Ensure all unit tests pass and validate against the defined success criteria.
- [ ] Run tests and confirm that all course functionalities are correctly implemented and validated.

---

These tasks provide a detailed breakdown to implement the Course entity feature, ensuring proper integration and adherence to the existing coding standards. Each task is independent and can be executed and tested in isolation.