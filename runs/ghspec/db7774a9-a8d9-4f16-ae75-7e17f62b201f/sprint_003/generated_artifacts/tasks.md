# Tasks: Create Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `tests/test_student.py` (2182 bytes)

Instructions for Task Breakdown:
1. Identify which existing files need modifications
2. Create new files for new functionality
3. Ensure integration tasks are included
4. Maintain consistency with existing code style and patterns

---

## Tasks Breakdown

- [ ] **Create Course Model**  
  Create a file for the `Course` entity model.  
  **File**: `src/models/course.py`  
  ```python
  from sqlalchemy import Column, Integer, String
  from database import Base

  class Course(Base):
      __tablename__ = 'courses'
      
      id = Column(Integer, primary_key=True, index=True)
      name = Column(String, index=True, nullable=False)
      level = Column(String, index=True, nullable=False)
  ```

- [ ] **Create Pydantic Schema for Course**  
  Define the Pydantic schema for validation of the `Course` data.  
  **File**: `src/schemas/course.py`  
  ```python
  from pydantic import BaseModel, constr

  class CourseCreate(BaseModel):
      name: constr(min_length=1)  # Ensure name is a non-empty string
      level: constr(min_length=1)  # Ensure level is a non-empty string

  class CourseResponse(BaseModel):
      id: int
      name: str
      level: str
      
      class Config:
          orm_mode = True
  ```

- [ ] **Create Course Service Logic**  
  Implement service functions for handling business logic related to courses.  
  **File**: `src/services/course_service.py`  
  ```python
  from models.course import Course
  from schemas.course import CourseCreate
  from database import get_db
  from sqlalchemy.orm import Session

  def create_course(course: CourseCreate, db: Session):
      db_course = Course(name=course.name, level=course.level)
      db.add(db_course)
      db.commit()
      db.refresh(db_course)
      return db_course
  ```

- [ ] **Create Course Routes**  
  Implement routes for course API endpoints to handle CRUD operations.  
  **File**: `src/routes/course_routes.py`  
  ```python
  from fastapi import APIRouter, Depends, HTTPException
  from sqlalchemy.orm import Session
  from services.course_service import create_course
  from schemas.course import CourseCreate, CourseResponse
  from database import get_db

  router = APIRouter()

  @router.post("/courses", response_model=CourseResponse, status_code=201)
  def create_new_course(course: CourseCreate, db: Session = Depends(get_db)):
      return create_course(course, db)

  @router.get("/courses/{id}", response_model=CourseResponse)
  def get_course(id: int, db: Session = Depends(get_db)):
      course = db.query(Course).filter(Course.id == id).first()
      if not course:
          raise HTTPException(status_code=404, detail="Course not found")
      return course

  @router.get("/courses", response_model=list[CourseResponse])
  def list_courses(db: Session = Depends(get_db)):
      return db.query(Course).all()
  ```

- [ ] **Update Main Application to Include Course Routes**  
  Integrate the course routes into the FastAPI application main file.  
  **File**: `src/main.py`  
  ```python
  from fastapi import FastAPI
  from routes.student_routes import router as student_router
  from routes.course_routes import router as course_router

  app = FastAPI()

  app.include_router(student_router)
  app.include_router(course_router)
  ```

- [ ] **Create Database Migration for Course Table**  
  Modify the database schema to include the new `courses` table.  
  **File**: `src/database/database.py` (Add necessary migration logic)  

- [ ] **Create Tests for Course Functionality**  
  Implement tests for creating, retrieving, and listing courses including error handling cases.  
  **File**: `tests/test_course.py`  
  ```python
  import pytest
  from fastapi.testclient import TestClient
  from src.main import app

  client = TestClient(app)

  def test_create_course():
      """Test creating a course with valid name and level."""
      response = client.post("/courses", json={"name": "Math 101", "level": "Beginner"})
      assert response.status_code == 201
      assert "id" in response.json()
      assert response.json()["name"] == "Math 101"
      assert response.json()["level"] == "Beginner"

  def test_create_course_missing_name():
      """Test creating a course without a name should fail."""
      response = client.post("/courses", json={"level": "Beginner"})
      assert response.status_code == 422
  ```

- [ ] **Update README Documentation**  
  Add details about the new Course entity, including API endpoint specifics.  
  **File**: `README.md`  

---

This task breakdown provides clear, actionable steps to implement the `Course` entity while maintaining a focus on ensuring integration with existing features and code styles.