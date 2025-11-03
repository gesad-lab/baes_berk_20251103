```markdown
# Teacher Management System

A simple application for managing teachers, students, and courses using FastAPI and SQLAlchemy.

## Main Functions

This application provides the following functionalities:

- **Create and Manage Teachers**: Add new teachers with their names and email addresses.
- **Create and Manage Students**: Add new students with their names, email addresses, and enroll them in courses.
- **Create and Manage Courses**: Add new courses with their names and levels.
- **Retrieve Lists**: Get lists of teachers, students, and courses.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/teacher-management-system.git
   cd teacher-management-system
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install fastapi[all] sqlalchemy pydantic alembic
   ```

4. **Run Database Migrations**:
   Ensure that the database is set up correctly by running the migrations:
   ```bash
   alembic upgrade head
   ```

5. **Start the Application**:
   ```bash
   uvicorn main:app --reload
   ```

## How to Use the Application

### Creating a Teacher

To create a new teacher, send a POST request to `/teachers/` with the following JSON body:

```json
{
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

### Retrieving Teachers

To retrieve a list of teachers, send a GET request to `/teachers/`. You can also use query parameters `skip` and `limit` to paginate the results:

```
GET /teachers/?skip=0&limit=10
```

### Creating a Student

To create a new student, send a POST request to `/students/` with the following JSON body:

```json
{
  "name": "Jane Smith",
  "email": "jane.smith@example.com",
  "course_ids": [1, 2]  // Optional: List of course IDs for enrollment
}
```

### Retrieving Students

To retrieve a list of students, send a GET request to `/students/`. You can also use query parameters `skip` and `limit` to paginate the results:

```
GET /students/?skip=0&limit=10
```

### Creating a Course

To create a new course, send a POST request to `/courses/` with the following JSON body:

```json
{
  "name": "Mathematics",
  "level": "Beginner"
}
```

### Retrieving Courses

To retrieve a list of courses, send a GET request to `/courses/`. You can also use query parameters `skip` and `limit` to paginate the results:

```
GET /courses/?skip=0&limit=10
```

## Conclusion

This Teacher Management System is designed to streamline the management of teachers, students, and courses. By following the installation and usage instructions provided, you can easily set up and interact with the application. For further assistance or feature requests, please reach out to our support team.
```