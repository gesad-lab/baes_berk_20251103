# Tasks: Create Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `tests/test_routes.py`
- `tests/test_services.py`

---

## Task Breakdown

### Database Migration
- [ ] **Task 1:** Create migration for the `courses` table.
  - **File Path**: `migrations/versions/20230101010101_create_course_table.py`
  - **Description**: Implement the migration script for creating the `courses` table with `id`, `name`, and `level` columns. Ensure that it does not interfere with existing `Student` data.

### Models
- [ ] **Task 2:** Define the `Course` model.
  - **File Path**: `src/models.py`
  - **Description**: Add the `Course` class in this file, including fields for `id`, `name`, and `level`, following the conventions established in existing models.

### API Routes
- [ ] **Task 3:** Implement the `POST /courses` endpoint.
  - **File Path**: `src/routes.py`
  - **Description**: Create the route to handle course creation. Ensure appropriate status codes and JSON responses are returned based on success or failure (400 for bad input).

- [ ] **Task 4:** Implement the `GET /courses/{id}` endpoint.
  - **File Path**: `src/routes.py`
  - **Description**: Create the route to retrieve a course by ID, returning the correct course details or a 404 error if not found.

### Service Logic
- [ ] **Task 5:** Implement business logic for creating a course.
  - **File Path**: `src/services.py`
  - **Description**: Write a function that handles the creation of a course, checks for required fields (`name` and `level`), and interacts with the database.

- [ ] **Task 6:** Implement business logic for retrieving a course.
  - **File Path**: `src/services.py`
  - **Description**: Write a function that queries the database for a course by ID and returns the result or handles errors.

### Data Validation
- [ ] **Task 7:** Add Marshmallow schema for course validation.
  - **File Path**: `src/schemas.py`
  - **Description**: Define a new schema for Course that enforces the required fields using Marshmallow.

### Testing
- [ ] **Task 8:** Write unit tests for course creation logic.
  - **File Path**: `tests/test_services.py`
  - **Description**: Create unit tests to verify the business logic for course creation, ensuring proper handling of names, levels, and errors.

- [ ] **Task 9:** Write unit tests for course retrieval logic.
  - **File Path**: `tests/test_services.py`
  - **Description**: Create unit tests to verify the business logic for course retrieval, ensuring it returns valid courses and correctly handles missing courses.

- [ ] **Task 10:** Write integration tests for `POST /courses` endpoint.
  - **File Path**: `tests/test_routes.py`
  - **Description**: Create integration tests to verify that the API endpoint handles course creation requests correctly, including success and failure cases.

- [ ] **Task 11:** Write integration tests for `GET /courses/{id}` endpoint.
  - **File Path**: `tests/test_routes.py`
  - **Description**: Create integration tests for the course retrieval endpoint to ensure it returns the expected results.

### Documentation
- [ ] **Task 12:** Update `README.md` to include new API documentation.
  - **File Path**: `README.md`
  - **Description**: Document the new `/courses` API endpoints, including request formats, expected responses, and usage examples.

### Integration and Finalization
- [ ] **Task 13:** Ensure backward compatibility.
  - **File Path**: `src/models.py`, `src/routes.py`, `src/services.py`
  - **Description**: Verify that existing functionalities related to `Student` are not impacted by the new features. 

---
Each task is designed to be independent and small enough for focused execution and testing. The order respects the dependencies between database setup, model definitions, service logic, and route implementations, maintaining an organized approach to development.