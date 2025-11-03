# Tasks: Create Teacher Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `tests/test_routes.py` (1631 bytes)
- `tests/test_models.py` (2380 bytes)

---

## 1. Extend the Teacher Model

- [ ] **Task**: Extend `src/models.py` to include the `Teacher` model as specified  
  **File**: `src/models.py`  
  **Description**: Implement the `Teacher` class with fields for `id`, `name`, and `email`. Ensure `name` and `email` are required and that `email` has a unique constraint.

---

## 2. Database Migration Setup

- [ ] **Task**: Modify the migration script to create the Teacher table  
  **File**: `src/database.py`  
  **Description**: Create a migration script using Alembic that defines the `teachers` table, ensuring the fields correspond to the requirements below. Ensure migrations preserve existing Student and Course data.  
  **Migration Script Example**:
  ```python
  from alembic import op
  import sqlalchemy as sa

  def upgrade():
      op.create_table('teachers',
          sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
          sa.Column('name', sa.String(), nullable=False),
          sa.Column('email', sa.String(), nullable=False, unique=True)
      )

  def downgrade():
      op.drop_table('teachers')
  ```

---

## 3. API Endpoint Implementation for Creating Teacher

- [ ] **Task**: Implement `create_teacher()` in `src/api/routes.py` for handling `POST /teachers`  
  **File**: `src/api/routes.py`  
  **Description**: Create a function that validates input data for `name` and `email`. If valid, create a new Teacher record in the database and return its details in JSON format.

---

## 4. API Endpoint Implementation for Retrieving Teacher Details

- [ ] **Task**: Implement `get_teacher_details(teacher_id)` in `src/api/routes.py` for handling `GET /teachers/{teacher_id}`  
  **File**: `src/api/routes.py`  
  **Description**: Create a function that retrieves the Teacher record for the given `teacher_id` and returns its details in JSON format.

---

## 5. Input Validation Implementation

- [ ] **Task**: Set up input validation for the Teacher entity in `src/schemas.py`  
  **File**: `src/schemas.py`  
  **Description**: Define validation schemas to ensure that both `name` and `email` are provided when creating a Teacher.

---

## 6. Testing Implementation for Teacher Creation

- [ ] **Task**: Create tests for the Teacher creation in `tests/test_routes.py`  
  **File**: `tests/test_routes.py`  
  **Description**: Add unit tests to verify successful Teacher creation with valid data, incorrect data handling (e.g., missing `name` or `email`), and the expected JSON response structure.  
  **Sample Test**:
  ```python
  def test_create_teacher_success(client):
      """Test that creating a teacher with valid data succeeds."""
      response = client.post('/teachers', json={"name": "John Doe", "email": "john.doe@example.com"})
      assert response.status_code == 200
      assert response.get_json()['name'] == "John Doe"
  ```

---

## 7. Testing Implementation for Teacher Retrieval

- [ ] **Task**: Create tests for retrieving Teacher details in `tests/test_routes.py`  
 **File**: `tests/test_routes.py`  
  **Description**: Add unit tests to verify retrieval of Teacher details by ID, ensuring the correct JSON structure is returned.  
  **Sample Test**:
  ```python
  def test_get_teacher_details(client):
      """Test fetching details of a specific teacher."""
      client.post('/teachers', json={"name": "John Doe", "email": "john.doe@example.com"})
      response = client.get('/teachers/1')
      assert response.status_code == 200
      assert response.get_json()['name'] == "John Doe"
  ```

---

## 8. Testing Implementation for Teacher Model

- [ ] **Task**: Create tests for the Teacher model in `tests/test_models.py`  
  **File**: `tests/test_models.py`  
  **Description**: Add tests to verify the creation of a Teacher instance validates the fields correctly and satisfies constraints like unique email requirements.

---

## 9. Update Documentation

- [ ] **Task**: Update `README.md` to include new API endpoints and usage for Teacher management  
  **File**: `README.md`  
  **Description**: Document the new `POST /teachers` and `GET /teachers/{teacher_id}` endpoints, including request/response formats and examples.

---

## 10. Configuration Management

- [ ] **Task**: Update configuration settings and add new environment variables if necessary  
  **File**: `.env.example`  
  **Description**: Ensure the example config reflects any new settings required for the Teacher entity, such as database configurations or new environment variables.

---

This task breakdown provides a structured approach to implementing the Create Teacher Entity feature, ensuring each file is independently focused and testing can occur at every level.