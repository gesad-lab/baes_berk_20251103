# Implementation Plan: Add Teacher Relationship to Course Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Teacher Entity

---
## Version
1.0.0

## Overview
This implementation plan outlines the steps necessary to establish a relationship between the `Course` entity and the newly created `Teacher` entity within the educational management system. This feature enables courses to be assigned to specific teachers, which enhances management capabilities and lays the foundation for future enhancements related to course instruction and management.

## Technology Stack
- **Backend Framework**: Flask (Python)
- **Database**: SQLite (for simplicity and initial development)
- **Data Format**: JSON
- **Development Tools**:
  - Flask-SQLAlchemy for ORM (Object Relational Mapping)
  - Marshmallow for serialization
  - pytest for testing
- **Environment Management**: Virtualenv

## Architecture
The existing monolithic architecture will be extended to include the new relationship between Course and Teacher entities. The architecture ensures maintainability, scalability, and data integrity. The integration of the Teacher entity will be coupled with updates to the Course entity.

1. **API Layer**:
   - New endpoints to assign a Teacher to a Course and retrieve Course details including Teacher information.

2. **Service Layer**: 
   - Define business logic for assigning teachers to courses and retrieving course details.

3. **Data Access Layer**: 
   - Implement database interactions related to the Course-Teacher relationship.

4. **Database**: 
   - SQLite will be used; the database schema will be updated to include a foreign key relationship between `Course` and `Teacher`.

## Module Responsibilities
### 1. API Module (`api.py`)
- New routes to handle Course-Teacher operations:
  - `POST /api/v1/courses/{course_id}/assign_teacher/{teacher_id}`: Assign a teacher to an existing course.
  - `GET /api/v1/courses/{course_id}`: Retrieve course details including associated teacher.

### 2. Service Module (`services/course_service.py`)
- Define functions to:
  - Assign a teacher to a course, including validation.
  - Retrieve course details along with the assigned teacher's name.

### 3. Data Model (`models/course.py`)
- Update the existing `Course` entity to include `teacher_id` as a foreign key:
```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    """
    Represents a course in the system.

    Attributes:
        id (int): Unique identifier for the course (Primary Key).
        name (str): The name of the course (Required).
        level (str): The academic level of the course (Required).
        teacher_id (int): Foreign Key referencing the Teacher entity, can be nullable.
    """
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)

    teacher = relationship("Teacher")
```

### 4. Database Access (`data_access/course_repository.py`)
- Define methods for:
  - Assigning a teacher to a course.
  - Fetching course details along with associated teacher information.

## Data Models and API Contracts
### API Contract
#### Assign Teacher to Course
- **Endpoint**: `POST /api/v1/courses/{course_id}/assign_teacher/{teacher_id}`
- **Response**:
  - **Status**: 200 OK
  - **Body**:
  ```json
  {
      "message": "Teacher successfully assigned to course."
  }
  ```

#### Get Course Details
- **Endpoint**: `GET /api/v1/courses/{course_id}`
- **Response**:
  - **Status**: 200 OK
  - **Body**:
  ```json
  {
      "id": 1,
      "name": "Mathematics",
      "level": "Advanced",
      "teacher": {
          "id": 1,
          "name": "John Doe",
          "email": "john.doe@example.com"
      }
  }
  ```

## Implementation Approach
1. **Project Setup**:
   - Use the existing Git repository for the project. Update the `requirements.txt` with any necessary new dependencies.

2. **Update Course Data Model**:
   - Modify the `Course` model in `models/course.py` to include the `teacher_id` foreign key.

3. **Implement Database Migration**:
   - Create a migration script to add the `teacher_id` field to the existing `Course` table. Ensure that existing data integrity is preserved.
   
   Example Migration Script:
   ```python
   from flask_migrate import Migrate, MigrateCommand
   from flask_script import Manager
   from models import db

   # Initialize migration
   migrate = Migrate(app, db)
   manager = Manager(app)
   manager.add_command('db', MigrateCommand)

   # Migration to add teacher_id to courses
   def upgrade():
       with op.batch_alter_table('courses') as batch_op:
           batch_op.add_column(sa.Column('teacher_id', sa.Integer(), nullable=True))
           batch_op.create_foreign_key('fk_teacher', 'teachers', ['teacher_id'], ['id'])

   def downgrade():
       with op.batch_alter_table('courses') as batch_op:
           batch_op.drop_constraint('fk_teacher', 'courses')
           batch_op.drop_column('teacher_id')
   ```

4. **Create Service Layer**:
   - Implement functions in `services/course_service.py` for assigning teachers to courses and retrieving course details.

5. **Build API Layer**:
   - Add new endpoints to `api.py` for assigning a teacher to a course and getting course details.

6. **Testing**:
   - Write unit tests for the course-teacher assignment and retrieval in `tests/test_course_service.py` and test API endpoints in `tests/test_api.py`.

7. **Documentation**:
   - Update `README.md` with details on how to use the new endpoints related to assigning teachers and retrieving course information.

8. **Error Handling**:
   - Implement input validation in the API to check for valid course and teacher IDs before processing requests.

## Scalability Considerations
- The architecture remains capable of scaling for future functionalities regarding course management and teacher assignments.
- Future enhancements can incorporate more complex interactions between courses, teachers, and other educational entities.

## Security Considerations
- Input validation will be crucial to mitigate risks of SQL injection and other security vulnerabilities.
- Error responses will not expose sensitive information to users.

## Deployment Considerations
- Document environment variables and configuration settings necessary for deployment. Migrations should run smoothly without downtime or data loss.

## Testing Strategy
- **Unit Tests**: Validate the logic for assigning teachers to courses and retrieving course details through the service layer.
- **Integration Tests**: Ensure the correct function of the new API endpoints.
- **Contract Tests**: Confirm API compliance with defined contracts for new features.

## Success Metrics
- The application successfully assigns a Teacher to a Course and returns a confirmation message via the new API endpoint.
- The application correctly retrieves course details along with the assigned Teacher's name.
- Input validation failures return actionable error messages for any invalid input.
- The database schema reflects the changes while maintaining the integrity of existing Course and Teacher data.

## Conclusion
This implementation plan outlines the comprehensive approach to establish the relationship between the `Course` and `Teacher` entities in the educational management system, allowing for improved tracking and management of courses while ensuring data integrity and backward compatibility.

---

### Existing Code Files Modifications:
1. **File**: `models/course.py`
   - **Modifications**: Update the `Course` model to include `teacher_id` and define the relationship with the `Teacher` entity.

2. **File**: `api.py`
   - **Modifications**: Add new routes for assigning teachers to courses and retrieving course details with associated teachers.

3. **File**: `services/course_service.py`
   - **New Functionality**: Implement functions for assigning a teacher to a course and fetching course details.

4. **File**: `tests/test_course_service.py`
   - **New File**: Write tests for the new functionalities implemented in the Course service.

5. **File**: `tests/test_api.py`
   - **Modifications**: Add tests for the new API endpoints related to courses and teachers.

By adhering to this implementation plan, we can maintain existing functionality while introducing new capabilities to manage course and teacher relationships effectively.