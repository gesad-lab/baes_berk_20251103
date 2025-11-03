# Tasks: Create Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `tests/test_student.py` (1270 bytes)

---

## Task Breakdown

### Step 1: Create Course Model

- [ ] **Task 1**: Implement Course model in `src/models/course.py`
  - **File**: `src/models/course.py`
  - **Description**: Create a new Course model using SQLAlchemy with `name` and `level` fields.
  
  ```python
  from sqlalchemy import Column, String, Integer
  from sqlalchemy.ext.declarative import declarative_base
  
  Base = declarative_base()
  
  class Course(Base):
      __tablename__ = 'courses'
      
      id = Column(Integer, primary_key=True, index=True)
      name = Column(String, nullable=False)
      level = Column(String, nullable=False)
  ```

### Step 2: Create Course API Endpoints

- [ ] **Task 2**: Implement API endpoints for Course in `src/routes/course.py`
  - **File**: `src/routes/course.py`
  - **Description**: Develop the POST and GET endpoints for creating and retrieving courses respectively.
  
  ```python
  from fastapi import FastAPI, HTTPException
  from pydantic import BaseModel
  from src.models.course import Course
  from src.database import SessionLocal
  
  app = FastAPI()
  
  class CourseCreate(BaseModel):
      name: str
      level: str
  
  @app.post("/courses", response_model=Course)
  def create_course(course: CourseCreate):
      # Logic for creating course
      pass
  
  @app.get("/courses", response_model=list[Course])
  def read_courses():
      # Logic for retrieving courses
      pass
  ```

### Step 3: Create Database Migration for Courses

- [ ] **Task 3**: Create migration script for the Course table in `migrations/versions/xxxx_create_courses_table.py`
  - **File**: `migrations/versions/xxxx_create_courses_table.py`
  - **Description**: Implement Alembic migration to create the `courses` table.
  
  ```python
  from alembic import op
  import sqlalchemy as sa
  
  def upgrade() -> None:
      op.create_table(
          'courses',
          sa.Column('id', sa.Integer(), primary_key=True),
          sa.Column('name', sa.String(), nullable=False),
          sa.Column('level', sa.String(), nullable=False),
      )

  def downgrade() -> None:
      op.drop_table('courses')
  ```

### Step 4: Update Database Initialization Logic

- [ ] **Task 4**: Modify database initialization in `src/database.py`
  - **File**: `src/database.py`
  - **Description**: Ensure that the database initializes the new Course model and applies migrations correctly.
  
  ```python
  from sqlalchemy import create_engine
  from sqlalchemy.orm import sessionmaker
  from models.course import Base
  
  DATABASE_URL = "sqlite:///./courses.db"
  engine = create_engine(DATABASE_URL)
  
  def init_db():
      Base.metadata.create_all(bind=engine)  # Creates all tables
      migrate_database()  # Call for migrations to be applied
  ```

### Step 5: Create Input Validation

- [ ] **Task 5**: Implement input validation logic in `src/validators.py`
  - **File**: `src/validators.py`
  - **Description**: Create validation checks for required fields for course creation.
  
  ```python
  def validate_course_input(course_data):
      if not course_data.get("name"):
          raise ValueError("Name is required.")
      if not course_data.get("level"):
          raise ValueError("Level is required.")
  ```

### Step 6: Implement Error Handling in API

- [ ] **Task 6**: Update the API to incorporate error handling in `src/routes/course.py`
  - **File**: `src/routes/course.py`
  - **Description**: Add logic to return 400 Bad Request errors for missing course fields.

### Step 7: Write Unit Tests for Course Functionality

- [ ] **Task 7**: Create unit tests in `tests/test_course.py`
  - **File**: `tests/test_course.py`
  - **Description**: Write automated tests for creating courses, including scenarios for success and missing fields.

  ```python
  def test_create_course(client):
      response = client.post("/courses", json={"name": "Course Name", "level": "Beginner"})
      assert response.status_code == 201
      
  def test_create_course_missing_name(client):
      response = client.post("/courses", json={"level": "Beginner"})
      assert response.status_code == 400
      
  def test_create_course_missing_level(client):
      response = client.post("/courses", json={"name": "Course Name"})
      assert response.status_code == 400
  ```

### Step 8: Document API in OpenAPI format

- [ ] **Task 8**: Ensure correct API documentation is generated
  - **File**: `src/routes/course.py` (auto-generated)
  - **Description**: Verify that FastAPI generates OpenAPI documentation for the new Course endpoints.

### Step 9: Run Database Migrations

- [ ] **Task 9**: Ensure that migrations are run upon application start
  - **File**: `src/database.py`
  - **Description**: Validate that the application runs the Alembic migration upon initial setup.

---

By executing these incremental tasks, a new Course entity will be successfully integrated into the existing Student Entity Web Application, following the specifications and documentation provided. Each task is focused on a single file, ensuring independent testing and traceability throughout the implementation process.