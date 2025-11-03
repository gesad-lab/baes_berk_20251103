```markdown
# Student Course Management System

A FastAPI application for managing students and their enrolled courses.

## Overview

This application allows users to manage students and courses, enabling students to enroll in multiple courses. The system provides a RESTful API to create, retrieve, and manage students and courses, along with their relationships.

## Main Functions

- **Create Students**: Add new students to the system with their name and email.
- **Retrieve Students**: Get a list of all students with their details.
- **Create Courses**: Add new courses to the system with their name and level.
- **Retrieve Courses**: Get a list of all courses with their details.
- **Enroll Students in Courses**: Allow students to enroll in specific courses.

## Installation

To set up the environment and install the required dependencies, follow these steps:

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
   ```
   fastapi
   uvicorn
   sqlalchemy
   alembic
   pydantic
   ```

   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

To start the FastAPI application, use the following command:
```bash
uvicorn main:app --reload
```

The application will be accessible at `http://127.0.0.1:8000`.

## API Endpoints

### Students

- **Create a Student**
  - **Endpoint**: `POST /students/`
  - **Request Body**:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```

- **Retrieve Students**
  - **Endpoint**: `GET /students/`
  - **Query Parameters**: `skip`, `limit`

### Courses

- **Create a Course**
  - **Endpoint**: `POST /courses/`
  - **Request Body**:
    ```json
    {
      "name": "Mathematics",
      "level": "Beginner"
    }
    ```

- **Retrieve Courses**
  - **Endpoint**: `GET /courses/`
  - **Query Parameters**: `skip`, `limit`

### Enrollment

- **Enroll a Student in a Course**
  - **Endpoint**: `POST /students/{student_id}/courses/{course_id}`
  - **Path Parameters**: `student_id`, `course_id`

## Database Migration

To manage database migrations, ensure you have Alembic installed. You can create and apply migrations using the following commands:

1. **Create a Migration**:
   ```bash
   alembic revision --autogenerate -m "Add course relationship to Student entity"
   ```

2. **Apply Migrations**:
   ```bash
   alembic upgrade head
   ```

## Conclusion

This application provides a simple yet effective way to manage students and their course enrollments. For further customization and enhancements, feel free to modify the code as per your requirements.

For any issues or feature requests, please reach out to the development team.
```