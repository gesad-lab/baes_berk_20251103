# Implementation Plan: Add Teacher Relationship to Course Entity

---
**INCREMENTAL DEVELOPMENT CONTEXT**

### Previous Sprint Plan:
# Implementation Plan: Create Teacher Entity

---
**INCREMENTAL DEVELOPMENT CONTEXT**

### Previous Sprint Plan:
# Implementation Plan: Add Course Relationship to Student Entity

---
**INCREMENTAL DEVELOPMENT CONTEXT**

### Previous Sprint Plan:
# Implementation Plan: Create Course Entity

---
**INCREMENTAL DEVELOPMENT CONTEXT**

### Previous Sprint Plan:
# Implementation Plan: Add Email Field to Student Entity

---

## Version
**Version**: 1.1.0

## Purpose
This document outlines the technical plan for establishing a relationship between the Course entity and the newly created Teacher entity in the Student Management Web Application. This feature aims to enhance the educational administration by allowing courses to have assigned teachers, thereby consolidating management and communication capabilities regarding course delivery.

## Technology Stack
- **Backend**: Flask (Python) for API development
- **Database**: SQLite for persistent data storage
- **Data Access**: SQLAlchemy for ORM (Object-Relational Mapping)
- **API Testing**: pytest for unit and integration testing
- **Environment Management**: Flask-Migrate for database migrations
- **JSON Handling**: Flask for easy JSON responses

## Architecture Overview
The system architecture will integrate the Teacher relationship into the existing Course structure, respecting module boundaries while maintaining the system's integrity and functionality. 

### Component Responsibilities
- **API Layer**: Define new endpoints for associating teachers with courses and retrieving course details.
- **Service Layer**: Implement business logic for course-teacher associations.
- **Data Access Layer**: Handle data interactions specifically for the Course and Teacher relationship.
- **Model Layer**: Update the Course model to include a foreign key reference to the Teacher model.

## Module Breakdown

### 1. API Layer
**Endpoints**:
- **POST `/courses/<course_id>/teachers`**: Associate a teacher with an existing course.
    - **Request Body**:
    ```json
    {
      "teacher_id": 1
    }
    ```
    - **Response**:
    ```json
    {
      "message": "Teacher associated with course successfully.",
      "course": {
        "id": 1,
        "teacher_id": 1
      }
    }
    ```

- **GET `/courses/<course_id>`**: Retrieve course information, including the associated teacher's name and email.
    - **Response**:
    ```json
    {
      "id": 1,
      "teacher": {
        "name": "Jane Doe",
        "email": "jane.doe@example.com"
      }
    }
    ```

### 2. Service Layer
- **Functionality**:
   - Validate the teacher ID when associating a teacher with a course.
   - Call Data Access Layer methods to associate the teacher and fetch course details.

### 3. Data Access Layer
- **Operations**:
    - `associate_teacher_with_course(course_id: int, teacher_id: int)`: Update the course record to link with the specified teacher.
    - `get_course_with_teacher(course_id: int)`: Retrieve course details including associated teacher information.

### 4. Model Layer
- **Course Model Update**:
    ```python
    class Course(db.Model):
        __tablename__ = 'courses'
        id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'))
        # other fields...
    ```

## Database Migration Strategy
1. **Database Migration**:
   - Utilize `Flask-Migrate` to create a migration script to add the `teacher_id` foreign key column to the existing Course table.
   - Ensure that this migration does not impact existing Course or Teacher data.
   
   ```bash
   # Create a migration script
   flask db migrate -m "Add teacher_id foreign key to Course table"
   flask db upgrade
   ```

## Error Handling
- If a request attempts to associate a non-existent teacher, return a structured error response with appropriate HTTP status:
  ```json
  {
    "error": {
      "code": "E002",
      "message": "The specified teacher does not exist."
    }
  }
  ```

## Testing Strategy
- Automated tests will be implemented using pytest to ensure:
  - Successful association of a teacher with a valid course.
  - Accurate retrieval of course information, including teacher data.
  - Clear error messages are returned for invalid teacher IDs.

### Test Coverage Requirements
- Aim for a minimum of 70% coverage across business logic, with priority on achieving 90% for the critical paths related to course-teacher associations.

### New Test Cases
- Test successful association of a teacher with a valid course.
- Test retrieval of a course with associated teacher data.
- Test error messages when associating a teacher that does not exist.

## Configuration Management
- Use environment variables to configure the application, including database connection strings.
- Provide a `.env.example` file documenting required configuration options for managing course-teacher associations.

## Deployment Considerations
- Ensure the application meets production readiness criteria, including health checks and graceful shutdown mechanisms.
- Maintain backward compatibility with existing course structures.

## Success Metrics
- 100% successful association of teachers with existing courses.
- 100% successful retrieval of course information including teacher details.
- Clear and actionable error messages for invalid associations.
- Successful application of the database migration for the new `teacher_id` column.

## Risks & Trade-offs
- **Trade-offs**:
  - The implementation will focus on basic creation and retrieval without providing more nuanced features like unassignment or teacher deletion functionality.
- **Risks**:
  - Validating relationships properly to avoid issues with orphaned entries in the database if erroneous IDs are provided.

## Conclusion
This implementation plan outlines the steps necessary to establish a relationship between the Course and Teacher entities. This enhancement aligns with the objectives of better managing educational relationships within the existing framework of the Student Management Web Application.

## Modifications Needed to Existing Files
1. **Update the Course Model** to include `teacher_id` as a foreign key linking to the Teacher model.
2. **Add new methods** in the Data Access Layer for associating a teacher with a course and retrieving course information.
3. **Extend the API Layer** to incorporate new POST and GET endpoints related to course-teacher associations.
4. **Create new tests** in the existing test suite for validating this new functionality.

### Existing Code Files
File: `app/models.py` (to be modified)
```python
class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'))  # New foreign key
    # other fields...
```

File: `app/routes.py` (to be modified)
```python
@app.route('/courses/<int:course_id>/teachers', methods=['POST'])
def associate_teacher_with_course(course_id):
    data = request.get_json()
    teacher_id = data.get('teacher_id')

    # Check if teacher exists
    if not Teacher.query.get(teacher_id):
        return jsonify({"error": {"code": "E002", "message": "The specified teacher does not exist."}}), 404

    course = Course.query.get_or_404(course_id)
    course.teacher_id = teacher_id
    db.session.commit()

    return jsonify({"message": "Teacher associated with course successfully.", "course": {"id": course.id, "teacher_id": course.teacher_id}}), 200

@app.route('/courses/<int:course_id>', methods=['GET'])
def get_course_with_teacher(course_id):
    course = get_course_with_teacher(course_id)

    if course.teacher_id:
        teacher = Teacher.query.get(course.teacher_id)
        teacher_info = {"name": teacher.name, "email": teacher.email}
    else:
        teacher_info = None

    return jsonify({"id": course.id, "teacher": teacher_info}), 200
```

File: `tests/api/test_courses.py` (new test file to be created)
```python
def test_associate_teacher_with_course(test_client):
    response = test_client.post('/courses/1/teachers', json={
        'teacher_id': 1
    })
    assert response.status_code == 200
    assert response.json['message'] == "Teacher associated with course successfully."

def test_get_course_with_teacher(test_client):
    response = test_client.get('/courses/1')
    assert response.status_code == 200
    assert 'teacher' in response.json
```

This implementation plan ensures that the new functionality integrates seamlessly with the existing application structure and adheres to the guidelines provided in the specification.