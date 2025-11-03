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

---

**Version**: 1.0.0  
**Purpose**: To establish a relationship between the `Course` entity and the `Teacher` entity in the educational management system for enhancing course management functionalities.

---

## I. Overview

This implementation plan outlines the necessary modifications to the existing `Course` entity to establish a relationship with the new `Teacher` entity. The objective is to update the data model, introduce relevant API endpoints, and ensure data integrity and validation in the existing educational management system.

## II. Architecture Overview

### 1. Architecture Style
- **Microservices Architecture**: The existing microservices design allows for seamless integration of the `Teacher` relationship into the `Course` entity without affecting other system functionalities.

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
- **Data Access Layer**: Update the `Course` model to include the `teacher_id` foreign key.
- **Service Layer**: Create functions for associating and dissociating teachers from courses.
- **API Layer**: New endpoints for assigning and removing teachers from courses, as well as retrieving courses with teacher details.

## III. Functional Specification

### 1. Data Model
1. **Course**
    - The existing `Course` model will be extended with a new `teacher_id` attribute to establish the foreign key relationship:
    ```python
    from sqlalchemy import Column, Integer, String, ForeignKey
    from sqlalchemy.orm import relationship
    from database.db import Base

    class Course(Base):
        __tablename__ = 'courses'
        
        id = Column(Integer, primary_key=True, autoincrement=True)
        name = Column(String, nullable=False)
        level = Column(String, nullable=False)
        teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)
        
        # Relationships
        students = relationship('Student', secondary='course_students', back_populates='courses')
        teacher = relationship('Teacher', back_populates='courses')
    ```

2. **Teacher**
    - Update the `Teacher` model to include a back-reference to courses:
    ```python
    from sqlalchemy.orm import relationship

    class Teacher(Base):
        __tablename__ = 'teachers'
        
        id = Column(Integer, primary_key=True, autoincrement=True)
        name = Column(String, nullable=False)
        email = Column(String, nullable=False, unique=True)

        # Back-reference
        courses = relationship('Course', back_populates='teacher')
    ```

### 2. API Endpoints
- `POST /courses/{course_id}/teacher/{teacher_id}`: Associate a teacher with a course.
    - Request: No request body required.
    - Response: `200 OK` with message indicating successful association.
  
- `DELETE /courses/{course_id}/teacher`: Remove a teacher from a course.
    - Request: No request body required.
    - Response: `200 OK` with message indicating successful dissociation.

- `GET /courses/{id}`: Retrieve course details along with associated teacher information.
    - Response: `200 OK` with course and teacher data.

### 3. Error Handling
- On assigning a non-existent teacher, return: `404 Not Found` with an error message indicating the teacher does not exist.
- On removing a teacher from a course where none exists, return: `400 Bad Request` with a relevant error message.
- Invalid course ID handling will return: `404 Not Found` if the course does not exist.

## IV. Implementation Approach

### 1. Setup Project Structure Modifications
The modifications will be incorporated into the existing project structure.

```
student_management/
├── src/
│   ├── models/
│   │   ├── course.py  # Modify course.py to include teacher_id and back-reference
│   │   └── teacher.py  # Ensure teacher.py already exists from previous implementation
│   ├── services/
│   │   ├── course_service.py  # Add methods for managing teacher-course relationships
│   │   └── teacher_service.py  
│   ├── controllers/
│   │   ├── course_controller.py  # Add new endpoints to handle teacher associations
│   │   ├── teacher_controller.py
│   └── migrations/
│       └── 2023_10_01_0002_add_teacher_relationship.py  # New migration file for relationship
```

### 2. Development Tasks
1. **Update the Course Model**:
   - Modify `models/course.py` to include the new `teacher_id` attribute and the relationship back-reference to `Teacher`.

2. **Update API Controller for Course Management**:
   - Modify `controllers/course_controller.py` to add new endpoints for teacher assignment and removal, alongside appropriate request handling.

3. **Create Service Layer Logic**:
   - Update `services/course_service.py` with methods to handle associating and dissociating teachers to/from courses.
   - Implement logic to check for the existence of a teacher before assignment.

4. **Database Migration**:
   - Utilize Alembic to create a new migration script (e.g., `2023_10_01_0002_add_teacher_relationship.py`) that adds the `teacher_id` column to the `courses` table.
    ```python
    from alembic import op
    import sqlalchemy as sa

    revision = '2023_10_01_0002'
    down_revision = '2023_10_01_0001'  # Previous migration ID
    branch_labels = None
    depends_on = None

    def upgrade():
        """Add teacher_id column to courses table"""
        op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))
        op.create_foreign_key('fk_teacher_course', 'courses', 'teachers', ['teacher_id'], ['id'])

    def downgrade():
        """Remove teacher_id column from courses table"""
        op.drop_constraint('fk_teacher_course', 'courses', type_='foreignkey')
        op.drop_column('courses', 'teacher_id')
    ```

### 3. Testing
- Implement test cases in `tests/test_course.py`, including:
  - Tests for successfully assigning a teacher to a course.
  - Tests for removing a teacher from a course.
  - Tests for retrieving course details with the full associated teacher information.
  - Validate error handling correctly invokes response codes for various edge cases.

### 4. Documentation
- Update API documentation using OpenAPI to include details of the newly implemented endpoints for managing teacher relationships with courses.
- Modify `README.md` to reflect the changes made in managing the `Course` entity and document usage and testing instructions.

## V. Deployment Considerations

### 1. Environment Configuration
- Verify that updates in `.env.example` include any new configuration required for the teacher-course relationships, if applicable.

### 2. Logging Configuration
- Ensure logging captures teacher assignments and removals to assist in monitoring operations and troubleshooting.

### 3. Health Check Endpoint
- Ensure the health check endpoint tests the integrity and availability of the services associated with the course-teacher relationship.

## VI. Technical Trade-offs

1. **Database Constraints**:
   - While adding foreign key relationships enhances data integrity, it does introduce complexities in the handling of null values and orphaned records upon teacher deletions.

2. **API Extension Complexity**:
   - Expanding the API controller may lead to a slightly increased codebase and complexity but is necessary for improved functionality and relationships.

3. **Migration Overhead**:
   - Implementing a migration for foreign key constraints involves additional scrutiny but provides enhanced data consistency.

## VII. Success Criteria

- The system allows successful assignment and removal of teachers from courses while maintaining backward compatibility and data integrity.
- Database operations reflect the modified schema correctly, with migrations executed without data loss.
- Comprehensive tests ensure all functionalities work as expected, and error handling provides meaningful feedback to users.

---

This implementation plan prepares to effectively integrate a teacher relationship into the course entity, driving essential advancements in course management functionalities while adhering to best practices and ensuring seamless operation in the existing architecture.