# Tasks: Create Teacher Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `src/models.py`
- `src/controllers/teacher_controller.py`
- `tests/test_teacher.py`

---

## Task Breakdown

### Task 1: Create Teacher Model
- **File**: `src/models.py`
- **Description**: Introduce the new `Teacher` model.
- **Implementation**:
    ```python
    from sqlalchemy import Column, Integer, String
    from your_app.database import Base  # Adjust import based on actual structure

    class Teacher(Base):
        __tablename__ = 'teachers'
        
        id = Column(Integer, primary_key=True, autoincrement=True)
        name = Column(String, nullable=False)
        email = Column(String, nullable=False)

        def __repr__(self):
            return f'<Teacher {self.id}: {self.name}, Email: {self.email}>'
    ```

---

### Task 2: Implement Create Teacher Endpoint
- **File**: `src/controllers/teacher_controller.py`
- **Description**: Create the logic for the `POST /teachers` endpoint to handle teacher creation.
- **Implementation Steps**:
    ```python
    from flask import request, jsonify
    from models import Teacher, db

    @app.route('/teachers', methods=['POST'])
    def create_teacher():
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')

        if not name or not email:
            return jsonify({"error": {"code": "E001", "message": "Name and Email are required"}}), 400

        new_teacher = Teacher(name=name, email=email)
        db.session.add(new_teacher)
        db.session.commit()

        return jsonify({"id": new_teacher.id, "name": new_teacher.name, "email": new_teacher.email}), 201
    ```

---

### Task 3: Implement Retrieve Teacher Endpoint
- **File**: `src/controllers/teacher_controller.py`
- **Description**: Create the logic for the `GET /teachers/{id}` endpoint to retrieve teacher details.
- **Implementation Steps**:
    ```python
    @app.route('/teachers/<int:id>', methods=['GET'])
    def get_teacher(id):
        teacher = Teacher.query.get(id)
        if not teacher:
            return jsonify({"error": {"code": "E002", "message": "Teacher not found"}}), 404

        return jsonify({"id": teacher.id, "name": teacher.name, "email": teacher.email}), 200
    ```

---

### Task 4: Database Migration for Teacher Table
- **File**: `migrations/`
- **Description**: Create migration scripts to add the `teachers` table to the database.
- **Implementation Steps**:
    ```bash
    flask db migrate -m "Add Teacher table"
    flask db upgrade
    ```

---

### Task 5: Update Route Definitions
- **File**: `src/app.py`
- **Description**: Define routes to include the newly added teacher endpoints.
- **Implementation Steps**:
    ```python
    from controllers.teacher_controller import create_teacher, get_teacher

    @app.route('/teachers', methods=['POST'])
    @app.route('/teachers/<int:id>', methods=['GET'])
    ```

---

### Task 6: Create Unit Tests for Teacher Functionality
- **File**: `tests/test_teacher.py`
- **Description**: Write unit tests to validate the creation and retrieval of the teacher.
- **Implementation**:
    ```python
    import pytest
    from app import app  # Assuming 'app' is the Flask app instance
    from models import Teacher, db  # Assuming Teacher model is defined in 'models.py'

    @pytest.fixture
    def client():
        with app.test_client() as client:
            yield client

    def test_create_teacher_success(client):
        response = client.post('/teachers', json={"name": "John Doe", "email": "john.doe@example.com"})
        assert response.status_code == 201
        assert response.json['name'] == "John Doe"

    def test_create_teacher_missing_fields(client):
        response = client.post('/teachers', json={"name": "John Doe"})
        assert response.status_code == 400
        assert response.json['error']['code'] == 'E001'

    def test_get_teacher_success(client):
        new_teacher = Teacher(name="Jane Doe", email="jane.doe@example.com")
        db.session.add(new_teacher)
        db.session.commit()

        response = client.get(f'/teachers/{new_teacher.id}')
        assert response.status_code == 200
        assert response.json['name'] == "Jane Doe"

    def test_get_teacher_not_found(client):
        response = client.get('/teachers/999')
        assert response.status_code == 404
        assert response.json['error']['code'] == 'E002'
    ```

---

### Task 7: Document Teacher API in README.md
- **File**: `README.md`
- **Description**: Update the documentation to include the new endpoints for creating and retrieving teachers.
- **Implementation**:
    ```markdown
    ## Teacher API

    ### Create Teacher
    - **Endpoint**: `POST /teachers`
    - **Request Body**:
      ```json
      {
        "name": "John Doe",
        "email": "john.doe@example.com"
      }
      ```
    - **Responses**:
      - **201 Created**: on success with teacher details
      - **400 Bad Request**: error for missing fields

    ### Retrieve Teacher
    - **Endpoint**: `GET /teachers/{id}`
    - **Responses**:
      - **200 OK**: on successful retrieval of teacher details
      - **404 Not Found**: if the teacher does not exist
    ```

--- 

This structured task breakdown ensures all necessary steps are taken to integrate the `Teacher` entity into the application while adhering to the existing code structure and best practices.