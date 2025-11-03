# Tasks: Add Course Relationship to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `tests/api/test_courses.py` (2869 bytes)
- `tests/integration/test_integration.py` (1626 bytes)

---

## Task Breakdown

### Database Migration

- [ ] **Task 1**: Implement the migration for the new junction table
  - **File**: `migrations/migration_add_student_course.py`
    - Create the `student_course` junction table using SQLite.
    
```python
import aiosqlite

async def migrate():
    async with aiosqlite.connect("database.db") as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS student_course (
                student_id INTEGER,
                course_id INTEGER,
                PRIMARY KEY (student_id, course_id),
                FOREIGN KEY (student_id) REFERENCES student(id),
                FOREIGN KEY (course_id) REFERENCES course(id)
            )
        """)
        await db.commit()
```

### API Endpoints Creation

- [ ] **Task 2**: Create the API endpoint for enrolling a student in a course
  - **File**: `api/enrollment.py`
  
```python
from fastapi import APIRouter, HTTPException
from .models.enrollment import CourseEnrollment

router = APIRouter()

@router.post("/students/{student_id}/courses", response_model=None)
async def enroll_student(student_id: int, enrollment: CourseEnrollment):
    # Logic for enrolling the student
    ...
```

- [ ] **Task 3**: Create the API endpoint for retrieving courses associated with a student
  - **File**: `api/enrollment.py`

```python
@router.get("/students/{student_id}/courses", response_model=EnrolledCoursesResponse)
async def get_student_courses(student_id: int):
    # Logic to get courses for the student
    ...
```

- [ ] **Task 4**: Create the API endpoint for listing students enrolled in a specific course
  - **File**: `api/enrollment.py`
  
```python
@router.get("/courses/{course_id}/students")
async def get_students_enrolled_in_course(course_id: int):
    # Logic to list students for the specified course
    ...
```

### Pydantic Models

- [ ] **Task 5**: Create Pydantic models for data validation
  - **File**: `api/models/enrollment.py`
  
```python
from pydantic import BaseModel, conint

class CourseEnrollment(BaseModel):
    course_id: conint(ge=1)

class EnrolledCoursesResponse(BaseModel):
    course_ids: list[conint(ge=1)]
```

### Testing

- [ ] **Task 6**: Write tests for the enrollment functionality
  - **File**: `tests/api/test_enrollment.py`
  
```python
import pytest
from fastapi.testclient import TestClient
from myapp.main import app

client = TestClient(app)

def test_enroll_student_with_valid_course():
    response = client.post("/students/1/courses", json={"course_id": 1})
    assert response.status_code == 201

def test_enroll_student_with_invalid_course():
    response = client.post("/students/1/courses", json={"course_id": 999})
    assert response.status_code == 404
```

- [ ] **Task 7**: Write integration tests for the new endpoints
  - **File**: `tests/integration/test_enrollment_integration.py`
  
```python
def test_get_student_courses():
    response = client.get("/students/1/courses")
    assert response.status_code == 200

def test_get_students_by_course():
    response = client.get("/courses/1/students")
    assert response.status_code == 200
```

### Documentation

- [ ] **Task 8**: Update the `README.md` to include new API endpoints
  - **File**: `README.md`
    - Add documentation for the new endpoints and request/response formats.

### Final Integration and Validation

- [ ] **Task 9**: Validate the implementation and ensure data integrity after migration
  - **File**: `tests/integration/test_data_migration.py`
    - Test the database integrity after running the migration script to ensure existing data is preserved.

---

This structured task breakdown highlights the critical steps required to implement the relationship between the Student and Course entities effectively. Each task focuses on a specific file or functionality to ensure a modular development process, allowing for independent testing as specified.