Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Teacher Management System

A simple API for managing teachers, students, and courses in an educational environment.

## Main Functions

The Teacher Management System provides the following main functionalities:

- **Create and Manage Teachers**: Add new teachers with their names and email addresses.
- **Create and Manage Students**: Add new students with their names and email addresses.
- **Create and Manage Courses**: Add new courses with their names and levels.
- **Retrieve Lists**: Fetch lists of teachers, students, and courses from the database.

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

## Database Setup

Before running the application, ensure that the database is set up correctly:

1. **Run Migrations**:
   The application uses Alembic for database migrations. To apply the migrations and create the necessary tables, run:
   ```bash
   alembic upgrade head
   ```

## How to Use the API

### Starting the Application

To start the FastAPI application, run the following command:
```bash
python main.py
```
The application will be available at `http://127.0.0.1:8000`.

### API Endpoints

#### Teachers

- **Create a Teacher**:
  - **Endpoint**: `POST /teachers`
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

- **Retrieve Teachers**:
  - **Endpoint**: `GET /teachers`
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
  - **Endpoint**: `POST /students`
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

- **Retrieve Students**:
  - **Endpoint**: `GET /students`
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

#### Courses

- **Create a Course**:
  - **Endpoint**: `POST /courses`
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

- **Retrieve Courses**:
  - **Endpoint**: `GET /courses`
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

This Teacher Management System provides a simple yet effective way to manage teachers, students, and courses. For further customization or enhancements, feel free to modify the codebase as needed.

For any issues or support, please reach out to the development team.
```

This manual provides a comprehensive overview of the software, including installation instructions, usage details, and API endpoints.