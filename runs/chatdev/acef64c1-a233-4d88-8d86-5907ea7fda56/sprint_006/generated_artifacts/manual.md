Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Course Management System

A comprehensive application for managing courses, students, and teachers.

## Main Functions

The Course Management System provides the following key functionalities:

- **Student Management**: Create, retrieve, and enroll students in courses.
- **Course Management**: Create and manage courses, including associating them with teachers.
- **Teacher Management**: Create and retrieve teacher profiles.
- **Enrollment**: Enroll students in specific courses.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install fastapi sqlalchemy alembic
   ```

4. **Run the database migration**:
   Make sure to run the migration script to set up the database schema.
   ```bash
   alembic upgrade head
   ```

5. **Start the application**:
   ```bash
   uvicorn main:app --reload
   ```

## Usage

### API Endpoints

The application exposes several API endpoints for interacting with students, courses, and teachers.

#### Students

- **Create a Student**:
  - **Endpoint**: `POST /students/`
  - **Request Body**:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```

- **Get All Students**:
  - **Endpoint**: `GET /students/`

#### Courses

- **Create a Course**:
  - **Endpoint**: `POST /courses/`
  - **Request Body**:
    ```json
    {
      "name": "Mathematics 101",
      "level": "Beginner",
      "teacher_id": 1  // Optional, if a teacher is associated
    }
    ```

- **Enroll a Student in a Course**:
  - **Endpoint**: `POST /students/{student_id}/courses/{course_id}`

#### Teachers

- **Create a Teacher**:
  - **Endpoint**: `POST /teachers/`
  - **Request Body**:
    ```json
    {
      "name": "Jane Smith",
      "email": "jane.smith@example.com"
    }
    ```

- **Get All Teachers**:
  - **Endpoint**: `GET /teachers/`

## Database Schema

The application uses SQLite as the database. The following tables are created:

- **students**: Stores student information.
- **courses**: Stores course information and links to teachers.
- **teachers**: Stores teacher information.

## Migration

Database migrations are handled using Alembic. The migration script `migration_script.py` adds the `teachers` table and the `teacher_id` column to the `courses` table while preserving existing data.

## Conclusion

This Course Management System provides a robust framework for managing educational entities. For further assistance or to report issues, please contact the support team.
```

This manual provides a comprehensive overview of the software, including installation instructions, usage details, and API endpoints, ensuring users can effectively utilize the Course Management System.