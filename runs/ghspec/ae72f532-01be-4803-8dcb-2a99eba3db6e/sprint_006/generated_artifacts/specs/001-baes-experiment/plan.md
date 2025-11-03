# Implementation Plan: Add Teacher Relationship to Course Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Teacher Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Manage Student Relationships with Courses

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

## 1. Overview
This implementation plan outlines the approach for adding a relationship between the `Course` and `Teacher` entities within the existing Student Management Web Application. This enhancement will facilitate the assignment of a Teacher to a Course, improving educational management capabilities and enabling better tracking of teaching assignments.

## 2. Architecture
The architecture will remain consistent with the existing design while introducing the `teacher_id` field within the `Course` entity. The architecture includes:
- **Presentation Layer**: Flask (API endpoints)
- **Service Layer**: Business logic for managing teacher assignments to courses
- **Data Access Layer (DAL)**: SQLite for database interactions
- **Model Layer**: Updated `Course` model with the `teacher_id` foreign key reference

### Diagram

```
[Client] <---> [API (Flask)] <---> [Service Layer] <---> [Data Access Layer (SQLite)]
```

## 3. Technology Stack
- **Framework**: Flask (Python web framework)
- **Database**: SQLite (lightweight disk-based database)
- **ORM**: SQLAlchemy (to facilitate database operations)
- **Validation**: Marshmallow (for request validation and serialization)
- **Testing Framework**: pytest (for unit and integration testing)
- **Environment**: Python 3.11+
- **Deployment**: Docker (for containerization)

## 4. Module Boundaries and Responsibilities

### 4.1 Modules
1. **API Module**
   - Introduce new endpoints for assigning Teachers to Courses and for retrieving Course details along with associated Teacher information.

2. **Service Module**
   - Implement business logic for handling Teacher assignments to Courses, including retrieval of Courses with Teachers.

3. **Data Access Layer Module**
   - Implement CRUD operations for managing Course and Teacher relationships.

4. **Model Module**
   - Update the Course model to include the `teacher_id` field.

### 4.2 Responsibilities
- **API Module**: Define routes for assigning Teachers to Courses and retrieving Course details.
- **Service Module**: Logic for validating inputs and maintaining relationships between Teachers and Courses.
- **Data Access Layer Module**: Responsible for CRUD operations related to Course-Teacher relationships.
- **Model Module**: Update the Course model structure to accommodate the `teacher_id`.

## 5. Data Models

### Course Entity
The existing `Course` entity will be updated as follows:

```python
class Course(Base):  # SQLAlchemy model
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # Required field
    level = Column(String, nullable=False)  # Required field
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # New optional field

    teacher = relationship("Teacher", back_populates="courses")  # Define relationship with Teacher

    def __repr__(self):
        return f"<Course(id={self.id}, name='{self.name}', level='{self.level}', teacher_id={self.teacher_id})>"
```

### Teacher Entity
Unchanged as defined in the previous sprint.

### API Contracts
#### Assign Teacher to Course
- **Endpoint**: `POST /api/v1/courses/{course_id}/assign_teacher`
- **Request**: 
  ```json
  {
      "teacher_id": 1
  }
  ```
- **Response**:
  - Success (204 No Content):
  - Error (400 Bad Request):
    ```json
    {
        "error": {
            "code": "E003",
            "message": "Teacher does not exist."
        }
    }
    ```

#### Retrieve Course with Teacher Info
- **Endpoint**: `GET /api/v1/courses/{course_id}`
- **Response**:
  - Success (200 OK):
    ```json
    {
        "id": 1,
        "name": "Math 101",
        "level": "Introductory",
        "teacher": {
            "id": 1,
            "name": "John Doe",
            "email": "john.doe@example.com"
        }
    }
    ```
  - Error (404 Not Found):
    ```json
    {
        "error": {
            "code": "E004",
            "message": "Course not found."
        }
    }
    ```

## 6. Implementation Plan

### 6.1 Project Structure Modifications
```plaintext
student_management/
│
├── src/
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes.py         # Add routes for assigning Teacher to Course and retrieving Course info
│   ├── models/
│   │   ├── __init__.py
│   │   ├── student.py        # Existing, no change
│   │   ├── course.py         # Update to include teacher_id
│   │   └── teacher.py        # Existing, no change
│   ├── services/
│   │   ├── __init__.py
│   │   └── course_service.py  # New service logic for Course-Teacher relationship handling
│   ├── dal/
│   │   ├── __init__.py
│   │   └── course_dal.py     # New file for Course CRUD operations including Teacher assignments
│   ├── app.py
│   └── config.py
│
├── migrations/
│   └── 002_add_teacher_relationship_to_courses.py # New migration for Course-Teacher relationship
│
├── tests/
│   ├── __init__.py
│   ├── test_student_routes.py  # Existing, no change
│   ├── test_student_service.py  # Existing, no change
│   ├── test_course_service.py   # Update to include tests for Teacher assignments
│   └── test_teacher_service.py   # Existing, no change
│
├── .env.example
├── requirements.txt
└── README.md
```

### 6.2 Environment Configuration
- Introduce a new migration script that implements the modification of the `courses` table to add the `teacher_id` foreign key.

### Migration Strategy
1. Create a migration script that adds the `teacher_id` field to the existing `courses` table with a foreign key constraint.
2. Ensure that the migration does not affect existing data by allowing `teacher_id` to be nullable initially.

Example migration script outline:
```python
def upgrade():
    # Alter the courses table to add the teacher_id column
    op.add_column('courses', sa.Column('teacher_id', sa.Integer, sa.ForeignKey('teachers.id'), nullable=True))

def downgrade():
    # Remove the teacher_id column on downgrade
    op.drop_column('courses', 'teacher_id')
```

## 7. Testing Strategy
- **Unit Tests**: Implement tests to verify Course assignment and retrieval methods in `test_course_service.py`.
- **Integration Tests**: Add tests in `test_course_routes.py` for the new endpoints handling Teacher assignments and retrieval.
- **Contract Tests**: Ensure the response formats for the new API calls meet specifications.

### 7.1 Coverage Requirement
- Achieve a minimum of 70% coverage overall and 90% coverage on critical paths concerning Teacher assignments to Courses.

### 7.2 Continuous Improvement
- Use pytest to maintain a rapid feedback loop during ongoing development.

## 8. Security Considerations
- All inputs for Course assignment must be validated to prevent SQL injection or improper data.
- Return appropriate error messages without exposing internal code or database errors to users.

## 9. Deployment Considerations
- Use Docker to ensure smooth deployment processes, running migrations to appropriately update the database schema during deployment.

## 10. Conclusion
This implementation plan addresses the integration of Teacher relationships within Courses in the Student Management Web Application. By following established coding standards and maintaining backward compatibility, we will enhance the existing features while ensuring robust educational management capability.

Existing Code Files:
- **Modifications** within the `course.py` and `routes.py` files will incorporate the new `teacher_id` integration without replacing existing data structure or entities.

---
By adhering to this plan, we will successfully implement the necessary functionality to associate Teachers with Courses while maintaining alignment with previous architecture and coding standards.