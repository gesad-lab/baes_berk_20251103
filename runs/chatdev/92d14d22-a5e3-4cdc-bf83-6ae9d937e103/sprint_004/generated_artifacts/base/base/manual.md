Here's a detailed user manual for the Student application, formatted in Markdown as requested:

```markdown
# Student Application

A simple application for managing student records, including their names and email addresses.

## Main Functions

The Student application provides the following main functionalities:

- **Create Student**: Add a new student with a name and email address.
- **Get Students**: Retrieve a list of all students with their details.

## Quick Install

To set up the Student application, you need to install the required environment dependencies. You can do this using pip:

```bash
pip install fastapi sqlalchemy pydantic
```

Additionally, you will need a database. This application uses SQLite, which is included with Python. 

## Database Setup

Before running the application, ensure that the database is set up correctly. The application will automatically create the necessary tables when it starts.

## How to Use the Application

### Running the Application

To run the application, execute the following command in your terminal:

```bash
uvicorn main:app --reload
```

This command starts the FastAPI application, and you can access it at `http://127.0.0.1:8000`.

### API Endpoints

The application exposes the following API endpoints:

1. **Create Student**
   - **Endpoint**: `POST /students/`
   - **Request Body**:
     ```json
     {
       "name": "John Doe",
       "email": "john.doe@example.com"
     }
     ```
   - **Response**: Returns the created student object with an ID.

2. **Get Students**
   - **Endpoint**: `GET /students/`
   - **Query Parameters**:
     - `skip`: Number of records to skip (default is 0).
     - `limit`: Number of records to return (default is 10).
   - **Response**: Returns a list of student objects.

### Example Usage

To create a new student, you can use a tool like Postman or curl. Here’s an example using curl:

```bash
curl -X POST "http://127.0.0.1:8000/students/" -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john.doe@example.com"}'
```

To retrieve the list of students:

```bash
curl -X GET "http://127.0.0.1:8000/students/"
```

## Database Migration

The application includes a migration script to add the email field to the existing Student table. This script ensures that existing student data is preserved while adding the new column.

To run the migration, execute the following command:

```bash
python student.py
```

This will alter the existing `students` table to include the `email` column.

## Conclusion

The Student application is a straightforward tool for managing student records. With the ability to create and retrieve student information, it serves as a foundation for more complex educational applications. For further enhancements or questions, feel free to reach out.

```

This manual provides a comprehensive overview of the application, its functionalities, installation instructions, and usage examples, ensuring that users can easily understand and utilize the software.