# Tasks: Create Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `api.py` (2500 bytes)
- `models.py` (1200 bytes)
- `services.py` (800 bytes)
- `database.py` (600 bytes)

---

## Task Breakdown

### 1. Define Data Models
- [ ] **Task 1.1**: Create a new `Course` model in `src/models.py` to define attributes for `id`, `name`, and `level`.  
  **File**: `src/models.py`  
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

- [ ] **Task 1.2**: Define a Pydantic schema for course creation in a new file, `schemas.py`.  
  **File**: `src/schemas.py`  
  ```python
  from pydantic import BaseModel

  class CourseCreate(BaseModel):
      name: str
      level: str
  ```

### 2. Database Management
- [ ] **Task 2.1**: Create a migration script using Alembic to add the Course table to the existing database schema.  
  **File**: `migrations/versions/xxxx_create_courses_table.py`  
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

### 3. Implement API Endpoints
- [ ] **Task 3.1**: Add a new `POST /courses` endpoint in `src/api.py` for creating courses.  
  **File**: `src/api.py`  
  ```python
  @app.post("/courses", response_model=CourseCreate, status_code=201)
  def create_course(course: CourseCreate):
      return create_course_service(course.name, course.level)
  ```

- [ ] **Task 3.2**: Implement the `GET /courses` endpoint in `src/api.py` to retrieve all courses.  
  **File**: `src/api.py`  
  ```python
  @app.get("/courses", response_model=List[CourseCreate])
  def get_courses():
      return get_all_courses_service()
  ```

### 4. Implement Business Logic
- [ ] **Task 4.1**: Define service functions in `src/services.py` to handle logic for creating and retrieving courses.  
  **File**: `src/services.py`  
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

### 5. Error Handling
- [ ] **Task 5.1**: Ensure appropriate error handling in `src/api.py` for missing `name` or `level` fields.  
  **File**: `src/api.py`  
  ```python
  @app.post("/courses", response_model=CourseCreate, status_code=201)
  def create_course(course: CourseCreate):
      if not course.name:
          raise HTTPException(status_code=400, detail="Name field is required.")
      if not course.level:
          raise HTTPException(status_code=400, detail="Level field is required.")
      return create_course_service(course.name, course.level)
  ```

### 6. Testing
- [ ] **Task 6.1**: Create a new test file `tests/test_courses.py` to cover the new functionality including tests for course creation and error handling.  
  **File**: `tests/test_courses.py`  
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

### 7. Documentation
- [ ] **Task 7.1**: Update the existing `README.md` file to include new API requirements for course creation and retrieval.  
  **File**: `README.md`  
  - Include usage examples for POST and GET requests related to the `/courses` endpoint.

## Conclusion
This task breakdown organizes the creation of a Course entity in a structured manner, facilitating a clean and efficient implementation. Each task is designed to be small and focused, promoting independent testability.