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

## I. Overview
This implementation plan outlines the architecture and necessary steps for adding a relationship between the `Student` entity and `Course` entity. The goal is to allow multiple Course IDs to be linked to each Student, enhancing the application's management of educational data and enabling users to track student enrollments effectively.

## II. Architecture
- **Architecture Style**: Microservices-oriented design focused on a single service managing Students and Courses.
- **Framework**: FastAPI will be used for creating RESTful APIs.
- **Database**: SQLite, leveraging its simplicity for development.
- **Response Format**: JSON for all API interactions.

### Module Boundaries
1. **API Layer**: This will handle all HTTP requests concerning both Students and their associated Courses.
2. **Service Layer**: Contains business logic for linking Students and Courses, specifically for handling enrollments and validation.
3. **Data Access Layer**: Responsible for all database interactions, including fetching and saving Student and Course enrollment data using SQLAlchemy.
4. **Validation Layer**: Utilizes Pydantic to validate incoming data to ensure correct Course IDs are provided.

## III. Technology Stack
- **Programming Language**: Python 3.11+
- **Framework**: FastAPI
- **Database**: SQLite
- **ORM**: SQLAlchemy for database interactions
- **Testing**: pytest for unit and integration testing
- **Dependency Management**: Poetry or pip for Python package management

## IV. Data Model
### Course Entity
```python
from sqlalchemy import Column, Integer, String
from database import Base

class Course(Base):
    __tablename__ = 'courses'

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
```

### Junction Table for Student-Course Relationship
```python
from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.orm import relationship
from database import Base

student_courses = Table('student_courses', Base.metadata,
    Column('student_id', String, ForeignKey('students.id'), primary_key=True),
    Column('course_id', String, ForeignKey('courses.id'), primary_key=True)
)
```

### Migration Strategy
To introduce the many-to-many relationship:
1. Create a migration script using Alembic to add `student_courses` junction table:
   ```bash
   alembic revision --autogenerate -m "Create student_courses table"
   ```
2. The migration will ensure existing `Student` and `Course` records are preserved.

## V. API Specification
### Endpoints
- **Link Student to Courses**
  - **Endpoint**: `PATCH /students/{student_id}`
  - **Request Body**: 
    ```json
    {
        "courses": ["course_id_1", "course_id_2"]
    }
    ```
  - **Success Response**: 
    ```json
    {
        "id": "student_id",
        "name": "John Doe",
        "courses": ["course_id_1", "course_id_2"]
    }
    ```
  - **Error Response** (invalid course IDs):
    ```json
    {
        "error": {
            "code": "E002",
            "message": "Invalid Course IDs: course_id_3"
        }
    }
    ```

- **Retrieve Student with Courses**
  - **Endpoint**: `GET /students/{student_id}`
  - **Success Response**: 
    ```json
    {
        "id": "student_id",
        "name": "John Doe",
        "courses": ["course_id_1", "course_id_2"]
    }
    ```

## VI. Implementation Steps
1. **Environment Setup**
   - Validate that Python packages such as `FastAPI`, `SQLAlchemy`, and `Alembic` are installed and functional.

2. **Project Structure Modifications**
   ```plaintext
   student_api/
   ├── src/
   │   ├── main.py              # Modify to include new PATCH and GET methods for Student courses
   │   ├── models.py            # Update to include Junction table (`student_courses`) and Course class
   │   ├── crud.py              # Add methods for linking and retrieving courses for students
   │   ├── schemas.py           # Create Pydantic model for PATCH requests while linking courses
   │   ├── database.py          # Ensure connection and base are set up correctly (No change needed)
   │   ├── migrations/           # Directory for Alembic containing migration scripts
   ├── tests/
   │   ├── test_students.py      # Add tests for linking courses and retrieving student information with courses
   ├── .env.example              # Configuration for environment variables
   ├── requirements.txt          # Update to reflect new dependencies if required
   └── README.md                 # Update to reflect the new course management functionality
   ```

3. **Code Implementation Changes**
   - **models.py**: Add the `student_courses` junction table code as specified.
   - **crud.py**: Implement `link_courses_to_student` for updating a Student's courses and `get_student_with_courses` for fetching Student data with associated courses.
   - **schemas.py**: Create a schema for validating PATCH requests to link courses to a student.
   - **main.py**: Update with new endpoints, linking request handlers to the service layer.

4. **Validation and Error Handling**
   - Implement Pydantic validations in the API layer when PATCH requests are received to ensure all Course IDs exist.
   - Return structured error responses for invalid Course entries.

5. **Testing**
   - Expand `tests/test_students.py` to include tests for course linking and retrieval functionalities.
   - Ensure high test coverage on both success paths and validation error scenarios.

6. **Documentation**
   - Revise the `README.md` to describe API capabilities related to course linking, including relevant endpoints, request, and response formats.

## VII. Deployment Considerations
- Validate the application starts and ensures all required environment variables are set.
- The migration strategy must not disrupt existing data, and existing students should be retrievable post-migration.

## VIII. Scalability & Future Improvements
- Future updates could include an endpoint to manage course lifecycle (create/update/delete courses).
- Transitioning to a more robust database such as PostgreSQL could facilitate scale.

## IX. Technical Trade-offs
- Integrating a many-to-many relationship necessitates judicious API response design and validation logic.
- Using SQLite promotes ease of development but may not scale well under concurrent loads; future transitions should aim for more scalable architecture.

## X. Conclusion
This implementation plan provides a coherent approach to integrating the Course relationship with the Student entity in the existing system, following best practices using FastAPI. These proposed steps align with the defined specifications to ensure a seamless transition while maintaining compatibility with existing data models.

Existing Code Files:
No code files found from previous sprint.