# Implementation Plan: Add Teacher Relationship to Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Teacher Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Course Relationship to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Course Entity

## I. Overview
This document outlines the technical implementation plan for adding a relationship between the Course entity and the Teacher entity in the Student Management Web Application. Establishing this relationship aims to enhance course management by accurately associating teachers with their respective courses.

## II. Architecture
- **Type**: Microservices architecture
- **Components**:
  - **API Service**: Extend current functionalities to manage the association of Teachers with Courses.
  - **Database**: SQLite for storing Course and Teacher data together.

### Component Interaction
1. The API service will interact with the SQLite database to update Course records to include associated Teacher IDs.
2. New RESTful API endpoints will be created to manage Teacher associations with Courses.

## III. Tech Stack
- **Backend Framework**: FastAPI (Python 3.11+)
- **Database**: SQLite (via SQLAlchemy ORM)
- **Serialization**: Pydantic for data validation and serialization
- **Testing Framework**: Pytest for unit and integration testing
- **Environment Management**: Poetry (to manage dependencies)

## IV. Module Boundaries and Responsibilities
### API Service (`api` module)
- Responsible for:
  - Associating a Teacher with an existing Course.
  - Retrieving Course details, including Teacher information.
  - Updating the Course's associated Teacher.

### Database Model (`models` module)
- Update the Course model to include the new field `teacher_id` (Foreign Key to Teacher).

### Validation (`schemas` module)
- Create Pydantic schemas relevant to Course Teacher associations.

## V. Data Models
### Course Model Update
```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, index=True)
    # Existing fields...
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=False)

    teacher = relationship("Teacher", back_populates="courses")
```

### Teacher Model (from previous implementation)
```python
class Teacher(Base):
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

    courses = relationship("Course", back_populates="teacher")
```

### Pydantic Schemas
#### Course Teacher Association Schema
```python
class CourseTeacherAssign(BaseModel):
    teacher_id: int
```

### Course Details Response Schema
```python
class CourseResponse(BaseModel):
    id: int
    name: str
    teacher_id: int
    teacher_name: str
    teacher_email: str
```

## VI. API Contracts
### Endpoints Specification
- **POST /courses/{course_id}/teachers**: Associate a Teacher with an existing Course
  - **Request Body**: `{"teacher_id": 1}`
  - **Response**: `200 OK` with updated Course details or `404 Not Found` if Course does not exist.

- **GET /courses/{course_id}**: Retrieve Course details including Teacher information
  - **Response**: `200 OK` with Course details and Teacher information or `404 Not Found` if Course does not exist.

- **PUT /courses/{course_id}/teachers**: Update the Teacher associated with an existing Course
  - **Request Body**: `{"teacher_id": 2}`
  - **Response**: `200 OK` with updated Course details or `404 Not Found` if Course or Teacher does not exist.

## VII. Implementation Approach
1. **Environment Setup**: Ensure Python 3.11+ and Poetry are configured as needed.
2. **Update FastAPI Application**:
   - Modify `courses.py` to add endpoints related to Teacher associations.
   - Enhance the `models.py` file to reflect changes in the Course model.
   - Update `schemas.py` to include the new CourseTeacherAssign and CourseResponse schemas.
3. **Database Migration**:
   - Use Alembic to create migration scripts that add the `teacher_id` column to the existing Courses table with foreign key constraints.
4. **CRUD Logic Implementation**:
   - Implement endpoint logic in `courses.py` for handling Course-Teacher associations.
5. **Input Validation Logic**:
   - Utilize Pydantic for input validation on Teacher associations.
6. **Testing**:
   - Write new tests in `tests/test_courses.py` to validate new functionalities.

## VIII. Testing Strategy
### Coverage Goals
- Aim for at least 80% test coverage for the functionalities regarding Teacher associations with Courses.
- Implement tests based on specified user scenarios:
  - Successful association of Teachers with Courses.
  - Accurate retrieval of Course and Teacher information.

### Test Organization
- Directory Structure:
```
.
├── src/
│   ├── api/
│   │   ├── courses.py               # Updated for Course-Teacher management
│   ├── models.py                     # Updated for Course model
│   ├── schemas.py                    # Updated for new Course-Teacher schemas
│   └── main.py
├── tests/
│   ├── test_courses.py               # Tests for Course-Teacher functionalities
└── README.md
```

## IX. Security Considerations
- Input validation to prevent SQL injections or malformed data submissions.
- Ensure that sensitive data (like Teacher emails) is protected in API responses.

## X. Deployment Considerations
- Use environment variables for database URLs and sensitive settings.
- Ensure the deployment pipeline incorporates tests for the new features.

## XI. Documentation
- Update the README.md file with setup instructions for the new features.
- Provide API usage instructions for new endpoints related to associating Teachers with Courses.

## XII. Future Enhancements
- Future considerations may include expanding capabilities for Course roster management and functionalities surrounding Teacher performance metrics.

## XIII. Trade-offs and Decisions
- **Migration Strategy**: Careful Alembic migration scripts prevent data integrity issues while integrating new relationships.
- **FastAPI**: This framework offers built-in validation capabilities essential for robust API management.
- **Testing Focus**: Prioritize initial test coverage on new functionalities now with a plan to enhance it in subsequent sprints.

### Existing Code Files Modifications:
- **models.py**: Introduce the `teacher_id` column in Course class and set a relationship with the Teacher entity.
- **schemas.py**: Add schemas for validating Teacher associations with Courses.
- **courses.py**: Introduce new endpoints for assigning, updating, and retrieving Course-Teacher relationships.

### Database Migration Strategy:
Alembic migration script to update the `courses` table:
```python
"""Add teacher_id to courses

Revision ID: xxxxxxxx
Revises: previous_revision_id
Create Date: YYYY-MM-DD HH:MM:SS

"""
from alembic import op
import sqlalchemy as sa

revision = 'xxxxxxxx'
down_revision = 'previous_revision_id'
branch_labels = None
depends_on = None

def upgrade():
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=False))
    op.create_foreign_key('fk_teacher', 'courses', 'teachers', ['teacher_id'], ['id'])

def downgrade():
    op.drop_constraint('fk_teacher', 'courses', type_='foreignkey')
    op.drop_column('courses', 'teacher_id')
```

### Testing Example:
File: `tests/test_courses.py`
```python
import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

@pytest.fixture(scope="module", autouse=True)
def setup_database():
    # Setup logic for creating necessary records or test database
    response = client.post("/teachers", json={"name": "Jane Doe", "email": "jane.doe@example.com"})
    assert response.status_code == 201
    teacher_id = response.json()['id']
    response = client.post("/courses", json={"name": "Mathematics 101"})
    assert response.status_code == 201
    yield {"teacher_id": teacher_id}  # Use this teacher_id for further tests

def test_assign_teacher_to_course(setup_database):
    teacher_id = setup_database["teacher_id"]
    response = client.post("/courses/1/teachers", json={"teacher_id": teacher_id})
    assert response.status_code == 200
    data = response.json()
    assert data['teacher_id'] == teacher_id

def test_retrieve_course_details():
    response = client.get("/courses/1")
    assert response.status_code == 200
    data = response.json()
    assert 'teacher_name' in data  # Ensure teacher's name is returned

def test_update_teacher_for_course(setup_database):
    teacher_id = setup_database["teacher_id"]
    new_teacher_response = client.post("/teachers", json={"name": "John Smith", "email": "john.smith@example.com"})
    new_teacher_id = new_teacher_response.json()['id']
    
    update_response = client.put("/courses/1/teachers", json={"teacher_id": new_teacher_id})
    assert update_response.status_code == 200
    updated_data = update_response.json()
    assert updated_data['teacher_id'] == new_teacher_id
```

This technical implementation plan is developed to fully integrate the new Teacher relationship into the existing Course functionality in the Student Management Web Application while adhering to the coding standards, architecture, and incremental development philosophy established in prior sprints.