# Implementation Plan: Add Course Relationship to Student Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

### Previous Sprint Plan:
# Implementation Plan: Create Course Entity

---

## Version: 1.1.0  
**Purpose**: Introduce a relationship between Students and Courses in the educational platform, enhancing data organization and tracking of student enrollments.

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
  - `models/`: Database models (including Student and Course models)  
  - `schemas/`: Pydantic models for request/response validation  
  - `routes/`: API endpoints for handling HTTP requests  
  - `database/`: Database connection and setup
- `tests/`: Test files  
- `README.md`: Setup and documentation  

---

## II. Module Responsibilities

### 2.1 Models
- **Student**:
  - Existing fields of the Student entity.
- **Course**:
  - **Fields**: 
    - `id`: Integer, primary key, auto-incremented
    - `name`: String, required
    - `level`: String, required
- **StudentCourses (Intermediary Table)**:
  - **Fields**:
    - `student_id`: Foreign key (Integer).
    - `course_id`: Foreign key (Integer).
  - **Responsibilities**: Handle the many-to-many relationship between Student and Course.

### 2.2 Schemas
- **CourseSchema**:
  - Properties: 
    - `id`: Integer
    - `name`: String
    - `level`: String
- **CourseAssociationRequestSchema**:
  - Properties:
    - `course_id`: Integer
  - Responsibilities: Validate incoming request data for associating courses with a student.

### 2.3 Routes
- **Student Course Routes**:
  - `POST /students/{student_id}/courses`:
    - Responsibilities: Associate a course to a student.
  - `GET /students/{student_id}/courses`:
    - Responsibilities: Retrieve all courses associated with a specific student.
  - `DELETE /students/{student_id}/courses/{course_id}`:
    - Responsibilities: Remove a specific course association from a student.

### 2.4 Database
- **Database Management**:
  - Responsibilities: Set up the SQLite database, create the new intermediary "student_courses" table on application startup, and handle session management with SQLAlchemy.

---

## III. Database Model and API Contracts

### 3.1 Database Schema
- **Intermediary Table Creation**:
  ```sql
  CREATE TABLE student_courses (
      student_id INTEGER,
      course_id INTEGER,
      FOREIGN KEY (student_id) REFERENCES students(id),
      FOREIGN KEY (course_id) REFERENCES courses(id),
      PRIMARY KEY (student_id, course_id)
  );
  ```

### 3.2 API Contract

#### 3.2.1 POST /students/{student_id}/courses
##### Request
- URL Parameter: `student_id`
- Body:
  ```json
  {
    "course_id": 1
  }
  ```

##### Responses
- **200 OK**:
  ```json
  {
    "message": "Course associated successfully."
  }
  ```
- **400 Bad Request** (if student or course is invalid):
  ```json
  {
    "error": {
      "code": "E001",
      "message": "Invalid student or course ID."
    }
  }
  ```

#### 3.2.2 GET /students/{student_id}/courses
##### Request
- URL Parameter: `student_id`

##### Responses
- **200 OK**:
  ```json
  {
    "courses": [
      {
        "id": 1,
        "name": "Algebra 101",
        "level": "Beginner"
      }
    ]
  }
  ```
- **404 Not Found** (if student does not exist):
  ```json
  {
    "error": {
      "code": "E002",
      "message": "Student not found."
    }
  }
  ```

#### 3.2.3 DELETE /students/{student_id}/courses/{course_id}
##### Request
- URL Parameters:
  - `student_id`: Integer
  - `course_id`: Integer

##### Responses
- **200 OK**:
  ```json
  {
    "message": "Course removed successfully."
  }
  ```
- **404 Not Found** (if association does not exist):
  ```json
  {
    "error": {
      "code": "E003",
      "message": "Association not found."
    }
  }
  ```

---

## IV. Implementation Approach

### 4.1 Development Steps
1. **Update the database model**:
   - Create a new intermediary model `StudentCourses` to define the many-to-many relationship.

2. **Create request/response schemas**:
   - Implement Pydantic models to validate requests for course association and responses for retrieving courses associated with a student.

3. **Develop API routes**:
   - Implement `POST`, `GET`, and `DELETE` routes for managing the course associations for students.

4. **Set up database migration**:
   - Create a migration script to add the "student_courses" table. Use Alembic for migrations, ensuring the schema change is reversible.

5. **Implement error handling**:
   - Add validation logic to appropriately handle associations, returning structured error messages for invalid requests.

6. **Write tests**:
   - Develop unit and integration tests to ensure functionality works as intended, including tests for successful course associations, retrieval, and deletions.

7. **Documentation**:
   - Update `README.md` to reflect new API specifications and provide usage examples.

---

## V. Testing Strategy

### 5.1 Testing Requirements
- **Unit Tests**: Verify individual component logic (e.g., association logic, validation).
- **Integration Tests**: Test the API endpoints for successful and failed requests related to course associations using pytest.
- **Minimum Test Coverage**: Target a minimum of 70% coverage for business logic with critical paths achieving 90%+ coverage.

### 5.2 Test Organization
- Mirror the structure of the source code within the `tests/` directory, including tests for each route and functionality introduced.

---

## VI. Error Handling and Validation

### 6.1 Input Validation
- Validate that `student_id` and `course_id` parameters are present; return JSON error responses defined in the API contracts for invalid requests.

---

## VII. Security Considerations

### 7.1 Data Protection
- Ensure input validation and sanitization to protect against injection attacks and guarantee the integrity of student and course associations.

---

## VIII. Performance Considerations

### 8.1 Scalability
- SQLite as a lightweight database option for initial stages, and consider transitioning to PostgreSQL or another RDBMS as usage scales.

### 8.2 Optimization
- Evaluate indexing on the `student_courses` table for performance with frequent queries on student-course relationships.

---

## IX. Deployment Considerations

### 9.1 Environment Management
- Use environment variables for configuration, especially if the application scales beyond a development environment.

### 9.2 Database Migration Strategy
- Use Alembic to manage database migrations, ensuring all changes are tracked, reversible, and compatible with existing Student and Course data.

---

## X. Documentation

- Update `README.md` to cover setup instructions, project structure, and usage of the student-course association API.
- Utilize FastAPI's built-in features to auto-generate API documentation for easy access and clarity.

---

## Conclusion
This implementation plan outlines structured steps to introduce a course relationship to the student entity within the existing educational platform application. All modifications maintain compatibility with prior data structures and ensure enhanced functionality while adhering to established coding standards and practices.

### Existing Code Modifications:

#### File: `models/student.py`
```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    # Existing fields...

    courses = relationship("StudentCourses", back_populates="student")
```

#### File: `models/course.py`
```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
```

#### File: `models/student_courses.py`
```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class StudentCourses(Base):
    __tablename__ = 'student_courses'
    
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)
```

#### File: `schemas/course_association_schema.py`
```python
from pydantic import BaseModel

class CourseAssociationRequestSchema(BaseModel):
    course_id: int
```

#### File: `routes/student_course_routes.py`
```python
from fastapi import APIRouter, HTTPException, Depends
from typing import List
from models.student_courses import StudentCourses
from schemas.course_association_schema import CourseAssociationRequestSchema
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter()

@router.post("/students/{student_id}/courses")
def associate_course(student_id: int, course: CourseAssociationRequestSchema, db: Session = Depends(get_db)):
    # Logic to associate the course with the student
    pass

@router.get("/students/{student_id}/courses", response_model=List[CourseSchema])
def get_student_courses(student_id: int, db: Session = Depends(get_db)):
    # Logic to retrieve student's courses
    pass

@router.delete("/students/{student_id}/courses/{course_id}")
def remove_course_association(student_id: int, course_id: int, db: Session = Depends(get_db)):
    # Logic to remove course association from student
    pass
```

#### Migration
- Create migration script using Alembic to create the "student_courses" table:
```bash
alembic revision --autogenerate -m "Create student_courses table"
```

This structured implementation plan provides a complete guide for integrating course associations within the existing application while ensuring compatibility and adherence to established practices.