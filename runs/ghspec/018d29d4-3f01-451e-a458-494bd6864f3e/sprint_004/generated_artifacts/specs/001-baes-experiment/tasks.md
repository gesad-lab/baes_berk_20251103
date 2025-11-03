# Tasks: Add Course Relationship to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `tests/test_students_courses_api.py` (1517 bytes)

---

## Task Breakdown

### 1. Database Setup & Migration
- [ ] **Create Migration Script for StudentCourse Join Table**
  - **File**: `src/database/migrations/20231001_create_student_courses_table.py`
  - Update the database schema to include the `student_courses` join table for the many-to-many relationship.

```python
from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table(
        'student_courses',
        sa.Column('student_id', sa.Integer(), nullable=False),
        sa.Column('course_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['student_id'], ['students.id']),
        sa.ForeignKeyConstraint(['course_id'], ['courses.id']),
        sa.PrimaryKeyConstraint('student_id', 'course_id')
    )

def downgrade():
    op.drop_table('student_courses')
```

### 2. Develop Model
- [ ] **Implement StudentCourse Model**
  - **File**: `src/models/student_course.py`
  - Create a SQLAlchemy model for the `student_courses` join table.

```python
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class StudentCourse(Base):
    __tablename__ = 'student_courses'
    
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)
    student = relationship("Student")
    course = relationship("Course")
```

### 3. Develop API Endpoints
- [ ] **Implement API Endpoint to Associate Students with Courses**
  - **File**: `src/api/students.py`
  - Create an endpoint to handle `POST /students/{student_id}/courses` for associating students with multiple courses.

```python
from fastapi import FastAPI, HTTPException
from models.student_course import StudentCourse

app = FastAPI()

@app.post("/students/{student_id}/courses")
async def associate_student_courses(student_id: int, course_ids: List[int]):
    # Validation logic here
    # Insert associations into the database
    return {"message": "Courses associated successfully"}
```

- [ ] **Implement API Endpoint to Retrieve Student Courses**
  - **File**: `src/api/students.py`
  - Create an endpoint to handle `GET /students/{student_id}/courses`.

```python
@app.get("/students/{student_id}/courses")
async def retrieve_student_courses(student_id: int):
    # Logic to retrieve and return associated courses
    return {"courses": [{"id": 1, "name": "Course 1"}, {"id": 2, "name": "Course 2"}]}
```

### 4. Implement Input Validation
- [ ] **Input Validation for Course IDs**
  - **File**: `src/validation/course_validation.py`
  - Create a validation module to check if course IDs exist before association.

```python
def validate_course_ids(course_ids):
    # Logic to validate course IDs
    return True  # or raise an exception if invalid
```

### 5. Testing
- [ ] **Write Unit Tests for API Endpoints**
  - **File**: `tests/test_students_courses_api.py`
  - Add new tests for successful course association and retrieval.

```python
def test_associate_student_with_valid_courses():
    response = client.post("/students/1/courses", json={"course_ids": [1, 2]})
    assert response.status_code == 200

def test_retrieve_student_courses():
    response = client.get("/students/1/courses")
    assert response.status_code == 200
    assert "courses" in response.json()
```

- [ ] **Test Invalid Course Association**
  - **File**: `tests/test_students_courses_api.py`
  - Add a test for attempting to associate with non-existing course IDs.

```python
def test_associate_student_with_invalid_courses():
    response = client.post("/students/1/courses", json={"course_ids": [999]})  # Assuming 999 is invalid
    assert response.status_code == 400  # Assuming this returns a bad request for invalid IDs
```

### 6. Documentation
- [ ] **Update README.md for API Usage Instructions**
  - **File**: `README.md`
  - Document new API endpoints, including expected request and response formats.

---

### Additional Considerations
- Ensure complete integration with the existing system, following the established coding standards.
- Perform thorough testing to ensure all endpoints are working as intended.
- Keep all error handling consistent with how existing errors are managed in the application.