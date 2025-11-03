# Tasks: Create Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `tests/test_routes.py` (2263 bytes)

---

## Task Breakdown

- [ ] **Task 1: Update Database Models**
  - **File**: `src/models.py`
  - **Description**: Create a new `Course` model that includes `id`, `name`, and `level` fields.
  
- [ ] **Task 2: Create Course Marshmallow Schema**
  - **File**: `src/schemas.py`
  - **Description**: Add a Marshmallow schema for the `Course` entity with validations for the `name` and `level` fields to ensure they are required.
  
- [ ] **Task 3: Define API Routes for Course**
  - **File**: `src/routes.py`
  - **Description**: Implement `POST /courses` endpoint for course creation and `GET /courses` endpoint for course retrieval according to specifications.
  
- [ ] **Task 4: Implement Database Migration**
  - **File**: `src/db.py`
  - **Description**: Write a migration function to create a new `courses` table in the database without affecting the existing `Students` table.
  
- [ ] **Task 5: Write Course Creation Logic**
  - **File**: `src/routes.py`
  - **Description**: Implement the logic within the `POST /courses` route to create a course, ensuring it interacts correctly with the database and returns appropriate responses.
  
- [ ] **Task 6: Write Course Retrieval Logic**
  - **File**: `src/routes.py`
  - **Description**: Write the logic for the `GET /courses` route to fetch and return a list of courses from the database in the correct format.
  
- [ ] **Task 7: Update Testing for Course API**
  - **File**: `tests/test_routes.py`
  - **Description**: Add unit tests to cover course creation and retrieval scenarios, including validation error checks.
  
- [ ] **Task 8: Document API Endpoints in README**
  - **File**: `README.md`
  - **Description**: Update the documentation to include new API endpoints for creating and retrieving courses, along with usage examples.
  
- [ ] **Task 9: Implement Error Handling for Course Creation**
  - **File**: `src/routes.py`
  - **Description**: Ensure that appropriate error responses are returned when `name` or `level` fields are missing during course creation requests.
  
- [ ] **Task 10: Test Database Migration** 
  - **File**: `tests/test_models.py`
  - **Description**: Create tests to verify that the database migration correctly creates the `courses` table and that it can be interacted with as expected.

--- 

This task breakdown details each specific step necessary for implementing the Course entity, ensuring that development is organized and manageable while adhering to the provided specifications.