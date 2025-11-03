# Tasks: Create Teacher Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- api/enrollment.py (2242 bytes)
- api/models/enrollment.py (534 bytes)
- tests/api/test_enrollment.py (2698 bytes)
- tests/integration/test_data_migration.py (2390 bytes)
- tests/integration/test_enrollment_integration.py (1753 bytes)

## Task Breakdown

### Database Migration

- [ ] **Task 1**: Create migration script to add Teacher table  
  **File**: `migrations/20231007_add_teacher_table.py`  
  ```python
  async def migrate():
      async with aiosqlite.connect("database.db") as db:
          await db.execute("""
              CREATE TABLE IF NOT EXISTS teacher (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,
                  email TEXT NOT NULL UNIQUE
              )
          """)
          await db.commit()
  ```

### API Module

- [ ] **Task 2**: Create API endpoints for Teacher entity CRUD operations  
  **File**: `api/teachers.py`  
  ```python
  from fastapi import APIRouter, HTTPException
  from .models.teachers import TeacherCreateRequest, TeacherResponse
  import aiosqlite

  router = APIRouter()

  @router.post("/teachers", response_model=TeacherResponse)
  async def create_teacher(teacher: TeacherCreateRequest):
      async with aiosqlite.connect("database.db") as db:
          cursor = await db.execute("INSERT INTO teacher (name, email) VALUES (?, ?)",
                                     (teacher.name, teacher.email))
          await db.commit()
          teacher_id = cursor.lastrowid
          return TeacherResponse(id=teacher_id, name=teacher.name, email=teacher.email)

  @router.get("/teachers", response_model=list[TeacherResponse])
  async def list_teachers():
      async with aiosqlite.connect("database.db") as db:
          cursor = await db.execute("SELECT id, name, email FROM teacher")
          teachers = await cursor.fetchall()
          return [TeacherResponse(id=row[0], name=row[1], email=row[2]) for row in teachers]
  ```

### Models

- [ ] **Task 3**: Create Pydantic models for Teacher entity  
  **File**: `api/models/teachers.py`  
  ```python
  from pydantic import BaseModel, EmailStr, Field

  class TeacherCreateRequest(BaseModel):
      name: str = Field(..., min_length=1, example="John Doe")
      email: EmailStr = Field(..., example="john.doe@example.com")

  class TeacherResponse(BaseModel):
      id: int
      name: str
      email: EmailStr

      class Config:
          schema_extra = {
              "example": {
                  "id": 1,
                  "name": "John Doe",
                  "email": "john.doe@example.com"
              }
          }
  ```

### Tests

- [ ] **Task 4**: Create unit tests for Teacher entity API  
  **File**: `tests/api/test_teachers.py`  
  ```python
  import pytest
  from fastapi.testclient import TestClient
  from api.teachers import app  

  client = TestClient(app)

  def test_create_teacher_with_valid_data():
      response = client.post("/teachers", json={"name": "John Doe", "email": "john.doe@example.com"})
      assert response.status_code == 201

  def test_create_teacher_with_invalid_email():
      response = client.post("/teachers", json={"name": "Jane Doe", "email": "jane.doe"})
      assert response.status_code == 400
  ```

- [ ] **Task 5**: Create integration tests for Teacher table migration  
  **File**: `tests/integration/test_migration.py`  
  ```python
  from fastapi.testclient import TestClient
  from main import app  # Assuming main.py is where FastAPI app is initialized

  client = TestClient(app)

  def test_teacher_table_migration():
      response = client.get("/teachers")
      assert response.status_code == 200  # Test retrieval of a list of teachers
  ```

### Documentation

- [ ] **Task 6**: Update README.md with Teacher API endpoint documentation  
  **File**: `README.md`  
  ```markdown
  ## Teacher API Endpoints

  ### Create Teacher
  - **POST /teachers**
  - **Request Body**:
    ```json
    {
        "name": "string",
        "email": "string"
    }
    ```
  - **Responses**:
    - 201 Created: On successful creation of a teacher
    - 400 Bad Request: If input validation fails
  ```

### Integration with Existing Operations

- [ ] **Task 7**: Ensure that the new Teacher table functionally integrates with existing Student and Course records without disruption.  
  **File**: Update necessary integration files where referenced.

### Final Steps

- [ ] **Task 8**: Execute migration and test to ensure successful implementation  
  **File**: Execute in command line to inspect database state and application logs.

This breakdown ensures that tasks are manageable, focused on single file operations adhering to required specifications, and ready for independent testing before integration.