# Implementation Plan: Add Teacher Relationship to Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

### Previous Sprint Plan:
# Implementation Plan: Create Teacher Entity

---

## Version: 1.1.0  
**Purpose**: Establish a relationship between Course and Teacher entities to enhance course management functionalities within the educational platform.

---

## I. Architecture Overview

### 1.1 Technical Stack
- **Web Framework**: FastAPI (asynchronous, high-performance)
- **Database**: SQLite (for persistence with a lightweight setup)
- **ORM**: SQLAlchemy (for database interaction)
- **Testing Framework**: pytest (for unit and integration testing)
- **Documentation**: OpenAPI/Swagger (FastAPI provides built-in docs)

### 1.2 Application Structure
- `src/`: Application source code  
  - `main.py`: Entry point of the FastAPI application  
  - `models/`: Database models (including Student, Course, Teacher)
  - `schemas/`: Pydantic models for request/response validation  
  - `routes/`: API endpoints for handling HTTP requests  
  - `database/`: Database connection and setup
- `tests/`: Test files  
- `README.md`: Setup and documentation  

---

## II. Module Responsibilities

### 2.1 Models
- **Course**:
  - Existing fields of the Course entity.
  - **New Field**: 
    - `teacher_id`: Foreign key referencing Teacher entity (Integer).
- **Teacher**:
  - Fields as previously defined:
    - `id`: Integer, primary key, auto-incremented
    - `name`: String, required
    - `email`: String, required, unique
- **Database Responsibilities**: Update Course model to manage teacher assignments, including validation checks for existence of teacher IDs.

### 2.2 Schemas
- **CourseSchema**: (Existing schema)
  - Updated to include a new field, `teacher_id`.
- **TeacherSchema**:
  - Properties: 
    - `id`: Integer
    - `name`: String
    - `email`: String
- **UpdateCourseRequestSchema**: (New schema)
  - Properties:
    - `teacher_id`: Integer (optional)
  - Responsibilities: Validate incoming request data for updating the course, specifically the teacher assignment.

### 2.3 Routes
- **Course Routes**:
  - `PATCH /courses/{course_id}`:
    - Responsibilities: Update an existing Course to assign a Teacher.
  - `GET /courses/{course_id}`:
    - Responsibilities: Retrieve details of a specific Course, including assigned Teacher information.
  - `GET /courses`:
    - Responsibilities: List all Courses, each including their assigned Teachers.

### 2.4 Database
- **Database Management**:
  - Responsibilities: Modify the existing Course table to include `teacher_id`, manage relationships, and oversee session management with SQLAlchemy.

---

## III. Database Model and API Contracts

### 3.1 Database Schema
- **Course Table Modification**:
```sql
ALTER TABLE courses ADD COLUMN teacher_id INTEGER REFERENCES teachers(id);
```

### 3.2 API Contract

#### 3.2.1 PATCH /courses/{course_id}
##### Request
- Body:
```json
{
  "teacher_id": 1
}
```

##### Responses
- **200 OK**:
```json
{
  "id": 1,
  "teacher_id": 1
}
```
- **404 Not Found** (if course does not exist):
```json
{
  "error": {
    "code": "E001",
    "message": "Course not found."
  }
}
```
- **400 Bad Request** (if teacher ID does not exist):
```json
{
  "error": {
    "code": "E002",
    "message": "Teacher with ID 2 does not exist."
  }
}
```

#### 3.2.2 GET /courses/{course_id}
##### Request
- URL Parameter: `course_id`

##### Responses
- **200 OK**:
```json
{
  "id": 1,
  "teacher_id": 1,
  "teacher": {
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
}
```
- **404 Not Found** (if course does not exist):
```json
{
  "error": {
    "code": "E003",
    "message": "Course not found."
  }
}
```

#### 3.2.3 GET /courses
##### Request
- No parameters

##### Responses
- **200 OK**:
```json
{
  "courses": [
    {
      "id": 1,
      "teacher": {
        "name": "John Doe",
        "email": "john.doe@example.com"
      }
    }
  ]
}
```

---

## IV. Implementation Approach

### 4.1 Development Steps
1. **Update the database model**:
   - Modify the existing `Course` model to include the `teacher_id` attribute, establishing a foreign key relationship.

2. **Create update request/response schemas**:
   - Implement the `UpdateCourseRequestSchema` to validate requests for updating course assignments.

3. **Develop API routes**:
   - Implement `PATCH`, `GET` routes for managing course assignments to teachers.

4. **Set up database migration**:
   - Create migration scripts using Alembic to add the `teacher_id` column to the existing `courses` table.

5. **Implement error handling**:
   - Validate that the provided `teacher_id` exists in the database, and return structured error messages for invalid requests.

6. **Write tests**:
   - Develop unit and integration tests to ensure that course assignment, retrieval, and list functionalities work as intended.

7. **Documentation**:
   - Update `README.md` to reflect new API specifications and provide usage examples for the Course-Teacher relationship.

---

## V. Testing Strategy

### 5.1 Testing Requirements
- **Unit Tests**: Verify update and retrieval logic for Course-Teacher relationships.
- **Integration Tests**: Test the new API endpoints for successful and failed course assignments.
- **Minimum Test Coverage**: Target a minimum of 70% coverage for course update logic.

### 5.2 Test Organization
- Update `tests/test_course_routes.py` for new test methods to cover the implemented feature enhancements.

---

## VI. Error Handling and Validation

### 6.1 Input Validation
- Validate that `teacher_id` is present and corresponds to an existing Teacher. Return appropriate JSON error responses defined in the API contracts for invalid updates.

---

## VII. Security Considerations

### 7.1 Data Protection
- Ensure input validation and error handling to maintain data integrity when assigning teachers to courses.

---

## VIII. Performance Considerations

### 8.1 Scalability
- Maintain SQLite for initial deployment, but consider transitioning to PostgreSQL for enhanced performance with scaling Course and Teacher records in the future.

### 8.2 Optimization
- Monitor and optimize query performance for retrievals involving joins between Courses and Teachers.

---

## IX. Deployment Considerations

### 9.1 Environment Management
- Ensure that environment variables used for sensitive configurations are documented for production.

### 9.2 Database Migration Strategy
- Use Alembic to manage database migrations effectively to introduce the `teacher_id` column into the `courses` table.

---

## X. Documentation

- Update `README.md` with setup instructions, project structure, and usage examples regarding the Course-Teacher relationship API.
- Leverage FastAPI's built-in functionality to auto-generate API documentation.

---

## Conclusion
This implementation plan provides a structured approach to establishing a relationship between Course and Teacher entities within the educational platform. It maintains compatibility with existing data structures and ensures enhanced functionalities while adhering to established coding standards and practices.

### Existing Code Modifications:

#### File: `models/course.py`
```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Course(Base):
    __tablename__ = 'courses'
    
    # Existing Fields...
    
    teacher_id = Column(Integer, ForeignKey('teachers.id'))
    teacher = relationship("Teacher", back_populates="courses")
```

#### File: `schemas/course_schema.py`
```python
from pydantic import BaseModel
from typing import Optional

class UpdateCourseRequestSchema(BaseModel):
    teacher_id: Optional[int] = None  # New optional field

class CourseSchema(BaseModel):
    id: int
    teacher_id: Optional[int]
    teacher: Optional[TeacherSchema]  # Reference to TeacherSchema for related data
```

#### File: `routes/course_routes.py`
```python
@router.patch("/courses/{course_id}", response_model=CourseSchema)
def assign_teacher_to_course(course_id: int, update_request: UpdateCourseRequestSchema, db: Session = Depends(get_db)):
    # Logic to assign teacher to a course, including validation for teacher_id
    pass
```

#### Migration
- Create migration script using Alembic to modify the `courses` table to include the `teacher_id` field:
```bash
alembic revision -m "Add teacher_id to courses table"
``` 

This plan thoroughly outlines the required implementation and modifications to successfully add the Teacher relationship to the Course entity and aligns with the existing coding standards and architectural framework.