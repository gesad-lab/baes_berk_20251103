# Tasks: Create Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `models/student.py` (1250 bytes)
- `routes.py` (4500 bytes)
- `tests/test_student.py` (2312 bytes)

## Task Breakdown

### Task 1: Create Course Model
- **File**: `src/models/course.py`
- **Description**: Implement the Course model with attributes for id, name, and level.
- **Dependencies**: None
- [ ] Create course.py with the model definition.

```python
from app import db
from sqlalchemy import Column, Integer, String

class Course(db.Model):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
```

### Task 2: Create Database Migration Script
- **File**: `migrations/versions/<timestamp>_create_courses_table.py`
- **Description**: Create the migration script to add the new `courses` table.
- **Dependencies**: Task 1
- [ ] Implement upgrade function in migration script.

```python
def upgrade():
    op.create_table('courses',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('level', sa.String, nullable=False)
    )
```

### Task 3: Create API Endpoints
- **File**: `src/routes.py`
- **Description**: Implement the `POST /courses` and `GET /courses` endpoints.
- **Dependencies**: Task 1
- [ ] Add Flask routes for creating and retrieving courses.

```python
from flask import Blueprint, request, jsonify
from app.models import Course
from app import db

courses_bp = Blueprint('courses', __name__)

@courses_bp.route('/courses', methods=['POST'])
def create_course():
    ...
    
@courses_bp.route('/courses', methods=['GET'])
def get_courses():
    ...
```

### Task 4: Implement Validation Logic
- **File**: `src/routes.py`
- **Description**: Ensure validation checks for the request body on course creation.
- **Dependencies**: Task 3
- [ ] Validate that name and level are present in the request.

```python
if not data.get('name') or not data.get('level'):
    return jsonify({"error": {"code": "E001", "message": "Name and level are required."}}), 400
```

### Task 5: Implement Error Handling
- **File**: `src/routes.py`
- **Description**: Create structured error responses for missing required fields.
- **Dependencies**: Task 4
- [ ] Implement error handling and response formatting for invalid requests.

### Task 6: Write Unit Tests for Course Creation and Retrieval
- **File**: `tests/test_course.py`
- **Description**: Write unit tests to validate course creation and error handling.
- **Dependencies**: Task 3
- [ ] Create tests for successful creation and cases for missing attributes.

```python
def test_create_course(client):
    ...
    
def test_create_course_missing_name(client):
    ...
    
def test_get_courses(client):
    ...
```

### Task 7: Write Integration Tests
- **File**: `tests/integration/test_course_api.py`
- **Description**: Validate the complete interaction between the API, service layer, and database.
- **Dependencies**: Task 6
- [ ] Create integration tests for API responses.

### Task 8: Update API Documentation
- **File**: `docs/api_specification.md`
- **Description**: Update the API documentation to include new course-related endpoints.
- **Dependencies**: Task 3
- [ ] Document the new endpoints `POST /courses` and `GET /courses`.

### Task 9: Update README.md
- **File**: `README.md`
- **Description**: Include setup instructions and usage information for the course feature.
- **Dependencies**: Task 8
- [ ] Update README with details about course management features.

### Task 10: Execute Database Migration
- **File**: Environment setup
- **Description**: Run the migration script to create the courses table in the database.
- **Dependencies**: Task 2
- [ ] Apply the migration to the development database.

---
This structured breakdown ensures that each task operates on a single file, maintains dependencies, and can be independently tested, adhering to the project's coding standards and requirements.