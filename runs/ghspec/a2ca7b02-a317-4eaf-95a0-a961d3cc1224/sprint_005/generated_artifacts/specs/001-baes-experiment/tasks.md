# Tasks: Create Teacher Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `tests/test_student.py` (2310 bytes)

---

## Task Breakdown

### Task 1: Create Teacher Model
- **File Path**: `models/teacher.py`
- **Description**: Implement the `Teacher` model to represent the teacher entity with name and email fields, including ORM mappings.
- [ ] Create `models/teacher.py` with the following code:
```python
from sqlalchemy import Column, Integer, String
from db.database import Base

class Teacher(Base):
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
```

### Task 2: Database Migration Script
- **File Path**: `db/migrations/0001_create_teacher_table.sql`
- **Description**: Create a migration script for the new `teachers` table in the database, ensuring it has the necessary fields.
- [ ] Create `db/migrations/0001_create_teacher_table.sql` with the following SQL:
```sql
CREATE TABLE teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
);
```

### Task 3: Update Database Management
- **File Path**: `db/database.py`
- **Description**: Modify the database initialization script to include the Teacher model in the setup process.
- [ ] Update `db/database.py` to ensure the `teachers` table is created:
```python
from models.teacher import Teacher

# In the section that creates tables
Base.metadata.create_all(bind=engine)  # This will also create the teachers table.
```

### Task 4: Create API Endpoints
- **File Path**: `api/teacher.py`
- **Description**: Define the RESTful API endpoints for creating and retrieving Teacher entities using FastAPI.
- [ ] Create `api/teacher.py` with the following code:
```python
from fastapi import APIRouter, HTTPException
from services.teacher_service import TeacherService

router = APIRouter()

@router.post("/teachers")
async def create_teacher(teacher_data: dict):
    return await TeacherService.create_teacher(teacher_data)

@router.get("/teachers/{teacher_id}")
async def retrieve_teacher(teacher_id: int):
    return await TeacherService.get_teacher(teacher_id)
```

### Task 5: Implement Teacher Service Logic
- **File Path**: `services/teacher_service.py`
- **Description**: Develop the business logic to handle the creation and retrieval of teachers.
- [ ] Create `services/teacher_service.py` with the following code:
```python
from models.teacher import Teacher
from db.database import Session
from fastapi import HTTPException

class TeacherService:
    
    @staticmethod
    async def create_teacher(data: dict):
        async with Session() as session:
            teacher = Teacher(name=data['name'], email=data['email'])
            session.add(teacher)
            await session.commit()
            return teacher

    @staticmethod
    async def get_teacher(teacher_id: int):
        async with Session() as session:
            teacher = await session.get(Teacher, teacher_id)
            if not teacher:
                raise HTTPException(status_code=404, detail="Teacher not found")
            return teacher
```

### Task 6: Create Input Validator
- **File Path**: `validators/teacher_validator.py`
- **Description**: Implement validation logic for incoming request data to ensure required fields are present and valid.
- [ ] Create `validators/teacher_validator.py` with the following code:
```python
def validate_teacher_fields(name: str, email: str):
    if not name or not email:
        raise ValueError("Both name and email are required.")
    # Additional checks can be performed for email formatting if needed
```

### Task 7: Implement Tests for Teacher Functionality
- **File Path**: `tests/test_teacher.py`
- **Description**: Define unit and integration tests for the Teacher creation and retrieval functionalities.
- [ ] Create `tests/test_teacher.py` with the following structure:
```python
import pytest
from services.teacher_service import TeacherService

@pytest.fixture
def setup_database():
    # Setup an in-memory SQLite database for testing (implementation needed)
    pass  

def test_create_teacher_valid_data(setup_database):
    # Arrange
    teacher_data = {"name": "Jane Doe", "email": "jane.doe@example.com"}
    
    # Act
    teacher_response = TeacherService.create_teacher(teacher_data)
    
    # Assert
    assert teacher_response.name == "Jane Doe"
    assert teacher_response.email == "jane.doe@example.com"

def test_create_teacher_missing_fields(setup_database):
    # Act & Assert
    with pytest.raises(ValueError):
        TeacherService.create_teacher({"name": "", "email": "jane@example.com"})
```

### Task 8: Documentation Update
- **File Path**: `README.md`
- **Description**: Update the project README to include new API documentation for teacher creation and retrieval.
- [ ] Edit `README.md` to provide clear instructions on the new API endpoints:
```markdown
## API Endpoints

### Create Teacher
- POST `/teachers`
- Request Body:
    ```json
    {
      "name": "Jane Doe",
      "email": "jane.doe@example.com"
    }
    ```

### Retrieve Teacher
- GET `/teachers/{teacher_id}`
```

---

This breakdown provides a clear path for implementing the Create Teacher Entity feature, ensuring modular development and adherence to existing coding standards. Each task is independently testable and updates relevant sections of the codebase.