# Tasks: Create Teacher Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `tests/test_teachers.py` (file to be created)
- `src/models/teacher.py` (file to be created)
- `src/routes/teachers.py` (file to be created)

---

## Task Breakdown

### 1. Project Setup
- [ ] **Task**: Ensure existing FastAPI project structure is maintained.
  - **File**: `src/main.py`
  
### 2. Model Creation
- [ ] **Task**: Create the `Teacher` model.
  - **File**: `src/models/teacher.py`
  - **Content**:
    ```python
    from sqlalchemy import Column, Integer, String
    from sqlalchemy.ext.declarative import declarative_base

    Base = declarative_base()

    class Teacher(Base):
        __tablename__ = 'teachers'
        
        id = Column(Integer, primary_key=True, autoincrement=True)
        name = Column(String(255), nullable=False)
        email = Column(String(255), nullable=False, unique=True)
    ```

### 3. Database Schema Management
- [ ] **Task**: Create an Alembic migration script to add the `Teachers` table.
  - **File**: `migrations/versions/<timestamp>_create_teachers_table.py` (auto-generated path)
  - **Content** (ensure to replace `<timestamp>` based on your migration generation):
    ```python
    def upgrade():
        op.create_table(
            'teachers',
            sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
            sa.Column('name', sa.String(length=255), nullable=False),
            sa.Column('email', sa.String(length=255), nullable=False, unique=True)
        )

    def downgrade():
        op.drop_table('teachers')
    ```

### 4. API Development
- [ ] **Task**: Create a new API router for teachers.
  - **File**: `src/routes/teachers.py`
  - **Content**:
    ```python
    from fastapi import APIRouter, HTTPException, Depends
    from sqlalchemy.orm import Session
    from ..models.teacher import Teacher
    from ..database import get_db
    from pydantic import BaseModel

    router = APIRouter()

    class TeacherCreate(BaseModel):
        name: str
        email: str

    @router.post("/teachers", status_code=201)
    async def create_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
        existing_teacher = db.query(Teacher).filter(Teacher.email == teacher.email).first()
        if existing_teacher:
            raise HTTPException(status_code=400, detail="Email already exists.")
        
        new_teacher = Teacher(name=teacher.name, email=teacher.email)
        db.add(new_teacher)
        db.commit()
        db.refresh(new_teacher)
        return {"message": "Teacher created successfully.", "teacher": {"id": new_teacher.id, "name": new_teacher.name, "email": new_teacher.email}}

    @router.get("/teachers")
    async def get_teachers(db: Session = Depends(get_db)):
        teachers = db.query(Teacher).all()
        return [{'id': t.id, 'name': t.name, 'email': t.email} for t in teachers]
    ```

### 5. Update Main Application
- [ ] **Task**: Integrate the updated teacher router into the main FastAPI application.
  - **File**: `src/main.py`
  - **Content**: 
    ```python
    from fastapi import FastAPI
    from .routes.teachers import router as teacher_router

    app = FastAPI()

    app.include_router(teacher_router)
    ```

### 6. Testing
- [ ] **Task**: Create a test file for the teacher creation and retrieval functionalities.
  - **File**: `tests/test_teachers.py`
  - **Content**:
    ```python
    from fastapi.testclient import TestClient
    from main import app

    client = TestClient(app)

    def test_create_teacher():
        response = client.post("/teachers", json={"name": "John Doe", "email": "john.doe@example.com"})
        assert response.status_code == 201
        assert response.json() == {
            "message": "Teacher created successfully.",
            "teacher": {
                "id": 1,
                "name": "John Doe",
                "email": "john.doe@example.com"
            }
        }

    def test_create_teacher_duplicate_email():
        client.post("/teachers", json={"name": "Jane Smith", "email": "jane.smith@example.com"})
        response = client.post("/teachers", json={"name": "Duplicate", "email": "jane.smith@example.com"})
        assert response.status_code == 400
        assert response.json() == {
            "error": {
                "code": "E001",
                "message": "Email already exists."
            }
        }

    def test_retrieve_teachers():
        response = client.get("/teachers")
        assert response.status_code == 200
        assert isinstance(response.json(), list)
    ```

### 7. Documentation
- [ ] **Task**: Verify FastAPI automatically generates documentation for the new endpoints in Swagger.

### 8. Deployment
- [ ] **Task**: Update Docker configurations if necessary for the migrations.
  - **File**: `Dockerfile` or related Docker configuration files.

### 9. Run Migrations
- [ ] **Task**: Execute migration scripts to ensure the `Teachers` table is created.
  - **File**: Command line for migration.

---

This task breakdown covers all essential steps for implementing the Teacher entity, ensuring alignment with existing architectures and standards. Each task is scoped to drive focused development and testing, concluding with deployment preparedness.