# Tasks: Create Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `tests/test_migrations.py` (2131 bytes)
- `tests/test_student.py` (534 bytes)

---

## Task Breakdown

### Task 1: Update Project Structure
- [ ] Create directories for the new feature, ensuring proper organization.
  - **File Path**: `src/routers/`
  - **File Path**: `src/models/`
  - **File Path**: `src/services/`
  - **File Path**: `src/database/`

### Task 2: Database Migration for Courses Table
- [ ] Create migration script to add the courses table.
  - **File Path**: `migrations/versions/XXXXXX_create_courses_table.py` (replace `XXXXXX` with a timestamp)
  - **Migration Contents**:
    ```python
    def upgrade():
        op.create_table(
            'courses',
            sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
            sa.Column('name', sa.String, nullable=False),
            sa.Column('level', sa.String, nullable=False),
        )
    ```

### Task 3: Update Models
- [ ] Create a new model for the Course entity in `models.py`.
  - **File Path**: `src/models/models.py`
  - **Model Contents**:
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

### Task 4: Implement API Endpoints
- [ ] Create a new router for course API endpoints.
  - **File Path**: `src/routers/courses.py`
  - **Router Contents**:
    ```python
    from fastapi import APIRouter, HTTPException
    from pydantic import BaseModel
    from .models import Course
    from .database import session  # Assuming there's a session object for DB interaction

    router = APIRouter()

    class CourseCreate(BaseModel):
        name: str
        level: str

    class CourseResponse(BaseModel):
        id: int
        name: str
        level: str

    @router.post("/courses", response_model=CourseResponse)
    def create_course(course: CourseCreate):
        new_course = Course(name=course.name, level=course.level)
        session.add(new_course)
        session.commit()
        session.refresh(new_course)
        return new_course

    @router.get("/courses", response_model=list[CourseResponse])
    def get_courses():
        return session.query(Course).all()

    @router.put("/courses/{course_id}", response_model=CourseResponse)
    def update_course(course_id: int, course: CourseCreate):
        existing_course = session.query(Course).filter(Course.id == course_id).first()
        if not existing_course:
            raise HTTPException(status_code=404, detail="Course not found")
        existing_course.name = course.name
        existing_course.level = course.level
        session.commit()
        session.refresh(existing_course)
        return existing_course
    ```

### Task 5: Input Validation with Pydantic
- [ ] Ensure request body validation using Pydantic in the CourseCreate model.
  - **File Path**: `src/routers/courses.py` (included in Task 4)

### Task 6: Implement Unit and Integration Tests
- [ ] Create tests for course creation and validation.
  - **File Path**: `tests/test_courses.py`
  - **Test Contents**:
    ```python
    import pytest
    from fastapi.testclient import TestClient
    from src.main import app

    client = TestClient(app)

    def test_create_course():
        response = client.post("/courses", json={"name": "Math 101", "level": "Beginner"})
        assert response.status_code == 201
        assert response.json()["name"] == "Math 101"

    def test_create_course_missing_fields():
        response = client.post("/courses", json={"name": ""})
        assert response.status_code == 400
        assert "level" in response.json()["detail"][0]["loc"]
    ```

### Task 7: Documentation Generation
- [ ] Ensure API documentation is automatically generated and updated.
  - **File Path**: Automatically handled by FastAPI upon running the app.

### Task 8: Update Docker Configuration (if applicable)
- [ ] Update Dockerfiles or docker-compose as necessary to include new dependencies for the Course functionality.
  - **File Path**: `Dockerfile` or `docker-compose.yml`

### Task 9: Final Review and Testing
- [ ] Conduct a final review of all changes.
- [ ] Run tests to ensure all new features function as intended.

--- 

This task breakdown provides a clear and structured approach for implementing the new Course entity feature, facilitating independent execution and testing of each task.