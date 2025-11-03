# Implementation Plan: Add Teacher Relationship to Course Entity

---

## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Teacher Entity

---

## Overview
The purpose of this implementation plan is to outline the technical architecture, technology stack, module responsibilities, data models, API contracts, and key considerations for adding the Teacher relationship to the existing Course entity. This feature will enhance the application's capability to manage educational course assignments effectively while maintaining existing functionality and data integrity.

## Technology Stack
- **Programming Language**: Python 3.11+
- **Web Framework**: FastAPI
- **Database**: SQLite (using SQLAlchemy for ORM)
- **Testing Framework**: pytest
- **API Documentation**: Swagger UI (integrated with FastAPI)
- **Environment Management**: Poetry (for dependency management)
- **Type Checking**: MyPy (for static type checking)

## Module Structure
The existing application structure will be updated as follows:
- **src/**
  - **main.py**: 
    - **Modifications**: Add routes for assigning a Teacher to a Course and retrieving course details with teacher information.
  - **models/**
    - `course.py`: 
      - **Modifications**: Update the Course model to include the `teacher_id` foreign key.
  - **schemas/**:
    - `course_schema.py`: 
      - **Modifications**: Update course schemas to include `teacher_id`.
  - **routes/**:
    - `course_routes.py`: 
      - **Modifications**: Extend existing endpoints to handle PUT request for assigning a Teacher to a Course and GET request for retrieving Course details.
  - **database/**:
    - `migrations/**`: 
      - **New file**: Create migration scripts to update the Course schema to accommodate the new `teacher_id` foreign key.
- **tests/**:
  - `test_course.py`: 
      - **Modifications**: Update test cases to include tests for the new functionality associated with the Teacher relationship.

## Data Model
### Course Model Update
The Course entity will be updated using SQLAlchemy as follows:
```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.database import Base

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)

    teacher = relationship("Teacher", back_populates="courses")
```

### Teacher Model (For Reference)
The Teacher entity will remain unchanged but should be referenced for context:
```python
class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    courses = relationship("Course", back_populates="teacher")
```

### Pydantic Schemas
Request and response validations for updating Course details with Teacher assignments will be handled as follows:
```python
from pydantic import BaseModel

class CourseUpdate(BaseModel):
    teacher_id: int
```

### Course Retrieval Schema
This schema will now also return the associated Teacher:
```python
class CourseResponse(BaseModel):
    id: int
    name: str
    level: str
    teacher_id: int

    class Config:
        orm_mode = True
```

## API Contracts
### Endpoints
1. **Assign a Teacher to a Course**
   - **PUT** `/courses/{course_id}`
   - Request Body: 
   ```json
   {
     "teacher_id": 1
   }
   ```
   - Response: `200 OK` with `CourseResponse`.

2. **Retrieve Course Information with Teacher Assignment**
   - **GET** `/courses/{id}`
   - Response: `200 OK` with `CourseResponse` including `teacher_id`.

### Error Handling
- If required fields are missing or invalid:
```json
{"error": {"code": "E001", "message": "Missing Course ID or Teacher ID."}}
```

## Implementation Approach
1. **Setup Environment**
   - Use Poetry to ensure all dependencies for handling the Course-Teacher relationship are installed.

2. **Database Migration**
   - Create a migration script in the `migrations/` folder to add the `teacher_id` column to the existing `courses` table.
   ```python
   from sqlalchemy import Column, Integer, ForeignKey
   from sqlalchemy.orm import relationship
   from database.database import Base

   class MigrationAddTeacherToCourse(Base):
       __tablename__ = 'courses'
       id = Column(Integer, primary_key=True, index=True)
       teacher_id = Column(Integer, ForeignKey('teachers.id'))
   ```

3. **CRUD Functionality**
   - Implement `PUT` endpoint in `course_routes.py` to handle the assignment of a teacher to a course.
   - Ensure validation of Course ID and Teacher ID using CourseUpdate schema.

4. **Testing**
   - Develop unit tests in `test_course.py` to ensure coverage and correct behavior, targeting at least 70% coverage. Include scenarios for assigning teachers, validating errors for missing IDs, and fetching course details with assigned teacher information.

5. **Documentation**
   - Update FastAPI documentation to include the new course assignment endpoints and their expected behaviors.

## Scalability and Security Considerations
- Continue using SQLite for development; consider PostgreSQL for production to accommodate potential scaling requirements.
- Ensure foreign key constraints are managed correctly to maintain data integrity.

## Trade-offs and Decisions
- **Framework Choice**: Retaining FastAPI for this feature allows seamless integration with existing architecture.
- **Data Integrity**: Clear model definitions and schema adjustments will help maintain data integrity.

---

## Conclusion
This implementation plan outlines the steps to integrate a Teacher relationship to the Course entity within the existing application, adhering to specified coding standards and functional requirements. This enhancement will improve course management capabilities while ensuring data integrity and backward compatibility with existing functionalities.