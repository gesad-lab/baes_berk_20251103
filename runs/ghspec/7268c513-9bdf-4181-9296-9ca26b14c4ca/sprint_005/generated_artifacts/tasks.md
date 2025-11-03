# Tasks: Create Teacher Entity

---

## INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- Existing code for student and course management.

Instructions for Task Breakdown:
1. Identify which existing files need modifications
2. Create new files for new functionality
3. Ensure integration tasks are included
4. Maintain consistency with existing code style and patterns

---

- [ ] **Task 1: Set up Development Environment**
  - **File**: `README.md`
  - **Description**: Include setup instructions for the new teacher functionality.
  
- [ ] **Task 2: Create Teacher Model**
  - **File**: `models/teacher.py`
  - **Description**: Define the `Teacher` model class with attributes `id`, `name`, and `email`.
  
  ```python
  from app import db
  from sqlalchemy import Column, Integer, String
  
  class Teacher(db.Model):
      __tablename__ = 'teachers'
      
      id = Column(Integer, primary_key=True, autoincrement=True)
      name = Column(String, nullable=False)
      email = Column(String, nullable=False)
  ```

- [ ] **Task 3: Update API Routes for Teacher Creation**
  - **File**: `routes.py`
  - **Description**: Implement the `POST /teachers` endpoint to handle teacher creation requests.
  
  ```python
  from flask import Blueprint, request, jsonify
  from models.teacher import Teacher
  from app import db
  
  teachers_bp = Blueprint('teachers', __name__)
  
  @teachers_bp.route('/teachers', methods=['POST'])
  def create_teacher():
      data = request.get_json()
      name = data.get('name')
      email = data.get('email')
      
      if not name or not email:
          return jsonify({"error": {"code": "E001", "message": "Name and email are required."}}), 400
  
      new_teacher = Teacher(name=name, email=email)
      db.session.add(new_teacher)
      db.session.commit()
  
      return jsonify({"id": new_teacher.id, "name": new_teacher.name, "email": new_teacher.email}), 201
  ```

- [ ] **Task 4: Add Database Migration Script**
  - **File**: `migrations/versions/add_teachers_table.py`
  - **Description**: Create a migration script to add the `teachers` table to the existing database schema.
  
  ```python
  def upgrade():
      op.create_table('teachers',
          sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
          sa.Column('name', sa.String, nullable=False),
          sa.Column('email', sa.String, nullable=False)
      )
  ```

- [ ] **Task 5: Implement Validation Logic**
  - **File**: `routes.py`
  - **Description**: Ensure the request body contains both `name` and `email` before creating a teacher. If either field is missing, return a structured error response.

- [ ] **Task 6: Implement Error Handling**
  - **File**: `routes.py`
  - **Description**: Return a JSON error response for requests missing the required fields.
  
  ```python
  if not name or not email:
      return jsonify({"error": {"code": "E001", "message": "Name and email are required."}}), 400
  ```

- [ ] **Task 7: Create Unit Tests**
  - **File**: `tests/test_teacher.py`
  - **Description**: Write unit tests for teacher creation to verify correct integration of the teacher creation logic and error handling.
  
  ```python
  def test_create_teacher(client):
      response = client.post('/teachers', json={"name": "John Doe", "email": "john.doe@example.com"})
      assert response.status_code == 201
      assert "id" in response.json
      assert response.json["name"] == "John Doe"
      assert response.json["email"] == "john.doe@example.com"

  def test_create_teacher_without_name(client):
      response = client.post('/teachers', json={"email": "john.doe@example.com"})
      assert response.status_code == 400
      assert response.json['error']['code'] == "E001"

  def test_create_teacher_without_email(client):
      response = client.post('/teachers', json={"name": "John Doe"})
      assert response.status_code == 400
      assert response.json['error']['code'] == "E001"
  ```

- [ ] **Task 8: Update API Documentation**
  - **File**: `README.md`
  - **Description**: Document the new `POST /teachers` endpoint in the API section, detailing the request format and expected responses.

- [ ] **Task 9: Ensure Backward Compatibility of Existing Data**
  - **File**: `tests/test_integration.py`
  - **Description**: Write integration tests to ensure that existing student and course data are intact after the migration.

This task breakdown ensures that each part of the implementation is addressed in a modular way, making it easier to track progress and maintain code quality throughout the development process.