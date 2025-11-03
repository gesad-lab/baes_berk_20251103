```markdown
# Student Management System

A simple API for managing student records, including the ability to create, retrieve, and manage student data.

## Main Functions

- **Create Student**: Add a new student record with a name and email.
- **Retrieve Students**: Fetch a list of existing students with their details.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repo/student-management-system.git
   cd student-management-system
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install fastapi sqlalchemy alembic
   ```

4. **Run database migrations**:
   Make sure to run the migration script to update the database schema:
   ```bash
   alembic upgrade head
   ```

5. **Start the application**:
   ```bash
   uvicorn main:app --reload
   ```

## 🤔 What is this?

The Student Management System is designed to help manage student records efficiently. It allows users to create new student entries and retrieve existing records. The system is built using FastAPI and SQLAlchemy, providing a robust and scalable solution for managing student data.

## 📖 API Documentation

### Create Student

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

### Retrieve Students

- **Endpoint**: `GET /students/`
- **Query Parameters**:
  - `skip`: Number of records to skip (default is 0).
  - `limit`: Maximum number of records to return (default is 10).
- **Response**:
  ```json
  [
    {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com"
    },
    {
      "id": 2,
      "name": "Jane Smith",
      "email": "jane.smith@example.com"
    }
  ]
  ```

## Additional Information

- **Database**: The application uses SQLite for data storage. The database file is created automatically on startup.
- **Migrations**: The application uses Alembic for database migrations. Ensure to run migrations after making changes to the database schema.
- **Testing**: You can use tools like Postman or curl to test the API endpoints.

For more detailed documentation, please refer to the [FastAPI documentation](https://fastapi.tiangolo.com/).
```
