# Tasks: Add Teacher Relationship to Course Entity

---

## INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- models/course.py (702 bytes)
- models/teacher.py (687 bytes)
- api/courses.py (801 bytes)
- api/teachers.py (1059 bytes)
- api/errors.py (1925 bytes)
- tests/test_courses.py (3145 bytes)
- tests/test_teachers.py (3243 bytes)

---

## Task Breakdown

### Task 1: Update Course Model

- **File**: `src/models/course.py`
- **Description**: Add `teacher_id` foreign key reference in the Course model to represent the relationship with the Teacher entity.
- **Action**:
  - Modify `Course` class to include `teacher_id`.
  
```python
class Course(Base):
    """Course model to store course information."""
    
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # Foreign key to Teacher
```

- [ ] Implement change in the Course model to add `teacher_id`.

---

### Task 2: Create Database Migration

- **File**: `src/migrations/migration_add_teacher_to_course.py`
- **Description**: Write a migration script to alter the Course table and add the `teacher_id` column.
- **Action**:
  - Create a new migration script.

```python
def upgrade():
    """Add teacher_id to the courses table."""
    with engine.connect() as conn:
        conn.execute("ALTER TABLE courses ADD COLUMN teacher_id INTEGER;")

def downgrade():
    """Remove teacher_id from the courses table."""
    with engine.connect() as conn:
        conn.execute("ALTER TABLE courses DROP COLUMN teacher_id;")
```

- [ ] Implement database migration to add `teacher_id`.

---

### Task 3: Implement API Endpoint for Assigning Teacher

- **File**: `src/api/courses.py`
- **Description**: Create the `POST /courses/{course_id}/assign-teacher` API endpoint for assigning a Teacher to a Course.
- **Action**:
  - Add route and handler for assigning a teacher.

```python
@router.post('/courses/{course_id}/assign-teacher')
async def assign_teacher(course_id: int, teacher_id: int, db: Session = Depends(get_db)):
    # Validate and assign Teacher
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found.")
    
    if course.teacher_id is not None:
        raise HTTPException(status_code=400, detail="A Teacher is already assigned to this Course.")

    course.teacher_id = teacher_id
    db.commit()
    return {"message": "Teacher successfully assigned to the Course."}
```

- [ ] Develop the API endpoint for assigning a Teacher to a Course.

---

### Task 4: Implement API Endpoint for Retrieving Course Details

- **File**: `src/api/courses.py`
- **Description**: Enhance the `GET /courses/{course_id}` API endpoint to include Teacher details in the response.
- **Action**:
  - Update existing route to fetch Teacher info.

```python
@router.get('/courses/{course_id}')
async def get_course(course_id: int, db: Session = Depends(get_db)):
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found.")
    
    return {
        "id": course.id,
        "name": course.name,
        "teacher": {"id": course.teacher_id, ...}  # Fetch additional teacher details as needed
    }
```

- [ ] Enhance the course detail retrieval API endpoint to include teacher info.

---

### Task 5: Implement Error Handling

- **File**: `src/api/errors.py`
- **Description**: Define user-friendly error responses for invalid Course-Teacher relationships and conflicts.
- **Action**:
  - Ensure that meaningful error messages are returned in response to API calls.

```python
{
    "error": {
        "code": "E001",
        "message": "Course not found."
    }
},
{
    "error": {
        "code": "E002",
        "message": "A Teacher is already assigned to this Course."
    }
}
```

- [ ] Ensure error handling is implemented with appropriate messages for various scenarios.

---

### Task 6: Write Unit and Integration Tests

- **File**: `tests/test_courses.py`
- **Description**: Create tests for the new functionality including assigning a Teacher and retrieving Course details with Teacher info.
- **Action**:
  - Develop tests for each user scenario listed in the specification.
  
```python
@pytest.mark.asyncio
async def test_assign_teacher_to_course():
    # Prepare test setup that includes a course and teacher
    response = await client.post("/courses/1/assign-teacher", json={"teacher_id": 1})
    assert response.status_code == 200
    assert response.json()["message"] == "Teacher successfully assigned to the Course."

@pytest.mark.asyncio
async def test_get_course_info():
    response = await client.get("/courses/1")
    assert response.status_code == 200
    assert "teacher" in response.json()
```

- [ ] Implement comprehensive tests covering all critical paths of the new feature.

---

### Task 7: Update API Documentation

- **File**: `docs/api_documentation.md`
- **Description**: Document new API endpoints and their expected request/response formats.
- **Action**:
  - Add descriptions for the new functionality to the API documentation.

```markdown
### Assign a Teacher to a Course
- **POST /courses/{course_id}/assign-teacher**
- Request Body:
```json
{
    "teacher_id": 1
}
```
- Response:
```json
{
    "message": "Teacher successfully assigned to the Course."
}
```
```

- [ ] Ensure the API documentation reflects all new endpoints and usage scenarios.

---

This suite of tasks provides a structured approach to implementing the feature of adding a Teacher relationship to the Course entity, ensuring code integrity and system functionality while enabling independent testability of each task.