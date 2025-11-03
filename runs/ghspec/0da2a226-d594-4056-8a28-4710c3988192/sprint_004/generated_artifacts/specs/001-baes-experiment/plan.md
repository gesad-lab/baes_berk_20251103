# Implementation Plan: Add Course Relationship to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Email Field to Student Entity

## Version
1.0.1

## Overview
This implementation plan outlines the steps required to establish a relationship between the existing Student and Course entities within the Student Entity Web Application. Students will now have the ability to enroll in multiple courses, allowing advanced data management for educational offerings and an improved framework for future functionalities such as reporting and analytics.

## Architecture Overview
- **Architecture Pattern**: RESTful microservice (consistent with prior implementations)
- **Components**:
  - API Layer: New endpoints for student course enrollment and retrieval.
  - Service Layer: Business logic for managing course enrollments.
  - Data Layer: Existing SQLite database schema updated to include an association between Students and Courses.
- **Deployment**: Remains on the existing lightweight server setup, no infrastructure changes required.

## Technology Stack
- **Backend Framework**: FastAPI (Python)
- **Database**: SQLite
- **ORM**: SQLAlchemy (for database interactions)
- **Data Format**: JSON
- **Testing Framework**: pytest
- **Containerization**: Docker (optional for deployment)
- **Version Control**: Git

## Module Boundaries and Responsibilities

### 1. API Layer
- **Module Name**: `api`
- **Responsibilities**:
  - Define new routes for enrolling a student in a course and retrieving courses for a student.
  - Validate incoming requests for student enrollments.

### 2. Service Layer
- **Module Name**: `services`
- **Responsibilities**:
  - Implement business logic in a new `enrollment_service.py` to handle enrolling students in courses.

### 3. Data Layer
- **Module Name**: `models`
- **Responsibilities**:
  - Update the `Student` entity schema to incorporate a relationship with the new `Course` entity.
  - Manage database migrations ensuring existing records are preserved.

## Implementation Approach

### Project Structure
```
student_entity_app/
│
├── src/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── routes.py          # Update API endpoints for student course enrollments
│   │   └── dependencies.py     # Dependency functions
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── student_service.py  # Existing student service logic
│   │   └── enrollment_service.py # New business logic for enrolling courses
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── models.py           # Update to include course enrollment relationship
│   │
│   ├── main.py                 # Application entry point
│   └── config.py               # Configuration settings
│
├── tests/
│   ├── __init__.py
│   ├── test_routes.py          # Unit tests for API endpoints
│   ├── test_services.py        # Unit tests for business logic
│   └── test_enrollment.py      # New tests for course enrollment feature
│
├── .env.example                 # Sample environment variables
├── requirements.txt             # Project dependencies
└── README.md                    # Documentation
```

### Step-by-Step Implementation

1. **Update Data Models**
   - Modify `models.py` to define an association between `Student` and `Course` entities:
   ```python
   from sqlalchemy import Column, Integer, String, ForeignKey
   from sqlalchemy.ext.declarative import declarative_base
   from sqlalchemy.orm import relationship

   Base = declarative_base()

   class Student(Base):
       __tablename__ = 'students'

       id = Column(Integer, primary_key=True, autoincrement=True)
       name = Column(String, nullable=False)
       enrolled_courses = relationship("Course", secondary="enrollments")

   class Course(Base):
       __tablename__ = 'courses'

       id = Column(Integer, primary_key=True, autoincrement=True)
       name = Column(String, nullable=False)
       level = Column(String, nullable=False)
 
   class Enrollment(Base):
       __tablename__ = 'enrollments'
       student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
       course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)
   ```

2. **Database Migration Strategy**
   - Utilize Alembic for managing database schema changes. Create a new migration that:
     - Adds the `enrollments` table for associating students with courses.
     - Ensures no data loss occurs for existing Student records.
   ```bash
   alembic revision --autogenerate -m "Add enrollment relationship between Student and Course"
   ```

3. **Implement Services Logic**
   - In a new `enrollment_service.py`, implement:
     - `enroll_student(student_id: int, course_id: int)`: to enroll a student in a course.
     - `get_student_courses(student_id: int)`: to retrieve courses associated with a student.
   ```python
   def enroll_student(student_id: int, course_id: int):
       # Logic to enroll student in a course
       # Check if the course exists and if the student is already enrolled.
   ```

4. **Define API Endpoints**
   - In `routes.py`, create new endpoints:
   - **POST** `/students/{student_id}/courses` to enroll a student:
     ```json
     {
       "course_id": 1
     }
     ```
   - **GET** `/students/{student_id}/courses` to retrieve a student's courses:
     ```json
     {
       "courses": [
         {
           "id": 1,
           "name": "Mathematics",
           "level": "Advanced"
         }
       ]
     }
     ```

5. **Implement Input Validation**
   - Use Pydantic schemas to validate the `course_id` provided for enrollments.

6. **Error Handling**
   - Ensure all errors are handled and meaningful responses are returned for invalid course IDs or duplicate enrollments.

7. **Testing**
   - Create a new testing file `test_enrollment.py` to validate all course enrollment scenarios:
   ```python
   def test_enroll_student_in_valid_course():
       response = client.post("/students/1/courses", json={"course_id": 1})
       assert response.status_code == 201  # Created
   ```

8. **Documentation**
   - Update `README.md` to include instructions for the new course enrollment APIs, showcasing example requests and responses.

## Data Models

### Existing Student Entity
```json
{
  "id": "integer (primary key, automatically generated)",
  "name": "string (required)",
  "enrolled_courses": "list of Course IDs (relationship field)"
}
```

### New Enrollment Table
```json
{
  "student_id": "integer (foreign key reference)",
  "course_id": "integer (foreign key reference)"
}
```

## API Contracts

### Enroll Student in Course
- **Endpoint**: POST `/students/{student_id}/courses`
- **Request Body**:
  ```json
  {
    "course_id": 1
  }
  ```
- **Response** (201 Created):
  ```json
  {
    "message": "Student successfully enrolled in the course."
  }
  ```

### Retrieve Student's Courses
- **Endpoint**: GET `/students/{student_id}/courses`
- **Response**:
  ```json
  {
    "courses": [
      {
        "id": 1,
        "name": "Mathematics",
        "level": "Advanced"
      }
    ]
  }
  ```

### Error Responses
- **Course Not Found** (404):
```json
{
  "error": {
    "code": "E003",
    "message": "Course not found."
  }
}
```
- **Already Enrolled** (409):
```json
{
  "error": {
    "code": "E004",
    "message": "Student is already enrolled in this course."
  }
}
```

## Success Criteria
- All user scenarios pass without errors and the expected behavior is confirmed.
- The application correctly reflects student-course associations within the database.
- All API responses are valid JSON and correctly format the required course information.
- The database schema is successfully updated, preserving existing records.

## Final Considerations
### Scalability
- Plan for potential migration to a more robust database solution (e.g., PostgreSQL) as usage increases.

### Security
- Implement rigorous input validation and error handling to avoid common vulnerabilities.

### Maintainability
- Ensure adherence to clean code practices and maintain a clear project structure for ease of future modifications.

### Logging and Monitoring
- Implement structured logging within the API to track each enrollment action and its outcome.

--- 

This implementation plan provides a comprehensive guide to adding the enrollment feature to the Student entity, ensuring integration with existing functionalities and maintaining high development standards.