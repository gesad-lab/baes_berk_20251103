Here's the user manual for the software, formatted in Markdown as requested:

```markdown
# Course Management System

A simple application for managing students and courses.

## Overview

The Course Management System allows users to create and manage student and course entities. Users can add new students, create courses, and retrieve lists of students and courses. This application is built using FastAPI and SQLAlchemy, providing a robust and efficient backend for managing data.

## Main Functions

- **Create Student**: Add a new student with a name and email.
- **Create Course**: Add a new course with a name and level.
- **Retrieve Students**: Get a list of all students in the system.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repo/course-management-system.git
   cd course-management-system
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install fastapi[all] sqlalchemy alembic
   ```

4. **Create the database**:
   Run the following command to create the initial database and tables:
   ```bash
   python -c "from database import create_database; create_database()"
   ```

5. **Run migrations**:
   To apply any database migrations, run:
   ```bash
   alembic upgrade head
   ```

6. **Start the application**:
   You can start the FastAPI application using:
   ```bash
   uvicorn main:app --reload
   ```

## How to Use the Application

### Creating a Student

To create a new student, send a POST request to `/students/` with the following JSON body:

```json
{
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

### Creating a Course

To create a new course, send a POST request to `/courses/` with the following JSON body:

```json
{
  "name": "Introduction to Programming",
  "level": "Beginner"
}
```

### Retrieving Students

To retrieve a list of students, send a GET request to `/students/`. You can also use query parameters `skip` and `limit` to paginate the results:

```
GET /students/?skip=0&limit=10
```

## Additional Information

- **Database**: The application uses SQLite for data storage. The database file is located at `./students.db`.
- **API Documentation**: You can access the automatically generated API documentation at `http://127.0.0.1:8000/docs` after starting the application.

## Conclusion

This Course Management System provides a simple yet effective way to manage students and courses. Feel free to explore the code and modify it to suit your needs. For any issues or feature requests, please open an issue in the repository.

```

This manual provides a comprehensive overview of the software, installation instructions, and usage guidelines, ensuring that users can effectively utilize the Course Management System.