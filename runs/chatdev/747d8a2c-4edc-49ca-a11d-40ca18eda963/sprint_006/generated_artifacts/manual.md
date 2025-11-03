Here's a detailed user manual for the software, formatted in Markdown:

```markdown
# Course Management System

A comprehensive application for managing courses, students, and teachers.

## Overview

The Course Management System allows users to create and manage courses, enroll students, and assign teachers to courses. This application is built using Python and FastAPI, providing a robust API for interaction.

## Main Functions

- **Create Students**: Add new students to the system.
- **Create Courses**: Add new courses and assign teachers to them.
- **Create Teachers**: Add new teachers to the system.
- **Enroll Students in Courses**: Enroll students in specific courses.
- **Retrieve Lists**: Fetch lists of students and teachers.

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
   pip install fastapi sqlalchemy alembic
   ```

4. **Set Up the Database**:
   - Ensure you have SQLite installed (it comes pre-installed with Python).
   - Run the following command to create the database and tables:
     ```bash
     python -c "from database import create_database; create_database()"
     ```

5. **Run Migrations**:
   - To apply the latest database migrations, run:
     ```bash
     alembic upgrade head
     ```

## Usage

### Starting the Application

To start the FastAPI application, run the following command:
```bash
uvicorn main:app --reload
```
This will start the server at `http://127.0.0.1:8000`.

### API Endpoints

- **Create a Student**:
  - **Endpoint**: `POST /students/`
  - **Request Body**:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```

- **Create a Course**:
  - **Endpoint**: `POST /courses/`
  - **Request Body**:
    ```json
    {
      "name": "Mathematics",
      "level": "Beginner",
      "teacher_id": 1
    }
    ```

- **Create a Teacher**:
  - **Endpoint**: `POST /teachers/`
  - **Request Body**:
    ```json
    {
      "name": "Jane Smith",
      "email": "jane.smith@example.com"
    }
    ```

- **Enroll a Student in a Course**:
  - **Endpoint**: `POST /students/{student_id}/courses/{course_id}`
  - **Path Parameters**: Replace `{student_id}` and `{course_id}` with actual IDs.

- **Retrieve Students**:
  - **Endpoint**: `GET /students/`

- **Retrieve Teachers**:
  - **Endpoint**: `GET /teachers/`

## GUI Implementation

The application also includes a GUI built using Tkinter. To run the GUI, ensure you have Tkinter installed and run:
```bash
python gui.py
```

## Conclusion

This Course Management System provides a user-friendly interface for managing educational entities. For further assistance, please refer to the API documentation or contact support.
```

This manual provides a comprehensive overview of the software, installation instructions, and usage guidelines, ensuring users can effectively utilize the Course Management System.