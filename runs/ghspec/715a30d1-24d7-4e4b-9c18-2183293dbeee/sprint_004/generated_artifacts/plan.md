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
# Implementation Plan: Student Entity Web Application

## I. Overview & Purpose

This implementation plan focuses on establishing a relationship between the existing Student entity and a newly introduced Course entity. The main objective is to allow for multiple courses to be associated with each student, improving the educational data management capabilities of the application. This feature will enhance tracking of student enrollments, fostering a more comprehensive and informative educational system.

## II. Architecture & Technology Stack

- **Backend Framework**: FastAPI (for building RESTful APIs).
- **Database**: SQLite (embedded, lightweight database for development).
- **ORM**: SQLAlchemy (for handling database interactions and schema definitions).
- **Dependencies**:
  - FastAPI
  - SQLAlchemy
  - uvicorn (for running the FastAPI application)
- **Environment**: Python 3.11+ 

### Architecture Diagram

```
+--------------------------------------------------------+
|                      FastAPI Application                |
|                                                        |
| +--------------------+    +-----------------------+   |
| | Student Controller   | <->| Student Service        |   |
| +--------------------+    +-----------------------+   |
| | - enroll_student()   |    | - add_enrollment()    |   |
| | - get_student()      |<-->| - find_student()      |   |
| +--------------------+    +-----------------------+   |
|                                                        |
| +--------------------+                                 |
| | Student Repository   |                                |
| +--------------------+                                 |
| | - save()           |                                 |
| | - get_by_id()      |                                |
| +--------------------+                                 |
|                                                        |
+--------------------------------------------------------+
|                         SQLite Database                 |
|                      +------------------+              |
|                      |     students      |              |
|                      |  +---------------+              |
|                      |  | id (pk)       |              |
|                      |  | name          |              |
|                      |  +---------------+              |
|                      |  | created_at    |              |
|                      |  | updated_at    |              |
|                      |  +---------------+              |
|                      |     student_courses |            |
|                      |  +---------------+               |
|                      |  | student_id (fk) |            |
|                      |  | course_id (fk)   |            |
|                      |  +---------------+               |
+--------------------------------------------------------+

```

## III. Module Boundaries & Responsibilities

1. **Student Controller**: 
   - Exposes API endpoints for enrolling students in courses and retrieving student details with course associations.
   - Validates incoming requests and translates them into service calls.

2. **Student Service**: 
   - Contains business logic related to student enrollment in courses.
   - Interacts with the repository to persist and retrieve student data and their associated courses.

3. **Student Repository**: 
   - Responsible for directly accessing the database.
   - Implements CRUD operations related to the `students` table and the new `student_courses` relationship.

## IV. Data Model

### StudentCourse Relationship Entity

```python
class StudentCourse(Base):
    __tablename__ = 'student_courses'

    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)
```

### Updated API Contracts

**POST /students/enroll**
- **Request Body**:
    ```json
    {
        "student_id": 1,
        "course_ids": [1, 2, 3]
    }
    ```
- **Response (200 OK)**:
    ```json
    {
        "student_id": 1,
        "enrolled_courses": [
            {
                "course_id": 1,
                "name": "Course Name 1"
            },
            {
                "course_id": 2,
                "name": "Course Name 2"
            }
        ]
    }
    ```
- **Error Response (400 Bad Request)**:
    ```json
    {
        "error": {
            "code": "E001",
            "message": "Invalid course ID provided."
        }
    }
    ```

**GET /students/{id}**
- **Response (200 OK)**:
    ```json
    {
        "id": 1,
        "name": "Student Name",
        "enrolled_courses": [
            {
                "course_id": 1,
                "name": "Course Name 1"
            }
        ]
    }
    ```
- **Error Response (404 Not Found)**:
    ```json
    {
        "error": {
            "code": "E002",
            "message": "Student not found."
        }
    }
    ```

## V. Implementation Approach

1. **Set Up the FastAPI Application**:
   - Extend the existing Python project to include the enrollment feature.
   - Ensure the current virtual environment is activated and install/update required dependencies: FastAPI, SQLAlchemy, uvicorn.

2. **Define Relationship Models**:
   - Add the new `StudentCourse` ORM model definition in the `models.py` file.

3. **Database Migration Strategy**:
   - Use Alembic to create and manage migrations for the `student_courses` table, ensuring no existing data for students and courses is lost.
   - Example migration command:
     ```bash
     alembic revision --autogenerate -m "Create student_courses table"
     ```

4. **Implement Repository Layer**:
   - Create a new function in `repository.py` to handle enrollments (adding course associations to students).

5. **Implement Service Layer**:
   - Update the `service.py` to handle the logic for enrolling a student in courses and checking for course validity.

6. **Implement API Routes**:
   - Extend existing API routes in `main.py` to handle the new endpoint for enrolling students and retrieving student details along with their enrolled courses.

7. **Input Validation**:
   - Use Pydantic schemas to validate input when enrolling students in courses.

8. **Error Handling**:
   - Implement proper error handling to return clear messages for various error conditions (e.g., invalid student or course).

9. **Testing**:
   - Write unit and integration tests targeting the new functionality, ensuring coverage meets or exceeds the required thresholds.

## VI. Deployment Considerations

- Ensure the application remains stable and can handle requests with the introduction of the new relationship.
- Document the setup process and required changes in the `README.md` file.
- Implement a health check endpoint to verify the status of the new functionality.
- Maintain graceful shutdown conditions, ensuring existing operations can complete before server shutdown.

## VII. Security & Best Practices

- **Data Validation**: Validate all inputs related to course IDs during enrollment.
- **Error Messages**: Define and return clear, actionable error messages for input validation failures.
- **Environment Management**: Use environment variables to handle any sensitive configuration.
- **Structured Logging**: Implement logging for all major actions, particularly around student enrollment operations, without logging sensitive information.

## VIII. Trade-offs and Considerations

- **Migration Complexity**: Since no existing `student_courses` data exists, the migration process should be straightforward and low risk.
- **Backend Focus**: This implementation centers solely on backend changes without disrupting any frontend behaviors or expectations.

## IX. Success Criteria

- Functional requirements must be fully met as outlined in the specification.
- Users must be able to successfully enroll students in courses and retrieve student records, including course details.
- Proper error handling and messaging mechanisms should be in place for all equal endpoints.
- The migration process should execute without data loss.

## X. Conclusion

This implementation plan outlines a clear and structured approach to incorporating the course relationship into the existing student entity management system. By ensuring adherence to best coding practices and maintaining backward compatibility, we allow the application to enhance its educational management capabilities seamlessly.

## Modifications Needed in Existing Files

### 1. `models.py`
- Add a new class definition for the `StudentCourse` relationship model as follows:
```python
class StudentCourse(Base):
    __tablename__ = 'student_courses'

    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)
```

### 2. `repository.py`
- Extend existing repository methods to handle enrollment logic:
```python
def enroll_student_in_courses(student_id: int, course_ids: List[int]):
    # Logic to associate student with the listed courses
```

### 3. `service.py`
- Add a method for handling student enrollments:
```python
def add_enrollment(student_id: int, course_ids: List[int]):
    # Validate course IDs and call repository to create associations
```

### 4. `main.py`
- Add new API routes for enrollment and student retrieval:
```python
@app.post("/students/enroll", response_model=StudentEnrollmentResponse)
def enroll_student(enrollment: StudentEnrollmentRequest):
    # Call service to enroll a student in courses

@app.get("/students/{id}", response_model=StudentResponse)
def get_student(id: int):
    # Call service to retrieve student data along with courses
```

### 5. Migration Script (new)
- Create a migration file to add the `student_courses` table:
```python
def upgrade():
    op.create_table(
        'student_courses',
        sa.Column('student_id', sa.Integer, sa.ForeignKey('students.id'), primary_key=True),
        sa.Column('course_id', sa.Integer, sa.ForeignKey('courses.id'), primary_key=True)
    )
```

By following this detailed implementation plan, the application will effectively extend its functionality to manage course enrollments for students while adhering to existing data structures and business logic.