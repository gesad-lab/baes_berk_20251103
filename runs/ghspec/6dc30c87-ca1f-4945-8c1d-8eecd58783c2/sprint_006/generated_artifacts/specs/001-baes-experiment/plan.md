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
# Implementation Plan: Student Entity Management Web Application

---

## I. Project Overview

### 1.1 Purpose
To establish a relationship between the Course and Teacher entities, which will enhance administrative efficiency and provide an improved educational experience by allowing the assignment of teachers to specific courses.

### 1.2 Scope
The project will implement the following functionalities:
- API endpoints to assign a teacher to a course and to retrieve course details with the assigned teacher's information.
- Database schema updates to include a foreign key relationship between courses and teachers.

---

## II. Technical Architecture

### 2.1 High-Level Architecture
- **Frontend**: Not applicable for this iteration (API only)
- **Backend**: 
  - Web Framework: FastAPI (Python)
  - Database: SQLite (for simplicity and rapid development)
- **API Layer**: RESTful API
- **Testing Framework**: pytest

### 2.2 Component Diagram
```
+----------------+      +----------------+      +---------------------+
| API Clients     | ---> | FastAPI Server  | ---> | SQLite Database     |
| (Postman, curl) |      |                 |      |                     |
+----------------+      +----------------+      +---------------------+
           |                   |
           |     +------------+
           |     |
           V     V
      [API Responses]
```

---

## III. Technology Stack

### 3.1 Selected Technologies
- **Language**: Python 3.9+
- **Framework**: FastAPI
- **ORM**: SQLAlchemy (for database interaction)
- **Database**: SQLite
- **Testing**: pytest
- **Documentation**: OpenAPI (automatically provided by FastAPI)

### 3.2 Rationale for Technology Choices
- **FastAPI**: Ideal for building APIs rapidly with built-in validation and documentation support.
- **SQLite**: A lightweight and easy-to-manage data store for development.
- **SQLAlchemy**: Provides a powerful and flexible ORM for database interaction.

---

## IV. Module Boundaries and Responsibilities

### 4.1 API Endpoints
1. **PUT /courses/{course_id}/assign_teacher**
   - **Responsibility**: Assign a teacher to a specific course.
   - **Input**: JSON payload containing `{"teacher_id": integer}`.
   - **Output**: 
     - 200 OK with a success message on successful assignment.
     - 400 Bad Request if the course or teacher does not exist.

2. **GET /courses/{course_id}**
   - **Responsibility**: Retrieve details of a specific course, including its assigned teacher.
   - **Input**: Path parameter `{course_id}`.
   - **Output**:
     - 200 OK with course and teacher details if found.
     - 404 Not Found if the specified course ID does not exist.

### 4.2 Data Models
- **Course**
  - **Fields**:
    - `id` (integer, primary key, auto-increment)
    - `name` (string, required)
    - `level` (string, required)
    - `teacher_id` (integer, foreign key referencing Teacher)

- **Teacher** (to be referenced)
  - Previously established.

---

## V. Data Models and API Contracts

### 5.1 Data Model Definition

The `Course` model will be updated to include a teacher relationship:

```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))

    teacher = relationship("Teacher", back_populates="courses")
```

### 5.2 API Request/Response Contracts 

- **PUT /courses/{course_id}/assign_teacher**
  - **Request**: 
    ```json
    {
        "teacher_id": 1
    }
    ```
  - **Response** (on assignment success):
    ```json
    {
        "message": "Teacher assigned to course successfully."
    }
    ```
  - **Response** (on invalid teacher/course):
    ```json
    {
        "error": {
            "code": "E400",
            "message": "Invalid course ID or teacher ID."
        }
    }
    ```

- **GET /courses/{course_id}**
  - **Response** (on success):
    ```json
    {
        "id": 1,
        "name": "Mathematics",
        "level": "Intermediate",
        "teacher": {
            "id": 1,
            "name": "John Doe",
            "email": "john.doe@example.com"
        }
    }
    ```
  - **Response** (not found):
    ```json
    {
        "error": {
            "code": "E404",
            "message": "Course not found."
        }
    }
    ```

---

## VI. Implementation Approach

### 6.1 Development Steps
1. **Set Up Development Environment**
   - Ensure the virtual environment has the necessary dependencies (FastAPI, SQLAlchemy, SQLite).

2. **Update Database Models**
   - Modify the `Course` model to include the `teacher_id` as a foreign key.
   - Ensure the teacher relationship in the model using SQLAlchemy’s relationship feature.

3. **Implement API Endpoints**
   - Develop the `/courses/{course_id}/assign_teacher` PUT endpoint to allow for assigning a teacher to a course.
   - Implement the `/courses/{course_id}` GET endpoint to fetch course details, including the assigned teacher.

4. **Input Validation**
   - Implement checks to validate the existence of the course and teacher IDs during assignment.

5. **Automate Database Schema Creation/Migration**
   - Use Alembic to manage the schema changes ensuring backward compatibility.

6. **Testing**
   - Write unit and integration tests using pytest to ensure that API endpoints function as expected, respecting the defined contracts.

7. **Documentation**
   - Utilize FastAPI’s built-in documentation features for API clarity.

---

## VII. Testing Strategy

### 7.1 Test Types
- **Unit Tests**: Validate functionality of the individual API endpoints for assigning teachers and retrieving course details.
- **Integration Tests**: Verify the interactions between course and teacher data.
- **Contract Tests**: Ensure API responses comply with the specifications.

### 7.2 Success Criteria for Testing
- Achieve a minimum of 70% test coverage across new functionalities with 90%+ on critical paths.

---

## VIII. Risk Management

### 8.1 Potential Risks
- **Validation Errors**: Inadequate error handling could result in ambiguous responses for clients.
- **Database Integrity**: Any schema updates could potentially affect existing data.

### 8.2 Mitigation Strategies
- Implement stringent input validation and comprehensive testing to cover edge cases.
- Backup existing data before performing migrations or schema changes.

---

## IX. Deployment Considerations

### 9.1 Database Migration Strategy
- Use Alembic to handle the creation of the `teacher_id` field in the `courses` table while ensuring existing records are unaltered.

### 9.2 Future Considerations
- Extend functionalities concerning course management (e.g., teacher scheduling and course assignments) in subsequent iterations.

---

## X. Documentation

### 10.1 Required Documentation
- Provide API documentation via FastAPI to clearly articulate the course-teacher management operations.
- Update `README.md` with setup instructions, examples, and API endpoint documentation.

---

## XI. Conclusion

This implementation plan outlines the necessary steps to connect the Course and Teacher entities, enhancing the educational platform's capability to manage course offerings and teacher assignments. By following this structured plan and ensuring rigorous testing and validation, we anticipate a smooth integration that meets the outlined functional requirements.

---

## Modifications to Existing Files

### 11.1 New Code Files
1. **models.py**
   - Update the `Course` model to include a foreign key relationship to the `Teacher`.

2. **main.py**
   - Implement the `/courses/{course_id}/assign_teacher` PUT endpoint.
   - Implement the `/courses/{course_id}` GET endpoint.

### 11.2 Updates to Existing Test Files
1. **tests/test_course_api.py**
   - New tests for the course-teacher assignment and retrieval functionality.
   - Tests will validate input scenarios, successful assignments, and error responses.

2. **tests/test_migrations.py**
   - Ensure to test migrations that add the foreign key relationship.

### 11.3 Database Migration Strategy
Implement Alembic migration to add the `teacher_id` field to the `courses` table while ensuring the integrity of existing data. The migration script may resemble:

```python
def upgrade():
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), sa.ForeignKey('teachers.id')))
```

### Example Test File Modifications
- In `tests/test_course_api.py`, new test cases will be introduced to validate the behaviors for:
  1. Assigning a teacher to a course.
  2. Fetching course details with the assigned teacher.
  3. Handling invalid assignments. 

By ensuring these changes are well documented and thoroughly tested, we position ourselves to deliver a more robust and integrated educational platform.