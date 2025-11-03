# Implementation Plan: Add Course Relationship to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Student Management Web Application

**Version**: 1.0.0  
**Purpose**: To establish a many-to-many relationship between `Student` and `Course` entities, enhancing the student management system's capability to track educational progress.

---

## I. Overview

This implementation plan outlines the necessary changes to the existing architecture to establish a many-to-many relationship between the `Student` and `Course` entities within the student management system. As a result, students will be able to be related to multiple courses, improving course management and student tracking.

## II. Architecture Overview

### 1. Architecture Style
- **Microservices Architecture**: The current microservice design will accommodate the new course-student relationship without disrupting existing service functionality.

### 2. Technology Stack
- **Backend Framework**: FastAPI (Python)
- **Database**: SQLite (for development) transitioning to PostgreSQL for production
- **ORM**: SQLAlchemy
- **Data Validation**: Pydantic
- **Testing Framework**: pytest
- **Documentation**: OpenAPI
- **Environment Management**: Python's `venv`
- **Logging**: Python's built-in logging module

### 3. Module Boundaries
- **API Layer**: New endpoints for managing associations between students and courses.
- **Service Layer**: Logic to manage the relationship between `Student` and `Course`.
- **Data Access Layer**: Update existing models and create new models for the many-to-many relationship.

## III. Functional Specification

### 1. Data Model
1. **Student**
    - Existed as previously defined.
    - Updated associations:
        - `courses`: List of Course entities (many-to-many relationship).

2. **Course**
    - Existed as previously defined.
    - Updated associations:
        - `students`: List of Student entities (many-to-many relationship).

3. **StudentCourse Association**
    - New associative table to manage the many-to-many relationship:
    ```python
    from sqlalchemy import Column, Integer, ForeignKey
    from sqlalchemy.orm import relationship
    from database.db import Base

    class StudentCourse(Base):
        __tablename__ = 'student_courses'
        student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
        course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

        student = relationship("Student", back_populates="courses")
        course = relationship("Course", back_populates="students")
    ```

### 2. API Endpoints
- `POST /students/{student_id}/courses`: Assign one or more courses to a student.
    - Request Body: `{"course_ids": [1, 2, 3]}"
    - Response: `200 OK` with the updated student object.

- `GET /students/{id}`: Retrieve student details, including associated courses.
    - Response: `200 OK` with student information and an array of associated course objects.

- `DELETE /students/{student_id}/courses/{course_id}`: Remove a specific course from a student.
    - Response: `200 OK` with the updated student object after disassociation.

### 3. Error Handling
- If attempting to assign non-existent courses, return: `404 Not Found` with a clear indication of which course IDs were invalid.
- If a student ID does not exist, return: `404 Not Found` when trying to retrieve student details.
- Successful removal of a course should also confirm the course was removed in the response.

## IV. Implementation Approach

### 1. Setup Project Structure
The existing project structure will be updated as follows:

```
student_management/
├── src/
│   ├── main.py
│   ├── models/
│   │   ├── student.py
│   │   ├── course.py
│   │   └── student_course.py  # New associative model
│   ├── services/
│   │   ├── student_service.py
│   │   └── course_service.py
│   ├── controllers/
│   │   ├── student_controller.py
│   │   └── course_controller.py
│   └── database/
│       └── db.py
├── tests/
│   ├── test_student.py
│   ├── test_course.py
│   └── test_student_course.py   # New tests for Student-Course functionality
├── .env.example
├── requirements.txt
└── README.md
```

### 2. Development Tasks
1. **Create the StudentCourse Model**:
   - Implement `models/student_course.py` for associations as shown above.

2. **Update Student Model**:
   - Enhance `models/student.py` to define the relationship with courses using:
     ```python
     courses = relationship("Course", secondary="student_courses", back_populates="students")
     ```

3. **Update Course Model**:
   - Enhance `models/course.py` similarly to define the relationship:
     ```python
     students = relationship("Student", secondary="student_courses", back_populates="courses")
     ```

4. **Database Migration**:
   - Use Alembic to create migrations that include the new `student_courses` table while keeping current `Student` and `Course` records intact.
   - Responsibilities include creating the migration script to set up the associative table with foreign key relationships.

5. **Service Layer for Student-Course Associations**:
   - Implement `services/student_course_service.py` with necessary methods:
     - Method for assigning courses to students.
     - Method for disassociating courses from students.
     - Method to retrieve students with their associated courses.

6. **API Controller for Student-Course Associations**:
   - Implement `controllers/student_course_controller.py` defining endpoints for course assignments and retrievals.

7. **Request Validation**:
   - Utilize Pydantic for validating incoming student-course relation data to ensure correctness in requests.

### 3. Testing
- Implement test cases in `tests/test_student_course.py` including:
  - Tests for successfully assigning courses to students.
  - Tests for disassociating courses and retrieving students.
  - Validate error handling for invalid IDs.

### 4. Documentation
- Update API documentation to include new endpoints for student-course associations.
- Modify `README.md` to reflect final updates and provide endpoint usage examples.

## V. Deployment Considerations

### 1. Environment Configuration
- Ensure updates in `.env.example` reflect database schema changes and environment-specific values.

### 2. Logging Configuration
- Maintain structured logging with context on student-course related actions for monitoring.

### 3. Health Check Endpoint
- Ensure that the health check endpoint includes checks for the new association services.

## VI. Technical Trade-offs

1. **Complexity of Relationships**:
   - Introducing new relationships increases database complexity but is essential for managing many-to-many relationships.

2. **Migration Overhead**:
   - Although introducing migrations may require additional development time, they are crucial for maintaining data integrity across operations.

3. **Performance Impact**:
   - Initial associations may not involve performance optimizations; future enhancements may introduce caching strategies for frequently accessed student-course pairings.

## VII. Success Criteria

- The application manages the associations of courses to students correctly, including all CRUD behaviors.
- API responses demonstrate the intended functionality, especially around error situations.
- Database schema maintains integrity and compatibility, with successful migrations.

---

This implementation plan details a structured approach to introducing a many-to-many relationship between `Student` and `Course` entities, ensuring adherence to best practices and maintaining backward compatibility within the existing system architecture.