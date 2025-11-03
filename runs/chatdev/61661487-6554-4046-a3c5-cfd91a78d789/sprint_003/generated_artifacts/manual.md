```markdown
# Course Management System

A simple API for managing students and courses, allowing users to create and retrieve student and course data.

## Main Functions

- **Create Student**: Add a new student with a name and email.
- **Get Students**: Retrieve a list of students with pagination support.
- **Create Course**: Add a new course with a name and level.
- **Get Courses**: Retrieve a list of courses with pagination support.

## Quick Install

To set up the environment and install the required dependencies, follow these steps:

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
   pydantic
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## Database Migration

Before running the application, ensure that the database schema is updated to include the new Course table while preserving existing Student data. Run the migration script:

```bash
python main.py
```

## How to Use the API

### Start the Server

Run the FastAPI application using Uvicorn:

```bash
uvicorn routes:student_router --reload
```

### API Endpoints

- **Create a Student**
  - **Endpoint**: `POST /students/`
  - **Request Body**:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```
  - **Response**: Returns the created student object.

- **Get Students**
  - **Endpoint**: `GET /students/`
  - **Query Parameters**: `skip` (int), `limit` (int)
  - **Response**: Returns a list of students.

- **Create a Course**
  - **Endpoint**: `POST /courses/`
  - **Request Body**:
    ```json
    {
      "name": "Mathematics",
      "level": "Beginner"
    }
    ```
  - **Response**: Returns the created course object.

- **Get Courses**
  - **Endpoint**: `GET /courses/`
  - **Query Parameters**: `skip` (int), `limit` (int)
  - **Response**: Returns a list of courses.

## Conclusion

This Course Management System provides a straightforward way to manage students and courses through a RESTful API. You can extend its functionality by adding more features as needed. For any issues or feature requests, please contact the development team.
```