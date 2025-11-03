# Tasks: Create Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- tests/test_integration.py (2356 bytes)
- tests/test_student.py (2364 bytes)

---

## Task Breakdown

### Database Tasks

- [ ] **Create Course Model**  
  **File**: `src/models/course.py`  
  **Description**: Implement the Course model using SQLAlchemy with `id`, `name`, and `level` fields.
  ```python
  from sqlalchemy import Column, Integer, String
  from database import Base

  class Course(Base):
      __tablename__ = "courses"

      id = Column(Integer, primary_key=True, index=True)
      name = Column(String, nullable=False)
      level = Column(String, nullable=False)
  ```

- [ ] **Create Migration Script for Courses Table**  
  **File**: `alembic/versions/202310xx_add_courses_table.py` (create with timestamp)  
  **Description**: Generate the Alembic migration script to create the `courses` table while preserving existing Student data.  
  **Command**: `alembic revision --autogenerate -m "Add courses table"`

### API Endpoint Tasks

- [ ] **Implement Create Course Endpoint**  
  **File**: `src/routes/course.py`  
  **Description**: Implement the POST `/courses` endpoint to create a Course using FastAPI. Include input validation for `name` and `level`.  
  ```python
  from fastapi import APIRouter, HTTPException
  from pydantic import BaseModel

  router = APIRouter()

  class CourseCreate(BaseModel):
      name: str
      level: str

  @router.post("/courses", response_model=Course)
  async def create_course(course: CourseCreate):
      # Logic to create Course
      pass 
  ```

- [ ] **Implement Retrieve Course Endpoint**  
  **File**: `src/routes/course.py`  
  **Description**: Implement the GET `/courses/{id}` endpoint to retrieve a Course by its ID.  
  ```python
  @router.get("/courses/{id}", response_model=Course)
  async def get_course(id: int):
      # Logic to retrieve Course
      pass
  ```

### Middleware & Validation Tasks

- [ ] **Setup Error Handling & Input Validation**  
  **File**: `src/routes/course.py`  
  **Description**: Ensure validation checks are in place for missing `name` and `level`, returning appropriate error responses.  
  ```python
  # Include validation for required fields and raise HTTPException for errors
  ```

### Testing Tasks

- [ ] **Create Course Tests**  
  **File**: `tests/test_courses.py`  
  **Description**: Develop unit and integration tests for the create and retrieve course functionalities. Include scenarios for valid input, missing name, and missing level.  
  ```python
  def test_create_course(client, course_data):
      # Test creation of course with valid data
      pass
  ```

- [ ] **Test Cases for Error Handling**  
  **File**: `tests/test_courses.py`  
  **Description**: Implement tests to ensure proper error messages are returned for missing fields.  
  ```python
  def test_create_course_missing_name(client):
      # Test for missing course name
      pass

  def test_create_course_missing_level(client):
      # Test for missing course level
      pass
  ```

- [ ] **Test Retrieval of Course by ID**  
  **File**: `tests/test_courses.py`  
  **Description**: Implement tests for retrieving a course successfully and handling non-existent IDs.  
  ```python
  def test_get_course(client):
      # Test retrieval of existing course by ID
      pass

  def test_get_course_not_found(client):
      # Test retrieval of a non-existent course ID
      pass
  ```

### Documentation Tasks

- [ ] **Update API Documentation**  
  **File**: `README.md`  
  **Description**: Add documentation explaining the new API endpoints for creating and retrieving courses in the `README.md` file.  

### Migration Setup Task

- [ ] **Update FastAPI Startup Event for Migrations**  
  **File**: `src/main.py`  
  **Description**: Ensure the startup event applies migrations automatically when the application starts using Alembic.  
  ```python
  @app.on_event("startup")
  async def startup():
      # Migration logic
  ```

---

This breakdown ensures a clear path forward for implementing the Course entity while maintaining the project's coding standards and organization. Each task is scoped appropriately and involves modifications or additions to a single file for easy testing and integration.