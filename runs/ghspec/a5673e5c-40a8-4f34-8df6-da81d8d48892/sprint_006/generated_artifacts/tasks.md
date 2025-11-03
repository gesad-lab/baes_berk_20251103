# Tasks: Add Teacher Relationship to Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `src/models.py` (for Course and Teacher models)
- `src/schemas.py` (for Pydantic schemas)
- `src/api/courses.py` (for API endpoints)

## Task Breakdown

### Task 1: Update Course Model

- **File**: `src/models.py`
- **Description**: Modify the existing `Course` class to include a new field `teacher_id` as a Foreign Key to the `Teacher` entity.
- **Checklist**:
  - [ ] Add the `teacher_id` column to the `Course` model.
  - [ ] Establish a relationship to the `Teacher` model.
  
```python 
# Existing code for model modifications
class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, index=True)
    # Existing fields...
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=False)
    teacher = relationship("Teacher", back_populates="courses")
```

### Task 2: Create Course-Teacher Association Schema

- **File**: `src/schemas.py`
- **Description**: Add a Pydantic schema `CourseTeacherAssign` to validate the teacher association payload.
- **Checklist**:
  - [ ] Create `CourseTeacherAssign` schema.
  
```python
class CourseTeacherAssign(BaseModel):
    teacher_id: int
```

### Task 3: Create Course Details Response Schema

- **File**: `src/schemas.py`
- **Description**: Create a Pydantic schema `CourseResponse` that includes fields for Course and associated Teacher information.
- **Checklist**:
  - [ ] Create `CourseResponse` schema.
  
```python
class CourseResponse(BaseModel):
    id: int
    name: str
    teacher_id: int
    teacher_name: str
    teacher_email: str
```

### Task 4: Implement Course-Teacher Association Endpoint

- **File**: `src/api/courses.py`
- **Description**: Create a POST endpoint `/courses/{course_id}/teachers` to associate a Teacher with an existing Course.
- **Checklist**:
  - [ ] Implement POST logic to handle teacher association.
  - [ ] Validate input using `CourseTeacherAssign` schema.
  - [ ] Return updated Course details.
  
### Task 5: Implement Retrieve Course Details Endpoint

- **File**: `src/api/courses.py`
- **Description**: Create a GET endpoint `/courses/{course_id}` to retrieve a Course's details with associated Teacher information.
- **Checklist**:
  - [ ] Implement GET logic to retrieve Course details.
  - [ ] Include Teacher information in the response.
  
### Task 6: Implement Update Course Teacher Endpoint

- **File**: `src/api/courses.py`
- **Description**: Create a PUT endpoint `/courses/{course_id}/teachers` to update a Teacher associated with a Course.
- **Checklist**:
  - [ ] Implement PUT logic to update Teacher association for the Course.
  - [ ] Validate input using `CourseTeacherAssign` schema.
  - [ ] Return updated Course details.

### Task 7: Create Database Migration Script

- **File**: `migrations/versions/xxxx_add_teacher_id_to_courses.py`
- **Description**: Create an Alembic migration script to add the `teacher_id` column to the existing Courses table with foreign key constraints.
- **Checklist**:
  - [ ] Write migration script to add `teacher_id`.
  - [ ] Ensure Foreign Key relationship with the Teachers table.

### Task 8: Write Unit Tests for Course-Teacher Functionality

- **File**: `tests/test_courses.py`
- **Description**: Write unit tests for new functionalities regarding Teacher associations with Courses.
- **Checklist**:
  - [ ] Test associating a Teacher with a Course.
  - [ ] Test retrieving Course details that include Teacher information.
  - [ ] Test updating Teacher association for a Course.

### Task 9: Update README.md for New Features

- **File**: `README.md`
- **Description**: Update the documentation to include setup instructions and new API usage for associating Teachers with Courses.
- **Checklist**:
  - [ ] Add instructions for new endpoints related to Course-Teacher associations.
  
This task breakdown ensures a clear and actionable plan for integrating the Teacher relationship into the Course entity while maintaining adherence to existing standards and practices. Each task is manageable, focused on a single file, and independently testable.