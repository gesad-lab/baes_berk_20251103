# Tasks: Create Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `tests/test_routes.py` (2580 bytes)
- `tests/test_models.py` (2349 bytes)

---

## Task Breakdown

### Task 1: Update Environment Configuration
- **File**: `/.env`
- **Description**: Update the `.env` file for any new configuration settings necessary for the Course feature.
- **Dependencies**: None
- [ ] Update `.env` for relevant Course feature configurations.

### Task 2: Create Course Model
- **File**: `src/models.py`
- **Description**: Define the `Course` model with `name` and `level` attributes.
```python
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    level = db.Column(db.String, nullable=False)
```
- **Dependencies**: Task 1
- [ ] Implement the Course model in `models.py`.

### Task 3: Database Migration
- **File**: `src/database.py`
- **Description**: Create and apply a migration script to add the `Course` table to the database.
- **Command to Run**: 
```bash
flask db migrate -m "Add Course table"
flask db upgrade
```
- **Dependencies**: Task 2
- [ ] Use Flask-Migrate to create and apply the migration for the Course table.

### Task 4: Create Marshmallow Schema
- **File**: `src/schemas.py`
- **Description**: Create a `CourseSchema` for validating Course entity data.
```python
class CourseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Course
        fields = ("id", "name", "level")
```
- **Dependencies**: Task 2
- [ ] Implement `CourseSchema` in `schemas.py`.

### Task 5: Implement POST /courses Endpoint
- **File**: `src/routes.py`
- **Description**: Add an endpoint to create a new course with appropriate validation and response structure.
```python
@app.route('/courses', methods=['POST'])
def create_course():
    ...
```
- **Dependencies**: Task 4
- [ ] Implement the POST /courses endpoint in `routes.py`.

### Task 6: Implement GET /courses/{id} Endpoint
- **File**: `src/routes.py`
- **Description**: Add an endpoint to retrieve a course by its ID.
```python
@app.route('/courses/<int:id>', methods=['GET'])
def get_course(id):
    ...
```
- **Dependencies**: Task 4
- [ ] Implement the GET /courses/{id} endpoint in `routes.py`.

### Task 7: Implement GET /courses Endpoint
- **File**: `src/routes.py`
- **Description**: Add an endpoint to retrieve a list of all courses.
```python
@app.route('/courses', methods=['GET'])
def get_all_courses():
    ...
```
- **Dependencies**: Task 4
- [ ] Implement the GET /courses endpoint in `routes.py`.

### Task 8: Implement Validation for Required Fields
- **File**: `src/routes.py`
- **Description**: Add validation logic to check for required fields (`name` and `level`) in the POST request.
- **Dependencies**: Task 5
- [ ] Implement input validation for the POST /courses endpoint in `routes.py`.

### Task 9: Write Unit Tests for Course Model
- **File**: `tests/test_models.py`
- **Description**: Create tests for validating functionality of the `Course` model and its attributes.
- **Dependencies**: Task 2
- [ ] Implement unit tests for the Course model in `test_models.py`.

### Task 10: Write Integration Tests for Course API Endpoints
- **File**: `tests/test_routes.py`
- **Description**: Create tests for the newly implemented API endpoints (POST and GET).
- **Dependencies**: Task 5, Task 6, Task 7
- [ ] Implement integration tests for course functionalities in `test_routes.py`.

### Task 11: Update API Documentation
- **File**: `README.md`
- **Description**: Update the documentation to include new Course feature details and API endpoints.
- **Dependencies**: Tasks 5, 6, 7
- [ ] Update `README.md` with details regarding the new Course API endpoints.

### Task 12: Test and Verify All Implementations
- **File**: N/A
- **Description**: Run all tests and verify that course creation, retrieval, and validation are functioning as expected to achieve target coverage.
- **Dependencies**: Tasks 9, 10
- [ ] Execute tests to ensure compliance with required functionality and coverage.

---

Each task is structured to be executed independently within the context of the Course entity implementation, ensuring clarity and focus on specific modifications.