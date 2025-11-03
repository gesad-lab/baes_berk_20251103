# Tasks: Create Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `tests/api/test_routes.py` (1916 bytes)
- `tests/services/test_student_service.py` (1920 bytes)

---

## Task Breakdown

- [ ] **Task 1: Create Course Model**
  - **File Path**: `src/models.py`
  - **Action**: Implement the `Course` model with `id`, `name`, and `level` fields as specified.
  ```python
  class Course(Base):
      __tablename__ = 'courses'
      id = Column(Integer, primary_key=True, autoincrement=True)
      name = Column(String, nullable=False)
      level = Column(String, nullable=False)
  ```

- [ ] **Task 2: Create Database Migration for Courses Table**
  - **File Path**: `migrations/versions/create_courses_table.py`
  - **Action**: Add migration script to create the `courses` table. Ensure it's reversible.
  ```python
  from sqlalchemy import Column, String, Integer
  from alembic import op
   
  def upgrade():
      op.create_table(
          'courses',
          Column('id', Integer, primary_key=True, autoincrement=True),
          Column('name', String, nullable=False),
          Column('level', String, nullable=False)
      )
   
  def downgrade():
      op.drop_table('courses')
  ```

- [ ] **Task 3: Implement Course Service**
  - **File Path**: `src/services/course_service.py`
  - **Action**: Create the `CourseService` class with methods for creating and retrieving courses.
  ```python
  class CourseService:
      def create_course(self, name: str, level: str):
          if not name:
              raise ValueError("Name field is required.")
          if not level:
              raise ValueError("Level field is required.")
  ```

- [ ] **Task 4: Add API Routes for Course Endpoints**
  - **File Path**: `src/main.py`
  - **Action**: Add `POST /courses` and `GET /courses/{id}` routes to handle course creation and retrieval.
  ```python
  @app.post("/courses")
  def create_course(course: Course):
      # Logic to create course
      pass

  @app.get("/courses/{id}")
  def get_course(id: int):
      # Logic to retrieve course by ID
      pass
  ```

- [ ] **Task 5: Implement Error Handling in API**
  - **File Path**: `src/main.py`
  - **Action**: Ensure the API returns appropriate error messages for missing name and level fields.
  ```python
  @app.post("/courses")
  def create_course(course: Course):
      # Check for missing fields and return proper 400 responses
      pass
  ```

- [ ] **Task 6: Create Unit Tests for Course Service**
  - **File Path**: `tests/services/test_course_service.py`
  - **Action**: Write unit tests to validate functionality of course creation and error handling.
  ```python
  def test_create_course_with_valid_data():
      # Test for successful creation

  def test_create_course_missing_name():
      # Test for handling missing name
  ```

- [ ] **Task 7: Add Integration Tests for Course API**
  - **File Path**: `tests/api/test_routes.py`
  - **Action**: Write integration tests to validate the API responses for course creation and retrieval.
  ```python
  def test_create_course():
      # Test successful API call for course creation

  def test_get_course():
      # Test successful API call for retrieving an existing course
  ```

- [ ] **Task 8: Update API Documentation**
  - **File Path**: `docs/api_reference.md`
  - **Action**: Document the new course endpoints, request formats, and responses.
  
- [ ] **Task 9: Run Database Migrations**
  - **File Path**: Deployment script
  - **Action**: Ensure the database migrations run successfully to create the `courses` table without errors.

- [ ] **Task 10: Validate Application Health Post-Implementation**
  - **File Path**: Monitoring setup
  - **Action**: Ensure the application responds correctly after implementing new changes, including health checks.

---

This breakdown organizes tasks into manageable portions that align with the implementation plan, ensuring completeness and clarity for developers. Each task is directed towards modifying existing files or creating new files in order to achieve the MVP objectives for the Course entity feature.