# Tasks: Create Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `src/models.py` (Existing model definitions)
- `src/app.py` (Existing application setup)
- `tests/test_app.py` (Existing test suite)

Instructions for Task Breakdown:
1. Identify which existing files need modifications
2. Create new files for new functionality
3. Ensure integration tasks are included
4. Maintain consistency with existing code style and patterns

---

## Task List

### 1. Modify Existing Files

- [ ] **Update Course Model in Models File**
  - **File**: `src/models.py`
  - **Description**: Add the `Course` model definition based on the provided model blueprint.
  
```python
from sqlalchemy import Column, Integer, String
from your_app.database import Base  # Adjust import based on actual structure

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)

    def __repr__(self):
        return f'<Course {self.id}: {self.name}, Level: {self.level}>'
```

- [ ] **Define New Routes in Application File**
  - **File**: `src/app.py`
  - **Description**: Add route definitions for handling create and retrieve course requests.
  
```python
@app.route('/courses', methods=['POST'])
@app.route('/courses/<int:id>', methods=['GET'])
```

### 2. Create New Files

- [ ] **Implement Course Controller Logic**
  - **File**: `src/controllers/course_controller.py`
  - **Description**: Implement the controller logic for course creation and retrieval, including input validation and error responses.

```python
from flask import request, jsonify
from models import Course, db

@app.route('/courses', methods=['POST'])
def create_course():
    data = request.get_json()
    name = data.get('name')
    level = data.get('level')
    
    if not name or not level:
        return jsonify({"error": {"code": "E001", "message": "Name and Level are required"}}), 400
    
    course = Course(name=name, level=level)
    db.session.add(course)
    db.session.commit()
    return jsonify({"id": course.id, "name": course.name, "level": course.level}), 201

@app.route('/courses/<int:id>', methods=['GET'])
def get_course(id):
    course = Course.query.get(id)
    if not course:
        return jsonify({"error": {"code": "E002", "message": "Course not found"}}), 404
    return jsonify({"id": course.id, "name": course.name, "level": course.level}), 200
```

### 3. Database Management Tasks

- [ ] **Create Migration for New Course Table**
  - **File**: N/A (command line execution)
  - **Description**: Run migration commands to add `courses` table to the database schema.
  
```bash
flask db migrate -m "Add Course entity to the database"
flask db upgrade
```

### 4. Testing Tasks

- [ ] **Add Unit Tests for Course Functionality**
  - **File**: `tests/test_app.py`
  - **Description**: Write tests for creating and retrieving courses to ensure both positive and negative scenarios are covered.

```python
def test_create_course():
    response = client.post('/courses', json={"name": "Mathematics", "level": "Beginner"})
    assert response.status_code == 201
    assert response.json['name'] == "Mathematics"
    assert response.json['level'] == "Beginner"

def test_create_course_missing_fields():
    response = client.post('/courses', json={"name": ""})
    assert response.status_code == 400
    assert response.json['error']['code'] == "E001"

def test_get_course():
    response = client.get('/courses/1')
    assert response.status_code == 200
    assert response.json['id'] == 1
```

---

This task breakdown provides a structured plan to implement the Course entity feature, ensuring systematic development and testing while adhering to existing project standards. Each task is independent and can be executed and tested as a separate unit.