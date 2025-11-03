# Implementation Plan: Add Teacher Relationship to Course Entity

---

## INCREMENTAL DEVELOPMENT CONTEXT

### Previous Sprint Plan:
# Implementation Plan: Create Teacher Entity

---

## INCREMENTAL DEVELOPMENT CONTEXT

### Previous Sprint Plan:
# Implementation Plan: Add Course Relationship to Student Entity

---

## INCREMENTAL DEVELOPMENT CONTEXT

### Previous Sprint Plan:
# Implementation Plan: Create Course Entity

---

## INCREMENTAL DEVELOPMENT CONTEXT

### Previous Sprint Plan: 
# Implementation Plan: Add Email Field to Student Entity

---

## INCREMENTAL DEVELOPMENT CONTEXT

### Previous Sprint Plan: 
# Implementation Plan: Student Entity Management Web Application

## Version
1.0.0

## Purpose
To establish a relationship between the Course entity and the Teacher entity within the existing educational management system, improving resource management for academic courses and facilitating assignments.

## Technology Stack
- **Backend Framework**: Flask (Python 3.11+)
- **Database**: SQLite
- **API Format**: JSON
- **Data Storage**: SQLAlchemy ORM

## Module Structure
### 1. Database Module
- **Responsibility**: Manage the SQLite database schema, including modifications to the `courses` table to include the `teacher_id` foreign key.
- **Components**:
  - `models.py`: Update the `Course` model to include a foreign key reference to Teacher.
  - `database.py`: Handle database initialization and migrations for modifying the `courses` table.

### 2. API Module
- **Responsibility**: Define endpoints and manage requests related to course and teacher assignments.
- **Components**:
  - `routes.py`: Add routes for assigning teachers to courses and retrieving course details.
  - `validators.py`: Implement input validation for teacher assignment requests.

### 3. Main Application Module
- **Responsibility**: Serve as the application entry point and configuration management.
- **Components**:
  - `app.py`: Initialize the Flask app and database, ensuring new routes for course operations are registered.

## Data Models
### Updated Course Model
```python
# models.py
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Course(Base):
    __tablename__ = 'courses'
    course_id = Column(Integer, primary_key=True)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))  # Foreign key to Teacher
    teacher = relationship("Teacher", back_populates="courses")  # Set up relationship

class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    courses = relationship("Course", back_populates="teacher")  # Bidirectional relationship
```

## API Contracts
### 1. Assign Teacher to Course
- **Endpoint**: `PUT /courses/{course_id}/assign-teacher`
- **Request Body**:
```json
{
  "teacher_id": "teacher_id"
}
```
- **Response on Success**:
```json
{
  "message": "Teacher assigned successfully to the course."
}
```
- **Response on Error (e.g., Invalid Teacher ID)**:
```json
{
  "error": {
    "code": "E002",
    "message": "Invalid Teacher ID provided."
  }
}
```
- **Status Codes**:
  - 200 OK (on success)
  - 400 Bad Request (if validation fails, e.g., missing or invalid `teacher_id`)

### 2. Retrieve Course Information
- **Endpoint**: `GET /courses/{course_id}`
- **Response**:
```json
{
  "course_id": 1,
  "teacher": {
    "id": 2,
    "name": "Teacher Name",
    "email": "teacher@example.com"
  }
}
```
- **Status Code**:
  - 200 OK if found
  - 404 Not Found if course doesn't exist

## Key Implementation Details
1. **Database Schema Update**: 
   - Modify the existing `courses` table to add a new nullable `teacher_id` column that references `teachers.id`. Implement this change through a migration script.

2. **Migration Strategy**:
   - Utilize SQLAlchemy migration tools (Alembic) to create and manage migrations ensuring existing data stays intact.
   ```python
   from alembic import op
   import sqlalchemy as sa

   def upgrade():
       op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))
       op.create_foreign_key('fk_teacher_id', 'courses', 'teachers', ['teacher_id'], ['id'])

   def downgrade():
       op.drop_constraint('fk_teacher_id', 'courses', type_='foreignkey')
       op.drop_column('courses', 'teacher_id')
   ```

3. **Input Validation**:
   - Implement validation in `validators.py` to ensure the `teacher_id` is present and corresponds to a valid existing teacher when assigning them to a course.

4. **Error Handling**:
   - Create structured error responses for validation failures when assigning teachers, ensuring detailed error messages are returned.

5. **Backward Compatibility**:
   - Ensure existing functionalities for Student and Course entities remain functional and accessible. The addition of the `teacher_id` will enable potential future features without disrupting current operations.

## Scalability and Maintainability Considerations
- The modular architecture allows for straightforward extension of functionality as future requirements emerge, such as teacher management or more complex relationships.

## Security Considerations
- Use SQLAlchemy ORM features to mitigate risks of SQL injection.
- Validate incoming requests to preserve the integrity and structure of Course and Teacher relationships.

## Testing Strategy
- Develop test cases to cover:
  - Successful teacher assignment to a course via the PUT `/courses/{course_id}/assign-teacher` endpoint.
  - Proper error handling for missing or malformed `teacher_id` inputs during assignment.
  - Successful retrieval of course details via the GET `/courses/{course_id}` endpoint, including associated teacher information.

Test coverage should ensure a minimum of 70% overall, with critical path functions (assignment and retrieval operations) targeting at least 90% coverage.

## Deployment Considerations
- Ensure migration scripts are seamless and can execute on all target environments, creating the relationship between teachers and courses while safeguarding existing data.

## Conclusion
This implementation plan provides a robust outline for integrating the teacher relationship into the course structure, enhancing overall system capabilities while ensuring structural integrity and compatibility with existing entities. 

### Modifications Summary
- Update the `Course` model in `models.py` to include a foreign key reference to `Teacher`.
- Add a new endpoint in `routes.py` for assigning teachers to courses and retrieving course details.
- Implement validation logic in `validators.py` for teacher assignments.
- Introduce necessary migration logic in `database.py` to modify the existing `courses` table.

**Existing Code Files Modifications**:
- **File: `models.py`**: 
  - Update the `Course` model to include `teacher_id` foreign key and establish the relationship.
- **File: `routes.py`**: 
  - Implement PUT `/courses/{course_id}/assign-teacher` and GET `/courses/{course_id}` endpoints.
- **File: `validators.py`**:
  - Implement validation code for `teacher_id`.
- **File: `database.py`**:
  - Add migration logic for modifying the `courses` table.

This plan ensures a thorough and well-documented approach to enhancing the current educational management system with effective course and teacher relationship management.