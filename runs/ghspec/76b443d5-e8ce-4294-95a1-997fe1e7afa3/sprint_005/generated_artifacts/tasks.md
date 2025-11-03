# Tasks: Create Teacher Entity

---

## INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `tests/test_enrollments.py` (1856 bytes)

---

### Task Breakdown

- [ ] **Task 1:** Create Teacher Model  
  **File:** `src/models/teacher.py`  
  **Description:** Implement the Teacher data model in the system as per the specifications.  
  ```python
  from sqlalchemy import Column, Integer, String
  from sqlalchemy.ext.declarative import declarative_base

  Base = declarative_base()

  class Teacher(Base):
      __tablename__ = 'teachers'

      id = Column(Integer, primary_key=True, autoincrement=True)
      name = Column(String, nullable=False)
      email = Column(String, nullable=False, unique=True)
  ```  

- [ ] **Task 2:** Create Database Migration for Teacher Table  
  **File:** `migrations/versions/<timestamp>_add_teachers_table.py`  
  **Description:** Use Alembic to create a migration script that adds the teachers table schema.  
  ```python
  from alembic import op
  import sqlalchemy as sa

  def upgrade():
      op.create_table(
          'teachers',
          sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
          sa.Column('name', sa.String, nullable=False),
          sa.Column('email', sa.String, nullable=False, unique=True)
      )

  def downgrade():
      op.drop_table('teachers')
  ```

- [ ] **Task 3:** Implement Create Teacher API Endpoint  
  **File:** `src/api/teachers.py`  
  **Description:** Develop the POST endpoint `/teachers` for creating a new Teacher.  
  ```python
  from fastapi import APIRouter, HTTPException
  from pydantic import BaseModel, EmailStr
  from src.models.teacher import Teacher

  router = APIRouter()

  class TeacherCreateRequest(BaseModel):
      name: str
      email: EmailStr

      @validator('name', always=True)
      def check_name(cls, v):
          if not v:
              raise ValueError('Name field is required.')
          return v

  @router.post("/teachers", response_model=Teacher)
  async def create_teacher(teacher: TeacherCreateRequest):
      # Logic to save teacher in DB
      pass
  ```

- [ ] **Task 4:** Implement Retrieve Teacher API Endpoint  
  **File:** `src/api/teachers.py`  
  **Description:** Develop the GET endpoint `/teachers/{teacherId}` to fetch a Teacher's details by ID.  
  ```python
  @router.get("/teachers/{teacher_id}")
  async def get_teacher(teacher_id: int):
      # Logic to get teacher from DB or raise HTTP 404
      pass
  ```

- [ ] **Task 5:** Update Application Startup to Apply Migrations  
  **File:** `src/main.py`  
  **Description:** Ensure the application applies database migrations at startup.  
  ```python
  @app.on_event("startup")
  async def startup():
      alembic_cfg = Config("alembic.ini")
      command.upgrade(alembic_cfg, "head")
  ```

- [ ] **Task 6:** Create Unit Tests for Teacher Entity  
  **File:** `tests/test_teachers.py`  
  **Description:** Write tests for Teacher creation and retrieval as well as error cases.  
  ```python
  import pytest
  from fastapi.testclient import TestClient
  from src.main import app

  @pytest.fixture
  def client():
      with TestClient(app) as client:
          yield client

  def test_create_teacher(client):
      response = client.post("/teachers", json={"name": "John Doe", "email": "john.doe@example.com"})
      assert response.status_code == 201

  def test_create_teacher_missing_name(client):
      response = client.post("/teachers", json={"email": "john.doe@example.com"})
      assert response.status_code == 400

  def test_create_teacher_invalid_email(client):
      response = client.post("/teachers", json={"name": "John Doe", "email": "invalid-email"})
      assert response.status_code == 400

  def test_get_teacher_details(client):
      response = client.get("/teachers/1")
      assert response.status_code == 200

  def test_get_teacher_not_found(client):
      response = client.get("/teachers/9999")
      assert response.status_code == 404
  ```

- [ ] **Task 7:** Update README File  
  **File:** `README.md`  
  **Description:** Document the new Teacher API endpoints and usage instructions.  
  ```markdown
  ## Teacher Management API
  - POST `/teachers`: Create a new Teacher
  - GET `/teachers/{teacherId}`: Retrieve Teacher details
  ```

---

This task breakdown clearly delineates the individual responsibilities and files, ensuring a structured and maintainable approach to implementing the Teacher entity feature.