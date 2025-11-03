```markdown
# ChatDev Course Management System

A comprehensive API for managing courses, students, and teachers in an educational environment.

## Overview

The ChatDev Course Management System allows users to create and manage courses, students, and teachers. This system supports relationships between courses and teachers, enabling a structured approach to educational management.

### Main Functions

- **Create and manage students**: Add new students with their details and associate them with courses.
- **Create and manage courses**: Add new courses, specify their levels, and assign teachers.
- **Create and manage teachers**: Add new teachers with their details and link them to courses.
- **Retrieve information**: Fetch lists of students, courses, and teachers.

## Installation

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
   Create a `requirements.txt` file with the following content:
   ```plaintext
   fastapi
   uvicorn
   sqlalchemy
   pydantic
   alembic
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Application

To start the FastAPI application, run the following command:
```bash
uvicorn main:app --reload
```
This will start the server at `http://127.0.0.1:8000`.

### API Endpoints

The following endpoints are available for interacting with the system:

- **Students**
  - `POST /students/`: Create a new student.
  - `GET /students/`: Retrieve a list of all students.

- **Courses**
  - `POST /courses/`: Create a new course (assign a teacher using `teacher_id`).
  - `GET /courses/`: Retrieve a list of all courses.

- **Teachers**
  - `POST /teachers/`: Create a new teacher.
  - `GET /teachers/`: Retrieve a list of all teachers.

### Example Requests

1. **Creating a Student**:
   ```json
   POST /students/
   {
       "name": "John Doe",
       "email": "john.doe@example.com"
   }
   ```

2. **Creating a Course**:
   ```json
   POST /courses/
   {
       "name": "Mathematics 101",
       "level": "Beginner",
       "teacher_id": 1
   }
   ```

3. **Creating a Teacher**:
   ```json
   POST /teachers/
   {
       "name": "Jane Smith",
       "email": "jane.smith@example.com"
   }
   ```

### Database Migration

The system uses Alembic for database migrations. To apply migrations, run:
```bash
alembic upgrade head
```
This will ensure that the database schema is up to date while preserving existing data.

## Conclusion

The ChatDev Course Management System provides a robust framework for managing educational entities. By following the installation and usage instructions, users can effectively utilize the API to manage students, courses, and teachers.
```
