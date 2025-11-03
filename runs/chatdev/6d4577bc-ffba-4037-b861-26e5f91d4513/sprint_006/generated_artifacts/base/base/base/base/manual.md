Here's a detailed user manual for the software, following the structure you provided:

```markdown
# Student Management API

A FastAPI application for managing student records, including the ability to create and retrieve student information.

## Quick Install

To set up the environment and install the necessary dependencies, you can use pip:

```bash
pip install fastapi sqlalchemy pydantic
```

If you are using a virtual environment, make sure to activate it before running the above command.

## 🤔 What is this?

The Student Management API allows users to manage student records efficiently. The main features include:

- **Create a new student**: Add a new student record with a name and email.
- **Retrieve all students**: Fetch a list of all student records stored in the database.

This API is built using FastAPI and SQLAlchemy, ensuring high performance and easy scalability.

## 📖 Main Functions

### 1. Create a New Student

**Endpoint**: `POST /students/`

**Request Body**:
```json
{
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

**Response**:
Returns the created student record, including the assigned ID.

### 2. Retrieve All Students

**Endpoint**: `GET /students/`

**Query Parameters**:
- `skip`: Number of records to skip (default is 0).
- `limit`: Maximum number of records to return (default is 10).

**Response**:
Returns a list of student records.

## 🛠️ Database Migration

To add the email field to the existing Student entity, a migration script is provided. This script ensures that existing student data is preserved during the migration process.

### Migration Steps

1. **Upgrade**: Run the `upgrade` function in the `migration_script.py` to add the email column to the `students` table.
2. **Downgrade**: If necessary, the `downgrade` function can be used to remove the email column.

### Example Migration Command

To execute the migration, you can run the following command in your Python environment:

```python
from sqlalchemy.orm import Session
from database import get_db
from migration_script import upgrade

db = next(get_db())
upgrade(db)
```

## 🚀 How to Use the API

1. **Start the FastAPI server**:
   Run the following command in your terminal:
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the API Documentation**:
   Open your browser and navigate to `http://127.0.0.1:8000/docs` to view the interactive API documentation provided by FastAPI.

3. **Create a Student**:
   Use the `/students/` endpoint to create a new student by sending a POST request with the required JSON body.

4. **Retrieve Students**:
   Use the `/students/` endpoint to retrieve a list of all students by sending a GET request.

## 📚 Additional Resources

For more information on FastAPI and SQLAlchemy, please refer to the following links:

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/en/14/)

Feel free to reach out for support or further questions regarding the Student Management API.
```

This manual provides a comprehensive overview of the software, installation instructions, main functions, and usage guidelines. Let me know if you need any modifications or additional information!