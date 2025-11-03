Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Teacher Management System

A simple API for managing teachers, students, and courses in an educational context.

## Main Functions

This application provides the following functionalities:

- **Create and manage Teachers**: Add new teachers with their names and emails.
- **Create and manage Students**: Add new students with their names and emails.
- **Create and manage Courses**: Add new courses with their names and levels.
- **Retrieve lists of Teachers, Students, and Courses**: Fetch details of all teachers, students, or courses in the system.

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
   pip install fastapi[all] sqlalchemy alembic
   ```

4. **Initialize the database**:
   ```bash
   python -c "from database import init_db; init_db()"
   ```

## How to Use the Application

### Running the Application

To start the application, run the following command:

```bash
uvicorn main:app --reload
```

This will start the FastAPI server, and you can access the API at `http://127.0.0.1:8000`.

### API Endpoints

The application exposes several API endpoints for managing teachers, students, and courses. Below are the key endpoints:

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
      "email": "jane.smith@example.com"
    }
    ```

- **Get all Students**:
  - **Endpoint**: `GET /students/`

#### Courses

- **Create a Course**:
  - **Endpoint**: `POST /courses/`
  - **Request Body**:
    ```json
    {
      "name": "Mathematics",
      "level": "Intermediate"
    }
    ```

- **Get all Courses**:
  - **Endpoint**: `GET /courses/`

## Database Migration

The application uses Alembic for database migrations. To add the Teacher table to the database, run the migration script:

1. **Create a new migration**:
   ```bash
   alembic revision --autogenerate -m "Add Teacher table"
   ```

2. **Apply the migration**:
   ```bash
   alembic upgrade head
   ```

This will create the `teachers` table while preserving existing data for students and courses.

## Conclusion

This Teacher Management System provides a simple yet effective way to manage educational entities. For further details, please refer to the code documentation or reach out for support.
```

This manual provides a comprehensive overview of the software, including installation instructions, usage guidelines, and API endpoints. Let me know if you need any modifications or additional information!