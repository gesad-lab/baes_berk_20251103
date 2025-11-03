# Implementation Plan: Add Teacher Relationship to Course Entity

---
**INCREMENTAL DEVELOPMENT CONTEXT**

Previous Sprint Plan:  
# Implementation Plan: Create Teacher Entity

---
**INCREMENTAL DEVELOPMENT CONTEXT**

Previous Sprint Plan:  
# Implementation Plan: Add Email Field to Student Entity

---
**INCREMENTAL DEVELOPMENT CONTEXT**

Previous Sprint Plan:  
# Implementation Plan: Create Course Entity

---
**INCREMENTAL DEVELOPMENT CONTEXT**

Previous Sprint Plan:  
# Implementation Plan: Student Management Web Application

## I. Overview

This implementation plan outlines the necessary steps to establish a relationship between the Course and Teacher entities within the Student Management Web Application. The objective is to link each course to a specific teacher while allowing courses to exist independently of teacher assignments. This change aligns with the goal of enhancing the application's educational management capabilities.

## II. Architecture

### 1. Application Architecture
The application will continue to function as a RESTful web service using the Flask framework, with the following layers:

- **Presentation Layer**: APIs for managing Course and Teacher relationships.
- **Business Logic Layer**: Logic for creating, updating, and retrieving course-teacher associations.
- **Data Access Layer**: Interfaces with the SQLite database to manage Course and Teacher entity data.

### 2. Module Boundaries
- **Course Module**: Updated to include a foreign key field for teacher associations and the logic for handling course-teacher relationships.
- **Teacher Module**: Existing module with new functionality to support the association with courses.
- **Database Module**: Modified to accommodate the new foreign key relationship in the Course table without affecting existing Student and Teacher models.

## III. Technology Stack

- **Language**: Python 3.11+
- **Framework**: Flask
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Testing**: pytest
- **Documentation**: Markdown

## IV. Data Model

### 1. Course Entity
The `Course` model will be updated to include a `teacher_id` foreign key field:

```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.models import Base  # Assuming Base is defined as part of the SQLAlchemy setup

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)
    
    teacher = relationship("Teacher")  # Establish relationship with the Teacher model

    def __repr__(self):
        return f"<Course(title={self.title}, teacher_id={self.teacher_id})>"
```

### 2. Database Schema
The SQLite database will be updated to include the `teacher_id` foreign key in the `courses` table while ensuring that existing data in the `students`, `courses`, and `teachers` tables is preserved.

## V. API Contracts

### 1. Endpoints

#### a. Create Course
- **Endpoint**: `POST /api/v1/courses`
- **Request Body**:
  ```json
  {
    "title": "Introduction to Programming",
    "description": "Learn the basics of programming.",
    "teacher_id": 1  // Optional
  }
  ```
- **Responses**:
  - **201 Created**:
    ```json
    {
      "message": "Course created successfully.",
      "course": {
        "title": "Introduction to Programming",
        "description": "Learn the basics of programming.",
        "teacher_id": 1
      }
    }
    ```
  - **400 Bad Request** (if validation fails):
    ```json
    {
      "error": {"code": "E001", "message": "The specified teacher does not exist."}
    }
    ```

#### b. Update Course
- **Endpoint**: `PUT /api/v1/courses/{course_id}`
- **Request Body**:
  ```json
  {
    "title": "Advanced Programming",
    "description": "Learn advanced programming concepts.",
    "teacher_id": 2 // Optional
  }
  ```
- **Responses**:
  - **200 OK**:
    ```json
    {
      "message": "Course updated successfully."
    }
    ```

#### c. Retrieve Course
- **Endpoint**: `GET /api/v1/courses/{course_id}`
- **Responses**:
  - **200 OK**:
    ```json
    {
      "title": "Introduction to Programming",
      "description": "Learn the basics of programming.",
      "teacher_id": 1
    }
    ```

### 2. Error Handling
All error responses should follow a consistent formatted structure:
```json
{
  "error": {
    "code": "E001",
    "message": "Error description."
  }
}
```

## VI. Implementation Details

### 1. Project Structure
The overall project structure will be updated to reflect new module integrations:

```
student_management/
├── src/
│   ├── app.py               # Main application file (update logic for courses and teacher relationship here)
│   ├── models.py            # Update to include teacher_id in Course model
│   ├── routes.py            # Updated to include course-creation and update endpoints
│   ├── services.py          # Add logic for handling Course operations and relationships
│   └── db.py                # Migration scripts for new Course schema
├── tests/
│   ├── test_routes.py       # Add tests for course management endpoints
│   ├── test_services.py      # Tests covering course business logic
│   └── test_migrations.py    # Tests for database migrations
├── requirements.txt          # Updated to reflect any new dependencies
└── README.md                 # Updated documentation for new features
```

### 2. Dependencies
Ensure existing libraries are complemented with any necessary additional libraries. The `requirements.txt` will be revised as needed:
```
Flask
Flask-SQLAlchemy
pytest
```

## VII. Testing Strategy

### 1. Test Cases
Tests will validate:
- Successful creation of a course with or without a teacher.
- Input validation checks for non-existent teacher identifiers when creating or updating courses.
- Successful retrieval of course details including teacher info (if assigned).

### 2. Test Coverage
Ensure at least 70% overall coverage, focusing on achieving 90%+ coverage for course-teacher relationship functionalities.

### 3. Testing Structure
Tests should mirror the codebase structure to maintain clarity and accuracy:
```
tests/
├── test_routes.py           # Tests for course management endpoints
├── test_services.py         # Logic tests for course service methods
├── test_migrations.py       # Tests for applying new migration scripts
```

### 4. Example of New Test Case
```python
def test_create_course_with_teacher(client):
    """Test that creating a course with a valid teacher id succeeds."""
    response = client.post('/api/v1/courses', json={'title': 'Math 101', 'description': 'Basic Math Course', 'teacher_id': 1})
    assert response.status_code == 201
    assert response.json['message'] == "Course created successfully."
```

## VIII. Database Migration Strategy
Utilize Alembic to establish migration scripts that will add the `teacher_id` foreign key to the `courses` table. The migration will ensure that no data loss occurs during schema updates.

```bash
# Command to generate a migration
alembic revision --autogenerate -m "Add teacher_id to courses table"
```

### 1. Migration Script
```python
# Migration script example
def upgrade():
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), sa.ForeignKey('teachers.id'), nullable=True))

def downgrade():
    op.drop_column('courses', 'teacher_id')
```

### 2. Initialization
Ensure that migrations are automatically applied during startup or deployment for new changes to take effect without manual intervention.

## IX. Conclusion
This implementation plan provides a structured approach to link the Teacher entity with the Course entity in the Student Management Web Application. By following clear architectural practices, maintaining backward compatibility, and developing a thorough testing strategy, the enhancements will fulfill the outlined specifications. The modifications, migration procedures, and testing plans are designed to ensure smooth integration of this new functionality while preserving existing data integrity.