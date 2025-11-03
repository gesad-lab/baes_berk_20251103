# Tasks: Create Teacher Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `tests/test_student_course.py` (2600 bytes)

---

## Task Breakdown

### Task 1: Create Teacher Model
- **File**: `src/models/teacher.py`
- **Description**: Implement the `Teacher` SQLAlchemy model representing the `teachers` table in the database.
- **Dependencies**: None
- **Dependencies**: Ensure the database setup is functional.
- **Testable**: Validate that the model is correctly defined using a database migration test.

```python
from sqlalchemy import Column, Integer, String
from database import Base

class Teacher(Base):
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
```

- [ ] Implement Teacher model

---

### Task 2: Create Migration Script for Teacher Table
- **File**: `src/migrations/2023_10_01_create_teacher_table.py`
- **Description**: Create a migration file to add the `teachers` table to the database without affecting existing data.
- **Dependencies**: Task 1
- **Testable**: Run migration and verify the `teachers` table is created successfully.

```python
def upgrade():
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False, unique=True)
    )

def downgrade():
    op.drop_table('teachers')
```

- [ ] Create migration script

---

### Task 3: Implement Data Access Layer for Teacher
- **File**: `src/repositories/teacher_repository.py`
- **Description**: Develop repository methods for creating and retrieving Teachers, including email uniqueness checks.
- **Dependencies**: Task 1
- **Testable**: Test the repository functionality with unit tests that check for both creation and retrieval of Teacher entities.

```python
from sqlalchemy.orm import Session
from models.teacher import Teacher

def create_teacher(db: Session, name: str, email: str):
    new_teacher = Teacher(name=name, email=email)
    db.add(new_teacher)
    db.commit()
    db.refresh(new_teacher)
    return new_teacher

def get_teacher(db: Session, teacher_id: int):
    return db.query(Teacher).filter(Teacher.id == teacher_id).first()
```

- [ ] Implement teacher repository

---

### Task 4: Implement Service Layer Logic for Teacher
- **File**: `src/services/teacher_service.py`
- **Description**: Add service functions to manage business logic surrounding Teacher creation and retrieval.
- **Dependencies**: Task 3
- **Testable**: Validate that service logic correctly processes input and checks for duplication before persisting the data.

```python
from sqlalchemy.orm import Session
from .repositories.teacher_repository import create_teacher, get_teacher

def create_teacher_service(db: Session, name: str, email: str):
    existing_teacher = get_teacher_by_email(db, email)
    if existing_teacher:
        raise ValueError("Email already exists.")
    return create_teacher(db, name, email)
```

- [ ] Implement teacher service

---

### Task 5: Define API Route Handlers
- **File**: `src/main.py`
- **Description**: Set up the API routes for creating and retrieving Teacher entities.
- **Dependencies**: Task 4
- **Testable**: Ensure the API endpoints respond correctly using integration tests.

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .services.teacher_service import create_teacher_service  # Import your service function

app = FastAPI()

class TeacherRequest(BaseModel):
    name: str
    email: str

@app.post("/api/v1/teachers")
def create_teacher_endpoint(request: TeacherRequest):
    try:
        teacher = create_teacher_service(db, request.name, request.email)
        return {"message": "Teacher created successfully.", "id": teacher.id}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
```

- [ ] Define API routes for Teacher

---

### Task 6: Implement Input Validation
- **File**: Integrated into API route handlers in `src/main.py`
- **Description**: Implement validation to ensure fields are provided and return appropriate error messages.
- **Dependencies**: Task 5
- **Testable**: Use integration tests to ensure validation is handled correctly for creation requests.

- [ ] Implement input validation in the API

---

### Task 7: Write Unit and Integration Tests
- **File**: `tests/test_teacher.py`
- **Description**: Create tests for the Teacher entity's CRUD operations, ensuring at least 70% coverage, focusing on creating and retrieving Teachers.
- **Dependencies**: Task 1-6
- **Testable**: Run tests to confirm functionality and ensure error cases are handled correctly.

```python
def test_create_teacher_success():
    response = client.post("/api/v1/teachers", json={"name": "Jane Doe", "email": "jane.doe@example.com"})
    assert response.status_code == 201
    assert "id" in response.json()

def test_create_teacher_duplicate_email():
    client.post("/api/v1/teachers", json={"name": "John", "email": "john.doe@example.com"})
    response = client.post("/api/v1/teachers", json={"name": "Johnny", "email": "john.doe@example.com"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Email already exists."}}
```

- [ ] Write tests for Teacher functionality

---

### Task 8: Document API in README.md
- **File**: `README.md`
- **Description**: Update the README file to include information about the new Teacher API endpoints, including request/response formats.
- **Dependencies**: Task 5
- **Testable**: Self-review to ensure accuracy and clarity in the documentation.

- [ ] Document API endpoints in README.md

---

### Task 9: Health Check Endpoint
- **File**: `src/main.py`
- **Description**: Implement a health check endpoint to return the API’s operational status.
- **Dependencies**: Task 5
- **Testable**: Validate the response format when hit endpoint.

```python
@app.get("/health")
def health_check():
    return {"status": "ok"}
```

- [ ] Implement health check endpoint

---

In summary, this task breakdown clearly outlines each step to implement the Teacher entity functionality including code and tests while maintaining the integrity and quality of the existing system.