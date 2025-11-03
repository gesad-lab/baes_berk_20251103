# Tasks: Create Teacher Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `src/main.py`
- `src/models/student.py`
- `src/db/database.py`
- `src/routes/student_routes.py`
- `tests/test_student.py`

---

## Task Breakdown

### 1. **Database Schema Setup**
- [ ] **Create Teacher Model**  
  - **File**: `src/models/teacher.py`  
  - Create the SQLAlchemy model for the Teacher entity.
  
```python
from sqlalchemy import Column, Integer, String
from db.database import Base

class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
```

### 2. **Database Migration**
- [ ] **Add Migration Script**  
  - **File**: `src/db/migrations/create_teacher_table.py`  
  - Create migration script with Alembic to add the new `teachers` table.
  
```python
from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table('teachers',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False))

def downgrade():
    op.drop_table('teachers')
```

### 3. **Route Creation**
- [ ] **Implement Teacher Routes**  
  - **File**: `src/routes/teacher_routes.py`  
  - Define API endpoints for creating, retrieving, updating, and deleting teachers.

```python
from fastapi import APIRouter
from src.services.teacher_service import TeacherService
from src.schemas.teacher_schemas import TeacherCreate, TeacherResponse

router = APIRouter()

@router.post("/teachers", response_model=TeacherResponse)
async def create_teacher(teacher: TeacherCreate):
    return await TeacherService.create_teacher(teacher)

@router.get("/teachers/{teacher_id}", response_model=TeacherResponse)
async def get_teacher(teacher_id: int):
    return await TeacherService.get_teacher(teacher_id)

@router.put("/teachers/{teacher_id}", response_model=TeacherResponse)
async def update_teacher(teacher_id: int, teacher: TeacherCreate):
    return await TeacherService.update_teacher(teacher_id, teacher)

@router.delete("/teachers/{teacher_id}")
async def delete_teacher(teacher_id: int):
    return await TeacherService.delete_teacher(teacher_id)
```

### 4. **Service Logic**
- [ ] **Create Teacher Service**  
  - **File**: `src/services/teacher_service.py`  
  - Implement all business logic for CRUD operations related to the Teacher.

```python
class TeacherService:
    @staticmethod
    async def create_teacher(teacher_data):
        # logic to save teacher_data in the database

    @staticmethod
    async def get_teacher(teacher_id):
        # logic to retrieve teacher by ID

    @staticmethod
    async def update_teacher(teacher_id, teacher_data):
        # logic to update teacher information

    @staticmethod
    async def delete_teacher(teacher_id):
        # logic to delete teacher by ID
```

### 5. **Schema Creation**
- [ ] **Define Teacher Schemas**  
  - **File**: `src/schemas/teacher_schemas.py`  
  - Create Pydantic models for request and response validation of Teacher operations.

```python
from pydantic import BaseModel

class TeacherCreate(BaseModel):
    name: str
    email: str

class TeacherResponse(TeacherCreate):
    id: int
```

### 6. **Integrate Teacher Routes**
- [ ] **Update Main Application**  
  - **File**: `src/main.py`  
  - Import and include new teacher routes in the main FastAPI app.

```python
from fastapi import FastAPI
from src.routes.teacher_routes import router as teacher_router

app = FastAPI()

app.include_router(teacher_router)
```

### 7. **Testing Implementation**
- [ ] **Create Teacher Tests**  
  - **File**: `tests/test_teacher.py`  
  - Implement unit and integration tests for Teacher functionalities.

```python
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_create_teacher():
    response = client.post("/teachers", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201
    assert response.json()['data']['name'] == "John Doe"

def test_get_teacher():
    response = client.get("/teachers/1")
    assert response.status_code == 200
```

### 8. **Documentation**
- [ ] **Update API Documentation**  
  - **File**: `README.md`  
  - Ensure README includes instructions on the new Teacher entity and how to interact with the API.

### 9. **Migration Testing**
- [ ] **Test Database Migration**  
  - **File**: N/A  
  - Validate that the migration script correctly creates the Teacher table in a local testing environment.

### 10. **Create Sample Data for Testing**
- [ ] **Add Sample Data**  
  - **File**: `tests/test_db_setup.py`  
  - Create fixtures for the database with initial sample teacher data for integration testing.

```python
@pytest.fixture(autouse=True)
def setup_database():
    # Initialize the database and add sample teachers before each test
```

---

Each task is designed to be independent and testable within its own scope, ensuring that the feature is implemented successfully and efficiently while adhering to the project's coding standards.