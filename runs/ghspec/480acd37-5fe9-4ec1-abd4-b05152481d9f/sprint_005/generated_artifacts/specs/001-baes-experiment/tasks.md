# Tasks: Create Teacher Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `tests/test_api.py` (3102 bytes)

---

## Task Breakdown

### 1. Database Model Development

- [ ] Update `src/models.py` to define the `Teacher` model.  
  **File Path**: `src/models.py`  
  ```python
  from sqlalchemy import Column, Integer, String
  from sqlalchemy.ext.declarative import declarative_base

  Base = declarative_base()

  class Teacher(Base):
      __tablename__ = 'teachers'

      id = Column(Integer, primary_key=True, index=True, autoincrement=True)
      name = Column(String, nullable=False)
      email = Column(String, nullable=False, unique=True)
  ```

### 2. Data Validation Schema

- [ ] Create `src/schemas.py` for Pydantic models to validate teacher creation requests.  
  **File Path**: `src/schemas.py`  
  ```python
  from pydantic import BaseModel, EmailStr

  class TeacherCreate(BaseModel):
      name: str
      email: EmailStr
  ```

### 3. API Endpoint Implementation

- [ ] Implement API endpoints in `src/api.py`: 
  - Create a `POST /teachers` endpoint. 
  - Create a `GET /teachers` endpoint.  
  **File Path**: `src/api.py`  
  ```python
  from fastapi import FastAPI, HTTPException
  from schemas import TeacherCreate
  from models import Teacher
  from database import SessionLocal

  app = FastAPI()

  @app.post("/teachers")
  def create_teacher(teacher: TeacherCreate):
      # Validation and creation logic to be added here
      pass

  @app.get("/teachers")
  def get_teachers():
      # Logic to retrieve teachers
      pass
  ```

### 4. Teacher Creation Logic

- [ ] Implement the business logic for teacher creation within the `POST /teachers` endpoint in `src/api.py`. Ensure that input validation is applied.  
  **File Path**: `src/api.py`  
  ```python
  @app.post("/teachers")
  def create_teacher(teacher: TeacherCreate):
      if not teacher.name or not teacher.email:
          raise HTTPException(status_code=400, detail="Name and email are required.")
      # Further validation logic for unique email
      # Logic to add teacher to the database
  ```

### 5. Database Migration Script

- [ ] Create an Alembic migration script to add the `teachers` table. Ensure the migration script preserves existing data.  
  **File Path**: `migrations/versions/<timestamp>_create_teacher_table.py`  
  ```python
  from alembic import op
  import sqlalchemy as sa

  def upgrade():
      op.create_table(
          'teachers',
          sa.Column('id', sa.Integer, primary_key=True),
          sa.Column('name', sa.String, nullable=False),
          sa.Column('email', sa.String, nullable=False, unique=True),
      )

  def downgrade():
      op.drop_table('teachers')
  ```

### 6. Unit Tests Creation

- [ ] Add unit tests for the teacher creation and retrieval functions in `tests/test_api.py`.  
  **File Path**: `tests/test_api.py`  
  ```python
  def test_create_teacher(client):
      response = client.post("/teachers", json={"name": "John Doe", "email": "john@example.com"})
      assert response.status_code == 201
      assert response.json()["name"] == "John Doe"

  def test_create_teacher_missing_fields(client):
      response = client.post("/teachers", json={"name": "", "email": "john@example.com"})
      assert response.status_code == 400
      assert "required" in response.json()["detail"][0]["msg"]
  ```

### 7. Integration Tests Implementation

- [ ] Write integration tests to validate full end-to-end functionality for both the `POST /teachers` and `GET /teachers` endpoints.  
  **File Path**: `tests/test_api.py`  
  ```python
  def test_get_teachers(client):
      response = client.get("/teachers")
      assert response.status_code == 200
      assert isinstance(response.json(), list)
  ```

### 8. Documentation Update

- [ ] Update the `README.md` to include the new endpoints and provide usage examples.  
  **File Path**: `README.md`  
  ```markdown
  ## API Endpoints

  ### Create Teacher
  - **POST /teachers**
    ```json
    {
      "name": "string",
      "email": "string"
    }
    ```

  ### Fetch Teachers
  - **GET /teachers**
    - Returns a list of all teachers.
  ```

---

All tasks should be executed independently and tested to ensure compliance with the implementation plan.