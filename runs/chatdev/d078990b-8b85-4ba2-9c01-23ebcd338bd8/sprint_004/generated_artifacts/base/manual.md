```markdown
# Course Management System

A simple web application for managing students and courses using FastAPI and SQLAlchemy.

## Main Functions

This application allows users to perform the following operations:

- **Create a Student**: Add a new student with a name and email.
- **Retrieve Students**: Get a list of all students in the database.
- **Create a Course**: Add a new course with a name and level.
- **Retrieve Courses**: Get a list of all courses in the database.

## Installation

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/course-management-system.git
   cd course-management-system
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install fastapi[all] sqlalchemy pydantic
   ```

4. **Run the Application**:
   ```bash
   uvicorn main:app --reload
   ```

   The application will be running at `http://127.0.0.1:8000`.

## How to Use the Application

### Creating a Student

To create a new student, send a POST request to `/students/` with the following JSON body:

```json
{
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

### Retrieving Students

To retrieve a list of students, send a GET request to `/students/`. You can also use query parameters `skip` and `limit` to paginate results:

```
GET /students/?skip=0&limit=10
```

### Creating a Course

To create a new course, send a POST request to `/courses/` with the following JSON body:

```json
{
  "name": "Introduction to Programming",
  "level": "Beginner"
}
```

### Retrieving Courses

To retrieve a list of courses, send a GET request to `/courses/`. Similar to students, you can paginate results using `skip` and `limit`:

```
GET /courses/?skip=0&limit=10
```

## Database Schema

The application uses SQLite as the database. The following tables are created:

- **students**: Stores student information (id, name, email).
- **courses**: Stores course information (id, name, level).

## Database Migration

The application is designed to preserve existing student data during database migrations. When the application starts, it checks if the `courses` table exists and creates it if it does not.

## Additional Information

For more detailed documentation, please refer to the FastAPI documentation at [FastAPI Docs](https://fastapi.tiangolo.com/).

For any issues or feature requests, please open an issue in the repository.

Happy coding!
```