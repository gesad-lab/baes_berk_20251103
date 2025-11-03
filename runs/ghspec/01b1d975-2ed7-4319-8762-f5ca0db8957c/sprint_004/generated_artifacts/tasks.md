# Tasks: Add Course Relationship to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `src/models.py` 
- `src/routes.py` 
- `src/controllers.py` 
- `src/validation.py` 
- Database schema and migration setup

Instructions for Task Breakdown:
1. Identify which existing files need modifications
2. Create new files for new functionality
3. Ensure integration tasks are included
4. Maintain consistency with existing code style and patterns
---

## Task List

### Database Migration
- [ ] **Task**: Create a migration script to add the `enrollments` association table.
  - **File Path**: `migrations/20230401_add_enrollment_table.py`
  
### Model Updates
- [ ] **Task**: Extend the `Student` model to include an `enrolled_courses` relationship.
  - **File Path**: `src/models.py`
  
### API Routes
- [ ] **Task**: Implement route for enrolling a student in a course.
  - **File Path**: `src/routes.py`
  
- [ ] **Task**: Implement route for retrieving a student's enrolled courses.
  - **File Path**: `src/routes.py`

### Controller Logic
- [ ] **Task**: Create function for enrolling a student in a course.
  - **File Path**: `src/controllers.py`
  
- [ ] **Task**: Create function for retrieving a student's enrolled courses.
  - **File Path**: `src/controllers.py`

### Validation Logic
- [ ] **Task**: Implement validation logic for checking course existence before enrollment.
  - **File Path**: `src/validation.py`

### Testing
- [ ] **Task**: Write unit tests for enrolling students in courses.
  - **File Path**: `tests/test_student_courses.py`
  
- [ ] **Task**: Write unit tests for retrieving enrolled courses.
  - **File Path**: `tests/test_student_courses.py`
  
- [ ] **Task**: Write tests for validation error cases when enrolling students in non-existing courses.
  - **File Path**: `tests/test_student_courses.py`

### Environment Setup
- [ ] **Task**: Ensure that the virtual environment is properly set up using Poetry and all dependencies are installed.
  - **File Path**: `README.md` (update with setup instructions)

### Documentation
- [ ] **Task**: Update documentation to reflect the new endpoints and functionality.
  - **File Path**: `README.md` 

### Configuration Management
- [ ] **Task**: Create a `.env.example` file with required environment variables for configuration.
  - **File Path**: `.env.example`

By completing these tasks, we will effectively add a relationship between the `Student` and `Course` entities, enhancing the system's functionality while adhering to the established coding and organizational standards.