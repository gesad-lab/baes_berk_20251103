# Tasks: Create Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `tests/test_routes.py` (1799 bytes)
- `tests/test_validation.py` (2097 bytes)

## Task Breakdown

### 1. Database Model
- [ ] **Update Data Model**  
  - **File**: `src/models.py`  
  - **Description**: Add the new `Course` class to represent the Course entity in the database.
  - **Example Code**:
    ```python
    class Course(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(100), nullable=False)
        level = db.Column(db.String(50), nullable=False)
    ```

### 2. Marshmallow Schema
- [ ] **Set Up Marshmallow Schema**  
  - **File**: `src/schemas.py`  
  - **Description**: Create a new `CourseSchema` for serialization and validation of course data.
  - **Example Code**:
    ```python
    from marshmallow import Schema, fields
    
    class CourseSchema(Schema):
        id = fields.Int(dump_only=True)
        name = fields.Str(required=True)
        level = fields.Str(required=True)
    ```

### 3. API Endpoints
- [ ] **Create API Endpoints**  
  - **File**: `src/routes.py`  
  - **Description**: Develop the `POST /courses` endpoint to handle course creation requests and validate input.
  - **Example Code**:
    ```python
    @app.route('/courses', methods=['POST'])
    def create_course():
        # Implementation for creating a course
    ```
  
- [ ] **Implement Get Course by ID Endpoint**  
  - **File**: `src/routes.py`  
  - **Description**: Implement the `GET /courses/{id}` endpoint to retrieve course details.
  - **Example Code**:
    ```python
    @app.route('/courses/<int:id>', methods=['GET'])
    def get_course(id):
        # Implementation for retrieving a course by ID
    ```

### 4. Database Migration
- [ ] **Update Database Schema**  
  - **File**: `src/db.py`  
  - **Description**: Create a migration script to add the `courses` table to the SQLite database.
  - **Example SQL**:
    ```sql
    CREATE TABLE courses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(100) NOT NULL,
        level VARCHAR(50) NOT NULL
    );
    ```

### 5. Input Validation
- [ ] **Implement Input Validation**  
  - **File**: `src/routes.py`  
  - **Description**: Add validation checks to ensure `name` and `level` are provided before accepting requests.
  - **Example Validation Logic**: 
    ```python
    if not name or not level:
        return {"error": {"code": "E001", "message": "Name and level are required"}}, 400
    ```

### 6. Testing
- [ ] **Create Unit Tests for Course Validation**  
  - **File**: `tests/test_validation.py`  
  - **Description**: Extend existing tests to include validation for the Course entity.
  - **Example Test**:
    ```python
    def test_course_validation_missing_name(self, course_schema):
        invalid_data = {"level": "Beginner"}
        with pytest.raises(ValidationError):
            course_schema.load(invalid_data)
    ```

- [ ] **Add Integration Tests for API Endpoints**  
  - **File**: `tests/test_routes.py`  
  - **Description**: Validate the new endpoints for creating and retrieving course entities.
  - **Example Test**:
    ```python
    def test_create_course_with_valid_data(client):
        response = client.post('/courses', ... )  # Include valid course data
    ```

### 7. Documentation
- [ ] **Update Project Documentation**  
  - **File**: `README.md`  
  - **Description**: Document the new API endpoints for creating and retrieving Course entities. Include JSON structure and error codes.
  
### 8. Deployment Considerations
- [ ] **Prepare Migration Instructions**  
  - **File**: `README.md`  
  - **Description**: Provide clear instructions for applying the new database migrations in production without downtime.

---

This structured task breakdown allows for independent execution and testing of each step within the implementation of the Course entity. Each task is file-specific, ensuring clarity and focus.