Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Teacher Management System

A simple application for managing teachers, students, and courses.

## Overview

The Teacher Management System allows users to create and manage entities such as teachers, students, and courses. This application is built using FastAPI and SQLAlchemy, providing a RESTful API for easy interaction.

### Main Functions

- **Create Teacher**: Add a new teacher with a name and email.
- **Create Student**: Add a new student with a name and email.
- **Create Course**: Add a new course with a name and level.
- **Enroll Student in Course**: Enroll a student in a specific course.
- **Retrieve Lists**: Get lists of teachers, students, and courses.

## Quick Install

To set up the environment and install dependencies, follow these steps:

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
   pip install -r requirements.txt
   ```

   Ensure you have the following dependencies in your `requirements.txt`:
   ```
   fastapi
   sqlalchemy
   alembic
   pydantic
   uvicorn
   ```

4. **Run Database Migrations**:
   Ensure you have Alembic set up correctly, then run:
   ```bash
   alembic upgrade head
   ```

5. **Start the Application**:
   ```bash
   uvicorn main:app --reload
   ```

   The application will be running at `http://127.0.0.1:8000`.

## How to Use the Application

### API Endpoints

The application exposes several endpoints for interacting with the system:

1. **Create a Teacher**:
   - **Endpoint**: `POST /teachers/`
   - **Request Body**:
     ```json
     {
       "name": "John Doe",
       "email": "john.doe@example.com"
     }
     ```

2. **Retrieve Teachers**:
   - **Endpoint**: `GET /teachers/`
   - **Response**: Returns a list of teachers.

3. **Create a Student**:
   - **Endpoint**: `POST /students/`
   - **Request Body**:
     ```json
     {
       "name": "Jane Smith",
       "email": "jane.smith@example.com"
     }
     ```

4. **Retrieve Students**:
   - **Endpoint**: `GET /students/`
   - **Response**: Returns a list of students.

5. **Create a Course**:
   - **Endpoint**: `POST /courses/`
   - **Request Body**:
     ```json
     {
       "name": "Mathematics",
       "level": "Beginner"
     }
     ```

6. **Retrieve Courses**:
   - **Endpoint**: `GET /courses/`
   - **Response**: Returns a list of courses.

7. **Enroll a Student in a Course**:
   - **Endpoint**: `POST /students/{student_id}/courses/{course_id}`
   - **Path Parameters**: `student_id` and `course_id` must be provided.

### Example Usage with cURL

- **Create a Teacher**:
   ```bash
   curl -X POST "http://127.0.0.1:8000/teachers/" -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john.doe@example.com"}'
   ```

- **Get All Teachers**:
   ```bash
   curl -X GET "http://127.0.0.1:8000/teachers/"
   ```

## Conclusion

This Teacher Management System provides a straightforward way to manage teachers, students, and courses through a RESTful API. For further customization and enhancements, feel free to explore the codebase and contribute!

For any issues or feature requests, please open an issue in the repository.
```

This manual provides a comprehensive overview of the application, installation instructions, and usage examples, ensuring that users can easily understand and utilize the software.