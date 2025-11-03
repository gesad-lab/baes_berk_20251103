# Implementation Plan: Add Teacher Relationship to Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Teacher Entity

---

## Version: 1.0.0

### I. Architecture Overview
This plan outlines the process of adding a teacher relationship to the Course entity within the existing Educational Management System. The new relationship will link teachers directly to courses, enabling better educational resource management. We will utilize FastAPI as the framework due to its scalability and maintainability.

### II. Technology Stack
- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Database**: SQLite
- **ORM**: SQLAlchemy for ORM management
- **Data Validation**: Pydantic for request and response validation
- **Testing**: Pytest for unit and integration tests
- **Environment**: Python 3.11+

### III. Module Design

#### 1. Project Structure
```
educational_management/
├── src/
│   ├── main.py             # Entry point of FastAPI application
│   ├── models.py           # SQLAlchemy models (Course and Teacher)
│   ├── schemas.py          # Pydantic schemas for Course and Teacher requests
│   ├── database.py         # Database connection and initialization
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── teachers.py      # New API routes for managing teacher assignments
│   │   ├── courses.py       # Existing API routes for course management
├── tests/
│   ├── __init__.py
│   ├── test_teachers.py     # Tests for teacher functionalities
│   ├── test_courses.py      # Existing tests for courses API
├── README.md                # Project documentation
└── requirements.txt         # Dependency management
```

#### 2. Components Breakdown
- **models.py**: Update the `Course` model to include a `teacher_id` foreign key.
- **schemas.py**: Create Pydantic schemas for validating requests for assigning teachers and retrieving courses.
- **routes/teachers.py**: Implement API routes for assigning teachers and retrieving course details with teacher information.
- **tests/test_teachers.py**: Create tests for teacher assignment functionalities.

### IV. Data Models

#### 1. Updated Course Model 
Enhance `models.py` to include `teacher_id`:
```python
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)

    teacher = relationship("Teacher", backref="courses")

class Teacher(Base):
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

    def __repr__(self):
        return f"<Teacher(name={self.name}, email={self.email})>"
```

### V. API Contracts

#### 1. Assign Teacher to Course Endpoint
- **Endpoint**: `POST /courses/{course_id}/assign_teacher`
- **Request Body**:
  ```json
  {
      "teacher_id": "1"
  }
  ```
- **Response**:
  - **Success**:
    ```json
    {
        "message": "Teacher assigned to course successfully"
    }
    ```
  - **Error (Course Not Found)**:
    ```json
    {
        "error": {
            "code": "E404",
            "message": "Course not found"
        }
    }
    ```

#### 2. Retrieve Course with Teacher Endpoint
- **Endpoint**: `GET /courses/{course_id}`
- **Response**:
  ```json
  {
      "id": 1,
      "name": "Mathematics 101",
      "level": "Beginner",
      "teacher": {
          "name": "John Doe",
          "email": "john.doe@example.com"
      }
  }
  ```

### VI. Implementation Steps

1. **Initialize Project**:
   - Set up the project environment with required dependencies specified in `requirements.txt`.

2. **Database Schema Update**:
   - Implement migration scripts to alter the `courses` table:
     ```sql
     ALTER TABLE courses ADD teacher_id INTEGER;
     ```

3. **Update API Endpoints**:
   - In `routes/teachers.py`, create endpoints for assigning a teacher, linking it to the course:
     - `POST /courses/{course_id}/assign_teacher` for assigning a teacher to a course.
     - `GET /courses/{course_id}` for retrieving course details along with teacher information.

4. **Input Validation**:
   - Expand Pydantic schemas in `schemas.py`:
     ```python
     from pydantic import BaseModel

     class AssignTeacher(BaseModel):
         teacher_id: int

     class CourseResponse(BaseModel):
         id: int
         name: str
         level: str
         teacher: Optional[TeacherResponse]  # Include teacher details if assigned
     ```

5. **Testing**:
   - Implement test cases in `tests/test_teachers.py` for:
     - Successfully assigning a valid teacher to a valid course.
     - Attempting to assign a teacher to a non-existent course and validating error response.
     - Retrieving course details and verifying that assigned teacher information is returned correctly.

6. **Documentation**:
   - Update `README.md` with details about the new API endpoints for assigning teachers and retrieving course information.

### VII. Success Criteria
- The API allows the successful assignment of teachers to courses and correctly retrieves course details with teacher information.
- JSON responses to requests match the specified format and include appropriate success/error messages.
- Tests validate the functionality, achieving at least 70% coverage with all critical paths verified.
- Database migration operates without error, maintaining integrity across all existing entities.

### VIII. Deployment Considerations
- Ensure the application is set to deploy in a stable production environment.
- Run migration scripts on a staging environment prior to production deployment to catch potential issues.

### IX. Future Enhancements (Out of Scope for v1.0.0)
- More complex scenarios involving multiple teachers per course.
- Frontend integration to visualize teacher-course assignments.

### X. Conclusion
This implementation plan offers a structured approach to adding a teacher relationship to the Course entity in the Educational Management System. Following these guidelines ensures that the integration improves the overall functionality of the system while maintaining data integrity and system performance.

**Existing Code Files**:
This implementation modifies/includes `models.py`, `schemas.py`, `routes/teachers.py`, and `tests/test_teachers.py`. 

**Instructions for Technical Plan**:
1. Use the same tech stack as previous sprints.
2. Integrate new modules while maintaining existing functionality.
3. Document necessary modifications to existing files without replacements.
4. Ensure backward compatibility with existing data models.
5. Specify migration strategy for data model updates.