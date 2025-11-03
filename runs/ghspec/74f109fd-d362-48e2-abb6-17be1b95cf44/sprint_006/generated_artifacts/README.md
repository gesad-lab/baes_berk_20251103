# README.md

# Project Title

A brief description of what this project entails.

## Course

### Updated Attributes:
- **`id`**: Primary key, auto-increment integer.
- **`name`**: String representing the course name (required).
- **`description`**: String providing details about the course (optional).
- **`teacher_id`**: Foreign key referencing the Teacher entity (optional).

### Course Model Changes
The `Course` model has been updated to include a new attribute, `teacher_id`, which establishes a relationship with the `Teacher` model. This allows for the assignment of a teacher to a course.

### Database Migration
To accommodate the changes in the `Course` model, a new database migration script has been implemented. This script adds the `teacher_id` column to the `courses` table:
```sql
ALTER TABLE courses ADD COLUMN teacher_id INTEGER REFERENCES teachers(id);
```

### API Endpoints
New Flask routes have been added to handle teacher assignments to courses and retrieval of course details:
- **Assign Teacher**: `POST /api/v1/courses/<int:course_id>/assign_teacher`
- **Get Course Details**: `GET /api/v1/courses/<int:course_id>`

These endpoints allow for better management of course assignments and retrieval of associated teacher data.

### Course Repository Updates
The `CourseRepository` has been modified to include methods for assigning and retrieving teachers related to a course:
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

### Course Service Logic
The business logic for course operations has been updated to encompass new methods for assigning a teacher and retrieving courses with their respective teachers:
```python
from repositories.course_repository import CourseRepository

class CourseService:
    """Encapsulates business logic for Course operations."""

    def __init__(self):
        self.course_repo = CourseRepository()
```

## Setup Instructions
1. Ensure you have Python installed.
2. Clone the repository.
3. Install dependencies using `pip install -r requirements.txt`.
4. Run the migration with the command: `python -m src.db.migrations`.
5. Start the application.

## Contributing
- Please submit a pull request or report issues if you'd like to contribute.

## License
Specify the license under which the project is distributed.