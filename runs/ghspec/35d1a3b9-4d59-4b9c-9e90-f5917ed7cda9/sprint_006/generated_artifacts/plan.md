# Implementation Plan: Add Teacher Relationship to Course Entity

---

## INCREMENTAL DEVELOPMENT CONTEXT

### Previous Sprint Plan:
# Implementation Plan: Create Teacher Entity

---

## INCREMENTAL DEVELOPMENT CONTEXT

### Previous Sprint Plan:
# Implementation Plan: Add Course Relationship to Student Entity

---

## INCREMENTAL DEVELOPMENT CONTEXT

### Previous Sprint Plan:
# Implementation Plan: Create Course Entity

---

## INCREMENTAL DEVELOPMENT CONTEXT

### Previous Sprint Plan:
# Implementation Plan: Add Email Field to Student Entity

---

## INCREMENTAL DEVELOPMENT CONTEXT

### Previous Sprint Plan:
# Implementation Plan: Student Management Web Application

## I. Architecture Overview

### 1.1 High-Level Architecture
The architecture will expand to include a new reference from the **Course** entity to the **Teacher** entity. The updated architecture will include:
- **API Layer**: New endpoints for assigning teachers to courses and for retrieving course details including teacher information.
- **Service Layer**: Business logic to facilitate the relationship management between courses and teachers.
- **Data Access Layer (DAL)**: Modifications to manage course assignments and implement required database migrations.

### 1.2 Technology Stack
- **Programming Language**: Python
- **Framework**: FastAPI for the API layer.
- **Database**: SQLite for persistence.
- **ORM**: SQLAlchemy for database interactions.
- **Testing Tool**: pytest for unit and integration testing.
- **Documentation Tool**: Swagger UI (automatically generated with FastAPI).
- **Migration Tool**: Alembic for database migrations.

## II. Module Breakdown

### 2.1 Module Overview
1. **API Module** (`src/api/`)
   - New endpoints for assigning teachers to courses and retrieving course details.

2. **Service Module** (`src/services/`)
   - Business logic for assigning teachers to courses and retrieving course information.

3. **Data Access Layer (DAL)** (`src/repository/`)
   - Extend the `Course` model to include a foreign key reference to the `Teacher` model.
   - Implement migration scripts to add the `teacher_id` field to the `courses` table.

4. **Testing Module** (`tests/`)
   - New tests for the teacher-to-course assignment and course retrieval functionalities.

## III. Data Model

### 3.1 Course Model Definition (Modification)
We will update the existing `Course` model to include the `teacher_id` foreign key relationship:
```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)

    teacher = relationship("Teacher", backref="courses")
```

### 3.2 Teacher Model Definition
Previously defined `Teacher` model remains unchanged:
```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Teacher(Base):
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
```

## IV. API Contracts

### 4.1 API Endpoints
#### 1. Assign a Teacher to a Course
- **Endpoint**: `POST /api/v1/courses/{course_id}/assign_teacher`
- **Request Body**:
    ```json
    {
      "teacher_id": 1
    }
    ```
- **Response**:
  - **Status Code**: 200 OK
  - **Body**:
    ```json
    {
      "message": "Teacher assigned to course successfully"
    }
    ```

#### 2. Retrieve Course Details Including Teacher
- **Endpoint**: `GET /api/v1/courses/{id}`
- **Response**:
  - **Status Code**: 200 OK
  - **Body**:
    ```json
    {
      "id": 1,
      "name": "Math 101",
      "level": "Beginner",
      "teacher": {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com"
      }
    }
    ```

## V. Implementation Approach

### 5.1 Database Migration
Use Alembic to create a migration script to add the new `teacher_id` column to the `courses` table:
```python
# Alembic Migration Script
from alembic import op
import sqlalchemy as sa

def upgrade():
    op.add_column('courses', sa.Column('teacher_id', sa.Integer, sa.ForeignKey('teachers.id'), nullable=True))

def downgrade():
    op.drop_column('courses', 'teacher_id')
```

### 5.2 Error Handling
- Implement input validation using Pydantic models in FastAPI for routes.
- Validate that both the course ID and teacher ID are valid.
- Return appropriate error messages for validation failures.

### 5.3 Dependency Management
- Update `requirements.txt` to include packages:
    ```
    fastapi
    uvicorn
    sqlalchemy
    alembic
    pytest
    ```

## VI. Testing Strategy

### 6.1 Test Coverage
- Implement unit tests for the new API endpoint for assigning teachers to courses and for retrieving course information.
- Ensure coverage targets are met: minimum 70% for new functionalities, with critical paths achieving 90%+ coverage.

### 6.2 Test Organization
Structure test files to mirror the source code layout:
```
tests/
│
├── api/
│   ├── test_teacher_assignment.py  # New test suite for course-teacher assignment API endpoints
│   └── test_course_retrieval.py    # Test suite for course retrieval including teacher
│
└── services/
    └── test_course_service.py       # Test suite for course service logic
```

### 6.3 Example Test Cases
- `test_assign_teacher_to_course_with_valid_data_succeeds()`: Validates assigning a teacher to a course successfully.
- `test_retrieve_course_with_teacher_information_returns_correct_data()`: Checks if retrieving a course returns the correct data structure and details.

## VII. Environment Configuration

### 7.1 Environment Variables
- Ensure database URI can be configured via environment variables using a `.env` file.

### 7.2 Configuration Example
```env
DATABASE_URL=sqlite:///./test.db
```

## VIII. Deployment Considerations

### 8.1 Production Readiness
- Test migration scripts to ensure they function without errors before deployment.
- Implement health check endpoints to monitor API availability and functionalities.

### 8.2 Backward Compatibility
- The addition of the `teacher_id` field will not affect existing `students` or `courses` tables, ensuring current functionalities remain intact.

## IX. Future Considerations

- Explore adding features for updating and removing teacher assignments from courses in future iterations.
- Potential developments may include extending administrative functionalities for teacher assignments through the user interface in later sprints.

---
By following this implementation plan, the educational system will successfully incorporate the relationship between the Course and Teacher entities, improving resource management capabilities while ensuring existing features remain operational.