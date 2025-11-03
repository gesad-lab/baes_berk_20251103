# Implementation Plan: Add Teacher Relationship to Course Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Teacher Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Course Relationship to Student Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Course Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Email Field to Student Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Student Entity Web Application

**Version**: 1.0.0  
**Purpose**: To implement the relationship between the Course entity and the Teacher entity, enhancing course management functions and enabling clarity on course assignments.

## 1. Architecture Overview

### 1.1 High-Level Architecture
This implementation will establish a back-end relationship between the Course and Teacher entities within the existing architecture:
- **API Layer**: Integrate new endpoints for updating courses and retrieving course details along with teacher associations.
- **Service Layer**: Contains business logic for managing the course-teacher associations.
- **Data Access Layer**: Manages interactions with the SQLite database for the updated Course and Teacher tables.

### 1.2 Technology Stack
- **Programming Language**: Python 3.11+
- **Web Framework**: FastAPI
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Testing Framework**: Pytest
- **JSON Validator**: Pydantic (used with FastAPI)

## 2. Module Boundaries and Responsibilities

### 2.1 API Layer
- **Endpoints**:
  - `PATCH /courses/{course_id}`: Update an existing course with a teacher association.
  - `GET /courses/{course_id}`: Retrieve course details along with associated teacher information.

### 2.2 Service Layer
- **Responsibilities**:
  - Handle requests for associating a teacher to a course and for retrieving course-teacher data, including validation checks.

### 2.3 Data Access Layer
- **Responsibilities**:
  - Interact with the SQLite database to manage the courses and teachers relational data.

## 3. Data Model

### 3.1 Course Model Update
1. Update the existing Course entity to include a foreign key to the Teacher entity.
```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)

    teacher = relationship("Teacher", back_populates="courses")
```

### 3.2 Teacher Relationship
In the Teacher model:
```python
class Teacher(Base):
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    
    courses = relationship("Course", back_populates="teacher")
```

## 4. API Contract

### 4.1 Request and Response Structure
#### Update Course Endpoint
- **Request**: `PATCH /courses/{course_id}`
```json
{
  "teacher_id": 1
}
```
- **Response (Success)**: `200 OK`
```json
{
  "id": 2,
  "title": "Physics 101",
  "description": "Introduction to Physics",
  "teacher": {
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
}
```
- **Response (Error)**: `404 Not Found`
```json
{
  "error": {
    "code": "E002",
    "message": "Teacher ID does not exist."
  }
}
```

#### Retrieve Course with Teacher Endpoint
- **Request**: `GET /courses/{course_id}`
- **Response (Success)**: `200 OK`
```json
{
  "id": 2,
  "title": "Physics 101",
  "description": "Introduction to Physics",
  "teacher": {
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
}
```

## 5. Implementation Approach

### 5.1 Development Workflow
1. **Modify the Project Structure**:
   - Extend the existing `src/` directory to include updates for course handling.

2. **Database Migration Strategy**:
   - Create a migration script (using Alembic) to add the new `teacher_id` column to the `courses` table and establish the foreign key relationship.
   ```sql
   ALTER TABLE courses ADD COLUMN teacher_id INTEGER NULL;
   ALTER TABLE courses ADD FOREIGN KEY (teacher_id) REFERENCES teachers (id);
   ```

3. **Implement API Changes**:
   - Add the `PATCH /courses/{course_id}` endpoint for associating a teacher with a course.
   - Add the `GET /courses/{course_id}` endpoint to fetch course details along with the associated teacher.

### 5.2 Example Pydantic Models for Request Validation
#### Course Update Request
```python
from pydantic import BaseModel

class CourseUpdate(BaseModel):
    teacher_id: int
```

### 5.3 Testing
- Write unit tests for the course update and retrieval endpoints.
- Ensure at least 70% coverage for business logic, especially for error handling related to invalid teacher IDs.

### 5.4 Documentation
- Update `README.md` to detail new course API endpoints and usage examples as well as migration processes.

### 5.5 Error Handling
- Validate teacher IDs on updates.
- Return appropriate error messages for invalid or non-existent teacher references.

## 6. Performance Considerations
- Ensure that the API response time remains under 2 seconds for both updating and fetching course-teacher associations.
- Examine query optimization for fetching course details with associated teacher information.

## 7. Security Considerations
- Adhere to appropriate validation and sanitization practices throughout API endpoints.
- Ensure compliance with security protocols for sensitive data, especially in the Teacher entity.

## 8. Deployment Considerations
- Update `.env.example` as needed to reflect configuration changes related to the new Teacher relationship.

## 9. Success Criteria Validation
- Validate automated tests to ensure that the teacher can be associated with a course and that course retrieval includes correct teacher details, meeting performance benchmarks.

## 10. Future Scalability
- Designs should accommodate future features such as expanded course management and teacher performance evaluations.

## Modifications to Existing Files
### 1. Update Course Model
In `src/models.py`:
- Update the Course class to include the `teacher_id` foreign key mapping.

### 2. Update API Endpoints
In `src/main.py`:
- Add the `PATCH /courses/{course_id}` endpoint for linking teachers to courses.
- Update the `GET /courses/{course_id}` endpoint to return associated teacher data.

### 3. Create Tests for API Endpoints
In `tests/test_api/test_course_api.py`:
- Develop tests for course update functionality to check teacher associations and retrieval.

### 4. Input Validation Test Cases
In `tests/test_services/test_course_service.py`:
- Implement tests for handling non-existent teacher associations during course updates.

This implementation plan lays out the necessary steps to establish a relationship between the Course and Teacher entities, including API modifications, testing, and adherence to performance and security standards. It ensures backward compatibility with existing data models and facilitates future enhancements.