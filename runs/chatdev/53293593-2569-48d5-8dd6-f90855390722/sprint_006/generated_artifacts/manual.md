```markdown
# ChatDev Course Management System

Welcome to the ChatDev Course Management System! This software allows you to manage courses, students, and teachers effectively. With the recent updates, you can now associate teachers with courses, enhancing the educational experience.

## Main Functions

- **Manage Courses**: Create, update, and delete courses.
- **Manage Students**: Add, update, and remove students from the system.
- **Manage Teachers**: Add, update, and remove teachers.
- **Course-Teacher Relationship**: Each course can now have an associated teacher.
- **Student-Course Enrollment**: Students can enroll in multiple courses.

## Quick Install

To get started, you need to install the required environment dependencies. You can do this using pip:

```bash
pip install sqlalchemy pydantic
```

If you prefer using conda, you can install the dependencies with:

```bash
conda install sqlalchemy -c conda-forge
```

## Setting Up the Environment

1. **Clone the Repository**: 
   Clone the repository containing the source code to your local machine.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create the Database**: 
   The application uses SQLite as the database. The database will be created automatically when you run the migration script.

3. **Run Migrations**: 
   To set up the database schema, run the migration script:

   ```bash
   python main.py
   ```

   This will create the necessary tables and relationships in the database while preserving existing data.

## How to Use the Application

### Adding a Teacher

1. Create a new teacher by providing their name and email.
2. The teacher will be stored in the database and can be associated with courses.

### Adding a Course

1. Create a new course by providing the course name, level, and the teacher's ID.
2. The course will be linked to the specified teacher.

### Enrolling a Student in a Course

1. Add a student to the system by providing their name and email.
2. Enroll the student in one or more courses.

### Viewing Data

You can query the database to view all courses, students, and teachers, along with their relationships.

## Example Usage

Here’s a quick example of how to create a course and associate it with a teacher:

```python
from sqlalchemy.orm import Session
from models import Course, Teacher

# Assuming you have a session created
def add_course(session: Session, course_name: str, level: str, teacher_id: int):
    new_course = Course(name=course_name, level=level, teacher_id=teacher_id)
    session.add(new_course)
    session.commit()
```

## Documentation

For more detailed documentation, including API references and advanced usage, please refer to the [official documentation](https://your-documentation-url).

## Support

If you encounter any issues or have questions, please reach out to our support team via the provided contact methods.

Thank you for using the ChatDev Course Management System! We hope it enhances your educational management experience.
```