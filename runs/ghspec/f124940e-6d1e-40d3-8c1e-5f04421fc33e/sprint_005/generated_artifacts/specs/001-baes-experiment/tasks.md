# Tasks: Create Teacher Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- src/models.py
- src/database.py
- src/main.py
- tests/test_student_courses.py

---

## Task 1: Update `models.py` for Teacher Entity
- **File**: `src/models.py`
- **Description**: Add the `Teacher` model to define the database schema for the teacher entity.
- **Implementation**:
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
- **Testing**: Ensure the model passes basic integrity checks.
- [ ] Task complete.

## Task 2: Create Migration Script for Teachers Table
- **File**: `migrations/versions/` (create new migration file)
- **Description**: Write an Alembic migration script to create the `teachers` table in the database.
- **Implementation**:
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
- **Testing**: Run migration to verify the `teachers` table is created without errors.
- [ ] Task complete.

## Task 3: Update `main.py` to Include Router
- **File**: `src/main.py`
- **Description**: Import and include the teacher router to handle teacher-related endpoints.
- **Implementation**:
  ```python
  from fastapi import FastAPI
  from routers.teachers_router import router as teachers_router

  app = FastAPI()

  app.include_router(teachers_router, prefix="/teachers", tags=["teachers"])
  ```
- **Testing**: Confirm that the FastAPI app is running and the router is included.
- [ ] Task complete.

## Task 4: Create Teachers Router
- **File**: `src/routers/teachers_router.py`
- **Description**: Implement the API endpoints for creating and retrieving teachers, including input validation.
- **Implementation**:
  ```python
  from fastapi import APIRouter, HTTPException, Depends
  from pydantic import BaseModel
  from sqlalchemy.orm import Session
  from .models import Teacher
  from .database import get_db

  router = APIRouter()

  class TeacherCreate(BaseModel):
      name: str
      email: str

  @router.post("/", response_model=TeacherCreate)
  def create_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
      db_teacher = db.query(Teacher).filter(Teacher.email == teacher.email).first()
      if db_teacher:
          raise HTTPException(status_code=400, detail="Email already registered")
      
      new_teacher = Teacher(name=teacher.name, email=teacher.email)
      db.add(new_teacher)
      db.commit()
      db.refresh(new_teacher)
      return new_teacher

  @router.get("/{teacher_id}", response_model=TeacherCreate)
  def read_teacher(teacher_id: int, db: Session = Depends(get_db)):
      teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
      if teacher is None:
          raise HTTPException(status_code=404, detail="Teacher not found")
      return teacher

  @router.get("/", response_model=List[TeacherCreate])
  def get_teachers(db: Session = Depends(get_db)):
      return db.query(Teacher).all()
  ```
- **Testing**: Ensure the endpoints work without error; further tests will be done in the next task.
- [ ] Task complete.

## Task 5: Write Unit Tests for Teacher Functionality
- **File**: `tests/test_teachers.py`
- **Description**: Create unit tests to cover the functionalities of creating, retrieving, and listing teachers.
- **Implementation**:
  ```python
  import pytest
  from fastapi.testclient import TestClient
  from src.main import app 

  client = TestClient(app)

  def test_create_teacher():
      response = client.post("/teachers", json={"name": "John Doe", "email": "john@example.com"})
      assert response.status_code == 201
      assert response.json()["name"] == "John Doe"

  def test_get_teacher():
      response = client.get("/teachers/1")
      assert response.status_code == 200
      assert response.json()["id"] == 1

  def test_get_all_teachers():
      response = client.get("/teachers")
      assert response.status_code == 200
      assert isinstance(response.json(), list)

  def test_create_teacher_missing_fields():
      response = client.post("/teachers", json={"email": "john@example.com"})
      assert response.status_code == 400
      assert response.json()["error"]["code"] == "E001"
  ```
- **Testing**: Run tests to confirm all functionalities for teacher management are covered.
- [ ] Task complete.

## Task 6: Update Documentation
- **File**: `README.md`
- **Description**: Document the new API endpoints related to teacher management in the project README.
- **Implementation**:
  - Add a section for `Teacher Management API` with details of all endpoints.
- **Testing**: Ensure all documentation is clear and up to date.
- [ ] Task complete.

## Task 7: Implement Input Validation Logic
- **File**: `src/routers/teachers_router.py`
- **Description**: Ensure validation is in place to check for missing fields during teacher creation.
- **Implementation**: This is already included in Task 4, but ensure that proper error messages are raised.
- **Testing**: Validate that the application correctly identifies missing fields.
- [ ] Task complete.

## Task 8: Final Integration Testing
- **File**: All relevant service files tested via the main app
- **Description**: Running the entire application to ensure all pieces interact as expected.
- **Testing**: Start the application and use a tool like Postman to test the endpoints thoroughly.
- [ ] Task complete.

## Task 9: Review Code and Merge
- **File**: All modified files
- **Description**: Review all code changes for quality, adherence to coding standards, and ensure functionality meets requirements.
- **Testing**: Manual review and potential automated checks against the code repository.
- [ ] Task complete.

---

This structured task breakdown allows for independent implementation and testing of the new Teacher entity functionality while maintaining consistency with the existing code style and patterns. Each task is clearly defined to ensure focused development efforts.