```markdown
# ChatDev Course Management API

Welcome to the ChatDev Course Management API documentation. This API allows you to manage students and courses effectively, providing endpoints for creating and retrieving student and course data.

## Main Functions

- **Student Management**: Create and retrieve student records.
- **Course Management**: Create and retrieve course records.
- **Database Migration**: Automatically migrate the database schema to include the new Course table while preserving existing Student data.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repo/chatdev-course-management.git
   cd chatdev-course-management
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## How to Use the API

### 1. Start the FastAPI Application

Run the FastAPI application using Uvicorn:
```bash
uvicorn main:app --reload
```
This will start the server at `http://127.0.0.1:8000`.

### 2. API Endpoints

#### Student Endpoints

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

#### Course Endpoints

- **Create a Course**
  - **Endpoint**: `POST /courses/`
  - **Request Body**:
    ```json
    {
      "name": "Introduction to Programming",
      "level": "Beginner"
    }
    ```
  - **Response**: Returns the created course object.

- **Get Courses**
  - **Endpoint**: `GET /courses/`
  - **Query Parameters**: `skip` (int), `limit` (int)
  - **Response**: Returns a list of courses.

### 3. Database Migration

The database schema is automatically updated on application startup. The migration process ensures that existing student data is preserved while adding the new Course table.

To manually run migrations, you can execute the following command:
```bash
alembic upgrade head
```

## Additional Resources

For more detailed documentation, including examples and advanced usage, please refer to the following resources:

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Alembic Documentation](https://alembic.sqlalchemy.org/)

## Conclusion

This API provides a robust solution for managing students and courses, with a focus on ease of use and efficient data handling. We hope you find it useful for your educational management needs!
```