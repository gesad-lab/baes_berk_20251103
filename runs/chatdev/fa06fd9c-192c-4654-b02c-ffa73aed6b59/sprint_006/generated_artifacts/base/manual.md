```markdown
# Teacher Management System

A simple API for managing teachers, students, and courses in an educational setting.

## Main Functions

This software provides the following functionalities:

- **Create and Manage Teachers**: Add new teachers with their names and email addresses.
- **Create and Manage Students**: Add new students with their names and email addresses.
- **Create and Manage Courses**: Add new courses with names and levels.
- **Enroll Students in Courses**: Enroll students in various courses.
- **Retrieve Lists**: Get lists of all teachers, students, and courses.

## Installation

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   Make sure you have `pip` installed, then run:
   ```bash
   pip install fastapi sqlalchemy
   ```

4. **Run Database Migration**:
   To create the necessary database tables, run:
   ```bash
   python main.py
   ```

## Usage

### Starting the API

To start the FastAPI server, run:
```bash
uvicorn routes:router --reload
```
This will start the server on `http://127.0.0.1:8000`.

### API Endpoints

- **Create a Teacher**:
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

- **Get All Teachers**:
  - **Endpoint**: `GET /teachers/`
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

- **Create a Student**:
  - **Endpoint**: `POST /students/`
  - **Request Body**:
    ```json
    {
      "name": "Jane Smith",
      "email": "jane.smith@example.com"
    }
    ```

- **Get All Students**:
  - **Endpoint**: `GET /students/`
  - **Response**:
    ```json
    [
      {
        "id": 1,
        "name": "Jane Smith",
        "email": "jane.smith@example.com"
      }
    ]
    ```

- **Create a Course**:
  - **Endpoint**: `POST /courses/`
  - **Request Body**:
    ```json
    {
      "name": "Mathematics",
      "level": "Beginner"
    }
    ```

- **Get All Courses**:
  - **Endpoint**: `GET /courses/`
  - **Response**:
    ```json
    [
      {
        "id": 1,
        "name": "Mathematics",
        "level": "Beginner"
      }
    ]
    ```

- **Enroll a Student in a Course**:
  - **Endpoint**: `POST /students/{student_id}/courses/{course_id}/`
  - **Response**:
    ```json
    {
      "message": "Student enrolled in course successfully"
    }
    ```

## Conclusion

This Teacher Management System is designed to be simple and efficient for managing educational entities. For further details and advanced usage, please refer to the API documentation or contact support.
```