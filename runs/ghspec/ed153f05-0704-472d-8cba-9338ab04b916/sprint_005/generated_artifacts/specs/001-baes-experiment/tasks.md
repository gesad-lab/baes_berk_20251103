# Tasks: Create Teacher Entity

---

## INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `tests/test_routes.py` (2444 bytes)
- `tests/test_models.py` (1844 bytes)

---

### Task List

#### 1. Setup Environment
- [ ] **Task**: Ensure the `.env` file is updated with any necessary configuration settings.
  - **File Path**: `./.env`

#### 2. Update the Model
- [ ] **Task**: Create the `Teacher` model in `models.py` to define the `Teacher` entity.
  - **File Path**: `./src/models.py`
  
  ```python
  class Teacher(db.Model):
      __tablename__ = 'teachers'
      id = db.Column(db.Integer, primary_key=True)
      name = db.Column(db.String, nullable=False)
      email = db.Column(db.String, nullable=False, unique=True)
  ```

#### 3. Database Migration
- [ ] **Task**: Use Flask-Migrate to create a migration script for adding the `teachers` table.
  - **File Path**: Command Line
  ```bash
  flask db migrate -m "Create teachers table"
  flask db upgrade
  ```

#### 4. Update Marshmallow schemas
- [ ] **Task**: Create a new schema for the `Teacher` model in `schemas.py`.
  - **File Path**: `./src/schemas.py`
  
  ```python
  class TeacherSchema(ma.SQLAlchemyAutoSchema):
      class Meta:
          model = Teacher
          fields = ("id", "name", "email")
  ```

#### 5. Add API Endpoint
- [ ] **Task**: Implement the `POST /teachers` endpoint in `routes.py`.
  - **File Path**: `./src/routes.py`
  
  ```python
  @app.route('/teachers', methods=['POST'])
  def create_teacher():
      data = request.get_json()
      # validation for name and email
      if not data.get('name'):
          return {"error": {"code": "E001", "message": "Name is required."}}, 400
      if not data.get('email'):
          return {"error": {"code": "E002", "message": "Email is required."}}, 400

      new_teacher = Teacher(name=data['name'], email=data['email'])
      db.session.add(new_teacher)
      db.session.commit()
      
      return {"message": "Teacher created successfully."}, 201
  ```

#### 6. Implement Error Handling and Validation
- [ ] **Task**: Ensure structured error responses in the `create_teacher` function for missing name or email.
  - **File Path**: `./src/routes.py` (included in previous task)

#### 7. Testing
- [ ] **Task**: Write unit tests for the `Teacher` model and API endpoint in `test_routes.py`.
  - **File Path**: `./tests/test_routes.py`
- [ ] **Task**: Write unit tests for the functionalities of the `Teacher` model in `test_models.py`.
  - **File Path**: `./tests/test_models.py`
  
```python
def test_create_teacher_success(db):
    """Test creating a new teacher with valid data."""
    response = app.test_client().post('/teachers', json={"name": "John Smith", "email": "john.smith@example.com"})
    assert response.status_code == 201
    assert response.json['message'] == "Teacher created successfully."

def test_create_teacher_missing_name(db):
    """Test creating a teacher without a name."""
    response = app.test_client().post('/teachers', json={"email": "john.smith@example.com"})
    assert response.status_code == 400
    assert response.json['error']['code'] == "E001"
    assert response.json['error']['message'] == "Name is required."

def test_create_teacher_missing_email(db):
    """Test creating a teacher without an email."""
    response = app.test_client().post('/teachers', json={"name": "John Smith"})
    assert response.status_code == 400
    assert response.json['error']['code'] == "E002"
    assert response.json['error']['message'] == "Email is required."
```

#### 8. Documentation
- [ ] **Task**: Update the README.md file to include the new `/teachers` API endpoint and how to create a teacher.
  - **File Path**: `./README.md` 

---

Each task is focused on a specific file or functionality, ensuring that every aspect of creating the `Teacher` entity can be implemented independently and tested efficiently.