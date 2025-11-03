Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Teacher Management System

A simple API for managing teachers, students, and courses in an educational setting.

## Overview

This application allows you to create, retrieve, and manage entities related to teachers, students, and courses. The main features include:

- **Create and manage Teachers**: Add new teachers with their names and email addresses.
- **Manage Students**: Create and retrieve student records.
- **Manage Courses**: Create and retrieve courses linked to students.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repo/teacher-management-system.git
   cd teacher-management-system
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install fastapi[all] sqlalchemy
   ```

4. **Run the database migration** to create the necessary tables:
   ```bash
   python main.py
   ```

## API Endpoints

### Teachers

- **Create a Teacher**
  - **Endpoint**: `POST /teachers/`
  - **Request Body**:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```
  - **Response**:
    ```json
    {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```

- **Get All Teachers**
  - **Endpoint**: `GET /teachers/`
  - **Query Parameters**: `skip` (int), `limit` (int)
  - **Response**:
    ```json
    [
      {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com"
      }
    ]
    ```

### Students

- **Create a Student**
  - **Endpoint**: `POST /students/`
  - **Request Body**:
    ```json
    {
      "name": "Jane Smith",
      "email": "jane.smith@example.com"
    }
    ```
  - **Response**:
    ```json
    {
      "id": 1,
      "name": "Jane Smith",
      "email": "jane.smith@example.com",
      "courses": []
    }
    ```

- **Get All Students**
  - **Endpoint**: `GET /students/`
  - **Query Parameters**: `skip` (int), `limit` (int)
  - **Response**:
    ```json
    [
      {
        "id": 1,
        "name": "Jane Smith",
        "email": "jane.smith@example.com",
        "courses": []
      }
    ]
    ```

### Courses

- **Create a Course**
  - **Endpoint**: `POST /courses/`
  - **Request Body**:
    ```json
    {
      "name": "Mathematics",
      "level": "Beginner",
      "student_id": 1
    }
    ```
  - **Response**:
    ```json
    {
      "id": 1,
      "name": "Mathematics",
      "level": "Beginner",
      "student_id": 1
    }
    ```

- **Get All Courses**
  - **Endpoint**: `GET /courses/`
  - **Query Parameters**: `skip` (int), `limit` (int)
  - **Response**:
    ```json
    [
      {
        "id": 1,
        "name": "Mathematics",
        "level": "Beginner",
        "student_id": 1
      }
    ]
    ```

## Running the Application

To run the application, use the following command:

```bash
uvicorn routes:student_router --reload
```

This will start the FastAPI server, and you can access the API at `http://127.0.0.1:8000`.

## Conclusion

This Teacher Management System provides a simple yet effective way to manage educational entities. For further customization or feature requests, please reach out to the development team.

For more detailed documentation, please refer to the code comments and structure.
```

This manual provides a comprehensive overview of the software, installation instructions, and usage details for the API endpoints. Let me know if you need any further modifications or additional information!