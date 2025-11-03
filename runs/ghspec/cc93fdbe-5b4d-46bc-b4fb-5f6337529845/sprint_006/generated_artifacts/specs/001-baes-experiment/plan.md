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
# Implementation Plan: Student Management Web Application

## Version
**Version**: 1.1.0

## 1. Architecture Overview
This implementation introduces a relationship between the existing `Course` entity and the newly introduced `Teacher` entity. The architecture utilizes FastAPI for API interactions, SQLite for the database, and SQLAlchemy as the ORM to manage the data layer effectively. This relationship will enable better tracking of each course's instructor for educational management.

### Architecture Components
- **FastAPI**: To continue developing RESTful API endpoints for managing courses and teachers.
- **SQLite**: As our database, maintaining simplicity and ease for data migrations.
- **SQLAlchemy**: To handle the ORM interactions between the `Course` and new `Teacher` entities.

## 2. Technology Stack
- **Programming Language**: Python 3.11+
- **Framework**: FastAPI
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Testing Framework**: pytest
- **API Testing Tool**: Postman (for manual API tests)

## 3. Module Boundaries & Responsibilities
### 3.1 Services
- **CourseService**: This existing service will be updated to include methods for updating the `teacher_id` for a course.
- **TeacherService**: This new service will manage the business logic related to `Teacher` entities.

### 3.2 Data Models
#### Updated Course Model
- **Course**: Existing model with an added `teacher_id` attribute.
  
#### New Teacher Model
- **Teacher**: Represents the `Teacher` entity.

## 4. Data Models
```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # New field

    teacher = relationship("Teacher", back_populates="courses")  # Relationship

class Teacher(Base):
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    courses = relationship("Course", back_populates="teacher")  # One-to-many relationship
```

## 5. API Contracts
### 5.1 Endpoints Specification
#### 5.1.1 Update a Course (Assign a Teacher)
- **Endpoint**: `PATCH /courses/{course_id}`
- **Request Body**:
    ```json
    {
        "teacher_id": 1  // Required
    }
    ```
- **Response** (200 OK):
    ```json
    {
        "id": 1,
        "name": "Introduction to Programming",
        "level": "Beginner",
        "teacher_id": 1
    }
    ```
- **Error Response** (400 Bad Request):
    ```json
    {
        "error": {
            "code": "E001",
            "message": "Invalid course ID."
        }
    }
    ```
- **Error Response** (400 Bad Request):
    ```json
    {
        "error": {
            "code": "E002",
            "message": "Invalid teacher ID."
        }
    }
    ```

## 6. Database Migration Strategy
### 6.1 Migration Strategy
- Utilize `Alembic` for the migration to add a new `teacher_id` column to the existing `Course` table while maintaining data integrity and partnership with existing tables.

```bash
# Create migration file using Alembic 
alembic revision --autogenerate -m "Add teacher_id to courses table"
```

### 6.2 Migration Script Example
```python
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'xxxxxxx'
down_revision = 'yyyyyyy'
branch_labels = None
depends_on = None

def upgrade():
    # Add a new column to the courses table for the teacher_id
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), sa.ForeignKey('teachers.id'), nullable=True))

def downgrade():
    # Remove the teacher_id column
    op.drop_column('courses', 'teacher_id')
```

## 7. Testing Approach
### 7.1 Test Cases
1. **Patch Course with Valid Teacher**: Validate that providing a valid `course_id` and `teacher_id` updates the course successfully.
2. **Error Handling for Invalid Course IDs**: Ensure the appropriate error response is returned for invalid `course_id`s.
3. **Error Handling for Invalid Teacher IDs**: Ensure that invalid `teacher_id`s are handled correctly, returning an error.
4. **Database Schema Verification**: Ensure the `teacher_id` is present after migration with no loss of existing data.

### 7.2 Testing Framework
- Use `pytest` for unit and integration testing. Tests will be organized similarly to the current project structure with a focus on the new endpoints and services.

## 8. Security Considerations
- Validate inputs for `teacher_id` and `course_id` in the API logic to avoid SQL injection and ensure data integrity.
- Maintain appropriate structured error responses for API endpoints to prevent revealing internal error details.

## 9. Error Handling
- Implement structured error responses for all course update related requests.
- Ensure specific validation checks for `teacher_id` and clarify errors in responses.

## 10. Documentation
- Update project API documentation (`README.md`) to reflect the new `/courses/{course_id}` route and its expected responses and errors.
- Document migration processes within the `README.md`.

## 11. Deployment Considerations
- Test thoroughly in a staging environment to ensure that the new functionality does not disrupt existing features.
- Validate all API responses conform to the expected JSON structure throughout the application.

## 12. Version Control Practices
- Ensure clear and meaningful commit messages corresponding to changes made, especially concerning the addition of the teacher relationship.
- Use `.gitignore` to avoid committing test databases or cache files.

## 13. Implementation Timeline
- **Week 1**: Define and implement the teacher relationship within the existing `Course` model and create the API endpoint to associate a teacher with a course.
- **Week 2**: Write migration scripts with Alembic, test their functionality, and verify data integrity.
- **Week 3**: Conduct thorough integration testing, finalize documentation updates, and prepare for deployment.

---

**Trade-offs and Decisions**:
- Continuing with SQLite ensures ease of migration and supports the existing database structure.
- FastAPI remains an effective framework for API development, allowing smooth integration of new features.
- Ensuring backward compatibility is essential to prevent any disruptions to existing functionality.

### Existing Code Files Modifications:
1. **models.py**: Update the `Course` model to add the `teacher_id` foreign key.
   
   ```python
   class Course(Base):
       ...
       teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # New field
       ...
   ```

2. **services/course_service.py**: Update the service to include logic for assigning a teacher to a course.

   ```python
   class CourseService:
       @staticmethod
       def assign_teacher(course_id: int, teacher_id: int):
           # Logic to update the course's teacher_id
           pass
   ```

3. **main.py**: Add the new route to handle PATCH requests for course updates.

   ```python
   @app.patch("/courses/{course_id}", response_model=CourseResponse)
   async def update_course_teacher(course_id: int, teacher: TeacherUpdate):
       # Call CourseService to assign teacher
       pass
   ```

4. **tests/services/test_course_service.py**: Add tests for the `assign_teacher` method.
   
   ```python
   def test_assign_teacher_success():
       # Test logic for assigning a teacher to a course
       pass
   ```

5. **tests/integration/test_course_api.py**: Create test cases for the course update API endpoint.

   ```python
   def test_update_course_teacher_api():
       response = client.patch("/courses/1", json={"teacher_id": 1})
       assert response.status_code == 200
       assert response.json()["teacher_id"] == 1
   ```

This implementation plan provides the necessary steps for integrating the `Teacher` entity with the `Course`, complete with a clear migration strategy, testing approach, and documentation setup. Ensuring backward compatibility with existing features remains a priority throughout this integration.