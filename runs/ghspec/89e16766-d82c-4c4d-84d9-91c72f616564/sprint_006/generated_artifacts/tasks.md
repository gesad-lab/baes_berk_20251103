# Tasks: Add Teacher Relationship to Course Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `app/models.py`
- `app/routes.py`
- `tests/api/test_courses.py` 

---

### Task Breakdown:

- [ ] **Task 1: Update Course Model**  
  Modify the `Course` model to include a foreign key for the teacher.
  - **File**: `app/models.py`

    ```python
    class Course(db.Model):
        __tablename__ = 'courses'
        id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'))  # New foreign key
        # other fields...
    ```

- [ ] **Task 2: Implement Associate Teacher Endpoint**  
  Create a POST endpoint for associating a teacher with a course, including error handling for non-existent teachers.
  - **File**: `app/routes.py`

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
    ```

- [ ] **Task 3: Implement Retrieve Course Details Endpoint**  
  Create a GET endpoint to retrieve course details and associated teacher information.
  - **File**: `app/routes.py`

    ```python
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

- [ ] **Task 4: Create Database Migration for teacher_id**  
  Construct a migration script to add the `teacher_id` column to the Course table.
  - **File**: Migration script (to be created via `Flask-Migrate` CLI)

    ```bash
    flask db migrate -m "Add teacher_id foreign key to Course table"
    flask db upgrade
    ```

- [ ] **Task 5: Create Unit Tests for Teacher Association**  
  Create a new test file that includes tests for the new endpoint functionalities.
  - **File**: `tests/api/test_courses.py` (new file)

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

- [ ] **Task 6: Update Documentation**  
  Update API documentation to reflect the new endpoints and their expected inputs/outputs.
  - **File**: Existing API documentation file (specify which)

---

This task breakdown outlines the necessary steps to implement the feature of associating a Teacher with a Course entity, ensuring all modifications align with the existing code structure and standards.