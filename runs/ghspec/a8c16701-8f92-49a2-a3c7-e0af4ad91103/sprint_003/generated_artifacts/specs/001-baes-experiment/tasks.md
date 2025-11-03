# Tasks: Create Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `tests/test_api.py` (2634 bytes)
- `tests/test_models.py` (2344 bytes)

---

## Task List

- [ ] **Create Course Model**
  - **File**: `src/models/course.py`
  - **Description**: Implement the Course data model with `id`, `name`, and `level` attributes.
  - **Implementation**:
    ```python
    from sqlalchemy import Column, Integer, String
    from src.database import Base

    class Course(Base):
        __tablename__ = 'courses'
        
        id = Column(Integer, primary_key=True, index=True)
        name = Column(String, nullable=False)  # Required
        level = Column(String, nullable=False)  # Required
    ```

- [ ] **Database Migration**
  - **File**: Migration script for Alembic
  - **Description**: Generate and define a migration for adding a new `courses` table.
  - **Implementation**:
    1. Run command:
       ```bash
       alembic revision --autogenerate -m "Add Course table"
       ```
    2. Edit the generated migration script:
    ```python
    def upgrade():
        op.create_table(
            'courses',
            sa.Column('id', sa.Integer(), nullable=False),
            sa.Column('name', sa.String(), nullable=False),
            sa.Column('level', sa.String(), nullable=False),
            sa.PrimaryKeyConstraint('id')
        )
    
    def downgrade():
        op.drop_table('courses')
    ```
    3. Apply migration upon app startup:
       ```bash
       alembic upgrade head
       ```

- [ ] **Implement API Endpoints for Course**
  - **File**: `src/api.py`
  - **Description**: Add new API routes for creating and retrieving courses.
  - **Implementation**:
    Implement the following routes in the API file:
    - `POST /courses`: For creating a new course.
    - `GET /courses/{id}`: For retrieving course details by ID.

- [ ] **Implement Error Handling for Course**
  - **File**: `src/errors.py`
  - **Description**: Extend centralized error handling to include errors related to course validations.
  - **Implementation**: Validate presence of `name` and `level` fields for the creation endpoint.

- [ ] **Update Application Entry Point**
  - **File**: `src/app.py`
  - **Description**: Ensure the application entry point is set to manage new Course routes correctly.
  - **Implementation**: Confirm integration of the new API routes; modify as necessary.

- [ ] **Create Unit Tests for Course API**
  - **File**: `tests/test_course.py`
  - **Description**: Add tests specifically for course creation and retrieval.
  - **Implementation**:
    - **Tests to include**:
      - Successful creation with valid data.
      - Error handling for missing fields.

```python
def test_create_course_success(test_db):
    # Implement test logic for successful course creation

def test_create_course_missing_fields(test_db):
    # Implement test logic for missing fields handling
```

- [ ] **Create Integration Tests for Course**
  - **File**: `tests/test_api.py`
  - **Description**: Extend existing tests to verify new interactions involving `Course`.
  - **Implementation**:
    - Confirm existing functionalities with `Student` remain intact and test API integration.

```python
def test_retrieve_course_success(test_db):
    # Implement test logic for successful retrieval of a course
```

- [ ] **Update Documentation for API**
  - **File**: `README.md`
  - **Description**: Add information regarding the new Course API endpoints.
  - **Implementation**:
    - Document input and output data specifications for new endpoints, including error responses.

- [ ] **Ensure Database Integrity During Migration**
  - **File**: Add relevant tests to `tests/test_models.py`
  - **Description**: Write tests that verify the Student data remains unaffected post migration.
  - **Implementation**: Ensure that tests confirm existing `Student` records are unchanged.

```python
def test_student_data_integrity_after_migration(test_db):
    # Implement test logic to verify Student entity integrity
```

--- 

Each task is designed to be independently executable and testable, ensuring that the new Course entity integration follows the project's existing architecture paradigms while maintaining clarity and separation of concerns.