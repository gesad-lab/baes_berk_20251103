# Tasks: Add Teacher Relationship to Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `models/course.py`
- `models/teacher.py`
- `schemas/course_schema.py`
- `routes/course_routes.py`
- `tests/test_course_routes.py`
- Database Migration Scripts

---

## Task List

### Task 1: Update Course Model
- **File Path**: `src/models/course.py`
- **Description**: Modify the existing Course model to add the `teacher_id` foreign key relationship to the Teacher entity.
- **Dependencies**: None
- **Testable**: Verify the Course model reflects the new `teacher_id` attribute.

- [ ] Modify the Course class to add the `teacher_id` attribute.  
```python
teacher_id = Column(Integer, ForeignKey('teachers.id'))
```
- [ ] Establish a relationship with the Teacher model.
```python
teacher = relationship("Teacher", back_populates="courses")
```

### Task 2: Create Update Course Request Schema
- **File Path**: `src/schemas/course_schema.py`
- **Description**: Create a new schema for updating the course that includes an optional `teacher_id`.
- **Dependencies**: Task 1
- **Testable**: Validate the schema through test that checks for proper schema validation for the `teacher_id`.

- [ ] Add a new `UpdateCourseRequestSchema` class to the schemas file.  
```python
class UpdateCourseRequestSchema(BaseModel):
    teacher_id: Optional[int] = None
```

### Task 3: Implement PATCH /courses/{course_id} Route
- **File Path**: `src/routes/course_routes.py`
- **Description**: Create a route for updating an existing course to assign a teacher.
- **Dependencies**: Task 1, Task 2
- **Testable**: Test via POSTMAN or Swagger UI for proper response after assigning a teacher.

- [ ] Add a new PATCH route and implement the logic for assigning a `teacher_id` to a course.  

### Task 4: Implement GET /courses/{course_id} Route
- **File Path**: `src/routes/course_routes.py`
- **Description**: Implement a route to get the details of a specific course, including assigned teacher information.
- **Dependencies**: Task 1
- **Testable**: Send a GET request and ensure the response includes the teacher's name and email.

- [ ] Create the GET route definition and ensure it retrieves the course with associated teacher data.

### Task 5: Implement GET /courses Route
- **File Path**: `src/routes/course_routes.py`
- **Description**: Create a route to retrieve a list of all courses with their associated teachers.
- **Dependencies**: Task 1
- **Testable**: Validate that a GET request returns a full list of courses with teacher details.

- [ ] Create the GET route to return an overview of all courses, including assigned teachers.

### Task 6: Create Database Migration Script
- **File Path**: `migrations/versions/`
- **Description**: Generate a migration script to add the `teacher_id` column to the courses table.
- **Dependencies**: Task 1
- **Testable**: Test the migration for successful application and observe data integrity.

- [ ] Create a migration script using Alembic to alter the courses table to include the `teacher_id`.

### Task 7: Implement Error Handling
- **File Path**: `src/routes/course_routes.py`
- **Description**: Ensure comprehensive error handling for invalid teacher assignments, including relevant error messages.
- **Dependencies**: Tasks 3, 4
- **Testable**: Send invalid requests and measure that the correct error responses are returned.

- [ ] Write validation logic to check for the existence of a teacher ID before assignment.

### Task 8: Write Unit and Integration Tests
- **File Path**: `tests/test_course_routes.py`
- **Description**: Add tests for the new functionality covering the PATCH and GET routes, and error cases.
- **Dependencies**: Tasks 3, 4, 5, 6
- **Testable**: Ensure tests pass against the new API functionality to validate expectations and requirements.

- [ ] Implement unit tests for course assignments and retrieval.
- [ ] Write tests for error handling scenarios to ensure coverage.

### Task 9: Update Documentation
- **File Path**: `README.md`
- **Description**: Update API documentation to reflect the new Course-Teacher relationships and usage examples.
- **Dependencies**: Tasks 3, 5, 8
- **Testable**: Review the README after changes to verify completeness and accuracy of the new documentation.

- [ ] Document the new API endpoints and expected request/response formats in the README.

---

Ensure all tasks are completed, adequately tested, and adhere to the project's coding standards while maintaining consistency with existing implementations. Each task aims to support the integration of a Teacher relationship with Course entities in a structured manner.