# Implementation Plan: Add Course Relationship to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:  
# Implementation Plan: Create Course Entity

---

## I. Project Overview
This implementation plan details the architectural modifications, technology stack, module boundaries, and technical specifications required to establish a relationship between Student and Course entities. This feature enables a Student to enroll in multiple Courses, facilitating enhanced tracking of students' educational engagements. The implementation promotes scalability for future functionalities such as enrolling students in courses and retrieving their course data.

---

## II. Technology Stack
- **Backend Framework**: FastAPI (Python) - For building the RESTful API.
- **Database**: SQLite - A lightweight database for data persistence.
- **HTTP Client for Testing**: HTTPX - For performing API tests.
- **Asynchronous Support**: Uvicorn - An ASGI server to run the FastAPI application.
- **ORM**: SQLAlchemy - For database interactions.

---

## III. Architecture & Modules

### 3.1 High-Level Architecture
- **API Layer**: Handles all incoming HTTP requests related to students and courses and routes them to the appropriate service.
- **Service Layer**: Contains business logic for enrolling students in courses and retrieving their course records.
- **Data Access Layer**: Interacts with the SQLite database to perform CRUD operations on the `student_courses` join table.

### 3.2 Module Responsibilities

1. **API Module (`api/`)**:
   - Endpoint definitions for enrolling a student in a course and retrieving a student’s courses.
   - Input validation and crafting of JSON responses.

2. **Service Module (`services/`)**:
   - Business logic for enrolling students in courses and retrieving courses linked to a student, including necessary validations.

3. **Data Access Module (`db/`)**:
   - Database model for the `student_courses` join table.
   - Functions for database interactions, including schema updates.

---

## IV. Data Models

### SQLite Database Model

```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class StudentCourse(Base):
    __tablename__ = 'student_courses'

    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="students")
```

### Updates to Existing Models
Ensure that the `Student` and `Course` models are updated to establish relationships with `StudentCourse`.

```python
# In Student Model
class Student(Base):
    __tablename__ = 'students'
    
    # Existing fields...
    
    courses = relationship('StudentCourse', back_populates='student')

# In Course Model
class Course(Base):
    __tablename__ = 'courses'
    
    # Existing fields...
    
    students = relationship('StudentCourse', back_populates='course')
```

---

## V. API Endpoints

### 5.1 API Design

1. **POST `/students/{student_id}/courses`**:
   - **Path Parameter**:
     - `student_id` (int, required)
   - **Request Body**:
     - `course_id` (int, required)
   - **Response**:
     ```json
     {
       "message": "Student enrolled in course successfully",
       "student": {
         "id": 1,
         "name": "John Doe",
         "courses": [
           {
             "course_id": 101,
             "name": "Mathematics",
             "level": "Introductory"
           }
         ]
       }
     }
     ```
   - **Error Handling**:
     - Status 400: Invalid course ID.
     ```json
     {
       "error": {
         "code": "E001",
         "message": "Invalid course ID."
       }
     }
     ```

2. **GET `/students/{student_id}/courses`**:
   - **Path Parameter**:
     - `student_id` (int, required)
   - **Response**:
   ```json
   [
     {
       "course_id": 101,
       "name": "Mathematics",
       "level": "Introductory"
     },
     {
       "course_id": 102,
       "name": "Physics",
       "level": "Intermediate"
     }
   ]
   ```

---

## VI. Implementation Steps

1. **Project Update**:
   - Maintain the existing project structure:
     ```
     course-management/
     ├── api/
     ├── db/
     ├── services/
     ├── main.py
     ├── requirements.txt
     └── README.md
     ```

2. **Update Requirements**:
   - Ensure existing dependencies are sufficient. No new packages are needed for this implementation. Verify `requirements.txt` includes necessary libraries:

   ```plaintext
   fastapi
   uvicorn
   sqlalchemy
   httpx
   ```

3. **Database Schema Migration**:
   - Create a migration script to add the `student_courses` join table without affecting existing Student and Course data:
   ```python
   from sqlalchemy import create_engine, MetaData, Table, Column, Integer, ForeignKey

   engine = create_engine('sqlite:///courses.db')
   metadata = MetaData(bind=engine)

   student_courses_table = Table('student_courses', metadata,
        Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
        Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
   )

   metadata.create_all(engine)  # This will create the table
   ```

4. **Implement API Endpoints**:
   - Define API endpoints for enrolling a student in a course and retrieving a student's courses in the `api` module. Use Pydantic for request validation, ensuring that `course_id` is given when enrolling a student.

5. **Implement Business Logic**:
   - Create service functions:
     - `enroll_student_in_course(student_id, course_id)` to handle course enrollment with necessary validations.
     - `get_student_courses(student_id)` to retrieve a list of courses for the given student.

6. **Testing**:
   - Write unit tests for service functions ensuring input validations.
   - Implement integration tests for API endpoints using `httpx`.

---

## VII. Testing Strategy

### 7.1 Test Coverage
- Aim for at least 70% coverage on business logic.
- Ensure critical paths (student enrollment and course retrieval) have 90%+ coverage.

### 7.2 Types of Tests
- **Unit Tests**: Validate functions for adding enrollments and retrieving student courses, ensuring proper functioning of validations.
- **Integration Tests**: Validate API endpoints for enrolling and retrieving courses for a student.

---

## VIII. Error Handling and Input Validation

### 8.1 Input Validation
- Validate that `course_id` is provided during enrollment. 
- Implement checks to ensure that the `student_id` and `course_id` are valid before processing the request; return error responses if not valid.

### 8.2 Error Responses
- Structure error responses to match JSON format as outlined in the API Design.

---

## IX. Security Considerations

### 9.1 Data Protection
- Input sanitization to prevent SQL injection and ensure data integrity.
- Use of `.env` for managing sensitive configurations will be implemented in future iterations.

---

## X. Deployment Considerations

### 10.1 Local Development
- Ensure that the application starts successfully, creates the required database schema, and completes migrations without issues. Validate basic functionality.

---

## XI. Logging & Monitoring

### 11.1 Basic Logging
- Set up basic logging for API interactions, focusing on tracking requests and responses, while recognizing that extensive logging is beyond the scope of this phase.

---

## XII. Conclusion

This implementation plan outlines the necessary steps to establish a relationship between Student and Course entities within the educational management system. It ensures that new functionalities integrate smoothly with existing operations, allowing for further developments in course management and student engagement moving forward.

**Existing Code Files:**

- **File**: `api/students.py` (to be updated)
- **File**: `services/student_service.py` (to be created)
- **File**: `tests/test_students.py` (to be created)

**Modifications Needed**:
1. **In `api/students.py`**:
   - Add new endpoints for enrolling students and retrieving courses.

2. **In `services/student_service.py`**:
   - Create business logic functions for enrolling students and retrieving course information.

3. **In `tests/test_students.py`**:
   - Add test cases covering the new API endpoints and service logic.

The outlined strategy ensures backward compatibility with existing data models and functionality, while integrating new features seamlessly into the application architecture.