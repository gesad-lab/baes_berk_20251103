# Tasks: Add Teacher Relationship to Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- **Existing Entities**: Course and Teacher
- **Framework**: Flask (Python web framework)
- **Database**: SQLite (using SQLAlchemy for ORM)

Instructions for Task Breakdown:
1. Identify which existing files need modifications
   - Modify `src/models.py` to add a new field in the Course model.
2. Create new files or sections for new functionality
   - Implement API endpoints in `src/api.py`.
   - Create a migration script in `migrations/`.
3. Ensure integration tasks are included
   - Develop unit and integration tests in the `tests/` directory.
4. Maintain consistency with existing code style and patterns

---

## Task Breakdown

### Task 1: Modify Course Model to Add Teacher Relationship

- **File Path**: `src/models.py`
- **Description**: Update the Course model to include a new `teacher_id` column as a foreign key referencing the Teacher table.
- **Dependencies**: None.

```python
# Modifications made in src/models.py for Course
class Course(Base):
    ...
    teacher_id = Column(Integer, ForeignKey('teachers.id'))  # New field for teacher relationship
    ...
```

- [ ] Modify Course Model to Add Teacher Relationship (src/models.py)

### Task 2: Create Database Migration Script

- **File Path**: `migrations/20230301_add_teacher_relationship.py`
- **Description**: Create a migration script that adds `teacher_id` to the `courses` table. Ensure that existing data is preserved.
- **Dependencies**: Task 1.

```python
def upgrade():
    op.add_column('courses', sa.Column('teacher_id', sa.Integer, sa.ForeignKey('teachers.id')))
    
def downgrade():
    op.drop_column('courses', 'teacher_id')
```

- [ ] Create Database Migration Script (migrations/20230301_add_teacher_relationship.py)

### Task 3: Implement Assign Teacher API Endpoint

- **File Path**: `src/api.py`
- **Description**: Implement the `POST /courses/{course_id}/assign-teacher` endpoint to assign a teacher to a course.
- **Dependencies**: Task 1.

```python
@app.route('/courses/<int:course_id>/assign-teacher', methods=['POST'])
def assign_teacher(course_id):
    ...
```

- [ ] Implement Assign Teacher API Endpoint (src/api.py)

### Task 4: Implement Retrieve Course Information API Endpoint

- **File Path**: `src/api.py`
- **Description**: Implement the `GET /courses/{course_id}` endpoint to retrieve course details, including the assigned teacher.
- **Dependencies**: Task 1.

```python
@app.route('/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    ...
```

- [ ] Implement Retrieve Course Information API Endpoint (src/api.py)

### Task 5: Implement Update Teacher Assignment API Endpoint

- **File Path**: `src/api.py`
- **Description**: Implement the `PUT /courses/{course_id}/update-teacher` endpoint to update the teacher assigned to a course.
- **Dependencies**: Task 1.

```python
@app.route('/courses/<int:course_id>/update-teacher', methods=['PUT'])
def update_teacher(course_id):
    ...
```

- [ ] Implement Update Teacher Assignment API Endpoint (src/api.py)

### Task 6: Develop Unit and Integration Tests

- **File Path**: `tests/test_course_teacher.py`
- **Description**: Create tests for assigning a teacher, retrieving course details, and updating teacher assignments.
- **Dependencies**: Tasks 3, 4, and 5.

```python
def test_assign_teacher():
    ...

def test_get_course():
    ...

def test_update_teacher():
    ...
```

- [ ] Develop Unit and Integration Tests (tests/test_course_teacher.py)

### Task 7: Add API Documentation

- **File Path**: `README.md`
- **Description**: Update the README to include API endpoint specifications, request/response examples, and usage instructions.
- **Dependencies**: Tasks 3, 4, and 5.

```markdown
## API Endpoints
- `POST /courses/{course_id}/assign-teacher`
- `GET /courses/{course_id}`
- `PUT /courses/{course_id}/update-teacher`
```

- [ ] Add API Documentation (README.md)

### Task 8: Validate and Run Database Migration

- **File Path**: NA
- **Description**: Execute the migration script and confirm successful application without data loss.
- **Dependencies**: Task 2.

- [ ] Validate and Run Database Migration 

---

This structure lays out focused and independent tasks that can be executed sequentially and tested effectively, adhering to the development context and ensuring compliance with coding standards.