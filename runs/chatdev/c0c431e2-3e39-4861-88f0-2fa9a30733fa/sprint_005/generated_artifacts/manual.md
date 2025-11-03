Here's the `manual.md` file that provides a detailed user manual for the software, including an introduction to the main functions, installation instructions, and usage guidelines.

```markdown
# Teacher Management System

A FastAPI application for managing teachers, students, and courses.

## Overview

The Teacher Management System allows users to create and manage entities for teachers, students, and courses. This application provides a RESTful API for performing CRUD operations on these entities, enabling seamless integration into educational platforms.

### Main Functions

- **Create and manage teachers**: Add new teachers with their names and email addresses.
- **Create and manage students**: Add new students with their names and email addresses.
- **Create and manage courses**: Add new courses with their names and levels.
- **Enroll students in courses**: Link students to courses they are enrolled in.
- **Retrieve lists of teachers, students, and courses**: Fetch all entries for each entity.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd student_app
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Application

To run the FastAPI application, execute the following command:

```bash
uvicorn main:app --reload
```

This command starts the server in development mode, allowing for hot-reloading of changes.

### API Endpoints

The application exposes several API endpoints for managing teachers, students, and courses. Below are the key endpoints:

- **Teachers**
  - `POST /teachers/`: Create a new teacher.
    - Request body:
      ```json
      {
        "name": "John Doe",
        "email": "john.doe@example.com"
      }
      ```
  - `GET /teachers/`: Retrieve a list of all teachers.

- **Students**
  - `POST /students/`: Create a new student.
    - Request body:
      ```json
      {
        "name": "Jane Smith",
        "email": "jane.smith@example.com"
      }
      ```
  - `GET /students/`: Retrieve a list of all students.

- **Courses**
  - `POST /courses/`: Create a new course.
    - Request body:
      ```json
      {
        "name": "Mathematics",
        "level": "Beginner"
      }
      ```
  - `GET /courses/`: Retrieve a list of all courses.

- **Enrollments**
  - `POST /students/{student_id}/courses/{course_id}`: Enroll a student in a course.

### Testing the API

You can test the API using tools like Postman or cURL. For example, to create a new teacher using cURL:

```bash
curl -X POST "http://127.0.0.1:8000/teachers/" -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john.doe@example.com"}'
```

## Database

The application uses SQLite as the database backend. The database schema is automatically created when the application starts. The `Teacher`, `Student`, and `Course` tables are defined in the `models.py` file, and migrations are handled in `database.py`.

## Conclusion

This Teacher Management System provides a robust framework for managing educational entities. With its RESTful API, it can be easily integrated into larger applications or used as a standalone service.

For further information and detailed documentation, please refer to the code comments and structure within the repository.
```

This manual provides a comprehensive overview of the application, installation instructions, and usage guidelines, ensuring that users can effectively utilize the Teacher Management System.