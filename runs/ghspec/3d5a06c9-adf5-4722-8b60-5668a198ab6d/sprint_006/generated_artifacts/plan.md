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
# Implementation Plan: Student Management Web Application

## I. Overview

This implementation plan outlines the technical architecture, technology stack, and implementation approach for establishing a relationship between the **Course** entity and the newly introduced **Teacher** entity in the existing Student Management Web Application. This relationship is aimed at enhancing course management by associating each course with its respective teachers, which supports better tracking and administration of courses.

## II. Technology Stack

- **Backend Framework**: FastAPI (Python 3.11+)
- **Database**: SQLite (embedded database)
- **Data Access**: SQLAlchemy (for ORM interaction with SQLite)
- **API Documentation**: FastAPI's automatic OpenAPI support
- **Testing Framework**: pytest for unit and integration testing
- **Environment Management**: `venv` for virtual environment management
- **Dependency Management**: `requirements.txt` for Python dependencies

## III. Architecture

### A. Module Structure

The project structure will accommodate the new teacher-course relationship. The modified structure is as follows:

```
/student_management_app
│
├── src/                     # Source code for the application
│   ├── main.py              # Entry point for the FastAPI application
│   ├── models.py            # Database models (SQLAlchemy)
│   ├── schemas.py           # Pydantic schemas for request/response validation
│   ├── routes/              # API route handlers
│   │   ├── student_routes.py # Endpoint definitions related to students
│   │   ├── course_routes.py  # Endpoint definitions related to courses, updated for new relationship
│   │   └── teacher_routes.py  # Existing endpoint definitions for teachers
│   └── database.py          # Database connection and setup
│
├── tests/                   # Testing files
│   ├── test_student_routes.py # Tests for student API routes
│   ├── test_course_routes.py  # Tests for course API routes
│   ├── test_teacher_routes.py  # Tests for teacher API routes
│   └── test_database.py      # Tests for database interactions
│
├── .env.example              # Example environment variables
├── requirements.txt          # Python dependencies
└── README.md                 # Documentation for setup and usage
```

### B. Module Responsibilities

1. **models.py**: Update the SQLAlchemy model for Course to include the `teacher_id` field for establishing a foreign key relationship with the Teacher entity.
2. **schemas.py**: Update existing Pydantic schemas to encompass request and response validation for teacher assignment to courses.
3. **routes/course_routes.py**: Implement the `POST /courses/{courseId}/assignTeacher` API endpoint to associate a teacher with a course.
4. **database.py**: Modify the database initialization process to include the new foreign key relationship in the Course table.

## IV. API Design

### A. API Endpoints

1. **Associate Teacher with Course**
   - **Endpoint**: `POST /courses/{courseId}/assignTeacher`
   - **Request Body**:
     ```json
     {
       "teacherId": 1
     }
     ```
   - **Response**:
     ```json
     {
       "id": "integer",
       "name": "Course Name",
       "teacher_id": "integer"
     }
     ```
   - **Error Handling**: On invalid teacher ID:
     ```json
     {
       "error": {
         "code": "E001",
         "message": "Teacher with ID not found.",
         "details": {}
       }
     }
     ```

### B. Error Handling

- Consistent error responses will be utilized for handling invalid inputs, ensuring all responses match the error handling specification provided in the previous sections.

## V. Database Design

### A. Schema Modification

- **Table**: Courses
  - **New Column**:
    - `teacher_id`: INTEGER (nullable, foreign key referencing the Teacher entity).

### B. Database Migration Strategy

- A database migration will be created to add the `teacher_id` column while ensuring existing Student and Course data remains intact. This will be implemented using Alembic.

```bash
# Migration command
alembic revision --autogenerate -m "Add teacher_id to Courses"
```

The migration script will include:
```python
def upgrade():
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))
    op.create_foreign_key('fk_course_teacher', 'courses', 'teachers', ['teacher_id'], ['id'], ondelete='SET NULL')

def downgrade():
    op.drop_constraint('fk_course_teacher', 'courses', type_='foreignkey')
    op.drop_column('courses', 'teacher_id')
```

## VI. Success Criteria

1. The API successfully validates input and associates a teacher to a course, returning valid JSON responses with course attributes.
2. The `teacher_id` column is successfully added to the database schema without data loss or corruption, and all existing Student and Course data remains intact after the migration.
3. Appropriate error messages are returned for invalid input scenarios (non-existent teacher associations).

## VII. Testing Plan

### A. Test Coverage

- Aim for a minimum of 70% coverage across new functionalities.
- Specifically test for successful association of a teacher to a course, along with boundary tests for invalid teacher IDs.

### B. Testing Structure

- **Unit Tests**: Tests for the `assignTeacher` functionality within the `tests/test_course_routes.py`.

```python
# Example test in tests/test_course_routes.py
def test_assign_teacher_to_course(client):
    response = client.post('/courses/1/assignTeacher', json={"teacherId": 1})
    assert response.status_code == 200
    assert response.json()["teacher_id"] == 1

def test_assign_teacher_non_existent(client):
    response = client.post('/courses/1/assignTeacher', json={"teacherId": 999})
    assert response.status_code == 404
    assert response.json()["error"]["code"] == "E001"  # Code for non-existent teacher
```

## VIII. Deployment Considerations

- Ensure compatibility with the existing Python 3.11+ and SQLite versions specified.
- Update the `.env.example` file to include any new environment variables if needed for configuration.
- Maintain continuity in automated deployment scripts to include new database migration commands.

## IX. Documentation

- Update the README.md to include setup steps, usage examples, and API endpoint documentation for the new teacher-course association functionality.

## X. Technical Trade-offs and Decisions

1. **Adhering to the Existing Tech Stack**: The decision to utilize FastAPI and SQLite was crucial in maintaining consistency and compatibility across the application. This also minimizes the learning curve for existing developers.
2. **SQLAlchemy for ORM**: This choice allows for straightforward integration and management of relationships between Course and Teacher entities while maintaining established practices.
3. **Future Scalability**: Establishing this relationship prepares the architecture for potential future enhancements, like managing multiple teachers per course, without major structural changes.

This implementation plan provides a comprehensive outline for integrating the Teacher relationship with Courses while aligning with existing functionalities, ensuring maintainability, and adhering to established best practices.