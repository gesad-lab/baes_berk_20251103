Here's a detailed user manual for the ChatDev Student Application, formatted in Markdown:

```markdown
# ChatDev Student Application

The ChatDev Student Application is designed to manage students, courses, and teachers efficiently. This application allows users to create and manage relationships between students and courses, as well as assign teachers to courses.

## Main Functions

- **Manage Students**: Create, read, update, and delete student records.
- **Manage Courses**: Create, read, update, and delete course records.
- **Assign Teachers**: Link teachers to courses, allowing for better organization and management of educational resources.
- **Student-Course Relationship**: Enable students to enroll in multiple courses and manage their course selections.

## Quick Install

To set up the ChatDev Student Application, you need to install the required dependencies. You can do this using pip:

```bash
pip install sqlalchemy pydantic
```

## Environment Setup

1. **Clone the Repository**: Start by cloning the repository to your local machine.

   ```bash
   git clone https://github.com/yourusername/chatdev_student_app.git
   cd chatdev_student_app
   ```

2. **Install Dependencies**: Use pip to install the necessary packages.

   ```bash
   pip install -r requirements.txt
   ```

3. **Database Setup**: The application uses SQLite for database management. The database will be created automatically when you run the application for the first time.

## How to Use the Application

1. **Run the Application**: Start the application by executing the `main.py` file.

   ```bash
   python main.py
   ```

2. **Database Migration**: The application will automatically handle database migrations, including adding the `teacher_id` relationship to the `Course` entity. This ensures that existing data for students, courses, and teachers is preserved.

3. **Interacting with the Application**:
   - You can create new students, courses, and teachers using the defined API endpoints (if applicable).
   - Assign teachers to courses by specifying the `teacher_id` when creating or updating a course.
   - Enroll students in courses by linking them through the many-to-many relationship.

## Example Usage

### Creating a Course with a Teacher

To create a new course and assign a teacher, you can use the following example:

```python
from models import Course, Teacher
from database import get_db

db = next(get_db())
new_teacher = Teacher(name="John Doe", email="john.doe@example.com")
db.add(new_teacher)
db.commit()

new_course = Course(name="Mathematics", level="Beginner", teacher_id=new_teacher.id)
db.add(new_course)
db.commit()
```

### Querying Courses and Their Teachers

You can query courses and their associated teachers as follows:

```python
courses = db.query(Course).all()
for course in courses:
    print(f"Course: {course.name}, Teacher: {course.teacher.name if course.teacher else 'No teacher assigned'}")
```

## Documentation

For more detailed documentation, including API references and advanced usage, please refer to the [ChatDev Documentation](https://yourdocumentationlink.com).

## Support

If you encounter any issues or have questions, please reach out to our support team via the support channel or email us at support@chatdev.com.
```

This manual provides a comprehensive overview of the ChatDev Student Application, including installation instructions, main functions, and usage examples. It also includes links for further documentation and support.