# Tasks: Create Teacher Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `tests/test_teacher.py` (existing testing framework)

Instructions for Task Breakdown:
1. Identify which existing files need modifications
2. Create new files for new functionality
3. Ensure integration tasks are included
4. Maintain consistency with existing code style and patterns

---

## Task 1: Create Teacher Model

- **File**: `src/models/teacher.py`
- **Description**: Define the Teacher entity and set up SQLAlchemy model fields according to specifications.
```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Teacher(Base):
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)  # Email should be unique
```
- [ ] Implement Teacher model.

---

## Task 2: Create Database Migration

- **File**: `migrations/versions/<timestamp>_create_teachers_table.py`
- **Description**: Create a new migration script that adds the Teacher table to the database schema.
```python
from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table('teachers',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False, unique=True)
    )

def downgrade():
    op.drop_table('teachers')
```
- [ ] Include `upgrade` and `downgrade` functions.

---

## Task 3: Implement Create Teacher API Endpoint

- **File**: `src/api/teachers.py`
- **Description**: Extend the existing API layer to include endpoints for adding a teacher.
```python
from flask import Blueprint, request, jsonify
from models.teacher import Teacher
from database import db  # Assuming a database module that initializes SQLAlchemy

teachers_bp = Blueprint('teachers', __name__)

@teachers_bp.route('/teachers', methods=['POST'])
def create_teacher():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    # Validating required fields
    if not name or not email:
        return jsonify({"error": {"code": "E001", "message": "Missing required fields: name, email."}}), 400

    new_teacher = Teacher(name=name, email=email)
    db.session.add(new_teacher)
    db.session.commit()

    return jsonify({
        "id": new_teacher.id,
        "name": new_teacher.name,
        "email": new_teacher.email
    }), 201
```
- [ ] Implement POST /teachers endpoint.

---

## Task 4: Implement Retrieve Teacher API Endpoint

- **File**: `src/api/teachers.py`
- **Description**: Extend the API layer to include an endpoint for retrieving teacher information by ID.
```python
@teachers_bp.route('/teachers/<int:teacher_id>', methods=['GET'])
def get_teacher(teacher_id):
    teacher = Teacher.query.get(teacher_id)
    if not teacher:
        return jsonify({"error": {"code": "E002", "message": "Teacher not found."}}), 404

    return jsonify({
        "id": teacher.id,
        "name": teacher.name,
        "email": teacher.email
    }), 200
```
- [ ] Implement GET /teachers/{teacher_id} endpoint.

---

## Task 5: Update Tests for Teacher API

- **File**: `tests/test_teacher.py`
- **Description**: Add tests for the new functionality of creating and retrieving teachers.
```python
def test_create_teacher(client):
    response = client.post('/teachers', json={"name": "Jane Doe", "email": "janedoe@example.com"})
    assert response.status_code == 201
    assert response.json['name'] == "Jane Doe"

def test_create_teacher_missing_fields(client):
    response = client.post('/teachers', json={"name": "", "email": "janedoe@example.com"})
    assert response.status_code == 400
    assert "Missing required fields" in response.json['error']['message']

def test_get_teacher(client):
    response = client.get('/teachers/1')  # Assuming "Jane Doe" has ID 1
    assert response.status_code == 200
    assert response.json['name'] == "Jane Doe"
```
- [ ] Add tests to cover the creation and retrieval functionalities.

---

## Task 6: Health Check Endpoint

- **File**: `src/api/health.py`
- **Description**: Create a health check endpoint to monitor application status.
```python
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200
```
- [ ] Implement health check endpoint.

---

## Task 7: Update README.md Documentation

- **File**: `README.md`
- **Description**: Document the new API endpoints and their usage.
```markdown
### Teacher Management

#### Create a Teacher
- **Endpoint**: POST /teachers
- **Request JSON**:
    ```json
    {
      "name": "Jane Doe",
      "email": "janedoe@example.com"
    }
    ```
- **Response**:
    ```json
    {
      "id": 1,
      "name": "Jane Doe",
      "email": "janedoe@example.com"
    }
    ```

#### Retrieve a Teacher
- **Endpoint**: GET /teachers/{id}
- **Response**:
    ```json
    {
      "id": 1,
      "name": "Jane Doe",
      "email": "janedoe@example.com"
    }
    ```
```
- [ ] Document new features and how to use the Teacher management API.

---

## Task 8: Ensure Migration is Run on Startup

- **File**: `src/app.py` (or the main application file)
- **Description**: Ensure the migration scripts are executed on application startup.
```python
from flask import Flask
from migrations import upgrade  # Ensure this imports the upgrade function from Alembic migration scripts

app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)

with app.app_context():
    upgrade()  # Run migrations to ensure the database is up-to-date
```
- [ ] Ensure migrations run on application startup.

--- 

This structured task breakdown ensures that each task is focused, small, and can be independently tested, following the guidelines provided in the project constitution.