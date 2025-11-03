# Implementation Plan: Add Teacher Relationship to Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Teacher Entity

---

## I. Architecture Overview

The existing application architecture will be enhanced to establish a relationship between the Course and Teacher entities. This involves updates to the Data Access Layer (DAL), Service Layer, and API Layer. The components involved include:

1. **API Layer**: Two new endpoints will be added to manage the teacher associations with the Course entity, including updating a course to specify a teacher and retrieving course details including teacher information.
2. **Service Layer**: Business logic will manage the relationship between courses and teachers, ensuring operations maintain integrity and follow business rules.
3. **Data Access Layer (DAL)**: Updated models and methods will facilitate CRUD operations managing the `teacher_id` relation in the `courses` table.
4. **Database**: SQLite will serve as the data persistence layer, accommodating the new `teacher_id` field in the `courses` table without affecting existing data integrity.

## II. Technology Stack

- **Programming Language**: Python
- **Web Framework**: Flask (for API development)
- **Database**: SQLite (for local development)
- **ORM**: SQLAlchemy (for database interactions)
- **Testing Framework**: pytest (for automated testing)
- **Logging**: Python's built-in logging module (for API monitoring)
- **Migration Tool**: Alembic (for database migrations)

## III. Module Boundaries

### 1. API Layer
- Responsible for exposing the following endpoints for Course-Teacher management:
  - `PATCH /courses/{course_id}`: Assign a teacher to a course.
  - `GET /courses/{course_id}`: Retrieve course details including associated teacher information.

### 2. Service Layer
- Methods to manage teacher assignments to courses, ensuring data integrity and application correctness.

### 3. Data Access Layer (DAL)
- Extend course model to accommodate the `teacher_id` field and provide CRUD operations for courses with teacher associations.

## IV. Data Models

### 1. Course Entity (Modified)

```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)

    teacher = relationship("Teacher", back_populates="courses")

class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

    courses = relationship("Course", back_populates="teacher")
```

### 2. Database Migration

#### Migration Strategy:
1. Create a migration script to add the `teacher_id` column to the `courses` table without disrupting existing data.

```python
# Migration script example
from alembic import op
import sqlalchemy as sa

def upgrade():
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))
    op.create_foreign_key('fk_course_teacher', 'courses', 'teachers', ['teacher_id'], ['id'], ondelete='SET NULL')

def downgrade():
    op.drop_constraint('fk_course_teacher', 'courses', type_='foreignkey')
    op.drop_column('courses', 'teacher_id')
```

## V. API Contracts

### 1. Update Course with Teacher

- **Endpoint**: `PATCH /courses/{course_id}`
- **Request Body**: 
  ```json
  {
      "teacher_id": 1
  }
  ```
- **Success Response**: 
  ```json
  {
      "id": 1,
      "title": "Course Title",
      "description": "Course Description",
      "teacher_id": 1
  }
  ```
- **HTTP Status Code**: 200 OK

### 2. Retrieve Course with Teacher

- **Endpoint**: `GET /courses/{course_id}`
- **Success Response**: 
  ```json
  {
      "id": 1,
      "title": "Course Title",
      "description": "Course Description",
      "teacher": {
          "id": 1,
          "name": "Teacher Name",
          "email": "teacher@example.com"
      }
  }
  ```
- **HTTP Status Code**: 200 OK

## VI. Testing Strategy

### Unit Tests:
- Focus on service methods responsible for updating courses and retrieving course information.

### Integration Tests:
- Verify that API endpoints respond correctly and adhere to the expected input/output contracts.

### Coverage Requirements:
- Aim for a minimum of 70% code coverage for the features; critical paths, such as assigning and updating course-teacher relations, should exceed 90% coverage.

```python
# Example Unit Test for Course Updates
def test_update_course_teacher(client):
    response = client.patch('/courses/1', json={"teacher_id": 1})
    assert response.status_code == 200
    assert response.json['teacher_id'] == 1

def test_get_course_with_teacher(client):
    response = client.get('/courses/1')
    assert response.status_code == 200
    assert 'teacher' in response.json  # Expecting the teacher details to be included
```

## VII. Logging and Monitoring

- Implement structured logging for all API requests and errors within the course teaching assignments.

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/courses/<int:course_id>', methods=['PATCH'])
def assign_teacher(course_id):
    logger.info("Updating course %d with teacher ID %s", course_id, request.json.get('teacher_id'))
    # Logic for updating the course with teacher ID...
```

## VIII. Security Considerations

- Validate input to ensure that the `teacher_id` provided is a valid integer referencing an existing teacher.
- Ensure error handling for invalid course IDs and non-existent teacher assignments.
- Sanitize user input to guard against injection attacks.

## IX. Deployment and Configuration Management

- **Local Development**: Use a `.env` file for environmental configurations.
- **Production Readiness**: Integrate the migration into the deployment pipeline, ensuring the database schema updates smoothly and does not disrupt existing workflow.

## X. Roadmap

1. **Development**: Implement the updated Course model, migration script, and the API endpoints.
2. **Testing**: Create and run unit tests and integration tests to verify feature functionality.
3. **Migration**: Develop and validate the migration script to modify the `courses` table for the `teacher_id` field.
4. **Deployment**: Ensure proper deployment with comprehensive pre-deployment testing.

## XI. Conclusion

This implementation plan establishes the groundwork for integrating the teacher relationship to the course entity, detailing the architecture, module responsibilities, data models, API contracts, and testing strategies. The plan is structured to build upon the existing system while ensuring compatibility with current data models and services.

### Existing Code Modifications
1. **Update models.py**: Add `teacher_id` to the `Course` class and establish the relationship with the `Teacher`.
2. **Implement migration script** in Alembic to handle modifying the `courses` table.
3. **Update tests** in `tests/test_routes.py` and other test files to include tests for the new endpoints related to course-teacher assignments.

The outlined approach ensures clarity, maintains data integrity, and provides extensibility for future improvements to the educational management system.