# Tasks: Add Course Relationship to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `tests/test_api.py` (2035 bytes)

---

## Task Breakdown

### 1. Database Schema Update
- [ ] **Create a Migration Script for `student_courses`**  
  **File:** `migrations/versions/001_create_student_courses.py`  
  - Create a join table `student_courses` with `student_id` and `course_id` foreign keys.
  
### 2. API Development
- [ ] **Implement PATCH Endpoint for Course Association**  
  **File:** `src/api.py`  
  - Define a function that handles `PATCH /students/{id}/courses` to associate courses with students.
  
- [ ] **Implement GET Endpoint for Fetching Courses**  
  **File:** `src/api.py`  
  - Define a function that handles `GET /students/{id}/courses` to retrieve associated courses for a student.

### 3. Error Handling
- [ ] **Implement Error Handling for Invalid Courses**  
  **File:** `src/errors.py`  
  - Create a centralized error handling function specifically for non-existent course associations.

### 4. Database Model Definition
- [ ] **Define the `StudentCourses` Model**  
  **File:** `src/models.py`  
  - Add a new data model class `StudentCourses` that represents the join table structure.

### 5. Update Existing Models
- [ ] **Update the Student Model**  
  **File:** `src/models.py`  
  - Add a relationship to the `Student` model for `courses`.
  
- [ ] **Update the Course Model**  
  **File:** `src/models.py`  
  - Add a relationship to the `Course` model for `students`.

### 6. Testing
- [ ] **Write Tests for Course Association Endpoint**  
  **File:** `tests/test_api.py`  
  - Create tests for the `PATCH /students/{id}/courses` ensuring valid course associations succeed and invalid ones fail.

- [ ] **Write Tests for Fetch Associated Courses Endpoint**  
  **File:** `tests/test_api.py`  
  - Create tests for the `GET /students/{id}/courses` ensuring correct data is returned.

### 7. Frontend Development 
- [ ] **Update Admin Forms for Course Association**  
  **File:** `src/templates/student_association.html`  
  - Modify the HTML forms to allow administrators to select and associate courses with students.

### 8. Documentation
- [ ] **Update API Documentation**  
  **File:** `README.md`  
  - Document the new endpoints and their request/response structures for course association and retrieval.

- [ ] **Add Docstrings to New Functions**  
  **Files:** `src/api.py`, `src/models.py`, `src/errors.py`  
  - Ensure all new methods have clear docstrings explaining their purpose, parameters, and return values.

---

This structured breakdown of tasks allows each file to be focused on specific pieces of functionality, ensuring that they can be implemented and tested independently while maintaining overall project integrity.