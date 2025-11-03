```markdown
# Student Course Management System

A FastAPI application for managing students and their enrolled courses, allowing for easy tracking and organization of educational data.

## Main Functions

- **Student Management**: Create, read, and manage student records including their names and emails.
- **Course Management**: Create, read, and manage course records including course names and levels.
- **Enrollment**: Enroll students in courses and retrieve a list of courses a student is enrolled in.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repo/student-course-management.git
   cd student-course-management
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install fastapi[all] sqlalchemy alembic pydantic
   ```

4. **Run the application**:
   ```bash
   uvicorn main:app --reload
   ```

## 🤔 What is this?

This application is designed to help educational institutions manage student and course data efficiently. It allows for the creation of students and courses, as well as the ability to enroll students in various courses. The application uses a SQLite database to store data persistently.

## 📖 Usage

### 1. Creating a Student

To create a new student, send a POST request to `/students/` with the following JSON body:

```json
{
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

### 2. Retrieving Students

To retrieve a list of students, send a GET request to `/students/`. You can also use query parameters `skip` and `limit` to paginate results.

### 3. Creating a Course

To create a new course, send a POST request to `/courses/` with the following JSON body:

```json
{
  "name": "Mathematics 101",
  "level": "Beginner"
}
```

### 4. Retrieving Courses

To retrieve a list of courses, send a GET request to `/courses/`. You can also use query parameters `skip` and `limit` to paginate results.

### 5. Enrolling a Student in a Course

To enroll a student in a course, send a POST request to `/students/{student_id}/courses/{course_id}`. Replace `{student_id}` and `{course_id}` with the respective IDs.

### 6. Retrieving a Student's Courses

To get a list of courses a student is enrolled in, send a GET request to `/students/{student_id}/courses`.

## Database Migration

The application includes a migration script (`migration.py`) that updates the database schema to add the necessary tables and relationships. To run the migration, use Alembic commands:

1. **Run the migration**:
   ```bash
   alembic upgrade head
   ```

2. **Downgrade if necessary**:
   ```bash
   alembic downgrade -1
   ```

## 📄 Documentation

For more detailed documentation on the FastAPI framework, please visit the [FastAPI Documentation](https://fastapi.tiangolo.com/).

For additional resources and examples, refer to the [SQLAlchemy Documentation](https://docs.sqlalchemy.org/) and [Pydantic Documentation](https://pydantic-docs.helpmanual.io/).

## Support

If you encounter any issues or have questions, please reach out via the support channel or open an issue in the repository.
```
