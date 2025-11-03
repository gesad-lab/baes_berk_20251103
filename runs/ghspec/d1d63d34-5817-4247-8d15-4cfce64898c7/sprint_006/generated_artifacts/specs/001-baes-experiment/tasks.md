# Tasks: Add Teacher Relationship to Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `src/services/course_service.py`
- `tests/services/test_course_service.py`
- Database schema for Courses and Teachers

---

### Task Breakdown

1. **Update Course Model**
   - **File**: `src/models/course.py`
   - **Description**: Extend the existing Course data model to include a foreign key reference to the Teacher entity (`teacher_id`).
   - **Task**:
     - Add a `teacher_id` field to the Course table definition.
     ```python
     class Course(Base):
         ...
         teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)
         teacher = relationship("Teacher")
     ```
   - [ ] Task complete to update Course model with teacher relationship.

2. **Create Database Migration**
   - **File**: `migrations/versions/add_teacher_id_to_courses.py`
   - **Description**: Create a migration script to update the Course table with the new `teacher_id` column.
   - **Task**:
     - Implement the migration to add the `teacher_id` column and create the foreign key reference.
   ```python
   def upgrade():
       op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))
       op.create_foreign_key('fk_courses_teachers', 'courses', 'teachers', ['teacher_id'], ['id'])
   ```
   - [ ] Task complete to create migration for teacher relationship in the Course entity.

3. **Implement Assign Teacher Endpoint**
   - **File**: `src/services/course_service.py`
   - **Description**: Implement the API endpoint to assign a Teacher to a Course.
   - **Task**:
     - Add a POST method to handle requests to `/courses/{course_id}/assign-teacher`.
   ```python
   @app.post("/courses/{course_id}/assign-teacher")
   async def assign_teacher_to_course(course_id: int, request: AssignTeacherRequest):
       ...
   ```
   - [ ] Task complete to implement assigning teacher endpoint.

4. **Implement Get Course Details Endpoint**
   - **File**: `src/services/course_service.py`
   - **Description**: Implement the API endpoint to retrieve details of a Course along with its assigned Teacher.
   - **Task**:
     - Add a GET method to handle requests to `/courses/{course_id}`.
   ```python
   @app.get("/courses/{course_id}")
   async def get_course_details(course_id: int):
       ...
   ```
   - [ ] Task complete to implement course details retrieval endpoint.

5. **Implement Update Teacher Assignment Endpoint**
   - **File**: `src/services/course_service.py`
   - **Description**: Implement the API endpoint to update the Teacher assigned to a Course.
   - **Task**:
     - Add a PUT method to handle requests to `/courses/{course_id}/update-teacher`.
   ```python
   @app.put("/courses/{course_id}/update-teacher")
   async def update_teacher_assignment(course_id: int, request: AssignTeacherRequest):
       ...
   ```
   - [ ] Task complete to implement update teacher endpoint.

6. **Implement Remove Teacher from Course Endpoint**
   - **File**: `src/services/course_service.py`
   - **Description**: Implement the API endpoint to remove a Teacher from a Course.
   - **Task**:
     - Add a DELETE method to handle requests to `/courses/{course_id}/remove-teacher`.
   ```python
   @app.delete("/courses/{course_id}/remove-teacher")
   async def remove_teacher_from_course(course_id: int):
       ...
   ```
   - [ ] Task complete to implement remove teacher endpoint.

7. **Create Unit Tests for Teacher Assignment**
   - **File**: `tests/services/test_course_service.py`
   - **Description**: Create unit tests for the new Teacher assignment endpoints.
   - **Task**:
     - Write tests for the following scenarios:
       - Assigning a Teacher to a Course
       - Retrieving Course details with a Teacher
       - Updating the Teacher for a Course
       - Removing a Teacher from a Course
   ```python
   def test_assign_teacher_to_course(create_teacher, create_course):
       response = client.post(f"/courses/{create_course['id']}/assign-teacher", json={"teacher_id": create_teacher["id"]})
       assert response.status_code == 201
   ```
   - [ ] Task complete to add unit tests for new functionality.

8. **Review and Update Documentation**
   - **File**: `README.md`
   - **Description**: Update the README to document the new API endpoints and any changes to the Course/Teacher data model.
   - **Task**:
     - Add sections for the new endpoint usages and data model updates.
   - [ ] Task complete to update documentation for new features.

---

This task breakdown outlines the steps required to implement the teacher relationship within the Course entity in the Student Management Application. Each task is designed to be independently executable, allowing for focused development and testing.