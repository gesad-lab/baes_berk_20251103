# Tasks: Create Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `models.py` (existing model definitions)
- `schemas.py` (existing Pydantic schemas)
- `routes/courses.py` (new functionality)
- `tests/test_students.py` (existing test structure)

Instructions for Task Breakdown:
1. Identify which existing files need modifications.
2. Create new files for new functionality.
3. Ensure integration tasks are included.
4. Maintain consistency with existing code style and patterns.

---

## Task List

- [ ] **Task 1**: Create a new Course model in `models.py`
  - **File**: `student_management/src/models.py`
  - **Description**: Add a new model `Course` that defines fields `id`, `name`, and `level`.
  ```python
  from sqlalchemy import Column, Integer, String
  from database import Base

  class Course(Base):
      __tablename__ = 'courses'

      id = Column(Integer, primary_key=True, autoincrement=True)
      name = Column(String, nullable=False)  # Required
      level = Column(String, nullable=False)  # Required
  ```

- [ ] **Task 2**: Create Pydantic schemas for Course entity in `schemas.py`
  - **File**: `student_management/src/schemas.py`
  - **Description**: Define request and response schemas for Course creation and retrieval.
  ```python
  from pydantic import BaseModel, constr

  class CourseCreate(BaseModel):
      name: constr(min_length=1)
      level: constr(min_length=1)

  class CourseResponse(BaseModel):
      id: int
      name: str
      level: str

      class Config:
          orm_mode = True
  ```

- [ ] **Task 3**: Implement the API route for creating courses in `routes/courses.py`
  - **File**: `student_management/src/routes/courses.py`
  - **Description**: Set up the script to handle `POST /courses` to create a new course.
  ```python
  from fastapi import APIRouter, HTTPException
  from schemas import CourseCreate, CourseResponse
  from models import Course
  from database import db

  router = APIRouter()

  @router.post("/courses", response_model=CourseResponse)
  async def create_course(course: CourseCreate):
      db_course = Course(name=course.name, level=course.level)
      db.add(db_course)
      db.commit()
      db.refresh(db_course)
      return {"message": "Course created successfully", "course_id": db_course.id}
  ```

- [ ] **Task 4**: Implement the API route for retrieving all courses in `routes/courses.py`
  - **File**: `student_management/src/routes/courses.py`
  - **Description**: Add a route for `GET /courses` to retrieve all courses.
  ```python
  @router.get("/courses", response_model=List[CourseResponse])
  async def get_courses():
      courses = db.query(Course).all()
      return courses
  ```

- [ ] **Task 5**: Create migration script for courses table in database
  - **File**: `student_management/src/migrations/0001_create_courses.py`
  - **Description**: Define SQL commands to create the `courses` table.
  ```sql
  CREATE TABLE courses (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT NOT NULL,
      level TEXT NOT NULL
  );
  ```

- [ ] **Task 6**: Write unit tests for course creation and retrieval in `tests/test_courses.py`
  - **File**: `student_management/tests/test_courses.py`
  - **Description**: Create tests that cover the scenarios defined, including successful creation and retrieval as well as handling errors for missing fields.
  ```python
  def test_create_course(client):
      response = client.post("/courses", json={"name": "Intro to Programming", "level": "Beginner"})
      assert response.status_code == 200
      assert "course_id" in response.json()

  def test_get_courses(client):
      response = client.get("/courses")
      assert response.status_code == 200
      assert isinstance(response.json(), list)
  ```

- [ ] **Task 7**: Update `README.md` with new API documentation
  - **File**: `student_management/README.md`
  - **Description**: Include details about the newly added `/courses` endpoints, their request/response formats, and examples.

---

## Summary
These tasks are designed to be self-contained and maintainable while ensuring a smooth integration of the new `Course` entity into the existing Student Entity Management Web Application. Each task focuses on a distinct aspect of the feature implementation and can be tested independently.