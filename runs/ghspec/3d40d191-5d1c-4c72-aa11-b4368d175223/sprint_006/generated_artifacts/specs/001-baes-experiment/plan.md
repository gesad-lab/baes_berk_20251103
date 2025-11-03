# Implementation Plan: Add Teacher Relationship to Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Teacher Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Course Relationship to Student Entity

---

## Overview
This implementation plan aims to establish a relationship between the Course and Teacher entities within the existing application. By enabling the assignment of a Teacher to a Course, we will enhance the educational management capabilities of the system, facilitating improved resource allocation and planning.

## Architecture
The architecture follows the Model-View-Controller (MVC) pattern, with the following components impacted by this implementation:

- **API Layer**: Introduce new endpoints for assigning a Teacher to a Course and retrieving course details with Teacher information.
- **Service Layer**: Logic for handling Teacher assignments to Courses and retrieving course details.
- **Data Access Layer (DAL)**: Update the data models to accommodate the new relationship between Courses and Teachers.
- **Database**: Update the SQLite database schema to add a `teacher_id` foreign key to the `courses` table, linking to the `teachers` table.

### Module Boundaries
- **api.py**: Introduce POST `/courses/{course_id}/assign-teacher` endpoint for assigning Teachers to Courses and GET `/courses/{course_id}` for retrieving Course details including Teacher information.
- **models.py**: Update the existing `Course` model to include a new `teacher_id` field.
- **services.py**: Implement service functions for assigning Teachers to Courses and retrieving Course details.
- **database.py**: Create a migration script to apply changes to the `courses` table while preserving existing data integrity.

## Technology Stack
- **Programming Language**: Python 3.11+
- **Framework**: FastAPI
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Serialization/Validation**: Pydantic
- **Testing Framework**: pytest
- **Migration Tool**: Alembic

## Implementation Steps

### 1. Environment Setup
- Verify that the existing environment maintains FastAPI, SQLAlchemy, and Alembic for database migrations, as specified in previous implementations.

### 2. Update Data Models
- Modify the existing `Course` model in `models.py` to include the new `teacher_id` field:

```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # New field

    teacher = relationship("Teacher", back_populates="courses")
```

- Ensure the `Teacher` model has a reverse relationship to courses:

```python
class Teacher(Base):
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    courses = relationship("Course", back_populates="teacher")  # New relationship
```

### 3. Database Management
- Create a migration script using Alembic to add the `teacher_id` column to the `courses` table:

```python
from alembic import op
import sqlalchemy as sa

def upgrade():
    op.add_column('courses', sa.Column('teacher_id', sa.Integer, sa.ForeignKey('teachers.id'), nullable=True))

def downgrade():
    op.drop_column('courses', 'teacher_id')
```

### 4. Implement API Endpoints
- Add the `POST /courses/{course_id}/assign-teacher` endpoint in `api.py` for assigning a Teacher to a Course:

```python
@app.post("/courses/{course_id}/assign-teacher", status_code=200)
def assign_teacher(course_id: int, teacher_id: int):
    return assign_teacher_service(course_id, teacher_id)
```

- Update the `GET /courses/{course_id}` endpoint in `api.py` to return detailed Course information including the assigned Teacher:

```python
@app.get("/courses/{course_id}", response_model=CourseDetailResponse)
def get_course_detail(course_id: int):
    return get_course_detail_service(course_id)
```

### 5. Implement Business Logic
- Define service functions in `services.py` for assigning Teachers to Courses and retrieving Course details:

```python
def assign_teacher_service(course_id: int, teacher_id: int):
    course = session.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    course.teacher_id = teacher_id
    session.commit()
    return course

def get_course_detail_service(course_id: int):
    course = session.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return {
        "id": course.id,
        "title": course.title,
        "description": course.description,
        "teacher": {
            "id": course.teacher.id if course.teacher else None,
            "name": course.teacher.name if course.teacher else None
        }
    }
```

### 6. Error Handling
- Ensure error handling for missing Teacher assignments when retrieving Course details:

```python
@app.get("/courses/{course_id}")
def get_course_detail(course_id: int):
    course_detail = get_course_detail_service(course_id)
    if not course_detail["teacher"]:
        raise HTTPException(status_code=404, detail="No Teacher assigned to this Course")
    return course_detail
```

### 7. Testing
- Create a new test file `tests/test_courses.py` to cover the Course functionalities, including assignments and retrieval:

```python
def test_assign_teacher(client):
    response = client.post("/courses/1/assign-teacher", json={"teacher_id": 1})
    assert response.status_code == 200
    assert response.json()["teacher_id"] == 1

def test_get_course_detail_with_teacher(client):
    response = client.get("/courses/1")
    assert response.status_code == 200
    assert response.json()["teacher"]["id"] is not None

def test_get_course_detail_without_teacher(client):
    response = client.get("/courses/2")  # Assume course 2 has no assigned teacher
    assert response.status_code == 404
    assert response.json()["detail"] == "No Teacher assigned to this Course"
```

### 8. Documentation
- Update `README.md` to describe the new API for assigning Teachers to Courses and retrieving Course details, including examples of requests and responses.

## Scalability and Security Considerations
- **Scalability**: The new associations are designed to scale efficiently, ensuring the API performs well as the number of Courses and Teachers increases.
- **Security**: Input validation will be enforced to prevent injection attacks, and user-facing error messages will not expose internal states.

## Deployment Considerations
- Run database migrations to add the `teacher_id` column to the `courses` table using:

```bash
alembic upgrade head
```

## Conclusion
This implementation plan effectively links Teachers to Courses within the existing application, enhancing educational management capabilities. Detailed steps ensure clear implementation, testing, and robust error handling while maintaining backward compatibility with existing data models.

### Existing Code Files Modifications
- **api.py** will be updated to add the new endpoints for assigning Teachers to Courses and retrieving Course details.
- **models.py** will be modified to include a new `teacher_id` in the `Course` model and establish a relationship with the `Teacher` model.
- **services.py** will implement logic for assigning Teachers to Courses and retrieving Course details.
- A new test file `tests/test_courses.py` will be created to test the new features related to Teacher assignments.

Existing Code Files:
```python
# The existing `api.py`, `models.py`, and `services.py` files will
# retain their previous structures with additions as described above
# to implement full Teacher-Course relationship functionality.
```

--- 

Overall, this plan incorporates the necessary updates to the system while preserving existing functional and data integrity.