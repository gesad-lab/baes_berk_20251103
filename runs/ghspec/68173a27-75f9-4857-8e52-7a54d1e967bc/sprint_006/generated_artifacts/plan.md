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
# Implementation Plan: Add Email Field to Student Entity

---

## I. Overview

This implementation plan outlines the architecture, technology stack, data models, API design, and implementation approach required to establish a relationship between the Course entity and the newly introduced Teacher entity as specified in the requirement document.

---

## II. Architecture

### 2.1 High-Level Architecture
- **Client**: API consumer that may include a web client or mobile application.
- **Backend**: RESTful API built using FastAPI (Python).
- **Database**: SQLite for local persistence.

### 2.2 Module Boundaries
- **API Layer**: Handles incoming requests for assigning a Teacher to a Course and retrieving Course details with Teacher information.
- **Service Layer**: Manages business logic related to Course and Teacher relationships, including validation and error handling.
- **Data Access Layer (Repository)**: Interfaces with the SQLite database to perform CRUD operations on the Course entity as well as handling relationships with the Teacher entity.

---

## III. Technology Stack

| Layer          | Technology                         |
|----------------|-------------------------------------|
| Language       | Python                              |
| Framework      | FastAPI                             |
| ORM            | SQLAlchemy                          |
| Database       | SQLite                              |
| Testing        | Pytest                              |
| Environment    | Docker for containerization (optional but recommended for local development) |

---

## IV. Data Model

### 4.1 Course Entity Update
- **Table Name**: `courses`
- **Fields**:
  - `id`: Integer, Primary Key (auto-increment).
  - `title`: String (required).
  - `description`: String (optional).
  - `teacher_id`: Integer (foreign key reference to the associated Teacher).

### 4.2 SQLAlchemy Models
```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)
    
    # Relationship to Teacher
    teacher = relationship("Teacher", back_populates="courses")

class Teacher(Base):
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    courses = relationship("Course", back_populates="teacher")
```

### 4.3 Migration Script
- Create a migration script to add the `teacher_id` field to the existing `courses` table as a foreign key referencing the `teachers` table while preserving all existing Course and Teacher data.

Example Migration Statement (using Alembic):
```python
def upgrade():
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))
    op.create_foreign_key('fk_teacher_course', 'courses', 'teachers', ['teacher_id'], ['id'])

def downgrade():
    op.drop_constraint('fk_teacher_course', 'courses', type_='foreignkey')
    op.drop_column('courses', 'teacher_id')
```

---

## V. API Design

### 5.1 Endpoints

1. **Assign Teacher to Course**
   - **Method**: POST
   - **Endpoint**: `/api/v1/courses/{course_id}/assign_teacher`
   - **Request Body**:
     ```json
     {
       "teacher_id": "integer (required)"
     }
     ```
   - **Responses**:
     - 200 OK: `{ "message": "Teacher assigned to course successfully." }`
     - 400 Bad Request: `{ "error": { "code": "E001", "message": "Invalid Course ID." } }`
     - 404 Not Found: `{ "error": { "code": "E002", "message": "Teacher not found." } }`

2. **Retrieve Course with Teacher Information**
   - **Method**: GET
   - **Endpoint**: `/api/v1/courses/{course_id}`
   - **Responses**:
     - 200 OK: 
     ```json
     {
       "id": integer,
       "title": "string",
       "description": "string",
       "teacher": {
         "id": integer,
         "name": "string",
         "email": "string"
       }
     }
     ```
   - **Error Handling for Retrieval**:
     - 404 Not Found: `{ "error": { "code": "E003", "message": "Course not found." } }`

### 5.2 Error Handling
- Error responses will follow the standard error format, providing clear information about invalid Course IDs and Teacher IDs.

---

## VI. Implementation Approach

### 6.1 Project Structure
```
/course_management
├── src/
│   ├── main.py
│   ├── models/
│   │   ├── course.py
│   │   └── teacher.py
│   ├── services/
│   │   └── course_service.py
│   ├── repositories/
│   │   ├── course_repository.py
│   │   └── teacher_repository.py
│   └── database.py
├── tests/
│   ├── test_course.py
│   └── test_teacher.py
├── Dockerfile
└── requirements.txt
```

### 6.2 Step-by-Step Implementation

1. **Update Course Model**: Modify `course.py` to include the `teacher_id` foreign key and establish the relationship with the `Teacher` model.
2. **Create Migration Script**: Write a migration script to add the `teacher_id` field to the `courses` table without disrupting existing data.
3. **Implement Data Access Layer**: Develop repository methods in `course_repository.py` for assigning a Teacher to a Course and retrieving Course details.
4. **Implement Service Layer Logic**: Populate `course_service.py` with functions for assigning Teacher IDs to courses and retrieving Course data alongside Teacher information.
5. **Define API Route Handlers**: Establish route handlers in `main.py` for managing requests related to course teacher assignments and course retrieval.
6. **Input Validation**: Validate both the course and teacher IDs in the assignment function to ensure they exist before proceeding.
7. **Testing**: Write unit tests and integration tests in `test_course.py` to test the new functionalities, aiming for a minimum of 70% coverage.

---

## VII. Security Considerations

- Input validation and error handling must effectively manage potential invalid data submissions.
- Ensure logging does not expose sensitive information or implementation details.

---

## VIII. Deployment Considerations

- The application should be containerized using Docker for seamless deployment.
- Implement a health check endpoint in `main.py` to monitor API operational status.
- Use logging and monitoring tools to assess performance and issues after deployment.

---

## IX. Testing Approach

### 9.1 Test Types
- **Unit Tests**: Validate the correctness of service and repository functions.
- **Integration Tests**: Ensure that full API functionality works correctly by testing endpoints.
- **Contract Tests**: Validate the structure of the responses from endpoints against specifications.

### 9.2 Coverage Goals
- Aim for a minimum of 70% test coverage, with particular emphasis on critical paths, such as assigning teachers and retrieving course details.

---

## X. Technical Trade-Offs and Decisions

1. **Database Modification**: Introducing a foreign key relationship into the existing database must ensure data integrity across Course and Teacher entities.
2. **Use of SQLAlchemy**: Leverage SQLAlchemy's ORM capabilities for database interactions, simplifying model management and migrations.
3. **Backward Compatibility**: The introduction of teacher relationships in the course model is designed to maintain existing functionality for students and courses.

---

## XI. Conclusion

This implementation plan outlines a detailed strategy for adding a Teacher relationship to the Course entity within the application. By adhering to these steps, the platform will improve its educational management capabilities while ensuring system integrity and facilitating future enhancements.

### Existing Code Files to be Modified:
- In `src/models/course.py`, add the new field `teacher_id` and establish a relationship with the Teacher model.
- Update `src/repositories/course_repository.py` for new data access methods to handle teacher assignments/relationships.
- Expand `src/main.py` to include new API endpoints for assigning Teachers and retrieving Course details.

The implementation of this feature aligns with existing coding practices and maintains backward compatibility with current data models, ensuring a smoother integration into the overall application architecture.