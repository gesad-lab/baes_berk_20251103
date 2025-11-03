Here's a detailed user manual for the software, following the structure you provided:

```markdown
# Student Course Management System

A simple application for managing students and their associated courses.

## Quick Install

To set up the environment and install the necessary dependencies, run the following command:

```bash
pip install fastapi sqlalchemy pydantic
```

You may also need to install an ASGI server like `uvicorn` to run the application:

```bash
pip install uvicorn
```

## 🤔 What is this?

The Student Course Management System allows users to manage students and their courses effectively. This application provides functionalities to create and retrieve students and courses, as well as establish relationships between them.

### Main Features:

- **Create Students**: Add new students to the system.
- **Retrieve Students**: Fetch a list of all students.
- **Create Courses**: Add new courses that can be associated with students.
- **Retrieve Courses**: Fetch a list of all courses.
- **Relationship Management**: Each student can have multiple courses associated with them.

## 📖 How to Use

### Running the Application

To run the application, use the following command:

```bash
uvicorn main:app --reload
```

This will start the FastAPI application, and you can access the API documentation at `http://127.0.0.1:8000/docs`.

### API Endpoints

#### 1. Students

- **Create a Student**

  **Endpoint**: `POST /students/`

  **Request Body**:
  ```json
  {
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
  ```

  **Response**:
  ```json
  {
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com",
    "courses": []
  }
  ```

- **Get All Students**

  **Endpoint**: `GET /students/`

  **Response**:
  ```json
  [
    {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com",
      "courses": []
    }
  ]
  ```

#### 2. Courses

- **Create a Course**

  **Endpoint**: `POST /courses/`

  **Request Body**:
  ```json
  {
    "name": "Mathematics",
    "level": "Beginner",
    "student_id": 1
  }
  ```

  **Response**:
  ```json
  {
    "id": 1,
    "name": "Mathematics",
    "level": "Beginner",
    "student_id": 1
  }
  ```

- **Get All Courses**

  **Endpoint**: `GET /courses/`

  **Response**:
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

### Database Migration

The application includes a migration script that creates the necessary database tables while preserving existing data. To run the migration, execute the following command:

```bash
python main.py
```

This will check if the `courses` table exists and create it if it does not, ensuring that existing student data remains intact.

## Conclusion

The Student Course Management System is a straightforward application designed to help you manage students and their courses efficiently. For further customization or enhancements, feel free to modify the code as per your requirements.

For any issues or support, please reach out to the development team.
```

This manual provides a comprehensive guide for users to understand the software's functionality, installation process, and usage instructions.