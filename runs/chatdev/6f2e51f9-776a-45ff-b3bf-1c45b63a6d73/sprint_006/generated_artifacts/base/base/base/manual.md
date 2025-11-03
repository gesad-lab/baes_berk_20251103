```markdown
# Course Management System

A simple API for managing students and courses, allowing users to create and retrieve information about students and courses.

## Main Functions

- **Student Management**: Create and retrieve student records, including their names and emails.
- **Course Management**: Create and retrieve course records, including course names and levels.
- **Database Migration**: Ensure that the database schema is updated without losing existing student data.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/course-management-system.git
   cd course-management-system
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install fastapi sqlalchemy alembic
   ```

4. **Run the Application**:
   ```bash
   uvicorn main:app --reload
   ```

## API Endpoints

### Student Endpoints

- **Create a Student**:
  - **Endpoint**: `POST /students/`
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

- **Get Students**:
  - **Endpoint**: `GET /students/`
  - **Query Parameters**: `skip`, `limit`
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

### Course Endpoints

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

- **Get Courses**:
  - **Endpoint**: `GET /courses/`
  - **Query Parameters**: `skip`, `limit`
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

## Database Migration

To add the Course table to the database while preserving existing student data, run the migration script using Alembic:

1. **Create a Migration**:
   ```bash
   alembic revision --autogenerate -m "Add Course table"
   ```

2. **Apply the Migration**:
   ```bash
   alembic upgrade head
   ```

## Conclusion

This Course Management System provides a straightforward way to manage students and courses through a RESTful API. For further customization or enhancements, feel free to modify the codebase as needed.
```
