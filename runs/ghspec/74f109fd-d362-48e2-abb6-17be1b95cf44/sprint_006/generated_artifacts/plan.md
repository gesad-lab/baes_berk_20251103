# Implementation Plan: Add Teacher Relationship to Course Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Teacher Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Course Relationship to Student Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Course Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Email Field to Student Entity

## Version: 1.1.0

## Overview
This implementation plan outlines the addition of a teacher relationship to the existing Course entity in the educational management system. This feature will establish a one-to-one relationship where each Course may be associated with one Teacher, thereby enabling enhanced course management reporting.

## Technology Stack
- **Backend Framework**: Flask (Python)
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **API Format**: JSON
- **Testing Framework**: pytest
- **Request Validation**: marshmallow

## Architecture Overview
The application will be updated to include the relationship from Course to Teacher with the following structure:

### Module Structure
- **src/**
  - **models/**: Contains the database models (e.g., Course, Teacher).
    - Update the existing `Course` model to add the `teacher_id` foreign key attribute.
  - **repositories/**: Handles all database interactions.
    - Update the `CourseRepository` to include methods for assigning and retrieving teachers related to a course.
  - **services/**: Contains business logic including course assignment logic.
    - Update the course service to manage teacher assignments and retrieval.
  - **api/**: Manages API routes and requests.
    - Add API routes to assign a teacher to a course and to retrieve courses with teacher information.
  - **db/**: Manages database initialization and migrations.
    - Create a migration script to add the `teacher_id` column in the Course table.
  - **config/**: Holds configuration settings.
  - **app.py**: Main application entry point.

- **tests/**: Contains unit and integration tests organized by feature.
  - Add tests for assigning teachers to courses and retrieving courses with teacher details.

## Data Model
### Updated Course Model
```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Course(Base):
    """Model for the Course entity."""
    
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    description = Column(String, nullable=True)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # New relationship

    # Relationship with Teacher
    teacher = relationship('Teacher', back_populates='courses')

# Update the Teacher model to include courses relationship
class Teacher(Base):
    """Model for the Teacher entity."""
    
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    email = Column(String, nullable=False)

    # New relationship to the Course entity
    courses = relationship('Course', back_populates='teacher')
```

## API Contract
### Endpoints
1. **Assign Teacher to Course**
   - **Method**: POST
   - **Endpoint**: `/api/v1/courses/<int:course_id>/assign_teacher`
   - **Request Payload**:
   ```json
   {
     "teacher_id": 2
   }
   ```

   - **Response (200 OK)**:
   ```json
   {
     "course_id": 1,
     "teacher_id": 2,
     "message": "Teacher has been successfully assigned to the course."
   }
   ```

   - **Response (404 Not Found)**: Course Not Found
   ```json
   {
     "error": {
       "code": "E002",
       "message": "The course does not exist."
     }
   }
   ```

2. **Retrieve Course with Teacher Details**
   - **Method**: GET
   - **Endpoint**: `/api/v1/courses/<int:course_id>`
   - **Response (200 OK)**:
   ```json
   {
     "id": 1,
     "name": "Mathematics 101",
     "description": "An introductory course on mathematics.",
     "teacher": {
       "id": 2,
       "name": "Jane Smith",
       "email": "jane.smith@example.com"
     }
   }
   ```

   - **Response (200 OK)**: No Teacher Assigned
   ```json
   {
     "id": 1,
     "name": "Mathematics 101",
     "description": "An introductory course on mathematics.",
     "teacher": null
   }
   ```

## Implementation Approach
1. **Set Up Project Structure**:
   - Utilize the existing directory layout and integrate the new files and modifications as described below.

2. **Update Course Model**:
   - Modify the existing `Course` model to add the `teacher_id` foreign key attribute and establish a relationship with the `Teacher` model.

3. **Database Schema Update**:
   - Create a database migration script to add the `teacher_id` column in the Course table:
   ```sql
   ALTER TABLE courses ADD COLUMN teacher_id INTEGER REFERENCES teachers(id);
   ```

4. **Implement API Endpoints**:
   - Add Flask routes in `api` to handle teacher assignment to courses and fetching course details:
   - The `/api/v1/courses/<int:course_id>/assign_teacher` route will handle teacher assignment.
   - The `/api/v1/courses/<int:course_id>` route will retrieve course details including teacher information.

5. **Create Course Repository Updates**:
   - Update the `CourseRepository` to include methods for assigning and retrieving teachers related to a course.
   ```python
   from models.course import Course
   from database import session

   class CourseRepository:
       """Handles database interactions for Course entity."""

       def assign_teacher(self, course_id, teacher_id):
           course = session.query(Course).filter_by(id=course_id).first()
           if course:
               course.teacher_id = teacher_id
               session.commit()
           return course
       
       def get_course_with_teacher(self, course_id):
           return session.query(Course).filter_by(id=course_id).first()
   ```

6. **Create Course Service Logic**:
   - Update the existing service logic to include methods for assigning a teacher and retrieving courses:
   ```python
   from repositories.course_repository import CourseRepository

   class CourseService:
       """Encapsulates business logic for Course operations."""

       def __init__(self):
           self.course_repo = CourseRepository()

       def assign_teacher_to_course(self, course_id, teacher_id):
           course = self.course_repo.assign_teacher(course_id, teacher_id)
           if not course:
               raise ValueError("The course does not exist.")
           return course

       def get_course_details(self, course_id):
           course = self.course_repo.get_course_with_teacher(course_id)
           return course
   ```

7. **Implement API Logic**:
   - Add routes in the `api` layer to implement teacher assignment to courses and retrieving course details:
   ```python
   from flask import Blueprint, request, jsonify
   from services.course_service import CourseService

   course_api = Blueprint('course_api', __name__)
   course_service = CourseService()

   @course_api.route('/api/v1/courses/<int:course_id>/assign_teacher', methods=['POST'])
   def assign_teacher(course_id):
       data = request.json
       try:
           course = course_service.assign_teacher_to_course(course_id, data['teacher_id'])
           return jsonify({
               "course_id": course.id,
               "teacher_id": data['teacher_id'],
               "message": "Teacher has been successfully assigned to the course."
           }), 200
       except ValueError as e:
           return jsonify({"error": {"code": "E002", "message": str(e)}}), 404

   @course_api.route('/api/v1/courses/<int:course_id>', methods=['GET'])
   def get_course(course_id):
       try:
           course = course_service.get_course_details(course_id)
           if course.teacher:
               teacher_details = {
                   "id": course.teacher.id,
                   "name": course.teacher.name,
                   "email": course.teacher.email,
               }
           else:
               teacher_details = None
           return jsonify({
               "id": course.id,
               "name": course.name,
               "description": course.description,
               "teacher": teacher_details
           }), 200
       except ValueError as e:
           return jsonify({"error": {"code": "E002", "message": str(e)}}), 404
   ```

8. **Testing**:
   - Write unit tests to validate both the teacher assignment and retrieval functionalities for courses, ensuring tests cover successful operations and error scenarios.
   ```python
   import pytest
   from services.course_service import CourseService

   @pytest.fixture
   def course_service():
       return CourseService()

   def test_assign_teacher_to_course(course_service):
       """Test assigning a teacher to a course."""
       course_service.assign_teacher_to_course(1, 2)  # Assumes course ID 1 exists
       assert course_service.get_course_details(1).teacher_id == 2

   def test_assign_teacher_to_non_existent_course(course_service):
       """Test assigning to a non-existent course raises ValueError."""
       with pytest.raises(ValueError, match="The course does not exist."):
           course_service.assign_teacher_to_course(999, 2)

   def test_get_course_with_teacher(course_service):
       """Test retrieving a course with assigned teacher."""
       course = course_service.get_course_details(1)  # Assumes course ID 1 exists
       assert course.id == 1
       assert course.teacher is not None  # Assumes teacher is assigned
   ```

9. **Documentation**:
   - Update `README.md` to reflect changes in the API structure, including endpoints for assigning and retrieving courses with teacher details.

## Key Considerations
- **Scalability**: Ensure the new relationship design takes future expansions into account, such as additional teacher attributes or more complex assignments.
- **Security**: Implement validation to prevent invalid or harmful user inputs.
- **Maintainability**: Follow the coding standards outlined in the Default Project Constitution for code quality.

## Success Criteria
- 100% success rate for valid teacher assignment requests, confirming teacher assignments are reflected correctly in course details.
- 100% success rate for retrieving courses, confirming the output reflects the correct teacher information or that teachers initialize as null when unassigned.
- Successful application startup without errors, confirming that the new schema and logic works with the existing models.
- All API responses returned in valid JSON format with appropriate HTTP status codes.

## Conclusion
This implementation plan details the necessary steps for integrating a teacher relationship into the existing Course entity. It ensures that future enhancements are supported while maintaining consistency with existing operational standards.

### Existing Code Modifications
Modifications to existing files:
- **Modify `src/models/course.py`** to include the `teacher_id` field and establish the relationship.
  
  ```python
  from sqlalchemy import Column, Integer, String, ForeignKey
  from sqlalchemy.orm import relationship
  from database import Base

  class Course(Base):
      """Model for the Course entity."""
      
      __tablename__ = 'courses'
      
      id = Column(Integer, primary_key=True, autoincrement=True)
      name = Column(String(255), nullable=False)
      description = Column(String, nullable=True)
      teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # New relationship

      # Relationship with Teacher
      teacher = relationship('Teacher', back_populates='courses')
  ```
  
- **Modify `src/models/teacher.py`** to include relationships back to courses.

  ```python
  from sqlalchemy import Column, Integer, String
  from database import Base
  from sqlalchemy.orm import relationship

  class Teacher(Base):
      """Model for the Teacher entity."""
      
      __tablename__ = 'teachers'
      
      id = Column(Integer, primary_key=True, autoincrement=True)
      name = Column(String(255), nullable=False)
      email = Column(String, nullable=False)

      # New relationship to the Course entity
      courses = relationship('Course', back_populates='teacher')
  ```

- **Modify `src/repositories/course_repository.py`** to add methods for assigning teachers to courses and modifying existing logic.

  ```python
  from models.course import Course
  from database import session

  class CourseRepository:
      """Handles database interactions for Course entity."""

      def assign_teacher(self, course_id, teacher_id):
          course = session.query(Course).filter_by(id=course_id).first()
          if course:
              course.teacher_id = teacher_id
              session.commit()
          return course
  ```

- **Modify `src/services/course_service.py`** to include the new assignment logic and adapt existing methods.

  ```python
  from repositories.course_repository import CourseRepository

  class CourseService:
      """Encapsulates business logic for Course operations."""

      def __init__(self):
          self.course_repo = CourseRepository()

      def assign_teacher_to_course(self, course_id, teacher_id):
          course = self.course_repo.assign_teacher(course_id, teacher_id)
          if not course:
              raise ValueError("The course does not exist.")
          return course
  ```

- **Modify `src/api/course_api.py`** to add new API routes for assigning teachers to courses and retrieving course details.

  ```python
  from flask import Blueprint, request, jsonify
  from services.course_service import CourseService

  course_api = Blueprint('course_api', __name__)
  course_service = CourseService()

  @course_api.route('/api/v1/courses/<int:course_id>/assign_teacher', methods=['POST'])
  def assign_teacher(course_id):
      data = request.json
      try:
          course = course_service.assign_teacher_to_course(course_id, data['teacher_id'])
          return jsonify({
              "course_id": course.id,
              "teacher_id": data['teacher_id'],
              "message": "Teacher has been successfully assigned to the course."
          }), 200
      except ValueError as e:
          return jsonify({"error": {"code": "E002", "message": str(e)}}), 404
  ```

- **Update Tests in `tests/test_course.py`** to cover new functionalities related to course-teacher relationships.

```python
import pytest
from services.course_service import CourseService

@pytest.fixture
def course_service():
    return CourseService()

def test_assign_teacher_to_course(course_service):
    """Test assigning a teacher to a course."""
    course_service.assign_teacher_to_course(1, 2)  # Assumes course ID 1 exists
    assert course_service.get_course_details(1).teacher_id == 2

def test_assign_teacher_to_non_existent_course(course_service):
    """Test assigning to a non-existent course raises ValueError."""
    with pytest.raises(ValueError, match="The course does not exist."):
        course_service.assign_teacher_to_course(999, 2)

def test_get_course_with_teacher(course_service):
    """Test retrieving a course with assigned teacher."""
    course = course_service.get_course_details(1)  # Assumes course ID 1 exists
    assert course.id == 1
    assert course.teacher is not None  # Assumes teacher is assigned
```

By carefully integrating changes into existing modules, ensuring no loss of previous functionality while adding valuable new features, we can enhance the educational management system efficiently.