```markdown
# Teacher Management System

A simple API for managing teachers, students, and courses in an educational environment.

## Main Functions

This software provides the following main functionalities:

- **Create and Manage Teachers**: Add new teachers with their names and emails.
- **Create and Manage Students**: Add new students with their names and emails, and assign courses to them.
- **Create and Manage Courses**: Add new courses with their names and levels.
- **Data Preservation**: Ensure that existing student and course data is preserved during database migrations.

## Quick Install

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
   ```bash
   pip install fastapi sqlalchemy alembic pydantic
   ```

4. **Run Database Migrations**:
   Ensure that your database is set up correctly and run the following command to create the necessary tables:
   ```bash
   alembic upgrade head
   ```

5. **Run the Application**:
   Start the FastAPI application using Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```

## How to Use the API

### Teacher Management

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

### Student Management

- **Create a Student**:
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

### Course Management

- **Create a Course**:
  - **Endpoint**: `POST /courses/`
  - **Request Body**:
    ```json
    {
      "name": "Mathematics",
      "level": "Intermediate"
    }
    ```
  - **Response**:
    ```json
    {
      "id": 1,
      "name": "Mathematics",
      "level": "Intermediate"
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
        "level": "Intermediate"
      }
    ]
    ```

## Conclusion

This Teacher Management System provides a simple yet effective way to manage teachers, students, and courses in an educational setting. By following the installation and usage instructions, you can quickly set up and start using the API to manage educational data efficiently.

For further documentation and examples, please refer to the code comments and the FastAPI documentation.
```