# README.md

# Project Title

Brief description of your project, its purpose, and functionality.

## Table of Contents

- [Setup Environment](#setup-environment)
- [Model Updates](#model-updates)
- [Database Migration](#database-migration)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)

## Setup Environment

Ensure the `.env` file is updated with any necessary configuration settings. The application requires specific configurations for database connections and other environment variables.

## Model Updates

We have added a new `StudentCourse` model in `models.py` to handle the relationship between students and courses:

```python
class StudentCourse(db.Model):
    __tablename__ = 'student_courses'
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), primary_key=True)
```

## Database Migration

To reflect the new model in the database, use Flask-Migrate to create a migration script for adding the `student_courses` join table:

```bash
flask db migrate -m "Add student_courses join table"
flask db upgrade
```

## API Endpoints

We have implemented new API endpoints to manage student enrollments in courses:

- **Enroll a student in a course**: `POST /students/{id}/courses`
- **Get all courses for a student**: `GET /students/{id}/courses`

Sample implementation in `routes.py`:

```python
@app.route('/students/<int:id>/courses', methods=['POST'])
def enroll_student_in_course(id):
    # Logic to enroll a student in a course
    ...

@app.route('/students/<int:id>/courses', methods=['GET'])
def get_student_courses(id):
    # Logic to retrieve all courses for a student
    ...
```

## Testing

To ensure reliability, new integration tests for course enrollment and retrieval have been added in the `tests` folder. Aim for a minimum of 70% coverage on the new business logic related to course enrollment functionality.

---

### Contributions

Feel free to contribute to this project. Follow the guidelines outlined for code contributions and testing.