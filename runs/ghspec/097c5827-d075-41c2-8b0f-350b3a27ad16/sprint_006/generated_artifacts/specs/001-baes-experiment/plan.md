# Implementation Plan: Add Teacher Relationship to Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Teacher Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan: 
# Implementation Plan: Add Course Relationship to Student Entity

---

## Version: 1.0.0
## Purpose
This implementation plan outlines the necessary changes to establish a `Teacher` relationship within the existing `Course` entity of the educational system. This feature will enable better course management by linking courses to their respective teachers, thereby improving visibility and enhancing the educational experience.

---

## I. Architecture Overview

The architecture will maintain its modular structure to ensure that introducing the teacher relationship does not disrupt existing functionalities. The `Course` and `Teacher` entities will be linked through a foreign key while preserving all current data and relationships.

### 1.1 Architecture Components
- **Web Framework**: Flask (Python) for handling HTTP requests and routing.
- **Database**: SQLite, continuing its utilization for ease of development.
- **Object Relational Mapping (ORM)**: SQLAlchemy for abstracting database interactions.
- **Testing Framework**: pytest for unit and integration testing.

### 1.2 Module Boundaries
- **controllers**: Extend `course_controller.py` to handle the new endpoints for assigning teachers to courses.
- **models**: Update `models.py` to include the `teacherId` in the `Course` entity.
- **services**: Extend existing `course_service.py` for business logic related to assigning teachers to courses.
- **database**: Implement database migrations to alter the `Course` entity schema.

---

## II. Technology Stack

- **Programming Language**: Python 3.x
- **Web Framework**: Flask
- **ORM**: SQLAlchemy
- **Database**: SQLite
- **Testing**: pytest
- **API Documentation**: OpenAPI/Swagger (for optional documentation generation)

---

## III. Data Models and API Contracts

### 3.1 Data Model

The `Course` model in `models.py` will be updated to include a foreign key reference to the `Teacher` entity:

```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
    teacherId = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # New relationship field

    teacher = relationship("Teacher", back_populates="courses")  # Establish bidirectional relationship
```

### 3.2 API Contracts

- **Assign Teacher to Course Endpoint**:
  - **Request**:
    - Method: PATCH
    - URL: `/courses/{courseId}/assign-teacher`
    - Body:
    ```json
    {
        "teacherId": 1
    }
    ```
  - **Response Success (200)**:
    ```json
    {
        "message": "Teacher assigned successfully."
    }
    ```
  - **Response Error (400)**:
    ```json
    {
        "error": {
            "code": "E001",
            "message": "Invalid course ID or teacher does not exist."
        }
    }
    ```

- **Retrieve Course Details with Teacher**:
  - **Request**:
    - Method: GET
    - URL: `/courses/{courseId}`
  - **Response Success (200)**:
    ```json
    {
        "courseId": 1,
        "courseName": "Mathematics",
        "level": "10",
        "teacher": {
            "id": 1,
            "name": "John Doe",
            "email": "john.doe@example.com"
        }
    }
    ```
  - **Response if No Teacher Assigned (200)**:
    ```json
    {
        "courseId": 1,
        "courseName": "Mathematics",
        "level": "10",
        "teacher": null
    }
    ```
  - **Response Error (404)**:
    ```json
    {
        "error": {
            "code": "E002",
            "message": "Course not found."
        }
    }
    ```

### 3.3 Database Migration Strategy
A new migration file will be created to add the `teacherId` column to the existing `courses` table while ensuring data integrity:

```python
def upgrade():
    op.add_column('courses', sa.Column('teacherId', sa.Integer(), sa.ForeignKey('teachers.id'), nullable=True))

def downgrade():
    op.drop_column('courses', 'teacherId')
```

---

## IV. Implementation Approach

### 4.1 Structure of the Project
```plaintext
course_teacher_entity_app/
│
├── src/
│   ├── app.py                    # Main application entry point
│   ├── models.py                 # SQLAlchemy models (includes Course and Teacher)
│   ├── controllers/
│   │   ├── course_controller.py    # Handles Course related endpoints, updates to include teacher assignments
│   ├── services/
│   │   ├── course_service.py       # Implements business logic related to Course assignment
│   └── database.py                # Database initialization & migrations
│
├── tests/
│   ├── test_course.py             # Unit tests for Course functionality, updated for teacher assignments
│   ├── test_course_integration.py  # Integration tests for Course endpoints, including teacher assignments
│
├── requirements.txt               # Dependency file
└── README.md                      # Project documentation
```

### 4.2 Modifications Needed to Existing Files
1. **`models.py`**:
   - Update the `Course` model to include a `teacherId` foreign key and establish a relationship with the Teacher model.

2. **`course_controller.py`**:
   - Add a new PATCH endpoint for assigning teachers to courses.
   - Modify existing GET endpoint for course details to return teacher information.

3. **`course_service.py`**:
   - Extend business logic functions to handle the assignment of teachers to courses and validate the existence of teachers.
   
4. **`tests/test_course.py`**:
   - Update unit tests for course functionalities to cover new endpoint scenarios involving assigning a teacher and retrieving course details.

5. **`tests/test_course_integration.py`**:
   - Extend integration tests to include the new teacher assignment endpoint and its expected behaviors.

### 4.3 Testing Strategy
- Implement unit tests in `tests/test_course.py` for new functions related to assigning teachers, focusing on both successful and erroneous cases.
- Integration tests in `tests/test_course_integration.py` will validate the behavior of the PATCH and GET endpoints, ensuring robust coverage.

---

## V. Security Considerations

- Validate the existence of teacher IDs against the database to prevent assignment of non-existent teachers.
- Structure error messages appropriately to avoid revealing sensitive implementation details.

---

## VI. Performance and Scalability

- Index the `teacherId` column in the `courses` table to maintain query performance.
- Maintain a modular approach in services and controllers to allow for easier scaling of the functionality in the future.

---

## VII. Deployment Considerations

- Deploy the migration first to ensure the schema is updated before adding new functionalities.
- Follow a staged rollout; begin with a controlled environment for regression testing before rolling out to production.

---

## Conclusion

This implementation plan provides a well-defined approach to integrating the `Teacher` relationship into the existing `Course` entity. It addresses all outlined requirements, adheres to current architecture, and promotes maintainability through modularity and rigorous testing protocols. The documentation has been structured to facilitate understanding and implementation by the development team.

Existing Code Reference:
```python
# src/database.py

from alembic import op
import sqlalchemy as sa

def upgrade():
    op.add_column('courses', sa.Column('teacherId', sa.Integer(), sa.ForeignKey('teachers.id'), nullable=True))

def downgrade():
    op.drop_column('courses', 'teacherId')
```

```python
# tests/test_course_integration.py

import pytest
from flask import json
from src.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_assign_teacher_to_course(client):
    response = client.patch('/courses/1/assign-teacher', data=json.dumps({
        'teacherId': 1
    }), content_type='application/json')
    assert response.status_code == 200
    assert response.json['message'] == "Teacher assigned successfully."
``` 

This implementation plan effectively manages the integration of a teacher's relationship to the course, ensuring functionality, performance, and security remain intact while expanding the system's capabilities.