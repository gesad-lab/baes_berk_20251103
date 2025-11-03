# Tasks: Create Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `models.py`
- `database.py`
- `routes.py`
- `validators.py`
- `tests/api/test_courses.py`
- `tests/api/test_validators.py`

## Task Breakdown

### Task 1: Define Course Model
- **File**: `src/models.py`
- **Description**: Introduce the `Course` model with `name` and `level` fields.
- **Implementation**:
  ```python
  class Course(Base):
      __tablename__ = 'courses'
      id = Column(Integer, primary_key=True)
      name = Column(String, nullable=False)
      level = Column(String, nullable=False)
  ```

- [ ] Implement `Course` model in `src/models.py`

### Task 2: Create Database Migration for Course Table
- **File**: `src/database.py`
- **Description**: Manage database schema changes to include the new `courses` table.
- **Implementation**: Use Alembic or SQLAlchemy to create migration logic.
- [ ] Implement migration strategy for `Course` table in `src/database.py`

### Task 3: Create Course Creation Endpoint
- **File**: `src/routes.py`
- **Description**: Add a new endpoint for creating a course that accepts `name` and `level`.
- **Implementation**:
  ```python
  @app.route('/courses', methods=['POST'])
  def create_course():
      data = request.get_json()
      # Validation logic here
  ```
- [ ] Implement `/courses` endpoint in `src/routes.py`

### Task 4: Implement Input Validation for Course Creation
- **File**: `src/validators.py`
- **Description**: Add validation logic to ensure `name` and `level` fields are provided.
- **Implementation**:
  ```python
  def validate_course(data):
      if not data.get('name') or not data.get('level'):
          raise ValueError('Name and level fields are required')
  ```
- [ ] Implement input validation in `src/validators.py`

### Task 5: Create Course Retrieval Endpoint
- **File**: `src/routes.py`
- **Description**: Add a new endpoint for retrieving course details based on course ID.
- **Implementation**:
  ```python
  @app.route('/courses/<int:course_id>', methods=['GET'])
  def get_course(course_id):
      # Logic to fetch course
  ```
- [ ] Implement `/courses/{course_id}` endpoint in `src/routes.py`

### Task 6: Update Tests for Course Creation
- **File**: `tests/api/test_courses.py`
- **Description**: Ensure that tests are in place for course creation with valid and invalid data.
- **Implementation**:
  ```python
  def test_create_course_valid():
      response = test_client.post('/courses', json={"name": "Math 101", "level": "Beginner"})
      # Assertions here

  def test_create_course_missing_fields():
      response = test_client.post('/courses', json={"name": "", "level": ""})
      # Assertions here
  ```
- [ ] Add/Update tests for course creation in `tests/api/test_courses.py`

### Task 7: Update Tests for Input Validation
- **File**: `tests/api/test_validators.py`
- **Description**: Add tests for validation logic regarding course name and level.
- **Implementation**:
  ```python
  def test_validate_course_name_empty():
      assert not validate_course_name("")

  def test_validate_course_name_valid():
      assert validate_course_name("Math 101")
  ```
- [ ] Add tests for input validation in `tests/api/test_validators.py`

### Task 8: Migrate Existing Data Safely
- **File**: `src/database.py`
- **Description**: Ensure that the existing student data remains intact during the course table migration.
- [ ] Implement migration logic that preserves existing data in `src/database.py`

### Task 9: Validate and Test API Responses
- **File**: `tests/api/test_courses.py`
- **Description**: Ensure that the API responses are in JSON format and structured correctly.
- [ ] Validate response structure for both course creation and retrieval in `tests/api/test_courses.py`

### Task 10: Documentation Update
- **File**: `README.md`
- **Description**: Update the documentation to reflect the newly added Course entity and its API details.
- [ ] Update `README.md` to include information on the Course entity and API endpoints

--- 

Each task must be completed independently and tested to ensure successful integration into the overall system. Tasks are ordered by dependencies to maintain a logical progress workflow.