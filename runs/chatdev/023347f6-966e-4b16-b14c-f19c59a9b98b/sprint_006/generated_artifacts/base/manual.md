# Teacher Management System

A simple API for managing teachers, students, and courses in an educational application.

## Main Functions

This software provides the following main functionalities:

- **Create and manage Teachers**: Add new teachers with their names and emails.
- **Create and manage Students**: Add new students and associate them with courses.
- **Create and manage Courses**: Add new courses and manage their details.
- **Retrieve information**: Fetch lists of teachers, students, and courses.

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

3. **Install the required packages**:
   ```bash
   pip install fastapi sqlalchemy uvicorn
   ```

4. **Set up the database**:
   The application uses SQLite for the database. You can initialize the database by running the migration script:
   ```bash
   python main.py
   ```

## How to Use

### Starting the Application

To start the FastAPI application, run the following command:
```bash
uvicorn routes:student_router --reload
```
This will start the server on `http://127.0.0.1:8000`.

### API Endpoints

#### Teachers

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

- **Get all Teachers**:
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

#### Students

- **Create a Student**:
  - **Endpoint**: `POST /students/`
  - **Request Body**:
    ```json
    {
      "name": "Jane Smith",
      "email": "jane.smith@example.com",
      "course_ids": [1]
    }
    ```
  - **Response**:
    ```json
    {
      "id": 1,
      "name": "Jane Smith",
      "email": "jane.smith@example.com",
      "course_ids": [1]
    }
    ```

- **Get all Students**:
  - **Endpoint**: `GET /students/`
  - **Response**:
    ```json
    [
      {
        "id": 1,
        "name": "Jane Smith",
        "email": "jane.smith@example.com",
        "course_ids": [1]
      }
    ]
    ```

#### Courses

- **Create a Course**:
  - **Endpoint**: `POST /courses/`
  - **Request Body**:
    ```json
    {
      "name": "Mathematics",
      "level": "Beginner"
    }
    ```
  - **Response**:
    ```json
    {
      "id": 1,
      "name": "Mathematics",
      "level": "Beginner"
    }
    ```

- **Get all Courses**:
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

## Conclusion

This Teacher Management System provides a simple yet effective way to manage teachers, students, and courses in an educational environment. With the provided API endpoints, you can easily create, retrieve, and manage the data as needed. For further customization and enhancements, feel free to modify the codebase as per your requirements.