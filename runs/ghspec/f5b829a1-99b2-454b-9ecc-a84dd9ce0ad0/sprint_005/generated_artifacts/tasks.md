# Tasks: Create Teacher Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `src/main.py` (2450 bytes)
- `src/models.py` (1020 bytes)
- `src/services/teacher_service.py` (975 bytes)
- `tests/api/test_routes.py` (3455 bytes)
- `tests/services/test_teacher_service.py` (new file)

---

### Task 1: Create Teacher Model

- **File**: `src/models.py`
- **Description**: Implement the `Teacher` SQLAlchemy model as per the outlined structure.
- **Checklist**:
  - [ ] Add `Teacher` class definition to `models.py`.
  - [ ] Create fields: `id`, `name`, `email` with appropriate types and constraints.
  
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

---

### Task 2: Create Teacher Service Logic

- **File**: `src/services/teacher_service.py`
- **Description**: Implement the `TeacherService` class with a method to create a teacher.
- **Checklist**:
  - [ ] Define `TeacherService` class in `teacher_service.py`.
  - [ ] Implement `create_teacher(name: str, email: str)` method with input validation.
  - [ ] Handle logic for throwing errors on missing fields and checking email uniqueness.

```python
class TeacherService:
    def create_teacher(self, name: str, email: str):
        if not name:
            raise ValueError("Name is required.")
        if not email:
            raise ValueError("Email is required.")
        # Further validation and creation logic goes here.
```

---

### Task 3: Add API Endpoint for Creating Teachers

- **File**: `src/main.py`
- **Description**: Create the `POST /teachers` route in the FastAPI application.
- **Checklist**:
  - [ ] Import necessary methods from `teacher_service.py`.
  - [ ] Add route to handle teacher creation requests.
  - [ ] Ensure appropriate HTTP status responses and error handling.

---

### Task 4: Create Database Migration for Teacher Table

- **File**: `migrations/versions/xxx_create_teachers_table.py` (new file)
- **Description**: Create a migration script to add the `teachers` table to the database.
- **Checklist**:
  - [ ] Implement upgrade and downgrade functions in the migration file.
  - [ ] Test migration to ensure it runs successfully and preserves existing data.

```python
def upgrade():
    op.create_table(
        'teachers',
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('name', String, nullable=False),
        Column('email', String, nullable=False, unique=True)
    )

def downgrade():
    op.drop_table('teachers')
```

---

### Task 5: Create Tests for Teacher Endpoint

- **File**: `tests/api/test_routes.py`
- **Description**: Add tests for the new API endpoint, validating success and error cases.
- **Checklist**:
  - [ ] Write tests for successful teacher creation.
  - [ ] Write tests for missing required fields (name and email).
  - [ ] Ensure that valid email formats are checked.

---

### Task 6: Create Unit Tests for Teacher Service

- **File**: `tests/services/test_teacher_service.py` (new file)
- **Description**: Write unit tests for the `TeacherService` methods.
- **Checklist**:
  - [ ] Test `create_teacher` for valid input.
  - [ ] Test for errors on missing name and email.
  - [ ] Implement test for handling and confirming unique email logic.

---

### Task 7: Update API Documentation

- **File**: `docs/api.md` or equivalent
- **Description**: Document the new API endpoint for creating a teacher.
- **Checklist**:
  - [ ] Add details about the `POST /teachers` endpoint.
  - [ ] Include request and response formats.
  - [ ] Document potential error responses.

---

### Task 8: Run Migrations and Validate Application

- **File**: N/A
- **Description**: Execute the database migration and check application integrity.
- **Checklist**:
  - [ ] Run migration scripts to add the `teachers` table.
  - [ ] Ensure existing Student and Course data is unaffected.
  - [ ] Verify that the application starts successfully with no errors.

---

By following these tasks, we will successfully implement the `Teacher` entity while maintaining adherence to coding standards and ensuring test coverage for the new functionality.