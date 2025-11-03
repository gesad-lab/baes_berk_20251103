# Tasks: Create Teacher Entity

---

**INCREMENTAL DEVELOPMENT CONTEXT**

Existing Code to Build Upon:
- `src/app.py` (2432 bytes)
- `src/models.py` (1350 bytes)
- `src/routes.py` (2775 bytes)
- `src/services.py` (1220 bytes)
- `tests/test_routes.py` (3816 bytes)
- `tests/test_services.py` (3030 bytes)

---

## Task Breakdown

### Database Migration

- [ ] **Create Migration Script for Teacher Table**  
  **File:** `src/db.py`  
  **Task:** Write Alembic migration script to create the `teachers` table with columns for `id`, `name`, and `email`. Ensure the `email` column is unique and nullable. (Include upgrade and downgrade methods.)

### Model Definition

- [ ] **Define Teacher Model**  
  **File:** `src/models.py`  
  **Task:** Create the `Teacher` model class with `id`, `name`, and `email` attributes. Ensure that both `name` and `email` fields are required, and `email` must be unique.

### API Endpoints

- [ ] **Implement Create Teacher Endpoint**  
  **File:** `src/routes.py`  
  **Task:** Define the `POST /api/v1/teachers` endpoint to handle teacher creation. Ensure it processes incoming JSON, validates input, and interacts with the service layer. Return appropriate HTTP response codes based on the result.

- [ ] **Implement Retrieve Teachers Endpoint**  
  **File:** `src/routes.py`  
  **Task:** Define the `GET /api/v1/teachers` endpoint to return a list of teachers with their names and emails in JSON format.

### Business Logic

- [ ] **Implement Teacher Service Logic**  
  **File:** `src/services.py`  
  **Task:** Create service methods to handle teacher creation and retrieval. Include input validation to check for duplicates and required fields. 

### Input Validation

- [ ] **Setup Input Validation Logic**  
  **File:** `src/services.py`  
  **Task:** Implement logic to validate that names and emails are provided when creating a teacher. Check for valid email format and uniqueness of the email.

### Testing

- [ ] **Write Tests for Create Teacher Endpoint**  
  **File:** `tests/test_routes.py`  
  **Task:** Add tests to ensure the `POST /api/v1/teachers` endpoint functions correctly, including valid cases and error cases for invalid inputs.

- [ ] **Write Tests for Retrieve Teachers Endpoint**  
  **File:** `tests/test_routes.py`  
  **Task:** Add tests to ensure the `GET /api/v1/teachers` endpoint correctly retrieves and displays teacher data.

- [ ] **Write Unit Tests for Teacher Service Logic**  
  **File:** `tests/test_services.py`  
  **Task:** Add unit tests to cover the business logic for creating and retrieving teachers, focusing on validation checking.

### Documentation

- [ ] **Update README.md**  
  **File:** `README.md`  
  **Task:** Document the new Teacher entity features, including API endpoints, expected request formats, and example responses.

---

With these tasks outlined, let's ensure clear dependencies are respected and focus on achieving the MVP by prioritizing the creation and retrieval of teacher entities. Each task is scoped to a single file for ease of testing and integration.