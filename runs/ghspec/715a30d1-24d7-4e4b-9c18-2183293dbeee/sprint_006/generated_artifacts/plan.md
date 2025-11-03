# Implementation Plan: Add Teacher Relationship to Course Entity

---

INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:  
# Implementation Plan: Create Teacher Entity

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

This implementation plan outlines the development of a relationship between the existing "Course" entity and a newly defined "Teacher" entity in the educational management system. The primary objective is to enable each course to be associated with one teacher, enhancing course management and educational organization. This feature will streamline the assignment process of teachers to courses and provide users with comprehensive course information.

## II. Architecture & Technology Stack

- **Backend Framework**: FastAPI (for building RESTful APIs).
- **Database**: SQLite (embedded, lightweight database for development).
- **ORM**: SQLAlchemy (for handling database interactions and schema definitions).
- **Dependencies**:
  - FastAPI
  - SQLAlchemy
  - uvicorn (for running the FastAPI application)
  - Alembic (for handling migrations)
- **Environment**: Python 3.11+

### Architecture Diagram

```
+--------------------------------------------------------+
|                      FastAPI Application                |
|                                                        |
| +--------------------+    +-----------------------+   |
| | Course Controller     | <->| Course Service         |   |
| +--------------------+    +-----------------------+   |
| | - assign_teacher()    |    | - assign_teacher()    |   |
| | - get_course()       |<-->| - get_course()        |   |
| +--------------------+    +-----------------------+   |
|                                                        |
| +--------------------+                                 |
| | Course Repository     |                                |
| +--------------------+                                 |
| | - save()           |                                 |
| | - get_by_id()      |                                |
| +--------------------+                                 |
|                                                        |
+--------------------------------------------------------+
|                         SQLite Database                 |
|                      +------------------+              |
|                      |     courses       |              |
|                      |  +---------------+              |
|                      |  | id (pk)       |              |
|                      |  | name          |              |
|                      |  | teacher_id    |              |
|                      |  +---------------+              |
|                      |  | created_at    |              |
|                      |  | updated_at    |              |
|                      |  +---------------+              |
|                      |     teachers      |              |
|                      |  +---------------+              |
|                      |  | id (pk)       |              |
|                      |  | name          |              |
|                      |  | email         |              |
|                      |  +---------------+              |
|                      |  | created_at    |              |
|                      |  | updated_at    |              |
|                      |  +---------------+              |
+--------------------------------------------------------+
```

## III. Module Boundaries & Responsibilities

1. **Course Controller**: 
   - Exposes API endpoints for assigning teachers to courses and retrieving course information.
   - Validates incoming requests and translates them into service calls.

2. **Course Service**: 
   - Contains business logic related to assigning teachers to courses and retrieving course details.
   - Interacts with the repository to persist and retrieve course data, including teacher information.

3. **Course Repository**: 
   - Responsible for directly accessing the database.
   - Implements CRUD operations related to the `courses` table and its associations.

## IV. Data Model

### Updated Course Entity

```python
class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    teacher = relationship("Teacher", back_populates="courses")
```

### Updated Teacher Entity

```python
class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    courses = relationship("Course", back_populates="teacher")  # Bidirectional relationship
```

### Updated API Contracts

**POST /courses/assign-teacher**
- **Request Body**:
    ```json
    {
        "course_id": 1,
        "teacher_id": 2
    }
    ```
- **Response (200 OK)**:
    ```json
    {
        "id": 1,
        "name": "Course Name",
        "teacher_id": 2,
        "teacher": {
            "id": 2,
            "name": "Jane Smith",
            "email": "jane.smith@example.com"
        }
    }
    ```
- **Error Response (400 Bad Request)**:
    ```json
    {
        "error": {
            "code": "E001",
            "message": "Teacher not found."
        }
    }
    ```

**GET /courses/{id}**
- **Response (200 OK)**:
    ```json
    {
        "id": 1,
        "name": "Course Name",
        "teacher": {
            "id": 2,
            "name": "Jane Smith",
            "email": "jane.smith@example.com"
        }
    }
    ```
- **Error Response (404 Not Found)**:
    ```json
    {
        "error": {
            "code": "E002",
            "message": "Course not found."
        }
    }
    ```

## V. Implementation Approach

1. **Set Up API Endpoints**:
   - Extend the existing FastAPI application to include new endpoints for assigning teachers to courses and retrieving course details with associated teachers.

2. **Define Course and Teacher Models**:
   - Modify the `models.py` file to include the new `teacher_id` column in the `Course` model as well as the necessary relationship definition.

3. **Database Migration Strategy**:
   - Use Alembic to create a migration file that adds the `teacher_id` foreign key column to the `courses` table.
   - Example migration command:
     ```bash
     alembic revision --autogenerate -m "Add teacher_id to courses table"
     ```
   
4. **Implement Repository Layer for Courses**:
   - Create functions in `repository.py` to handle assignment of teachers to courses and retrieving course details.

5. **Implement Service Layer**:
   - Update `service.py` to handle the logic for assigning teachers to courses and retrieving course details.

6. **Implement API Routes**:
   - Extend existing API routes in `main.py` to handle the new endpoint for assigning teachers to courses and retrieving courses.

7. **Input Validation**:
   - Use Pydantic schemas to validate input for the assignment of teachers to courses.

8. **Error Handling**:
   - Implement proper error handling to return clear messages for various error conditions, such as when a teacher ID does not exist.

9. **Testing**:
   - Write unit tests and integration tests targeting the new functionality to ensure coverage meets or exceeds the required thresholds.

## VI. Deployment Considerations

- Ensure the application remains stable and can handle teacher assignments without compromise to existing functionality.
- Document the setup process and required changes in the `README.md` file.
- Implement a health check endpoint to verify the status of the new feature.
- Maintain graceful shutdown conditions, ensuring existing operations can complete before server shutdown.

## VII. Security & Best Practices

- **Data Validation**: Validate all inputs related to teacher assignment to courses.
- **Error Messages**: Define and return clear, actionable error messages for input validation failures.
- **Environment Management**: Use environment variables to handle any sensitive configuration information.
- **Structured Logging**: Implement logging for all major actions, particularly around course-teacher assignment processes, without exposing any sensitive information.

## VIII. Trade-offs and Considerations

- **Migration Complexity**: Ensure the added foreign key does not impact existing course data integrity and complies with the current schemas and relationships.
- **Backend Focus**: This implementation centers on backend changes to extend course management functionality without disrupting existing operations.

## IX. Success Criteria

- Functional requirements are met as outlined in the specification.
- Users must successfully assign and retrieve information about courses associated with teachers.
- Proper error handling and messaging mechanisms should be implemented for all endpoints.
- The database migration process executes without data loss or integrity issues.

## X. Conclusion

This implementation plan delineates a structured approach to establishing a relationship between the Course and Teacher entities in the educational management system. By ensuring adherence to best coding practices and maintaining backward compatibility, the application is poised to enhance its educational management capabilities seamlessly.

## Modifications Needed in Existing Files

### 1. `models.py`
- Update the `Course` class definition to include the `teacher_id` FK:
```python
class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    teacher = relationship("Teacher", back_populates="courses")
```

### 2. `repository.py`
- Add methods to handle teacher assignments:
```python
def assign_teacher_to_course(course_id: int, teacher_id: int) -> Course:
    # Logic to assign teacher to a course by updating the teacher_id
    course = get_course_by_id(course_id)
    if course:
        course.teacher_id = teacher_id
        save(course)
        return course
    raise ValueError("Course not found")
```

### 3. `service.py`
- Extend service methods to handle teacher assignments:
```python
def assign_teacher_to_course(course_id: int, teacher_id: int) -> Course:
    # Validate if teacher_id exists and call the repository method
    return repository.assign_teacher_to_course(course_id, teacher_id)

def get_course_details(course_id: int) -> Course:
    # Call repository to retrieve course information along with teacher details
```

### 4. `main.py`
- Add new API routes for assigning teachers to courses and getting course details:
```python
@app.post("/courses/assign-teacher", response_model=CourseResponse)
def assign_teacher(assignment: TeacherCourseAssignmentRequest):
    course = assign_teacher_to_course(assignment.course_id, assignment.teacher_id)
    return course

@app.get("/courses/{id}", response_model=CourseDetailsResponse)
def get_course(id: int):
    return get_course_details(id)
```

### 5. Migration Script (new)
- Create a migration file to add the `teacher_id` FK to the `courses` table:
```python
def upgrade():
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), sa.ForeignKey('teachers.id'), nullable=True))
```

By implementing these specified modifications, the application will effectively integrate the functionality of assigning teachers to courses while maintaining existing workflows and data integrity.