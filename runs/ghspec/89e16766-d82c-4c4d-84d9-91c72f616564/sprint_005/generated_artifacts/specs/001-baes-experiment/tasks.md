# Tasks: Create Teacher Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- app/models.py (define new Teacher model)
- app/routes.py (extend with new endpoints for teacher management)
- tests/api/test_students.py (for example test structures)

## Task Breakdown

### 1. Create Teacher Model

- **Task**: Define the Teacher model.
- **File**: `app/models.py`
- **Description**: Implement the Teacher class with specified attributes.
```python
class Teacher(db.Model):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
```
- [ ] Implement Teacher model in `app/models.py`

### 2. Extend API Layer with Teacher Endpoints

- **Task**: Add the POST `/teachers` endpoint.
- **File**: `app/routes.py`
- **Description**: Create function for adding a new teacher, validating input, and returning the created teacher's details.
```python
@app.route('/teachers', methods=['POST'])
def create_teacher():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    
    # Validation logic...

    teacher = Teacher(name=name, email=email)
    db.session.add(teacher)
    db.session.commit()
    
    return jsonify({"message": "Teacher created successfully.", "teacher": {"id": teacher.id, "name": teacher.name, "email": teacher.email}}), 201
```
- [ ] Implement create_teacher method in `app/routes.py`

- **Task**: Add the GET `/teachers/<teacher_id>` endpoint.
- **File**: `app/routes.py`
- **Description**: Create function for retrieving a teacher by ID and returning their details.
```python
@app.route('/teachers/<int:teacher_id>', methods=['GET'])
def get_teacher(teacher_id):
    teacher = Teacher.query.get_or_404(teacher_id)
    return jsonify({"id": teacher.id, "name": teacher.name, "email": teacher.email})
```
- [ ] Implement get_teacher method in `app/routes.py`

### 3. Create Database Migration for Teacher Table

- **Task**: Create a database migration for the new Teacher table.
- **File**: `migrations/versions/` (generated migration file)
- **Description**: Run migration commands to create the new `teachers` table.
```bash
flask db migrate -m "Add teachers table"
flask db upgrade
```
- [ ] Execute migration commands and verify migration file is created

### 4. Implement Input Validation in Teacher Endpoints

- **Task**: Add validation logic to endpoints.
- **File**: `app/routes.py`
- **Description**: Ensure appropriate validation checks are performed for name and email before creating a teacher.
```python
if not name or not email:
    return jsonify({"error": {"code": "E001", "message": "Name is required."}}), 400
```
- [ ] Implement input validation logic in `app/routes.py`

### 5. Create Unit Tests for Teacher Endpoints

- **Task**: Write unit tests for creating and retrieving teachers.
- **File**: `tests/api/test_teachers.py`
- **Description**: Implement tests for the new endpoints ensuring they work as expected.
```python
def test_create_teacher(test_client):
    response = test_client.post('/teachers', json={'name': 'Jane Doe', 'email': 'jane.doe@example.com'})
    assert response.status_code == 201
    assert response.json['message'] == "Teacher created successfully."

def test_get_teacher(test_client):
    response = test_client.get('/teachers/1')
    assert response.status_code == 200
    assert response.json['name'] == "Jane Doe"
```
- [ ] Implement testing cases in `tests/api/test_teachers.py`

### 6. Execute Tests to Validate Functionality

- **Task**: Run tests to verify functionality of teacher endpoints and validation.
- **File**: - (pytest command line)
- **Description**: Validate using pytest to ensure all tests pass successfully.
```bash
pytest tests/
```
- [ ] Execute tests and validate all tests pass 

### 7. Update Documentation with New Endpoints

- **Task**: Document the new teacher API functionality.
- **File**: `README.md` or relevant docs file
- **Description**: Describe the new teacher endpoints, request/response formats, and example inputs/outputs.
- [ ] Update API documentation in `README.md`

This task breakdown creates a structured approach for effectively implementing the feature while ensuring adherence to coding standards and practices. Each task is scoped to a single file for independent testing and validation.