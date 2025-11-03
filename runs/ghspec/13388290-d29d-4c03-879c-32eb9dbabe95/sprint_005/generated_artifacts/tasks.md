# Tasks: Create Teacher Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- tests/test_api/test_student.py (2300 bytes)
- tests/test_models/test_student_courses.py (2404 bytes)

## Task Breakdown

### Database Schema & Migration

- [ ] **Task 1: Create Teacher Model**
  - **File**: `src/models/teacher.py`
  - **Description**: Implement SQLAlchemy model for the `Teacher` entity with fields for `name` and `email`.
  ```python
  class Teacher(db.Model):
      __tablename__ = 'teachers'
      id = db.Column(db.Integer, primary_key=True)
      name = db.Column(db.String, nullable=False)
      email = db.Column(db.String, nullable=False, unique=True)
  ```

- [ ] **Task 2: Create Migration Script**
  - **File**: `migrations/versions/XXXX_create_teacher_table.py`
  - **Description**: Add a new migration file to create the `teachers` table in the database. Ensure no existing data is affected.
  ```python
  def upgrade():
      op.create_table(
          'teachers',
          sa.Column('id', sa.Integer, primary_key=True),
          sa.Column('name', sa.String, nullable=False),
          sa.Column('email', sa.String, nullable=False, unique=True),
      )
  
  def downgrade():
      op.drop_table('teachers')
  ```

### API Endpoints Implementation

- [ ] **Task 3: Implement POST /teachers Endpoint**
  - **File**: `src/routes/teacher.py`
  - **Description**: Create Flask route to handle teacher creation logic including validation for `name` and `email`.
  ```python
  @app.route('/teachers', methods=['POST'])
  def create_teacher():
      data = request.get_json()
      name = data.get("name")
      email = data.get("email")

      if not name or not email:
          return jsonify(error={'code': 'E001', 'message': 'Name and email are required.'}), 400

      new_teacher = Teacher(name=name, email=email)
      db.session.add(new_teacher)
      db.session.commit()
      return jsonify(id=new_teacher.id, name=new_teacher.name, email=new_teacher.email), 201
  ```

- [ ] **Task 4: Implement GET /teachers Endpoint**
  - **File**: `src/routes/teacher.py`
  - **Description**: Create Flask route to return a list of all teachers in the system.
  ```python
  @app.route('/teachers', methods=['GET'])
  def get_teachers():
      teachers = Teacher.query.all()
      return jsonify(teachers=[{'id': t.id, 'name': t.name, 'email': t.email} for t in teachers]), 200
  ```

### Testing

- [ ] **Task 5: Create Tests for Teacher API**
  - **File**: `tests/test_api/test_teacher.py`
  - **Description**: Write unit tests for `create_teacher` and `get_teachers` endpoints, including validation for required fields.
  ```python
  def test_create_teacher(client):
      response = client.post('/teachers', json={'name': 'Jane Doe', 'email': 'janedoe@example.com'})
      assert response.status_code == HTTPStatus.CREATED
      assert 'id' in response.json
  
  def test_create_teacher_without_name(client):
      response = client.post('/teachers', json={'email': 'janedoe@example.com'})
      assert response.status_code == HTTPStatus.BAD_REQUEST
      assert response.json['error']['code'] == 'E001'
  
  def test_get_teachers(client):
      client.post('/teachers', json={'name': 'John Doe', 'email': 'johndoe@example.com'})
      response = client.get('/teachers')
      assert response.status_code == HTTPStatus.OK
      assert len(response.json['teachers']) > 0
  ```

### Documentation

- [ ] **Task 6: Update API Documentation**
  - **File**: `docs/api_reference.md`
  - **Description**: Document the new `/teachers` endpoint for API reference including request and response examples.

- [ ] **Task 7: Update README.md**
  - **File**: `README.md`
  - **Description**: Update README with setup instructions and an overview of the new Teacher entity functionality.

### Migration & Integration

- [ ] **Task 8: Run Database Migration**
  - **File**: N/A (CLI Command)
  - **Description**: Execute the migration to add the `teachers` table using Flask-Migrate.

- [ ] **Task 9: Confirm No Disruption to Existing Functionality**
  - **File**: N/A
  - **Description**: Verify that the existing functionality for Students and Courses remains intact after migration.

By following these tasks, the implementation of the Teacher entity will be systematically completed, ensuring all aspects of functionality, testing, and documentation are covered.