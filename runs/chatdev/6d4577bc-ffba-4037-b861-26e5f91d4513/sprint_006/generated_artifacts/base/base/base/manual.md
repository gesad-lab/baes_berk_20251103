Here's the user manual for the software, formatted in Markdown as requested:

```markdown
# Course Management System

A simple API for managing students and courses, built using FastAPI and SQLAlchemy.

## Main Functions

The Course Management System provides the following functionalities:

- **Student Management**: Create and retrieve student records.
- **Course Management**: Create and retrieve course records.
- **Database Migration**: Automatically updates the database schema to include new entities while preserving existing data.

## Quick Install

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
   pip install fastapi sqlalchemy pydantic
   ```

4. **Install an ASGI server** (e.g., uvicorn) to run the application:
   ```bash
   pip install uvicorn
   ```

## How to Use the Application

### Running the Application

To start the API server, run the following command in your terminal:

```bash
uvicorn main:app --reload
```

This will start the server at `http://127.0.0.1:8000`.

### API Endpoints

#### Student Endpoints

- **Create a new student**:
  - **Endpoint**: `POST /students/`
  - **Request Body**:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```
  - **Response**: Returns the created student object.

- **Get all students**:
  - **Endpoint**: `GET /students/`
  - **Response**: Returns a list of all students.

#### Course Endpoints

- **Create a new course**:
  - **Endpoint**: `POST /courses/`
  - **Request Body**:
    ```json
    {
      "name": "Introduction to Programming",
      "level": "Beginner"
    }
    ```
  - **Response**: Returns the created course object.

- **Get all courses**:
  - **Endpoint**: `GET /courses/`
  - **Response**: Returns a list of all courses.

## Database Migration

The application includes a migration script that updates the database schema to include the new Course table while preserving existing Student data. This is handled automatically when the application starts.

### Important Notes

- Ensure that the database file (`students.db`) is accessible and writable.
- The application uses SQLite for simplicity; for production, consider using a more robust database system.

## Conclusion

The Course Management System provides a straightforward way to manage students and courses through a RESTful API. For further customization or enhancements, feel free to modify the codebase as needed.

For any issues or support, please reach out to the development team.
```

This manual provides a comprehensive overview of the software, including installation instructions, usage details, and API endpoints. Let me know if you need any further modifications or additions!