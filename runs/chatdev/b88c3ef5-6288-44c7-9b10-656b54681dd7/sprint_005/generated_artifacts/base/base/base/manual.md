```markdown
# Student Management System

A simple API for managing student records, including the ability to create, read, and update student information.

## Main Functions

- **Create Student**: Add a new student record with a name and email.
- **Read Student**: Retrieve a student record by ID.
- **Database Migration**: Automatically updates the database schema to include the email field while preserving existing data.

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
   pip install fastapi sqlalchemy
   ```

4. **Run the database migration**:
   ```bash
   python main.py
   ```

## How to Use the API

### 1. Start the FastAPI server

Run the following command to start the FastAPI server:
```bash
uvicorn routers:app --reload
```

### 2. Create a Student

To create a new student, send a POST request to `/students/` with the following JSON body:
```json
{
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

### 3. Read a Student

To retrieve a student record, send a GET request to `/students/{student_id}`, replacing `{student_id}` with the actual ID of the student. For example:
```
GET /students/1
```

### 4. API Documentation

You can access the interactive API documentation provided by FastAPI at:
```
http://127.0.0.1:8000/docs
```

## Additional Information

### Database

The application uses SQLite as the database. The database file will be created automatically in the project directory. The schema will be updated to include the email field during the first run.

### Error Handling

The API will return appropriate HTTP status codes and messages for errors, such as:
- `404 Not Found` if a student is not found.
- `400 Bad Request` for invalid input.

## Conclusion

This Student Management System provides a simple yet effective way to manage student records. With the ability to create and read student information, it serves as a foundational tool for educational institutions or any organization needing to track student data.

For further assistance or feature requests, please reach out to our support team.
```