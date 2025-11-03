# Tasks: Create Course Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `models.py` (existing data models)
- `tests/test_routes.py` (for testing APIs)

---

### Task 1: Update Models for Course Entity
- **File**: `src/models.py`
- **Description**: Add the Course class to define the `courses` table schema.
- **Code**:
  ```python
  class Course(Base):
      __tablename__ = 'courses'
      
      id = Column(Integer, primary_key=True, autoincrement=True)
      name = Column(String(255), nullable=False)
      level = Column(String(255), nullable=False)
  ```
- [ ] Task 1 Complete

---

### Task 2: Create Migration Script for Courses Table
- **File**: `src/migrations/versions/XXXXX_add_courses_table.py` (Generate with Alembic)
- **Description**: Implement a migration that adds the `courses` table to the database.
- **Code**:
  ```python
  from alembic import op
  import sqlalchemy as sa

  def upgrade():
      op.create_table(
          'courses',
          sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
          sa.Column('name', sa.String(length=255), nullable=False),
          sa.Column('level', sa.String(length=255), nullable=False),
      )

  def downgrade():
      op.drop_table('courses')
  ```
- [ ] Task 2 Complete

---

### Task 3: Implement Course API Endpoints
- **File**: `src/controllers/course_controller.py`
- **Description**: Create the controller for handling course-related API endpoints.
- **Endpoints**:
  - `POST /courses`
  - `GET /courses`
  - `PUT /courses/{id}`
  - `DELETE /courses/{id}`
- [ ] Task 3 Complete

---

### Task 4: Define Course Service Layer Logic
- **File**: `src/services/course_service.py`
- **Description**: Implement business logic for course CRUD operations and validation.
- [ ] Task 4 Complete

---

### Task 5: Update API Routing to Include Course Endpoints
- **File**: `src/routes.py`
- **Description**: Add routing for the new course endpoints to the existing Flask app.
- [ ] Task 5 Complete

---

### Task 6: Create Unit Tests for Course Endpoints
- **File**: `tests/test_routes.py`
- **Description**: Write unit tests for all course-related API endpoints, ensuring coverage for CRUD operations.
- **Example Test Code**:
  ```python
  def test_create_course(client):
      response = client.post('/courses', json={"name": "Math 101", "level": "Beginner"})
      assert response.status_code == 201

  def test_retrieve_courses(client):
      response = client.get('/courses')
      assert response.status_code == 200
  ```
- [ ] Task 6 Complete

---

### Task 7: Integration Testing to Validate Course Creation
- **File**: `tests/test_integration.py`
- **Description**: Create integration tests that check creation, retrieval, update, and deletion of courses through the API.
- [ ] Task 7 Complete

---

### Task 8: Logging Implementation for Course API
- **File**: `src/controllers/course_controller.py`
- **Description**: Add structured logging for API requests and responses for course operations.
- **Code Example**:
  ```python
  import logging
  
  logging.basicConfig(level=logging.INFO)
  logger = logging.getLogger(__name__)
  
  logger.info("Creating new course record.")
  ```
- [ ] Task 8 Complete

---

### Task 9: Ensure Existing Records Remain Untouched During Migration
- **File**: `tests/test_migration_integration.py`
- **Description**: Write tests to verify that existing student records remain unaffected after running the migration.
- [ ] Task 9 Complete

---

### Task 10: Documentation Update
- **File**: `README.md`
- **Description**: Update the documentation to reflect the new `/courses` API endpoints and usage examples.
- [ ] Task 10 Complete

---

This structured breakdown outlines actionable tasks directed towards implementing the new Course entity, ensuring that each task is focused on a single file or responsibility and can be executed independently for testing and validation.